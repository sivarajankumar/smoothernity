#ifndef YMSTATE_HPP
#define YMSTATE_HPP

#include "btBulletDynamicsCommon.h"

class ymstate_c: public btMotionState {
public:
    ymstate_c();
    virtual ~ymstate_c();
    virtual void getWorldTransform(btTransform &) const;
    virtual void setWorldTransform(const btTransform &);

    btTransform m;
};

#endif /* YMSTATE_HPP */

