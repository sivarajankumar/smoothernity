#include "macosx_platform.hpp"

shy_macosx_platform_insider :: shy_macosx_platform_insider ( )
{
    mouse_insider . set_platform_insider ( this ) ;
    render_insider . set_platform_insider ( this ) ;
    sound_insider . set_platform_insider ( this ) ;
    platform . math_consts = math_consts ;
    platform . mouse = mouse ;
    platform . render = render ;
    platform . sound = sound ;
    platform . touch = touch ;
}
