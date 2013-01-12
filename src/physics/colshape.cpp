#include "colshape.hpp"

struct colshapes_t
{
    int count;
};

static colshapes_t g_colshapes;

int colshape_init(int count)
{
    g_colshapes.count = count;
    return 1;
}

void colshape_done(void)
{
}
