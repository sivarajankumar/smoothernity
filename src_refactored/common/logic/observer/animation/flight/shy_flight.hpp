namespace shy_guts
{
    namespace logic_observer_animation_flight_transform_state
    {
        static so_called_type_platform_vector_data eye ;
        static so_called_type_platform_vector_data target ;
        static so_called_type_platform_math_num_fract vertical_offset ;
        static so_called_type_platform_math_num_fract horizontal_offset ;
    }

    namespace logic_observer_update_state
    {
        static so_called_type_platform_math_num_fract time ;
    }

    static void compute_vertical_offset ( ) ;
    static void compute_horizontal_offset ( ) ;
    static void compute_eye ( ) ;
    static void compute_target ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation_flight > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_vertical_offset ( )
{
}

void shy_guts :: compute_horizontal_offset ( )
{
}

void shy_guts :: compute_eye ( )
{
}

void shy_guts :: compute_target ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_observer_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_logic_observer_animation_flight_transform_request )
{
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_logic_observer_update )
{
    so_called_type_platform_math_num_fract time_step ;
    so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
    so_called_platform_math :: add_to_fract ( shy_guts :: logic_observer_update_state :: time , time_step ) ;
}
