#include <thread>
#include <condition_variable>

struct uthread_mutex_t {
    std::mutex m;
    std::unique_lock<std::mutex> *u;
};

struct uthread_cond_t {
    std::condition_variable c;
};

struct uthread_t {
    std::thread *th;
};

extern "C" uthread_mutex_t * uthread_mutex_create(void) {
    uthread_mutex_t *m;
    m = new uthread_mutex_t;
    m->u = new std::unique_lock<std::mutex>(m->m, std::defer_lock);
    return m;
}

extern "C" void uthread_mutex_destroy(uthread_mutex_t *m) {
    delete m->u;
    delete m;
}

extern "C" void uthread_mutex_lock(uthread_mutex_t *m) {
    m->u->lock();
}

extern "C" void uthread_mutex_unlock(uthread_mutex_t *m) {
    m->u->unlock();
}

extern "C" uthread_cond_t * uthread_cond_create(void) {
    return new uthread_cond_t;
}

extern "C" void uthread_cond_destroy(uthread_cond_t *c) {
    delete c;
}

extern "C" void uthread_cond_wait(uthread_cond_t *c, uthread_mutex_t *m) {
    c->c.wait(*m->u);
}

extern "C" void uthread_cond_signal(uthread_cond_t *c) {
    c->c.notify_all();
}

extern "C" uthread_t * uthread_create(void (*fn)(void*), void *arg) {
    uthread_t *t;
    t = new uthread_t();
    t->th = new std::thread(fn, arg);
    return t;
}

extern "C" void uthread_destroy(uthread_t *t) {
    t->th->join();
    delete t->th;
    delete t;
}
