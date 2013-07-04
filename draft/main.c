#include "CL/cl.h"
#include <stdio.h>

#define MAX_DEVICES 10
#define MAX_PLATFORMS 10
#define DEVICE CL_DEVICE_TYPE_CPU

#define SRC(n) \
    "__kernel void mykern(__global float"n" *a, __global float"n" *b) {\n" \
    "   int id = get_global_id(0);\n" \
    "   b[id] = a[id] * a[id];\n" \
    "}\n"

int main(void) {
    cl_uint pfms_len, devs_len;
    cl_platform_id pfms[MAX_PLATFORMS];
    cl_device_id devs[MAX_DEVICES];
    cl_context ctx;
    cl_command_queue que;
    const char *src[] = {SRC(""), SRC("2"), SRC("4"), SRC("8"), SRC("16"), ""};
    const int comps[] = {1, 2, 4, 8, 16, 0};

    if (CL_SUCCESS != clGetPlatformIDs(MAX_PLATFORMS, pfms, &pfms_len)) {
        fprintf(stderr, "Cannot get platforms\n");
        return 1;
    }
    for (int pi = 0; pi < (int)pfms_len; ++pi) {
        cl_context_properties props[] = 
            {CL_CONTEXT_PLATFORM, (cl_context_properties)(pfms[pi]), 0};
        if (CL_SUCCESS !=
        clGetDeviceIDs(pfms[pi], DEVICE, MAX_DEVICES, devs, &devs_len)) {
            fprintf(stderr, "Cannot get devices\n");
            return 1;
        }
        if (!!(ctx = clCreateContext(props, devs_len, devs, 0, 0, 0)))
            goto ctx_created;
    }
    fprintf(stderr, "Cannot create context\n");
    return 1;

ctx_created:
    fprintf(stderr, "Using device 1 out of %i\n", (int)devs_len);
    if (!(que = clCreateCommandQueue(ctx, devs[0], 0, 0))) {
        fprintf(stderr, "Cannot create command queue\n");
        return 1;
    }
    for (int compi = 0; comps[compi]; ++compi) {
        cl_program prog;
        cl_kernel kern;

        fprintf(stderr, "Components %i\n", comps[compi]);
        if (!(prog = clCreateProgramWithSource(ctx, 1, src + compi, 0, 0)) ||
        CL_SUCCESS != clBuildProgram(prog, 0, 0, "-cl-std=CL1.1", 0, 0) ||
        !(kern = clCreateKernel(prog, "mykern", 0))) {
            fprintf(stderr, "Cannot create program\n");
            return 1;
        }
        if (CL_SUCCESS != clReleaseKernel(kern) ||
        CL_SUCCESS != clReleaseProgram(prog)) {
            fprintf(stderr, "Cannot release program\n");
            return 1;
        }
    }
    if (CL_SUCCESS != clReleaseCommandQueue(que) ||
    CL_SUCCESS != clReleaseContext(ctx)) {
        fprintf(stderr, "Cannot release context\n");
        return 1;
    }
    return 0;
}
