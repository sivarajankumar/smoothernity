#include "DXUT.h"
#include "win_platform.hpp"

shy_win_platform_insider :: shy_win_platform_insider ( )
{
    mouse_insider . set_platform_insider ( this ) ;
    render_insider . set_platform_insider ( * this ) ;
    platform_pointer :: bind ( platform . math_consts , math_consts ) ;
    platform_pointer :: bind ( platform . mouse , mouse ) ;
    platform_pointer :: bind ( platform . render , render ) ;
    platform_pointer :: bind ( platform . sound , sound ) ;
    platform_pointer :: bind ( platform . touch , touch ) ;
}
