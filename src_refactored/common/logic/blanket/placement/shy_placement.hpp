namespace shy_guts
{
    namespace logic_blanket_place_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_blanket_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_matrix_data transform ;
    }

    static void proceed_with_place ( ) ;
    static void request_animation_transform ( ) ;
    static void transform_mesh ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_placement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_place ( )
{
}

void shy_guts :: request_animation_transform ( )
{
}

void shy_guts :: transform_mesh ( )
{
}

void _shy_common_logic_blanket_placement :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_blanket_placement :: receive ( so_called_message_common_logic_blanket_animation_transform_reply )
{
}

void _shy_common_logic_blanket_placement :: receive ( so_called_message_common_logic_blanket_place )
{
}
