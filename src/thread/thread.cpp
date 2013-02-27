#include <thread>

struct thread_mutex_t
{
};

struct thread_cond_t
{
};

struct thread_t
{
};

extern "C"
thread_mutex_t * thread_mutex_create(void)
{
    return 0;
}

extern "C"
void thread_mutex_destroy(thread_mutex_t*)
{
}

extern "C"
void thread_mutex_lock(thread_mutex_t*)
{
}

extern "C"
void thread_mutex_unlock(thread_mutex_t*)
{
}

extern "C"
thread_cond_t * thread_cond_create(void)
{
    return 0;
}

extern "C"
void thread_cond_destroy(thread_cond_t*)
{
}

extern "C"
void thread_cond_wait(thread_cond_t*, thread_mutex_t*)
{
}

extern "C"
void thread_cond_signal(thread_cond_t*)
{
}

extern "C"
thread_t * thread_create(void (*)(void))
{
    return 0;
}

extern "C"
void thread_destroy(thread_t*)
{
}
