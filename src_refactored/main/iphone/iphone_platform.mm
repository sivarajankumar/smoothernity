#include "iphone_platform.hpp"

shy_iphone_platform_insider :: shy_iphone_platform_insider ( )
{
    render_insider . set_platform_insider ( this ) ;
    sound_insider . set_platform_insider ( this ) ;
    touch_insider . set_platform_insider ( this ) ;
    platform_pointer :: bind ( platform . math_consts , math_consts ) ;
    platform_pointer :: bind ( platform . mouse , mouse ) ;
    platform_pointer :: bind ( platform . render , render ) ;
    platform_pointer :: bind ( platform . sound , sound ) ;
    platform_pointer :: bind ( platform . touch , touch ) ;
}
