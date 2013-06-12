#include "mpool.h"
#include "../platform/mem.h"
#include <stdio.h>

#define MPOOL_CHUNK_SIZE 16
#define MPOOL_SHELF_SIZE 64

struct mpool_chunk_t {
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *next;
    char data[];
};

struct mpool_shelf_t {
    int size, count, left, left_min, allocs, frees, alloc_fails;
    char *chunks;
    struct mpool_chunk_t *vacant;
};

struct mpool_t {
    int largest_size, shelves_len;
    char *shelves;
};

_Static_assert(sizeof(struct mpool_shelf_t) <= MPOOL_SHELF_SIZE,
               "Invalid mpool_shelf_t size");
_Static_assert(sizeof(struct mpool_chunk_t) <= MPOOL_CHUNK_SIZE,
               "Invalid mpool_chunk_t size");

static struct mpool_shelf_t * mpool_get_shelf(struct mpool_t *mpool, int i) {
    if (i >= 0 && i < mpool->shelves_len)
        return (struct mpool_shelf_t*)(mpool->shelves + MPOOL_SHELF_SIZE * i);
    else
        return 0;
}

static int mpool_chunk_size(struct mpool_shelf_t *sh) {
    return MPOOL_CHUNK_SIZE + sh->size;
}

static struct mpool_chunk_t * mpool_get_chunk(int i, struct mpool_shelf_t *sh) {
    if (i >= 0 && i < sh->count)
        return (struct mpool_chunk_t*)(sh->chunks + mpool_chunk_size(sh) * i);
    else
        return 0;
}

void * mpool_alloc(struct mpool_t *mpool, size_t size) {
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (size > (size_t)mpool->largest_size)
        mpool->largest_size = (int)size;
    for (int i = 0; i < mpool->shelves_len; ++i) {
        shelf = mpool_get_shelf(mpool, i);
        if ((size_t)shelf->size >= size)
            break;
    }
    if ((size_t)shelf->size < size) {
        fprintf(stderr, "mpool_alloc: no shelf for size %i\n", (int)size);
        return 0;
    }
    if (!shelf->vacant) {
        fprintf(stderr, "mpool_alloc: no chunks in shelf %i\n", shelf->size);
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
    return chunk->data;
}

void mpool_free(void *ptr) {
    struct mpool_chunk_t *chunk;
    struct mpool_shelf_t *shelf;
    if (!ptr)
        return;
    chunk = (struct mpool_chunk_t*)ptr - 1;
    shelf = chunk->shelf;
    chunk->next = shelf->vacant;
    shelf->vacant = chunk;
    ++shelf->left;
    ++shelf->frees;
}

struct mpool_t * mpool_create(const int sizes[], const int counts[], int len) {
    struct mpool_t *mpool;
    struct mpool_shelf_t *shelf;
    struct mpool_chunk_t *chunk;
    int size, count;
    mpool = mem_alloc(MEM_ALIGNOF(struct mpool_t), sizeof(struct mpool_t));
    if (!mpool)
        return 0;
    mpool->shelves_len = len;
    mpool->largest_size = 0;
    mpool->shelves = mem_alloc(MEM_ALIGNOF(struct mpool_shelf_t),
                               MPOOL_SHELF_SIZE * len);
    if (!mpool->shelves)
        goto cleanup;
    for (int i = 0; i < len; ++i)
        mpool_get_shelf(mpool, i)->chunks = 0;
    for (int i = 0; i < len; ++i) {
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        size = sizes[i];
        count = counts[i];

        /* Ensure proper alignment for chunks. */
        if (size & (size - 1) || size < MPOOL_CHUNK_SIZE)
            goto cleanup;

        shelf = mpool_get_shelf(mpool, i);
        shelf->size = size;
        shelf->count = count;
        shelf->left = count;
        shelf->left_min = count;
        shelf->allocs = shelf->frees = shelf->alloc_fails = 0;
        shelf->chunks = mem_alloc(MEM_ALIGNOF(struct mpool_chunk_t),
                                  mpool_chunk_size(shelf) * count);
        if (!shelf->chunks)
            goto cleanup;
        for (int j = 0; j < count; ++j) {
            chunk = mpool_get_chunk(j, shelf);
            chunk->shelf = shelf;
            chunk->next = mpool_get_chunk(j + 1, shelf);
        }
        shelf->vacant = mpool_get_chunk(0, shelf);
    }
    return mpool;
cleanup:
    if (mpool->shelves) {
        for (int i = 0; i < mpool->shelves_len; ++i) {
            shelf = mpool_get_shelf(mpool, i);
            if (shelf->chunks)
                mem_free(shelf->chunks);
        }
        mem_free(mpool->shelves);
    }
    mem_free(mpool);
    return 0;
} 

void mpool_destroy(struct mpool_t *mpool) {
    struct mpool_shelf_t *shelf;
    if (!mpool->shelves)
        return;
    fprintf(stderr, "Largest requested memory chunk: %i B\n",
            mpool->largest_size);
    for (int i = 0; i < mpool->shelves_len; ++i) {
        shelf = mpool_get_shelf(mpool, i);
        fprintf(stderr, "Memory pool %i B chunks usage: %i/%i, "
                "allocs/frees: %i/%i (%i fails)\n",
                shelf->size,
                shelf->count - shelf->left_min, shelf->count,
                shelf->allocs, shelf->frees, shelf->alloc_fails);
        mem_free(shelf->chunks);
    }
    mem_free(mpool->shelves);
    mem_free(mpool);
}

