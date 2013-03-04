#include <thread>
#include <condition_variable>

struct thread_mutex_t
{
    std::mutex m;
    std::unique_lock<std::mutex> *u;
};

struct thread_cond_t
{
    std::condition_variable c;
};

struct thread_t
{
    std::thread *th;
};

extern "C"
thread_mutex_t * thread_mutex_create(void)
{
    thread_mutex_t *m;
    m = new thread_mutex_t;
    m->u = new std::unique_lock<std::mutex>(m->m, std::defer_lock);
    return m;
}

extern "C"
void thread_mutex_destroy(thread_mutex_t *m)
{
    delete m->u;
    delete m;
}

extern "C"
void thread_mutex_lock(thread_mutex_t *m)
{
    m->u->lock();
}

extern "C"
void thread_mutex_unlock(thread_mutex_t *m)
{
    m->u->unlock();
}

extern "C"
thread_cond_t * thread_cond_create(void)
{
    return new thread_cond_t;
}

extern "C"
void thread_cond_destroy(thread_cond_t *c)
{
    delete c;
}

extern "C"
void thread_cond_wait(thread_cond_t *c, thread_mutex_t *m)
{
    c->c.wait(*m->u);
}

extern "C"
void thread_cond_signal(thread_cond_t *c)
{
    c->c.notify_all();
}

extern "C"
thread_t * thread_create(void (*fn)(void*), void *arg)
{
    thread_t *t;
    t = new thread_t();
    t->th = new std::thread(fn, arg);
    return t;
}

extern "C"
void thread_destroy(thread_t *t)
{
    t->th->join();
    delete t->th;
    delete t;
}
