#ifndef VLOG_H
#define VLOG_H

#include <stdio.h>

#define VLOG_INFO(...) \
    vlog_out(VLOG_LEVEL_INFO, __FILE__, __LINE__, __VA_ARGS__)
#define VLOG_ERROR(...) \
    vlog_out(VLOG_LEVEL_ERROR, __FILE__, __LINE__, __VA_ARGS__)

enum vlog_level_e {
    VLOG_LEVEL_INFO,
    VLOG_LEVEL_ERROR,
    VLOG_LEVELS_TOTAL
};

int vlog_init(FILE*);
void vlog_done(void);
void vlog_out(enum vlog_level_e, const char *src, int line, const char*, ...);

#endif /* VLOG_H */

