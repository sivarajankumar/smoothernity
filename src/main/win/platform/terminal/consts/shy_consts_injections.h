#ifndef _shy_win_platform_terminal_consts_injections_included
#define _shy_win_platform_terminal_consts_injections_included

#ifdef shy_build_with_trace
    #include "src/platform/terminal/consts/ansi/shy_ansi_injections.h"
    typedef so_called_platform_terminal_consts_ansi so_called_platform_terminal_consts ;
#endif

#endif
