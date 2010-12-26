#ifndef _platform_included_
#define _platform_included_

#if build_for_iphone
    #include "iphone_platform.hpp"
    typedef iphone_platform so_called_platform ;
#elif build_for_macosx
    #include "macosx_platform.hpp"
    typedef macosx_platform so_called_platform ;
#else
    #error build target must be specified
#endif

#endif

