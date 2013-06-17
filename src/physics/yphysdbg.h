#ifndef YPHYSDBG_H
#define YPHYSDBG_H

#define YPHYSDBG(op) \
    op(NoDebug) op(DrawWireframe) op(DrawAabb) op(DrawFeaturesText) \
    op(DrawContactPoints) op(NoDeactivation) op(NoHelpText) op(DrawText) \
    op(ProfileTimings) op(EnableSatComparison) op(DisableBulletLCP) \
    op(EnableCCD) op(DrawConstraints) op(DrawConstraintLimits) \
    op(FastWireframe) op(DrawNormals)

#define DECL(x) extern const int YPHYSDBG_##x;
YPHYSDBG(DECL)
#undef DECL

#endif /* YPHYSDBG_H */
