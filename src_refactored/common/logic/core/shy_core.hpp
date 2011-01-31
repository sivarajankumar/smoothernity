class shy_guts
{
public :
    class consts
    {
    public :
        static const so_called_type_platform_math_num_fract z_far ;
        static const so_called_type_platform_math_num_fract z_near ;
    } ;
} ;

const so_called_type_platform_math_num_fract shy_guts :: consts :: z_far = so_called_platform_math :: init_num_fract ( 50 , 1 ) ;
const so_called_type_platform_math_num_fract shy_guts :: consts :: z_near = so_called_platform_math :: init_num_fract ( 1 , 1 ) ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_core > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_core :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_near_plane_distance_request )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_use_ortho_projection_request )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_logic_core_use_perspective_projection_request )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_render )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_update )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_video_mode_changed )
{
}
