#include "iphone_platform.hpp"

shy_iphone_platform_insider :: shy_iphone_platform_insider ( )
{
    render_insider . set_platform_insider ( this ) ;
    sound_insider . set_platform_insider ( this ) ;
    touch_insider . set_platform_insider ( this ) ;
    platform . math_consts . set ( math_consts ) ;
    platform . mouse . set ( mouse ) ;
    platform . render . set ( render ) ;
    platform . sound . set ( sound ) ;
    platform . touch . set ( touch ) ;
}
