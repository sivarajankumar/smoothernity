#ifndef PHYSICS_MSTATE_HPP
#define PHYSICS_MSTATE_HPP

#include "btBulletDynamicsCommon.h"

class mstate_c: public btMotionState {
public:
    mstate_c();
    virtual ~mstate_c();
    virtual void getWorldTransform(btTransform &) const;
    virtual void setWorldTransform(const btTransform &);

    btTransform m;
};

#endif /* PHYSICS_MSTATE_HPP */

