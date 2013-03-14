#include "interp.h"

float interp_spline(float t, float v0, float v1, float v2, float v3)
{
    float v, tt, ttt;
    tt = t * t;
    ttt = tt * t;
    v = 2.0f * v1;
    v += t * (-v0 + v2);
    v += tt * (2.0f*v0 - 5.0f*v1 + 4.0f*v2 - v3);
    v += ttt * (-v0 + 3.0f*v1 - 3.0f*v2 + v3);
    v *= 0.5f;
    return v;
}

float interp_linear(float t, float v0, float v1)
{
    return v0 + (t * (v1 - v0));
}
