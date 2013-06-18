#ifndef CUTIL_H
#define CUTIL_H

#include "lua.h"

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int cutil_isfloat(lua_State*, int);
int cutil_isint(lua_State*, int);

#endif /* CUTIL_H */

