#include "cmpool.h"
#include "pmem.h"
#include <stdio.h>

#define CMPOOL_CHUNK_SIZE 16
#define CMPOOL_SHELF_SIZE 64

struct cmpool_chunk_t {
    struct cmpool_shelf_t *shelf;
    struct cmpool_chunk_t *next;
    char data[];
};

struct cmpool_shelf_t {
    int size, count, left, left_min, allocs, frees, alloc_fails;
    char *chunks;
    struct cmpool_chunk_t *vacant;
};

struct cmpool_t {
    int largest_size, shelves_len;
    char *shelves;
};

_Static_assert(sizeof(struct cmpool_shelf_t) <= CMPOOL_SHELF_SIZE,
               "Invalid cmpool_shelf_t size");
_Static_assert(sizeof(struct cmpool_chunk_t) <= CMPOOL_CHUNK_SIZE,
               "Invalid cmpool_chunk_t size");

static struct cmpool_shelf_t * cmpool_get_shelf(struct cmpool_t *mpool, int i) {
    if (i >= 0 && i < mpool->shelves_len)
        return (struct cmpool_shelf_t*)(mpool->shelves + CMPOOL_SHELF_SIZE * i);
    else
        return 0;
}

static int cmpool_chunk_size(struct cmpool_shelf_t *sh) {
    return CMPOOL_CHUNK_SIZE + sh->size;
}

static struct cmpool_chunk_t * cmpool_get_chunk
(int i, struct cmpool_shelf_t *sh) {
    if (i >= 0 && i < sh->count)
        return (struct cmpool_chunk_t*)(sh->chunks + cmpool_chunk_size(sh) * i);
    else
        return 0;
}

void * cmpool_alloc(struct cmpool_t *mpool, size_t size) {
    struct cmpool_chunk_t *chunk;
    struct cmpool_shelf_t *shelf;
    if (size > (size_t)mpool->largest_size)
        mpool->largest_size = (int)size;
    for (int i = 0; i < mpool->shelves_len; ++i) {
        shelf = cmpool_get_shelf(mpool, i);
        if ((size_t)shelf->size >= size)
            break;
    }
    if ((size_t)shelf->size < size) {
        fprintf(stderr, "cmpool_alloc: no shelf for size %i\n", (int)size);
        return 0;
    }
    if (!shelf->vacant) {
        fprintf(stderr, "cmpool_alloc: no chunks in shelf %i\n", shelf->size);
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

void cmpool_free(void *ptr) {
    struct cmpool_chunk_t *chunk;
    struct cmpool_shelf_t *shelf;
    if (!ptr)
        return;
    chunk = (struct cmpool_chunk_t*)ptr - 1;
    shelf = chunk->shelf;
    chunk->next = shelf->vacant;
    shelf->vacant = chunk;
    ++shelf->left;
    ++shelf->frees;
}

struct cmpool_t * cmpool_create(const int sizes[], const int counts[], int len){
    struct cmpool_t *mpool;
    struct cmpool_shelf_t *shelf;
    struct cmpool_chunk_t *chunk;
    int size, count;
    mpool = pmem_alloc(PMEM_ALIGNOF(struct cmpool_t), sizeof(struct cmpool_t));
    if (!mpool)
        return 0;
    mpool->shelves_len = len;
    mpool->largest_size = 0;
    mpool->shelves = pmem_alloc(PMEM_ALIGNOF(struct cmpool_shelf_t),
                                CMPOOL_SHELF_SIZE * len);
    if (!mpool->shelves)
        goto cleanup;
    for (int i = 0; i < len; ++i)
        cmpool_get_shelf(mpool, i)->chunks = 0;
    for (int i = 0; i < len; ++i) {
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        size = sizes[i];
        count = counts[i];

        /* Ensure proper alignment for chunks. */
        if (size & (size - 1) || size < CMPOOL_CHUNK_SIZE)
            goto cleanup;

        shelf = cmpool_get_shelf(mpool, i);
        shelf->size = size;
        shelf->count = count;
        shelf->left = count;
        shelf->left_min = count;
        shelf->allocs = shelf->frees = shelf->alloc_fails = 0;
        shelf->chunks = pmem_alloc(PMEM_ALIGNOF(struct cmpool_chunk_t),
                                   cmpool_chunk_size(shelf) * count);
        if (!shelf->chunks)
            goto cleanup;
        for (int j = 0; j < count; ++j) {
            chunk = cmpool_get_chunk(j, shelf);
            chunk->shelf = shelf;
            chunk->next = cmpool_get_chunk(j + 1, shelf);
        }
        shelf->vacant = cmpool_get_chunk(0, shelf);
    }
    return mpool;
cleanup:
    if (mpool->shelves) {
        for (int i = 0; i < mpool->shelves_len; ++i) {
            shelf = cmpool_get_shelf(mpool, i);
            if (shelf->chunks)
                pmem_free(shelf->chunks);
        }
        pmem_free(mpool->shelves);
    }
    pmem_free(mpool);
    return 0;
} 

void cmpool_destroy(struct cmpool_t *mpool) {
    struct cmpool_shelf_t *shelf;
    if (!mpool->shelves)
        return;
    fprintf(stderr, "Largest requested memory chunk: %i B\n",
            mpool->largest_size);
    for (int i = 0; i < mpool->shelves_len; ++i) {
        shelf = cmpool_get_shelf(mpool, i);
        fprintf(stderr, "Memory pool %i B chunks usage: %i/%i, "
                "allocs/frees: %i/%i (%i fails)\n",
                shelf->size,
                shelf->count - shelf->left_min, shelf->count,
                shelf->allocs, shelf->frees, shelf->alloc_fails);
        pmem_free(shelf->chunks);
    }
    pmem_free(mpool->shelves);
    pmem_free(mpool);
}

