#include "mpool.h"
#include <stdlib.h>
#include <stdio.h>

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
    struct mpool_chunk_t *chunks;
    struct mpool_chunk_t *vacant;

    int left_min;
    int allocs;
    int frees;
    int alloc_fails;
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
    return ((void**)chunk->data) + 1;
}

void mpool_free(void *ptr)
{
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (ptr == 0)
        return;
    chunk = ((struct mpool_chunk_t**)ptr)[-1];
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
    int i, j;
    g_mpool.shelves = calloc(len, sizeof(struct mpool_shelf_t));
    if (g_mpool.shelves == 0)
        return 0;
    g_mpool.shelves_len = len;
    for (i = 0; i < len; ++i)
    {
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        shelf = g_mpool.shelves + i;
        shelf->size = sizes[i];
        shelf->count = counts[i];
        shelf->left = counts[i];
        shelf->left_min = counts[i];
        shelf->chunks = calloc(counts[i], sizeof(struct mpool_chunk_t));
        if (shelf->chunks == 0)
            goto cleanup;
        for (j = 0; j < counts[i]; ++j)
        {
            chunk = shelf->chunks + j;
            chunk->shelf = g_mpool.shelves + i;
            if (j < counts[i] - 1)
                chunk->next = shelf->chunks + j + 1;
            chunk->data = malloc((size_t)sizes[i] + sizeof(void*));
            if (chunk->data == 0)
                goto cleanup;
            *(void**)(chunk->data) = chunk;
        }
        shelf->vacant = shelf->chunks;
    }
    return 1;
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
    return 0;
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
