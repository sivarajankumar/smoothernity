#include "macosx_platform.hpp"

shy_macosx_platform_insider :: shy_macosx_platform_insider ( )
{
    mouse_insider . set_platform_insider ( this ) ;
    render_insider . set_platform_insider ( this ) ;
    sound_insider . set_platform_insider ( this ) ;
}

void shy_macosx_platform_insider :: register_platform_modules ( shy_macosx_platform & platform )
{
    platform . math_consts . set ( math_consts ) ;
    platform . mouse . set ( mouse ) ;
    platform . render . set ( render ) ;
    platform . sound . set ( sound ) ;
}
