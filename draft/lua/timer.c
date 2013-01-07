#include "timer.h"
#include "sys/time.h"
#include <stdlib.h>

struct timer_t
{
    struct timeval time;
};

struct timer_t * timer_create(void)
{
    struct timer_t * timer;
    timer = calloc(1, sizeof(struct timer_t));
    if (timer == 0)
        return 0;
    timer_reset(timer);
    return timer;
}

void timer_destroy(struct timer_t *timer)
{
    free(timer);
}

void timer_reset(struct timer_t *timer)
{
    gettimeofday(&timer->time, 0);
}

int timer_passed(struct timer_t *timer)
{
    struct timeval cur, diff;
    gettimeofday(&cur, 0);
    return (int)(((cur.tv_sec - timer->time.tv_sec) * 1000000) +
                 (cur.tv_usec - timer->time.tv_usec));
}
