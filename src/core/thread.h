#pragma once

#include <string.h>

int thread_init(int count, const int msizes[], const int mcounts[], int mlen);
void thread_done(void);
