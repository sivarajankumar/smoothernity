#ifndef THREAD_THREAD_H
#define THREAD_THREAD_H

struct thread_mutex_t;
struct thread_cond_t;
struct thread_t;

struct thread_mutex_t * thread_mutex_create(void);
void thread_mutex_destroy(struct thread_mutex_t*);
void thread_mutex_lock(struct thread_mutex_t*);
void thread_mutex_unlock(struct thread_mutex_t*);

struct thread_cond_t * thread_cond_create(void);
void thread_cond_destroy(struct thread_cond_t*);
void thread_cond_wait(struct thread_cond_t*, struct thread_mutex_t*);
void thread_cond_signal(struct thread_cond_t*);

struct thread_t * thread_create(void (*)(void*), void*);
void thread_destroy(struct thread_t*);

#endif /* THREAD_THREAD_H */

