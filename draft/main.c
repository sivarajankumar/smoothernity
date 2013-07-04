#include "CL/cl.h"
#include <stdio.h>

#define MAX_DEVICES 10
#define MAX_PLATFORMS 10
#define DEVICE CL_DEVICE_TYPE_CPU

#define SRC(n) \
    "__kernel void dp_sqr(__global float"#n" *a, __global float"#n" *b) {\n" \
    "   int id = get_global_id(0);\n" \
    "   b[id] = a[id] * a[id];\n" \
    "}\n"

int main(void) {
    cl_uint psn;
    cl_platform_id ps[MAX_PLATFORMS];
    cl_context ctx;
    const char *src[] = {SRC(1), SRC(2), SRC(3), SRC(4), SRC(8), SRC(16), ""};
    const int comps[] = {1, 2, 3, 4, 8, 16, 0};

    if (CL_SUCCESS != clGetPlatformIDs(MAX_PLATFORMS, ps, &psn)) {
        fprintf(stderr, "Cannot find any platforms\n");
        return 1;
    }
    for (int pi = 0; pi < (int)psn; ++pi) {
        cl_context_properties props[] = 
            {CL_CONTEXT_PLATFORM, (cl_context_properties)(ps[pi]), 0};
        ctx = clCreateContextFromType(props, DEVICE, 0, 0, 0);
    }
    if (!ctx) {
        fprintf(stderr, "Cannot create context\n");
        return 1;
    }
    for (int compi = 0; comps[compi]; ++compi) {
        cl_program prog;
        if (!(prog = clCreateProgramWithSource(ctx, 1, src + compi, 0, 0))) {
            fprintf(stderr, "Cannot create program\n");
            return 1;
        }
        if (CL_SUCCESS != clReleaseProgram(prog)) {
            fprintf(stderr, "Cannot release program\n");
            return 1;
        }
    }
    if (CL_SUCCESS != clReleaseContext(ctx)) {
        fprintf(stderr, "Cannot release context\n");
        return 1;
    }
    return 0;
}
