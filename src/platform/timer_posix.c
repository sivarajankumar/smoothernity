#include "sys/time.h"

static struct timeval g_pfm_timer;

int pfm_timer_init(void) {
    gettimeofday(&g_pfm_timer, 0);
    return 0;
}

float pfm_timer_get(void) {
    struct timeval cur;
    gettimeofday(&cur, 0);
    return 0.000001f *
        (float)(((cur.tv_sec - g_pfm_timer.tv_sec) * 1000000) +
                 (cur.tv_usec - g_pfm_timer.tv_usec));
}

