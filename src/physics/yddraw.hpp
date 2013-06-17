#ifndef YDDRAW_HPP
#define YDDRAW_HPP

#include "btBulletDynamicsCommon.h"

class yddraw_c: public btIDebugDraw {
public:
    yddraw_c();
    virtual ~yddraw_c();
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

#endif /* YDDRAW_HPP */

