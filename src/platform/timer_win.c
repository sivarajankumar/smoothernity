#include <windows.h>

struct pfm_timer_t
{
    LARGE_INTEGER time;
    LARGE_INTEGER freq;
};

static struct pfm_timer_t g_pfm_timer;

int pfm_timer_init(void)
{
    DWORD_PTR oldmask;
    oldmask = SetThreadAffinityMask(GetCurrentThread(), 1);
    if (QueryPerformanceFrequency(&g_pfm_timer.freq) == 0)
        return 1;
    if (QueryPerformanceCounter(&g_pfm_timer.time) == 0)
        return 1;
    SetThreadAffinityMask(GetCurrentThread(), oldmask);
}

float pfm_timer_get(void)
{
    DWORD_PTR oldmask;
    LARGE_INTEGER cur;
    oldmask = SetThreadAffinityMask(GetCurrentThread(), 1);
    QueryPerformanceCounter(&cur);
    SetThreadAffinityMask(GetCurrentThread(), oldmask);
    return (double)(cur.QuadPart - g_pfm_timer.time.QuadPart)
         / (double)g_pfm_timer.freq.QuadPart;
}
