#include "mpool.h"
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

static const size_t MPOOL_CHUNK_SIZE = 32;
static const size_t MPOOL_SHELF_SIZE = 64;
static const size_t MPOOL_DATA_ALIGN = 16;

struct mpool_chunk_t
{
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *next;
    void *data; /* store pointer to chunk, then actual data */
    char padding[8];
};

struct mpool_shelf_t
{
    int size;
    int count;
    int left;
    struct mpool_chunk_t *chunks;
    struct mpool_chunk_t *vacant;

    int left_min;
    int allocs;
    int frees;
    int alloc_fails;

    char padding[16];
};

struct mpool_t
{
    int shelves_len;
    struct mpool_shelf_t *shelves;
    int largest_size;
};

static struct mpool_t g_mpool;

void * mpool_alloc(size_t size)
{
    int i;
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (size > (size_t)g_mpool.largest_size)
        g_mpool.largest_size = (int)size;
    shelf = 0;
    for (i = 0; i < g_mpool.shelves_len; ++i)
    {
        if ((size_t)g_mpool.shelves[i].size >= size)
        {
            shelf = g_mpool.shelves + i;
            break;
        }
    }
    if (shelf == 0)
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

int mpool_init(const int sizes[], const int counts[], int len)
{
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *chunk;
    int i, j, size, count;
    if (sizeof(struct mpool_chunk_t) != MPOOL_CHUNK_SIZE
    ||  sizeof(struct mpool_shelf_t) != MPOOL_SHELF_SIZE
    ||  sizeof(void*) > MPOOL_DATA_ALIGN)
    {
        fprintf(stderr, "Invalid size:\n"
                        "sizeof(struct mpool_chunk_t) == %i\n"
                        "sizeof(struct mpool_shelf_t) == %i\n"
                        "sizeof(void*) == %i\n",
                (int)sizeof(struct mpool_chunk_t),
                (int)sizeof(struct mpool_shelf_t),
                (int)sizeof(void*));
        return 1;
    }
    g_mpool.shelves = aligned_alloc(MPOOL_SHELF_SIZE, MPOOL_SHELF_SIZE * len);
    if (g_mpool.shelves == 0)
        return 1;
    memset(g_mpool.shelves, 0, MPOOL_SHELF_SIZE * len);
    g_mpool.shelves_len = len;
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
        shelf = g_mpool.shelves + i;
        shelf->size = size;
        shelf->count = count;
        shelf->left = count;
        shelf->left_min = count;
        shelf->chunks = aligned_alloc(MPOOL_CHUNK_SIZE, MPOOL_CHUNK_SIZE * count);
        if (shelf->chunks == 0)
            goto cleanup;
        memset(shelf->chunks, 0, MPOOL_CHUNK_SIZE * count);
        for (j = 0; j < counts[i]; ++j)
        {
            chunk = shelf->chunks + j;
            chunk->shelf = g_mpool.shelves + i;
            if (j < counts[i] - 1)
                chunk->next = shelf->chunks + j + 1;
            /* preserve first MPOOL_DATA_ALIGN bytes for pointer to chunk */
            chunk->data = aligned_alloc(MPOOL_DATA_ALIGN, MPOOL_DATA_ALIGN + (size_t)size);
            if (chunk->data == 0)
                goto cleanup;
            *(void**)(chunk->data) = chunk;
        }
        shelf->vacant = shelf->chunks;
    }
    return 0;
cleanup:
    for (i = 0; i < g_mpool.shelves_len; ++i)
    {
        shelf = g_mpool.shelves + i;
        if (shelf->chunks)
        {
            for (j = 0; j < shelf->count; ++j)
            {
                if (shelf->chunks[j].data)
                    free(shelf->chunks[j].data);
            }
            free(shelf->chunks);
        }
    }
    free(g_mpool.shelves);
    g_mpool.shelves = 0;
    return 1;
} 

void mpool_done(void)
{
    int i, j;
    struct mpool_shelf_t *shelf;
    if (g_mpool.shelves == 0)
        return;
    printf("Largest requested memory chunk: %i B\n", g_mpool.largest_size);
    for (i = 0; i < g_mpool.shelves_len; ++i)
    {
        shelf = g_mpool.shelves + i;
        printf("Memory pool %i B chunks usage: %i/%i, allocs/frees: %i/%i "
               "(%i fails)\n",
               shelf->size,
               shelf->count - shelf->left_min, shelf->count,
               shelf->allocs, shelf->frees, shelf->alloc_fails);
        for (j = 0; j < shelf->count; ++j)
            free(shelf->chunks[j].data);
        free(shelf->chunks);
    }
    free(g_mpool.shelves);
    g_mpool.shelves = 0;
}
