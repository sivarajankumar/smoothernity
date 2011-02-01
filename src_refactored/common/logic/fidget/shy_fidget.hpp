namespace shy_guts
{
    static void update_fidget ( ) ;
    static void render_fidget_mesh ( ) ;
    static void create_fidget_mesh ( ) ;

    static so_called_type_platform_math_num_fract fidget_angle ;
    static so_called_type_platform_math_num_whole fidget_prepare_permitted ;
    static so_called_type_platform_math_num_whole fidget_mesh_created ;
    static so_called_type_platform_math_num_whole fidget_scale ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_platform_math_num_whole render_aspect_requested ;
    static so_called_type_platform_math_num_whole render_aspect_replied ;
    static so_called_type_platform_math_num_fract render_aspect_height ;
    static so_called_type_platform_math_num_whole render_frame_loss_requested ;
    static so_called_type_platform_math_num_whole render_frame_loss_replied ;
    static so_called_type_platform_math_num_whole render_frame_loss ;
    static so_called_type_common_engine_render_mesh_id fidget_mesh_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fidget > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_fidget ( )
{
}

void shy_guts :: render_fidget_mesh ( )
{
}

void shy_guts :: create_fidget_mesh ( )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_aspect_reply )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_frame_loss_reply )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_prepare_permit )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_render_request )
{
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_update )
{
}
