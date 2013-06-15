#include <atomic>

struct uatomic_int_t {
    std::atomic<int> i;
};

extern "C" uatomic_int_t * uatomic_int_create(void) {
    return new uatomic_int_t;
}

extern "C" void uatomic_int_destroy(uatomic_int_t *a) {
    delete a;
}

extern "C" int uatomic_int_load(uatomic_int_t *a) {
    return a->i.load();
}

extern "C" void uatomic_int_store(uatomic_int_t *a, int v) {
    a->i.store(v);
}

extern "C" void uatomic_int_add(uatomic_int_t *a, int v) {
    a->i.fetch_add(v);
}

extern "C" void uatomic_int_sub(uatomic_int_t *a, int v) {
    a->i.fetch_sub(v);
}
