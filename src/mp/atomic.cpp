#include <atomic>

struct atomic_int_t {
    std::atomic<int> i;
};

extern "C" atomic_int_t * atomic_int_create(void) {
    return new atomic_int_t;
}

extern "C" void atomic_int_destroy(atomic_int_t *a) {
    delete a;
}

extern "C" int atomic_int_load(atomic_int_t *a) {
    return a->i.load();
}

extern "C" void atomic_int_store(atomic_int_t *a, int v) {
    a->i.store(v);
}

extern "C" void atomic_int_add(atomic_int_t *a, int v) {
    a->i.fetch_add(v);
}

extern "C" void atomic_int_sub(atomic_int_t *a, int v) {
    a->i.fetch_sub(v);
}
