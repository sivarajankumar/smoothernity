class shy_guts
{
public :
    class consts
    {
    public :
        static const so_called_type_platform_math_num_fract z_far ;
        static const so_called_type_platform_math_num_fract z_near ;
    } ;
public :
    static void init_render ( ) ;
    static void get_near_plane_distance ( so_called_type_platform_math_num_fract & ) ;
public :
    static so_called_type_platform_math_num_whole fidget_prepared ;
    
    static so_called_type_platform_math_num_whole render_aspect_requested ;
    static so_called_type_platform_math_num_fract render_aspect_width ;
    static so_called_type_platform_math_num_fract render_aspect_height ;
    
    static so_called_type_platform_math_num_whole handling_near_plane_distance_request ;
    static so_called_type_platform_math_num_whole handling_use_ortho_projection_request ;
    static so_called_type_platform_math_num_whole handling_use_perspective_projection_request ;
} ;

const so_called_type_platform_math_num_fract shy_guts :: consts :: z_far = so_called_platform_math :: init_num_fract ( 50 , 1 ) ;
const so_called_type_platform_math_num_fract shy_guts :: consts :: z_near = so_called_platform_math :: init_num_fract ( 1 , 1 ) ;

so_called_type_platform_math_num_whole shy_guts :: fidget_prepared ;

so_called_type_platform_math_num_whole shy_guts :: render_aspect_requested ;
so_called_type_platform_math_num_fract shy_guts :: render_aspect_width ;
so_called_type_platform_math_num_fract shy_guts :: render_aspect_height ;

so_called_type_platform_math_num_whole shy_guts :: handling_near_plane_distance_request ;
so_called_type_platform_math_num_whole shy_guts :: handling_use_ortho_projection_request ;
so_called_type_platform_math_num_whole shy_guts :: handling_use_perspective_projection_request ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_core > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: init_render ( )
{
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
    so_called_sender_common_engine_render_enable_face_culling :: send ( so_called_message_common_engine_render_enable_face_culling ( ) ) ;
    so_called_sender_common_engine_render_texture_mode_modulate :: send ( so_called_message_common_engine_render_texture_mode_modulate ( ) ) ;
}

void _shy_common_logic_core :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_core :: receive ( so_called_message_common_init )
{
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_near_plane_distance_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_use_ortho_projection_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: handling_use_perspective_projection_request = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_prepared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: init_render ( ) ;
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
