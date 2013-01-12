#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*),
                 int colshape_count);
void physcpp_done(void);

