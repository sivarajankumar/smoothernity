#include "mstate.hpp"

mstate_c::mstate_c()
: was_set(0)
{
}

mstate_c::~mstate_c()
{
}

void mstate_c::getWorldTransform(btTransform &t) const
{
    t = get;
}

void mstate_c::setWorldTransform(const btTransform &t)
{
    set = t;
    was_set = 1;
}
