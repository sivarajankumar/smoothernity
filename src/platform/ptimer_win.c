#include "windows.h"

struct ptimer_t {
    LARGE_INTEGER time;
    LARGE_INTEGER freq;
};

static struct ptimer_t g_ptimer;

int ptimer_init(void) {
    if (!QueryPerformanceFrequency(&g_ptimer.freq))
        return 1;
    if (!QueryPerformanceCounter(&g_ptimer.time))
        return 1;
    return 0;
}

float ptimer_get(void) {
    LARGE_INTEGER cur;
    QueryPerformanceCounter(&cur);
    return (float)((double)(cur.QuadPart - g_ptimer.time.QuadPart)
                 / (double)g_ptimer.freq.QuadPart);
}

