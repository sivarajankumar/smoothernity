#pragma once

#include <btBulletDynamicsCommon.h>

class ddraw_c: public btIDebugDraw
{
public:
    ddraw_c();
    virtual ~ddraw_c();
    virtual void drawLine(const btVector3&, const btVector3&, const btVector3&);
    virtual void drawContactPoint(const btVector3&, const btVector3&,
                                  btScalar, int, const btVector3&);
    virtual void reportErrorWarning(const char *text);
    virtual void draw3dText(const btVector3 &pos, const char *text);
    virtual void setDebugMode(int mode);
    virtual int getDebugMode(void) const;

private:
    int mode;
};
