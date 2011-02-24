namespace shy_guts
{
    namespace logic_observer_animation_consts
    {
        static const so_called_type_platform_math_num_fract up_x = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract up_y = so_called_platform_math :: init_num_fract ( 1 , 1 ) ;
        static const so_called_type_platform_math_num_fract up_z = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
    }

    namespace logic_observer_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_observer_animation_flight_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data eye ;
        static so_called_type_platform_vector_data target ;
    }

    static void proceed_with_transform ( ) ;
    static void request_flight_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
}

void shy_guts :: request_flight_transform ( )
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

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_logic_observer_animation_flight_transform_reply )
{
}

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_logic_observer_animation_transform_request )
{
}
