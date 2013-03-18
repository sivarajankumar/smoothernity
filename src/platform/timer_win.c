#include <windows.h>

struct pfm_timer_t
{
    LARGE_INTEGER time;
    LARGE_INTEGER freq;
};

static struct pfm_timer_t g_pfm_timer;

int pfm_timer_init(void)
{
    if (QueryPerformanceFrequency(&g_pfm_timer.freq) == 0)
        return 1;
    if (QueryPerformanceCounter(&g_pfm_timer.time) == 0)
        return 1;
    return 0;
}

float pfm_timer_get(void)
{
    LARGE_INTEGER cur;
    QueryPerformanceCounter(&cur);
    return (float)((double)(cur.QuadPart - g_pfm_timer.time.QuadPart)
                 / (double)g_pfm_timer.freq.QuadPart);
}
