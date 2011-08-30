namespace shy_guts
{
    namespace logic_salutation_letters_animation_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_mesh_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_mesh ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_size ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_renderer_render_state
    {
        static so_called_platform_math_num_whole_type mesh_current ;
        static void on_request ( ) ;
    }

    static void move_to_next_mesh ( ) ;
    static void render ( ) ;
    static void replied_mesh_render ( ) ;
    static void replied_mesh_transform ( ) ;
    static void request_meshes_amount_in_storage ( ) ;
    static void request_current_mesh ( ) ;
    static void request_current_mesh_transform ( ) ;
    static void send_render_finished ( ) ;
    static void start_render ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_request ( )
{
    shy_guts :: request_meshes_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( )
{
    shy_guts :: start_render ( ) ;
    shy_guts :: render ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_reply ( )
{
    shy_guts :: request_current_mesh_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_transform_state :: on_reply ( )
{
    shy_guts :: replied_mesh_transform ( ) ;
    shy_guts :: replied_mesh_render ( ) ;
    shy_guts :: move_to_next_mesh ( ) ;
    shy_guts :: render ( ) ;
}

void shy_guts :: start_render ( )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current = so_called_platform_math_consts :: whole_0 ;
}

void shy_guts :: render ( )
{
    so_called_platform_math_num_whole_type mesh_current ;
    so_called_platform_math_num_whole_type meshes_total ;

    mesh_current = shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current ;
    meshes_total = shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . msg_reply . size ;

    if ( so_called_platform_conditions :: whole_less_than_whole ( mesh_current , meshes_total ) )
        shy_guts :: request_current_mesh ( ) ;
    else
        shy_guts :: send_render_finished ( ) ;
}

void shy_guts :: replied_mesh_render ( )
{
    so_called_common_engine_render_mesh_render_message msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_reply . mesh ;
    so_called_common_engine_render_mesh_render_sender :: send ( msg ) ;
}

void shy_guts :: replied_mesh_transform ( )
{
    so_called_common_engine_render_mesh_set_transform_message msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_reply . mesh ;
    msg . transform = shy_guts :: logic_salutation_letters_animation_transform_state :: taker . msg_reply . transform ;
    so_called_common_engine_render_mesh_set_transform_sender :: send ( msg ) ;
}

void shy_guts :: move_to_next_mesh ( )
{
    so_called_platform_math :: inc_whole
        ( shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current
        ) ;
}

void shy_guts :: request_current_mesh ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_request . index = shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . request ( ) ;
}

void shy_guts :: request_current_mesh_transform ( )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: taker . msg_request . letter = shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_meshes_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . request ( ) ;
}

void shy_guts :: send_render_finished ( )
{
    so_called_common_logic_salutation_letters_renderer_render_reply_sender :: send
        ( so_called_common_logic_salutation_letters_renderer_render_reply_message ( )
        ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_common_logic_salutation_letters_animation_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_common_logic_salutation_letters_meshes_storage_mesh_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_common_logic_salutation_letters_meshes_storage_size_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_common_logic_salutation_letters_renderer_render_request_message )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
