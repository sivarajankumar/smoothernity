#include "iphone_platform.hpp"

shy_iphone_platform_insider :: shy_iphone_platform_insider ( )
{
    render_insider . set_platform_insider ( this ) ;
    sound_insider . set_platform_insider ( this ) ;
    touch_insider . set_platform_insider ( this ) ;
    platform . math_consts = math_consts ;
    platform . mouse = mouse ;
    platform . render = render ;
    platform . sound = sound ;
    platform . touch = touch ;
}
