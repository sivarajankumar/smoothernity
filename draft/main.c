#include "CL/cl.h"
#include <stdio.h>

#define MAX_DEVICES 10
#define MAX_PLATFORMS 10
#define DEVICE CL_DEVICE_TYPE_CPU

int main(void) {
    cl_uint psn;
    cl_platform_id ps[MAX_PLATFORMS];
    cl_context ctx;

    if (CL_SUCCESS != clGetPlatformIDs(MAX_PLATFORMS, ps, &psn)) {
        fprintf(stderr, "Cannot find any platforms\n");
        return 1;
    }
    for (int pi = 0; pi < (int)psn; ++pi) {
        cl_context_properties props[] = {CL_CONTEXT_PLATFORM, (cl_context_properties)(ps[pi]), 0};
        ctx = clCreateContextFromType(props, DEVICE, 0, 0, 0);
    }
    if (!ctx) {
        fprintf(stderr, "Cannot create context\n");
        return 1;
    }
    fprintf(stderr, "Hello world\n");
    return 0;
}
