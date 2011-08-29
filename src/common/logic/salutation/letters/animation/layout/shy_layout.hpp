namespace shy_guts
{
    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg_request ;
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
    so_called_type_platform_vector_data origin ;
    so_called_platform_vector :: xyz
        ( origin
        , so_called_platform_math_consts :: fract_0
        , so_called_platform_math_consts :: fract_0
        , so_called_platform_math_consts :: fract_0
        ) ;

    so_called_type_platform_math_num_fract scale ;
    scale = so_called_platform_math_consts :: fract_1 ;

    so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_request . letter ;
    msg . origin = origin ;
    msg . scale = scale ;
    so_called_common_logic_salutation_letters_animation_layout_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg )
{
    so_called_type_platform_math_num_whole should_handle ;
    shy_guts :: logic_salutation_letters_meshes_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_storage_size_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_request = msg ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
