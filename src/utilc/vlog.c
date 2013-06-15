#include "vlog.h"
#include "uthread.h"
#include "uatomic.h"
#include "ptimer.h"
#include <stdarg.h>

struct vlog_t {
    FILE *file;
    struct uthread_mutex_t *mutex;
};

static struct vlog_t g_vlog;

int vlog_init(FILE *file) {
    g_vlog.file = file;
    if (!(g_vlog.mutex = uthread_mutex_create()))
        return 1;
    return 0;
}

void vlog_done(void) {
    if (g_vlog.mutex)
        uthread_mutex_destroy(g_vlog.mutex);
    g_vlog.mutex = 0;
}

static const char * vlog_level_text(enum vlog_level_e level) {
    if (level == VLOG_LEVEL_INFO)
        return "INFO";
    else /* level == VLOG_LEVEL_ERROR */
        return "ERROR";
}

void vlog_out
(enum vlog_level_e level, const char *src, int line, const char *msg, ...) {
    va_list ap;
    va_start(ap, msg);
    uthread_mutex_lock(g_vlog.mutex);
    fprintf(g_vlog.file, "[%7.3f] %s (%s:%i) ", (double)ptimer_get(),
            vlog_level_text(level), src, line);
    vfprintf(g_vlog.file, msg, ap);
    fprintf(g_vlog.file, "\n");
    uthread_mutex_unlock(g_vlog.mutex);
    va_end(ap);
}

