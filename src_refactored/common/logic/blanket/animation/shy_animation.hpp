namespace shy_guts
{
    namespace logic_blanket_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_blanket_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
        static so_called_type_platform_math_num_fract rotation ;
    }

    namespace logic_blanket_animation_disappear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
        static so_called_type_platform_math_num_fract rotation ;
    }

    namespace logic_blanket_animation_fit_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale ;
    }

    static void proceed_with_transform ( ) ;
    static void request_appear_transform ( ) ;
    static void request_disappear_transform ( ) ;
    static void request_fit_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: request_appear_transform ( )
{
}

void shy_guts :: request_disappear_transform ( )
{
}

void shy_guts :: request_fit_transform ( )
{
}

void shy_guts :: reply_computed_transform ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_blanket_animation :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_blanket_animation :: receive ( so_called_message_common_logic_blanket_animation_appear_transform_reply )
{
}

void _shy_common_logic_blanket_animation :: receive ( so_called_message_common_logic_blanket_animation_disappear_transform_reply )
{
}

void _shy_common_logic_blanket_animation :: receive ( so_called_message_common_logic_blanket_animation_fit_transform_reply )
{
}

void _shy_common_logic_blanket_animation :: receive ( so_called_message_common_logic_blanket_animation_transform_request )
{
}
