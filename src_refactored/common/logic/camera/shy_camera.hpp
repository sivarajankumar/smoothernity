#include "shy_camera.h"

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_camera > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_camera :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

