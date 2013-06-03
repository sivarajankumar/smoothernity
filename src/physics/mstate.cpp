#include "mstate.hpp"

mstate_c::mstate_c() {
}

mstate_c::~mstate_c() {
}

void mstate_c::getWorldTransform(btTransform &t) const {
    t = m;
}

void mstate_c::setWorldTransform(const btTransform &t) {
    m = t;
}
