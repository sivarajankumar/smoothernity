#ifndef VLOG_HPP
#define VLOG_HPP

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

extern "C" int vlog_init(FILE*);
extern "C" void vlog_done(void);
extern "C" void vlog_out(vlog_level_e, const char *src,
                         int line, const char*, ...);

#endif /* VLOG_HPP */

