#ifndef UTIL_ATOMIC_H
#define UTIL_ATOMIC_H

struct atomic_int_t;

struct atomic_int_t * atomic_int_create(void);
void atomic_int_destroy(struct atomic_int_t*);
int atomic_int_load(struct atomic_int_t*);
void atomic_int_store(struct atomic_int_t*, int);
void atomic_int_add(struct atomic_int_t*, int);
void atomic_int_sub(struct atomic_int_t*, int);

#endif /* UTIL_ATOMIC.H */
