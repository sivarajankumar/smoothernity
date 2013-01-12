#pragma once

int physcpp_init(void *(*memalloc)(size_t), void (*memfree)(void*));
void physcpp_done(void);

