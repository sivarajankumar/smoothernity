#ifndef _shy_macosx_platform_terminal_consts_injections_included
#define _shy_macosx_platform_terminal_consts_injections_included

#ifdef shy_build_with_trace
    #include "platform/terminal/consts/ansi/shy_ansi_injections.h"
    typedef so_called_platform_terminal_consts_ansi so_called_platform_terminal_consts ;
#endif

#endif
