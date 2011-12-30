namespace shy_guts
{
    namespace engine_render_aspect_state
    {
        static so_called_common_engine_taker_helper ( engine_render_aspect ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_common_logic_salutation_letters_animation_layout_transform_request_message msg_request ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_meshes_storage_size_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_storage_size ) taker ;
        static void on_reply ( ) ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_layout > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_request ( )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . request ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( )
{
    shy_guts :: engine_render_aspect_state :: taker . request ( ) ;
}

void shy_guts :: engine_render_aspect_state :: on_reply ( )
{
    so_called_platform_vector_data_type origin ;
    so_called_platform_math_num_fract_type scale ;

    so_called_common_logic_text_stateless :: layout_letters_in_a_row
        ( origin
        , scale
        , shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_request . letter
        , shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . msg_reply . size
        , so_called_common_logic_salutation_letters_meshes_consts :: mesh_size
        , so_called_common_logic_salutation_letters_meshes_consts :: mesh_size
        , so_called_common_logic_salutation_letters_animation_consts :: layout_step
        , so_called_common_logic_salutation_letters_animation_consts :: layout_border_width
        , so_called_common_logic_salutation_letters_animation_consts :: layout_border_height
        , shy_guts :: engine_render_aspect_state :: taker . msg_reply . width
        , shy_guts :: engine_render_aspect_state :: taker . msg_reply . height
        ) ;

    so_called_common_logic_salutation_letters_animation_layout_transform_reply_message msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_request . letter ;
    msg . origin = origin ;
    msg . scale = scale ;
    so_called_common_logic_salutation_letters_animation_layout_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_render_aspect_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_common_engine_render_aspect_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: engine_render_aspect_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: engine_render_aspect_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_common_logic_salutation_letters_meshes_storage_size_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_common_logic_salutation_letters_animation_layout_transform_request_message msg )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_request = msg ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
