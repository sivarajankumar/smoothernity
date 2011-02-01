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

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_aspect_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_aspect_requested ) )
    {
        shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_aspect_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: render_aspect_height = msg . height ;
        shy_guts :: update_fidget ( ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_frame_loss_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: render_frame_loss_requested ) )
    {
        shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: render_frame_loss_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: render_frame_loss = msg . frame_loss ;
        shy_guts :: update_fidget ( ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: fidget_mesh_id = msg . mesh ;
        shy_guts :: create_fidget_mesh ( ) ;
        shy_guts :: fidget_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_fidget_prepared :: send ( so_called_message_common_logic_fidget_prepared ( ) ) ;
    }
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_init )
{
    shy_guts :: fidget_angle = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: fidget_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: fidget_scale = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_aspect_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: render_frame_loss_replied = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_prepare_permit )
{
    shy_guts :: fidget_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_fidget_consts :: should_render_fidget ) )
    {
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_mesh_created ) )
            shy_guts :: render_fidget_mesh ( ) ;
    }
    so_called_sender_common_logic_fidget_render_reply :: send ( so_called_message_common_logic_fidget_render_reply ( ) ) ;
}

void _shy_common_logic_fidget :: receive ( so_called_message_common_logic_fidget_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: fidget_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: fidget_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
            
            so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = so_called_common_logic_fidget_consts :: fidget_edges ;
            mesh_create_msg . triangle_fan_indices = so_called_common_logic_fidget_consts :: fidget_edges ;
            mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
        }
        else
        {
            shy_guts :: render_aspect_requested = so_called_platform_math_consts :: whole_true ;
            shy_guts :: render_frame_loss_requested = so_called_platform_math_consts :: whole_true ;
            so_called_sender_common_engine_render_aspect_request :: send ( so_called_message_common_engine_render_aspect_request ( ) ) ;
            so_called_sender_common_engine_render_frame_loss_request :: send ( so_called_message_common_engine_render_frame_loss_request ( ) ) ;
        }
    }
}
