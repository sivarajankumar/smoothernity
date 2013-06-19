#include "cmpool.h"
#include "vlog.h"
#include "pmem.h"

struct cmpool_chunk_t {
    struct cmpool_shelf_t *shelf;
    struct cmpool_chunk_t *next;
    char data[];
};

struct cmpool_shelf_t {
    int size, count, left, left_min, allocs, frees, alloc_fails;
    struct cmpool_chunk_t *vacant;
    struct cmpool_chunk_t *chunks[];
};

struct cmpool_t {
    int largest_size, shelves_len;
    struct cmpool_shelf_t *shelves[];
};

static struct cmpool_shelf_t * cmpool_get_shelf(struct cmpool_t *mpool, int i) {
    if (i >= 0 && i < mpool->shelves_len)
        return mpool->shelves[i];
    else
        return 0;
}

static struct cmpool_chunk_t * cmpool_get_chunk
(int i, struct cmpool_shelf_t *sh) {
    if (i >= 0 && i < sh->count)
        return sh->chunks[i];
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
        VLOG_ERROR("no shelf for size %i", (int)size);
        return 0;
    }
    if (!shelf->vacant) {
        VLOG_ERROR("no chunks in shelf %i", shelf->size);
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
    mpool = pmem_alloc(PMEM_ALIGNOF(struct cmpool_t),
        sizeof(struct cmpool_t) + sizeof(struct cmpool_shelf_t*) * len);
    if (!mpool)
        return 0;
    mpool->shelves_len = len;
    mpool->largest_size = 0;
    for (int i = 0; i < len; ++i)
        mpool->shelves[i] = 0;
    for (int i = 0; i < len; ++i) {
        /* Chunk sizes must be sorted to simplify searching algorithm. */
        if (i > 0 && sizes[i-1] >= sizes[i])
            goto cleanup;
        size = sizes[i];
        count = counts[i];

        mpool->shelves[i] = pmem_alloc(PMEM_ALIGNOF(struct cmpool_shelf_t),
            sizeof(struct cmpool_shelf_t)+sizeof(struct cmpool_chunk_t*)*count);
        if (!(shelf = cmpool_get_shelf(mpool, i)))
            goto cleanup;
        shelf->size = size;
        shelf->count = count;
        shelf->left = count;
        shelf->left_min = count;
        shelf->allocs = shelf->frees = shelf->alloc_fails = 0;
        for (int j = 0; j < count; ++j)
            shelf->chunks[j] = 0;
        for (int j = 0; j < count; ++j) {
            shelf->chunks[j] = pmem_alloc(PMEM_ALIGNOF(struct cmpool_chunk_t),
                sizeof(struct cmpool_chunk_t) + size);
            if (!(chunk = cmpool_get_chunk(j, shelf)))
                goto cleanup;
            chunk->shelf = shelf;
            chunk->next = 0;
            if (j > 0)
                cmpool_get_chunk(j - 1, shelf)->next = chunk;
        }
        shelf->vacant = cmpool_get_chunk(0, shelf);
    }
    return mpool;
cleanup:
    cmpool_destroy(mpool);
    return 0;
} 

void cmpool_destroy(struct cmpool_t *mpool) {
    struct cmpool_shelf_t *shelf;
    struct cmpool_chunk_t *chunk;
    for (int i = 0; i < mpool->shelves_len; ++i) {
        if (!!(shelf = cmpool_get_shelf(mpool, i))) {
            for (int j = 0; j < shelf->count; ++j)
                if (!!(chunk = cmpool_get_chunk(j, shelf)))
                    pmem_free(chunk);
            pmem_free(shelf);
        }
    }
    pmem_free(mpool);
}

void cmpool_report(struct cmpool_t *mpool) {
    struct cmpool_shelf_t *shelf;
    VLOG_INFO("Largest requested memory chunk: %i B", mpool->largest_size);
    for (int i = 0; i < mpool->shelves_len; ++i) {
        shelf = cmpool_get_shelf(mpool, i);
        VLOG_INFO("Memory pool %i B chunks usage: %i/%i, "
                  "allocs/frees: %i/%i (%i fails)",
                  shelf->size,
                  shelf->count - shelf->left_min, shelf->count,
                  shelf->allocs, shelf->frees, shelf->alloc_fails);
        if (shelf->allocs != shelf->frees)
            VLOG_ERROR("Allocs/frees mismatch");
    }
}

