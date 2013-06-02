#ifndef PHYSICS_PHYSDBG_H
#define PHYSICS_PHYSDBG_H

#define PHYSDBG(op) \
    op(NoDebug) op(DrawWireframe) op(DrawAabb) op(DrawFeaturesText) \
    op(DrawContactPoints) op(NoDeactivation) op(NoHelpText) op(DrawText) \
    op(ProfileTimings) op(EnableSatComparison) op(DisableBulletLCP) \
    op(EnableCCD) op(DrawConstraints) op(DrawConstraintLimits) \
    op(FastWireframe) op(DrawNormals)

#define DECL(x) extern const int PHYSDBG_##x;
PHYSDBG(DECL)
#undef DECL

#endif /* PHYSICS_PHYSDBG_H */
