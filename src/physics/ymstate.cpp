#include "ymstate.hpp"

ymstate_c::ymstate_c() {
}

ymstate_c::~ymstate_c() {
}

void ymstate_c::getWorldTransform(btTransform &t) const {
    t = m;
}

void ymstate_c::setWorldTransform(const btTransform &t) {
    m = t;
}
