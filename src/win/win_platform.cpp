#include "DXUT.h"
#include "win_platform.hpp"

shy_win_platform_insider :: shy_win_platform_insider ( )
{
    render_insider . set_platform_insider ( * this ) ;
    platform . math_consts . set ( math_consts ) ;
    platform . mouse . set ( mouse ) ;
    platform . render . set ( render ) ;
    platform . sound . set ( sound ) ;
    platform . touch . set ( touch ) ;
}
