namespace shy_guts
{
    namespace logic_salutation_letters_animation_transform_state
    {
        static so_called_message_common_logic_salutation_letters_animation_transform_reply msg_replied ;
        static so_called_message_common_logic_salutation_letters_animation_transform_request msg_requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_mesh_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_mesh ) taker ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_size ) taker ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_renderer_render_state
    {
        static so_called_type_platform_math_num_whole mesh_current ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
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
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_renderer_render_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_renderer_render_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_animation_transform_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_animation_transform_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_renderer_render_state :: on_requested ( )
{
    shy_guts :: request_meshes_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( )
{
    shy_guts :: start_render ( ) ;
    shy_guts :: render ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( )
{
    shy_guts :: request_current_mesh_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_transform_state :: on_replied ( )
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
    so_called_type_platform_math_num_whole mesh_current ;
    so_called_type_platform_math_num_whole meshes_total ;

    mesh_current = shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current ;
    meshes_total = shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . msg_reply . size ;

    if ( so_called_platform_conditions :: whole_less_than_whole ( mesh_current , meshes_total ) )
        shy_guts :: request_current_mesh ( ) ;
    else
        shy_guts :: send_render_finished ( ) ;
}

void shy_guts :: replied_mesh_render ( )
{
    so_called_message_common_engine_render_mesh_render msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_reply . mesh ;
    so_called_sender_common_engine_render_mesh_render :: send ( msg ) ;
}

void shy_guts :: replied_mesh_transform ( )
{
    so_called_message_common_engine_render_mesh_set_transform msg ;
    msg . mesh = shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . msg_reply . mesh ;
    msg . transform = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_replied . transform ;
    so_called_sender_common_engine_render_mesh_set_transform :: send ( msg ) ;
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
    shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested . letter =
        shy_guts :: logic_salutation_letters_renderer_render_state :: mesh_current ;

    so_called_sender_common_logic_salutation_letters_animation_transform_request :: send 
        ( shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested
        ) ;
}

void shy_guts :: request_meshes_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . request ( ) ;
}

void shy_guts :: send_render_finished ( )
{
    so_called_sender_common_logic_salutation_letters_renderer_render_reply :: send
        ( so_called_message_common_logic_salutation_letters_renderer_render_reply ( )
        ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_animation_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested . letter , msg . letter )
       )
    {
        shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_letters_animation_transform_state :: msg_replied = msg ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_reply msg )
{
    so_called_type_platform_math_num_whole should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_mesh_state :: on_replied ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg )
{
    so_called_type_platform_math_num_whole should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_replied ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: receive ( so_called_message_common_logic_salutation_letters_renderer_render_request )
{
    shy_guts :: logic_salutation_letters_renderer_render_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_letters_renderer :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
