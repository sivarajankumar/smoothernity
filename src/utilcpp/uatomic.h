#ifndef UATOMIC_H
#define UATOMIC_H

struct uatomic_int_t;

struct uatomic_int_t * uatomic_int_create(void);
void uatomic_int_destroy(struct uatomic_int_t*);
int uatomic_int_load(struct uatomic_int_t*);
void uatomic_int_store(struct uatomic_int_t*, int);
void uatomic_int_add(struct uatomic_int_t*, int);
void uatomic_int_sub(struct uatomic_int_t*, int);

#endif /* UATOMIC.H */
