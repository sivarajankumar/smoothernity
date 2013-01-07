void * mpool_alloc(struct mpool_t *pool, void *ptr, size_t osize, size_t nsize)
{
}

int mpool_selftest(void)
{
    struct mpool_t *pool;
    void *ptr;
    pool = mpool_newpool();
    mpool_newchunk(pool, 16, 1);
    ptr = mpool_alloc(pool, 0, 0, 16);
    mpool_discard(pool);
}
