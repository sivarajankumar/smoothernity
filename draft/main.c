#include "CL/cl.h"
#include <stdio.h>
#include <math.h>
#include <limits.h>

#define MAX_RUNS 10
#define MAX_DEVICES 10
#define MAX_PLATFORMS 10
#define REPORT_FLOATS 0
#define MAX_FLOATS (1 << 18)
#define WG_SIZE (1 << 8)
#define BUF_SIZE (sizeof(float)*MAX_FLOATS)
#define DEVICE CL_DEVICE_TYPE_CPU

#define SRC(n) \
    "__kernel void mykern(__global float"n" *a, __global float"n" *b) {\n" \
    "   int id = get_global_id(0);\n" \
    "   float"n" aa = a[id], bb;\n" \
    "   for (int i = 0; i < 10000; ++i)\n" \
    "       bb = 2*bb + aa;\n" \
    "   b[id] = bb;\n" \
    "}\n"

int main(void) {
    cl_uint pfms_len, devs_len, comp_nat, comp_pref;
    cl_platform_id pfms[MAX_PLATFORMS];
    cl_device_id devs[MAX_DEVICES];
    cl_context ctx;
    cl_mem memr, memw;
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
    if (!(que=clCreateCommandQueue(ctx,devs[0],CL_QUEUE_PROFILING_ENABLE,0)) ||
    !(memr = clCreateBuffer(ctx, CL_MEM_READ_ONLY, BUF_SIZE, 0, 0)) ||
    !(memw = clCreateBuffer(ctx, CL_MEM_WRITE_ONLY, BUF_SIZE, 0, 0)) ||
    CL_SUCCESS!=clGetDeviceInfo(devs[0], CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT,
                                sizeof(cl_uint), &comp_pref, 0) ||
    CL_SUCCESS!=clGetDeviceInfo(devs[0], CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT,
                                sizeof(cl_uint), &comp_nat, 0)) {
        fprintf(stderr, "Cannot create command queue\n");
        return 1;
    }
    fprintf(stderr, "Float vector width: native %i, preferred %i\n",
            (int)comp_nat, (int)comp_pref);
    for (int compi = 0; comps[compi]; ++compi) {
        cl_program prog;
        cl_kernel kern;
        cl_event evt_end, evt_kern[MAX_RUNS];
        float *mapr, *mapw;
        int time_min = INT_MAX, time_max = 0, time_sum = 0;

        if (!(prog = clCreateProgramWithSource(ctx, 1, src + compi, 0, 0)) ||
        CL_SUCCESS != clBuildProgram(prog, 0, 0, "-cl-std=CL1.1", 0, 0) ||
        !(kern = clCreateKernel(prog, "mykern", 0)) ||
        CL_SUCCESS != clSetKernelArg(kern, 0, sizeof(cl_mem), &memr) ||
        CL_SUCCESS != clSetKernelArg(kern, 1, sizeof(cl_mem), &memw)) {
            fprintf(stderr, "Cannot create program\n");
            return 1;
        }
        if (!(mapr = clEnqueueMapBuffer(que, memr, CL_TRUE, CL_MAP_WRITE,
        0, BUF_SIZE, 0, 0, 0, 0))) {
            fprintf(stderr, "Cannot map read buffer\n");
            return 1;
        }
        for (int i = 0; i < MAX_FLOATS; ++i)
            mapr[i] = (float)(rand() % 10);
        if (CL_SUCCESS != clEnqueueUnmapMemObject(que, memr, mapr, 0, 0, 0)) {
            fprintf(stderr, "Cannot unmap read buffer\n");
            return 1;
        }
        for (int i = 0; i < MAX_RUNS; ++i) {
            size_t glob_size = MAX_FLOATS / (size_t)comps[compi];
            size_t local_size = WG_SIZE;

            if (CL_SUCCESS != clEnqueueNDRangeKernel(
            que, kern, 1, 0, &glob_size, &local_size, 0, 0, evt_kern + i)){
                fprintf(stderr, "Cannot execute kernel\n");
                return 1;
            }
        }
        if (CL_SUCCESS != clEnqueueMarker(que, &evt_end) ||
        CL_SUCCESS != clWaitForEvents(1, &evt_end)) {
            fprintf(stderr, "Cannot wait for event\n");
            return 1;
        }
        for (int i = 0; i < MAX_RUNS; ++i) {
            int t;
            cl_ulong time_start, time_end;
            if (CL_SUCCESS != clGetEventProfilingInfo(evt_kern[i],
            CL_PROFILING_COMMAND_START, sizeof(cl_ulong), &time_start, 0)
            || CL_SUCCESS != clGetEventProfilingInfo(evt_kern[i],
            CL_PROFILING_COMMAND_END, sizeof(cl_ulong), &time_end, 0)) {
                fprintf(stderr, "Cannot get profiling info\n");
                return 1;
            }
            t = (int)((time_end - time_start) / 1000);
            if (time_min > t)
                time_min = t;
            if (time_max < t)
                time_max = t;
            time_sum += t;
        }
        time_sum /= MAX_RUNS;
        fprintf(stderr, "Components: %i, time: %i us (+-%i%%)\n", comps[compi],
                time_sum, (50 * (time_max - time_min)) / time_sum);
        if (!(mapr = clEnqueueMapBuffer(que, memr, CL_TRUE, CL_MAP_READ,
                                        0, BUF_SIZE, 0, 0, 0, 0)) ||
        !(mapw = clEnqueueMapBuffer(que, memw, CL_TRUE, CL_MAP_READ,
                                    0, BUF_SIZE, 0, 0, 0, 0))) {
            fprintf(stderr, "Cannot map buffers\n");
            return 1;
        }
        for (int i = 0; i < REPORT_FLOATS; ++i) {
            fprintf(stderr, "%i : %i\n", (int)mapr[i], (int)mapw[i]);
        }
        if (CL_SUCCESS != clEnqueueUnmapMemObject(que, memr, mapr, 0, 0, 0) ||
        CL_SUCCESS != clEnqueueUnmapMemObject(que, memw, mapw, 0, 0, 0) ||
        CL_SUCCESS != clReleaseKernel(kern) ||
        CL_SUCCESS != clReleaseProgram(prog)) {
            fprintf(stderr, "Cannot release program\n");
            return 1;
        }
    }
    if (CL_SUCCESS != clReleaseMemObject(memr) ||
    CL_SUCCESS != clReleaseMemObject(memw) ||
    CL_SUCCESS != clReleaseCommandQueue(que) ||
    CL_SUCCESS != clReleaseContext(ctx)) {
        fprintf(stderr, "Cannot release context\n");
        return 1;
    }
    return 0;
}
