#ifdef shy_build_loadable_way
    #ifndef shy_build_with_stl
        #error "Loadable build requires STL."
    #endif
    #ifndef shy_build_with_generator
        #error "Loadable build requires generator."
    #endif
#endif

#ifdef shy_build_with_generator
    #ifndef shy_build_with_stl
        #error "Build with generator requires STL."
    #endif
#endif

#ifdef shy_build_with_profile
    #ifndef shy_build_with_stl
        #error "Build with profiling requires STL."
    #endif
    #ifndef shy_build_with_generator
        #error "Build with profiling requires generator."
    #endif
#endif

#ifdef shy_build_with_trace
    #ifndef shy_build_with_stl
        #error "Build with tracing requires STL."
    #endif
#endif

#if ! ( ( (   defined shy_build_loadable_way ) && ( ! defined shy_build_static_way ) ) \
     || ( ( ! defined shy_build_loadable_way ) && (   defined shy_build_static_way ) ) \
      )
    #error "External data handling style must be specified."
#endif

#if ! ( ( (   defined shy_build_with_generator ) && ( ! defined shy_build_without_generator ) ) \
     || ( ( ! defined shy_build_with_generator ) && (   defined shy_build_without_generator ) ) \
      )
    #error "Generator mode must be specified."
#endif

#if ! ( ( (   defined shy_build_with_profile ) && ( ! defined shy_build_without_profile ) ) \
     || ( ( ! defined shy_build_with_profile ) && (   defined shy_build_without_profile ) ) \
      )
    #error "Profiling mode must be specified."
#endif

#if ! ( ( (   defined shy_build_with_trace ) && ( ! defined shy_build_without_trace ) ) \
     || ( ( ! defined shy_build_with_trace ) && (   defined shy_build_without_trace ) ) \
      )
    #error "Tracing mode must be specified."
#endif

#if ! ( ( (   defined shy_scheduling_mode_random ) && ( ! defined shy_scheduling_mode_direct_call ) ) \
     || ( ( ! defined shy_scheduling_mode_random ) && (   defined shy_scheduling_mode_direct_call ) ) \
      )
    #error "Scheduling mode must be specified."
#endif

#if ! ( ( (   defined shy_build_for_iphone ) && ( ! defined shy_build_for_macosx ) && ( ! defined shy_build_for_win ) ) \
     || ( ( ! defined shy_build_for_iphone ) && (   defined shy_build_for_macosx ) && ( ! defined shy_build_for_win ) ) \
     || ( ( ! defined shy_build_for_iphone ) && ( ! defined shy_build_for_macosx ) && (   defined shy_build_for_win ) ) \
      )
    #error "Platform for build must be specified."
#endif
