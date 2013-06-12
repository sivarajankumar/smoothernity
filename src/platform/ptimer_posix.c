#include "sys/time.h"

static struct timeval g_ptimer;

int ptimer_init(void) {
    gettimeofday(&g_ptimer, 0);
    return 0;
}

float ptimer_get(void) {
    struct timeval cur;
    gettimeofday(&cur, 0);
    return 0.000001f *
        (float)(((cur.tv_sec - g_ptimer.tv_sec) * 1000000) +
                 (cur.tv_usec - g_ptimer.tv_usec));
}

