#include "CL/cl.h"
#include <stdio.h>

#define MAX_PLATFORMS 10
#define MAX_TEXT 100

int main(void) {
    cl_uint psn;
    cl_platform_id ps[MAX_PLATFORMS];
    struct {cl_platform_info id; const char *name;} ns[] =
        {{CL_PLATFORM_PROFILE, "Profile"}, {CL_PLATFORM_VERSION, "Version"},
         {CL_PLATFORM_NAME, "Name"}, {CL_PLATFORM_VENDOR, "Vendor"}, {0, ""}};

    if (CL_SUCCESS != clGetPlatformIDs(MAX_PLATFORMS, ps, &psn)) {
        fprintf(stderr, "Cannot find any platforms\n");
        return 1;
    }
    for (int pi = 0; pi < (int)psn; ++pi) {
        fprintf(stderr, "Platform #%i:\n", pi);
        for (int ni = 0; *(ns[ni].name); ++ni) {
            char v[MAX_TEXT];
            size_t vlen;
            if (CL_SUCCESS !=
            clGetPlatformInfo(ps[pi], ns[ni].id, MAX_TEXT, v, &vlen)) {
                fprintf(stderr, "Cannot get param\n");
                return 1;
            }
            fprintf(stderr, "    %s: %s\n", ns[ni].name, v);
        }
        fprintf(stderr, "\n");
    }
    fprintf(stderr, "Hello world\n");
    return 0;
}
