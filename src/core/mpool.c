#include "mpool.h"
#include "../util/util.h"
#include <stdio.h>
#include <string.h>

static const size_t MPOOL_SIZE = 16;
static const size_t MPOOL_CHUNK_SIZE = 32;
static const size_t MPOOL_SHELF_SIZE = 64;
static const size_t MPOOL_DATA_ALIGN = 16;

struct mpool_chunk_t
{
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *next;
    void *data; /* store pointer to chunk, then actual data */
};

struct mpool_shelf_t
{
    int size;
    int count;
    int left;
    char *chunks;
    struct mpool_chunk_t *vacant;

    int left_min;
    int allocs;
    int frees;
    int alloc_fails;
};

struct mpool_t
{
    int shelves_len;
    char *shelves;
    int largest_size;
};

static struct mpool_shelf_t * mpool_get_shelf(struct mpool_t *mpool, int shelfi)
{
    if (shelfi >= 0 && shelfi < mpool->shelves_len)
        return (struct mpool_shelf_t*)(mpool->shelves + MPOOL_SHELF_SIZE * shelfi);
    else
        return 0;
}

static struct mpool_chunk_t * mpool_get_chunk(int chunki, struct mpool_shelf_t *shelf)
{
    if (chunki >= 0 && chunki < shelf->count)
        return (struct mpool_chunk_t*)(shelf->chunks + MPOOL_CHUNK_SIZE * chunki);
    else
        return 0;
}

void * mpool_alloc(struct mpool_t *mpool, size_t size)
{
    int i;
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (size > (size_t)mpool->largest_size)
        mpool->largest_size = (int)size;
    for (i = 0; i < mpool->shelves_len; ++i)
    {
        shelf = mpool_get_shelf(mpool, i);
        if ((size_t)shelf->size >= size)
            break;
    }
    if ((size_t)shelf->size < size)
    {
        fprintf(stderr, "mpool_alloc: cannot find shelf for size %i\n",
                (int)size);
        return 0;
    }
    if (shelf->vacant == 0)
    {
        fprintf(stderr, "mpool_alloc: out of chunks in shelf %i\n",
                shelf->size);
        ++shelf->alloc_fails;
        return 0;
    }
    --shelf->left;
    if (shelf->left < shelf->left_min)
        shelf->left_min = shelf->left;
    ++shelf->allocs;
    chunk = shelf->vacant;
    shelf->vacant = shelf->vacant->next;
    chunk->next = 0;
    return ((char*)chunk->data) + MPOOL_DATA_ALIGN;
}

void mpool_free(void *ptr)
{
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (ptr == 0)
        return;
    chunk = *(struct mpool_chunk_t**)(((char*)ptr) - MPOOL_DATA_ALIGN);
    shelf = chunk->shelf;
    chunk->next = shelf->vacant;
    shelf->vacant = chunk;
    ++shelf->left;
    ++shelf->frees;
}

struct mpool_t * mpool_create(const int sizes[], const int counts[], int len)
{
    struct mpool_t *mpool;
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *chunk;
    int i, j, size, count;
    if (sizeof(struct mpool_chunk_t) > MPOOL_CHUNK_SIZE
    ||  sizeof(struct mpool_shelf_t) > MPOOL_SHELF_SIZE
    ||  sizeof(struct mpool_t) > MPOOL_SIZE
    ||  sizeof(void*) > MPOOL_DATA_ALIGN)
    {
        fprintf(stderr, "Invalid size:\n"
                        "sizeof(struct mpool_chunk_t) == %i\n"
                        "sizeof(struct mpool_shelf_t) == %i\n"
                        "sizeof(struct mpool_t) == %i\n"
                        "sizeof(void*) == %i\n",
                (int)sizeof(struct mpool_chunk_t),
                (int)sizeof(struct mpool_shelf_t),
                (int)sizeof(struct mpool_t),
                (int)sizeof(void*));
        return 0;
    }
    mpool = util_malloc(MPOOL_SIZE, MPOOL_SIZE);
    if (mpool == 0)
        return 0;
    memset(mpool, 0, MPOOL_SIZE);
    mpool->shelves = util_malloc(MPOOL_SHELF_SIZE, MPOOL_SHELF_SIZE * len);
    if (mpool->shelves == 0)
        goto cleanup;
    memset(mpool->shelves, 0, MPOOL_SHELF_SIZE * len);
    mpool->shelves_len = len;
    for (i = 0; i < len; ++i)
    {
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        size = sizes[i];
        count = counts[i];
        if ((size & (size - 1)) != 0)
        {
            fprintf(stderr, "Invalid shelf size == %i\n", size);
            goto cleanup;
        }
        shelf = mpool_get_shelf(mpool, i);
        shelf->size = size;
        shelf->count = count;
        shelf->left = count;
        shelf->left_min = count;
        shelf->chunks = util_malloc(MPOOL_CHUNK_SIZE, MPOOL_CHUNK_SIZE * count);
        if (shelf->chunks == 0)
            goto cleanup;
        memset(shelf->chunks, 0, MPOOL_CHUNK_SIZE * count);
        for (j = 0; j < counts[i]; ++j)
        {
            chunk = mpool_get_chunk(j, shelf);
            chunk->shelf = shelf;
            chunk->next = mpool_get_chunk(j + 1, shelf);
            /* preserve first MPOOL_DATA_ALIGN bytes for pointer to chunk */
            chunk->data = util_malloc(MPOOL_DATA_ALIGN, MPOOL_DATA_ALIGN + (size_t)size);
            if (chunk->data == 0)
                goto cleanup;
            *(void**)(chunk->data) = chunk;
        }
        shelf->vacant = mpool_get_chunk(0, shelf);
    }
    return mpool;
cleanup:
    if (mpool->shelves)
    {
        for (i = 0; i < mpool->shelves_len; ++i)
        {
            shelf = mpool_get_shelf(mpool, i);
            if (shelf->chunks)
            {
                for (j = 0; j < shelf->count; ++j)
                {
                    chunk = mpool_get_chunk(j, shelf);
                    if (chunk->data)
                        util_free(chunk->data);
                }
                util_free(shelf->chunks);
            }
        }
        util_free(mpool->shelves);
    }
    util_free(mpool);
    return 0;
} 

void mpool_destroy(struct mpool_t *mpool)
{
    int i, j;
    struct mpool_shelf_t *shelf;
    if (mpool->shelves == 0)
        return;
    printf("Largest requested memory chunk: %i B\n", mpool->largest_size);
    for (i = 0; i < mpool->shelves_len; ++i)
    {
        shelf = mpool_get_shelf(mpool, i);
        printf("Memory pool %i B chunks usage: %i/%i, allocs/frees: %i/%i "
               "(%i fails)\n",
               shelf->size,
               shelf->count - shelf->left_min, shelf->count,
               shelf->allocs, shelf->frees, shelf->alloc_fails);
        for (j = 0; j < shelf->count; ++j)
            util_free(mpool_get_chunk(j, shelf)->data);
        util_free(shelf->chunks);
    }
    util_free(mpool->shelves);
    util_free(mpool);
}
