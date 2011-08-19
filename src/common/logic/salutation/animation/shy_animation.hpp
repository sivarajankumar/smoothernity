namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_fract origin_x = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_type_platform_math_num_fract origin_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_type_platform_math_num_fract origin_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_logic_salutation_animation_transform_request )
{
    so_called_type_platform_vector_data origin ;
    so_called_platform_vector :: xyz 
        ( origin
        , shy_guts :: consts :: origin_x
        , shy_guts :: consts :: origin_y
        , shy_guts :: consts :: origin_z
        ) ;

    so_called_message_common_logic_salutation_animation_transform_reply msg ;
    so_called_platform_matrix :: identity ( msg . transform ) ;
    so_called_platform_matrix :: set_origin ( msg . transform , origin ) ;
    so_called_sender_common_logic_salutation_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_logic_salutation_animation_zoom_transform_reply )
{
}

void _shy_common_logic_salutation_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
