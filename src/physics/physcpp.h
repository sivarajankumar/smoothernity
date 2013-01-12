#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int cs_count, int rb_count);
void physcpp_done(void);

