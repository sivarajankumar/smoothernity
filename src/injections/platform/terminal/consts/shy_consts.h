#ifndef _shy_injections_platform_terminal_consts_included
#define _shy_injections_platform_terminal_consts_included

#ifdef shy_build_for_iphone
    #include "../../../../main/iphone/platform/terminal/consts/shy_consts_injections.h"
#endif

#ifdef shy_build_for_macosx
    #include "../../../../main/macosx/platform/terminal/consts/shy_consts_injections.h"
#endif

#ifdef shy_build_for_win
    #include "../../../../main/win/platform/terminal/consts/shy_consts_injections.h"
#endif

#endif
