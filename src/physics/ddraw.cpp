#include "ddraw.hpp"
#include <stdio.h>
#include <string.h>
#include "GL/glew.h"

ddraw_c::ddraw_c()
: mode(0)
{
}

ddraw_c::~ddraw_c()
{
}

void ddraw_c::drawLine(const btVector3 &from, const btVector3 &to,
                       const btVector3 &color)
{
    glBegin(GL_LINES);
    glColor3f(color.getX(), color.getY(), color.getZ());
    glVertex3d(from.getX(), from.getY(), from.getZ());
    glVertex3d(to.getX(), to.getY(), to.getZ());
    glEnd();
}

void ddraw_c::drawContactPoint(const btVector3 &pos, const btVector3 &norm,
                               btScalar dist, int, const btVector3 &color)
{
    drawLine(pos, pos + norm * dist, color);
}

void ddraw_c::reportErrorWarning(const char *text)
{
    fprintf(stderr, "physics: %s\n", text);
}

void ddraw_c::draw3dText(const btVector3&, const char*)
{
}

void ddraw_c::setDebugMode(int m)
{
    mode = m;
}

int ddraw_c::getDebugMode(void) const
{
    return mode;
}
