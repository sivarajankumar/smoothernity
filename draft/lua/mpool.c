#include "mpool.h"
#include <stdlib.h>
#include <stdio.h>

struct mchunk_t
{
    size_t size;
    size_t data_len;
    char *data;
    size_t vacant_len;
    size_t *vacant;
    char *busy;
    size_t allocs;
    size_t frees;
    size_t vacant_len_min;
    size_t alloc_fails;
    size_t free_fails;
};

struct mpool_t
{
    size_t chunks_len;
    struct mchunk_t *chunks;
    size_t no_chunk;
    size_t largest_size;
};

void * mpool_alloc(struct mpool_t *pool, void *ptr, size_t osize, size_t nsize)
{
    struct mchunk_t *ochunk, *nchunk;
    void *newptr;
    size_t i;
    /* inadequate request */
    if (osize == 0 && nsize == 0)
        return 0;
    if (nsize > pool->largest_size)
        pool->largest_size = nsize;
    ochunk = nchunk = 0;
    for (i = 0; i < pool->chunks_len; ++i)
    {
        if (pool->chunks[i].size >= osize)
        {
            ochunk = pool->chunks + i;
            break;
        }
    }
    for (i = 0; i < pool->chunks_len; ++i)
    {
        if (pool->chunks[i].size >= nsize)
        {
            nchunk = pool->chunks + i;
            break;
        }
    }
    /* cannot find chunk */
    if (ochunk == 0 || nchunk == 0)
    {
        ++pool->no_chunk;
        return 0;
    }
    /* allocate */
    if (osize == 0 && nsize > 0)
    {
        if (nchunk->vacant_len)
        {
            ++nchunk->allocs;
            i = nchunk->vacant[--nchunk->vacant_len];
            nchunk->busy[i] = 1;
            if (nchunk->vacant_len < nchunk->vacant_len_min)
                nchunk->vacant_len_min = nchunk->vacant_len;
            return nchunk->data + (nchunk->size * i);
        }
        else
        {
            ++nchunk->alloc_fails;
            return 0;
        }
    }
    /* free */
    else if (osize > 0 && nsize == 0)
    {
        i = (((char*)(ptr)) - ochunk->data) / ochunk->size;
        if (i < ochunk->data_len && ochunk->busy[i])
        {
            ++ochunk->frees;
            ochunk->vacant[ochunk->vacant_len++] = i;
            ochunk->busy[i] = 0;
        }
        else
            ++ochunk->free_fails;
        return 0;
    }
    /* realloc */
    else
    {
        newptr = mpool_alloc(pool, 0, 0, nsize);
        if (newptr)
        {
            if (osize <= nsize)
                memcpy(newptr, ptr, osize);
            else
                memcpy(newptr, ptr, nsize);
            mpool_alloc(pool, ptr, osize, 0);
            return newptr;
        }
        else
            return mpool_alloc(pool, ptr, osize, 0);
    }
}

struct mpool_t * mpool_create(const size_t sizes[], const size_t counts[], size_t len)
{
    struct mpool_t *pool;
    size_t i, j;
    pool = calloc(1, sizeof(struct mpool_t));
    if (pool == 0)
    {
        return 0;
    }
    pool->chunks_len = len;
    pool->chunks = calloc(len, sizeof(struct mchunk_t));
    if (pool->chunks == 0)
    {
        free(pool);
        return 0;
    }
    for (i = 0; i < len; ++i)
    {
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        pool->chunks[i].size = sizes[i];
        pool->chunks[i].data_len = counts[i];
        pool->chunks[i].data = malloc(sizes[i] * counts[i]);
        if (pool->chunks[i].data == 0)
            goto cleanup;
        pool->chunks[i].vacant_len = counts[i];
        pool->chunks[i].vacant = malloc(sizeof(size_t) * counts[i]);
        if (pool->chunks[i].vacant == 0)
            goto cleanup;
        for (j = 0; j < counts[i]; ++j)
            pool->chunks[i].vacant[j] = j;
        pool->chunks[i].busy = calloc(counts[i], sizeof(char));
        pool->chunks[i].vacant_len_min = counts[i];
    }
    return pool;
cleanup:
    for (i = 0; i < len; ++i)
    {
        if (pool->chunks[i].data)
            free(pool->chunks[i].data);
        if (pool->chunks[i].vacant)
            free(pool->chunks[i].vacant);
        if (pool->chunks[i].busy)
            free(pool->chunks[i].busy);
    }
    free(pool);
    return 0;
} 

void mpool_destroy(struct mpool_t *pool)
{
    size_t i;
    for (i = 0; i < pool->chunks_len; ++i)
    {
        free(pool->chunks[i].data);
        free(pool->chunks[i].vacant);
        free(pool->chunks[i].busy);
    }
    free(pool);
}

void mpool_print(struct mpool_t *pool)
{
    int i;
    printf("Memory pool statistics:\n");
    printf("Largest requested size: %i\n", pool->largest_size);
    printf("Cannot find chunk: %i\n", pool->no_chunk);
    for (i = 0; i < pool->chunks_len; ++i)
    {
        printf("Chunk size: %i, usage: %i/%i, allocs: %i (%i fails), frees: %i (%i fails).\n",
               pool->chunks[i].size,
               pool->chunks[i].data_len - pool->chunks[i].vacant_len_min,
               pool->chunks[i].data_len,
               pool->chunks[i].allocs,
               pool->chunks[i].alloc_fails,
               pool->chunks[i].frees,
               pool->chunks[i].free_fails);
    }
}
