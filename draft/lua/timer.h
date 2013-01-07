struct timer_t;

struct timer_t * timer_create(void);
void timer_destroy(struct timer_t *);
int timer_passed(struct timer_t *);
void timer_reset(struct timer_t *);
