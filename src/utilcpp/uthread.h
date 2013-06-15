#ifndef UTHREAD_H
#define UTHREAD_H

struct uthread_mutex_t;
struct uthread_cond_t;
struct uthread_t;

struct uthread_mutex_t * uthread_mutex_create(void);
void uthread_mutex_destroy(struct uthread_mutex_t*);
void uthread_mutex_lock(struct uthread_mutex_t*);
void uthread_mutex_unlock(struct uthread_mutex_t*);

struct uthread_cond_t * uthread_cond_create(void);
void uthread_cond_destroy(struct uthread_cond_t*);
void uthread_cond_wait(struct uthread_cond_t*, struct uthread_mutex_t*);
void uthread_cond_signal(struct uthread_cond_t*);

struct uthread_t * uthread_create(void (*)(void*), void*);
void uthread_destroy(struct uthread_t*);

#endif /* UTHREAD_H */

