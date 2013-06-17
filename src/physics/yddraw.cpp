#include "yddraw.hpp"
#include "vlog.hpp"
#include "GL/glew.h"

yddraw_c::yddraw_c() : mode(0) {
}

yddraw_c::~yddraw_c() {
}

void yddraw_c::drawLine
(const btVector3 &from, const btVector3 &to, const btVector3 &color) {
    glBegin(GL_LINES);
    glColor3f(color.getX(), color.getY(), color.getZ());
    glVertex3d(from.getX(), from.getY(), from.getZ());
    glVertex3d(to.getX(), to.getY(), to.getZ());
    glEnd();
}

void yddraw_c::drawContactPoint(const btVector3 &pos,
const btVector3 &norm, btScalar dist, int, const btVector3 &color) {
    drawLine(pos, pos + norm * dist, color);
}

void yddraw_c::reportErrorWarning(const char *text) {
    VLOG_ERROR(text);
}

void yddraw_c::draw3dText(const btVector3&, const char*) {
}

void yddraw_c::setDebugMode(int m) {
    mode = m;
}

int yddraw_c::getDebugMode(void) const {
    return mode;
}
