namespace shy_guts
{
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_layout > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_salutation_letters_animation_layout :: receive ( so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg )
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

    so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . origin = origin ;
    msg_reply . scale = scale ;
    so_called_sender_common_logic_salutation_letters_animation_layout_transform_reply :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_layout :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
