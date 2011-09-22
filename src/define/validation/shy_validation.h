#ifdef shy_build_loadable_way
    #ifndef shy_build_with_stl
        #error Loadable build requires STL.
    #endif
#endif

#ifdef shy_build_with_trace
    #ifndef shy_build_with_stl
        #error Build with tracing requires STL.
    #endif
#endif

#ifdef shy_build_with_profile
    #ifndef shy_build_with_stl
        #error Build with profiling requires STL.
    #endif
#endif
