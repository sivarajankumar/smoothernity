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
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract vertical_offset ;
    so_called_type_platform_math_num_fract vertical_offset_period ;
    so_called_type_platform_math_num_fract vertical_offset_amplitude ;
    so_called_type_platform_math_num_fract vertical_offset_phase ;

    time = shy_guts :: logic_observer_update_state :: time ;
    vertical_offset_period = so_called_common_logic_observer_animation_consts :: flight_vertical_offset_period ;
    vertical_offset_amplitude = so_called_common_logic_observer_animation_consts :: flight_vertical_offset_amplitude ;

    so_called_platform_math :: mul_fracts ( vertical_offset_phase , time , so_called_platform_math_consts :: fract_2pi ) ;
    so_called_platform_math :: div_fract_by ( vertical_offset_phase , vertical_offset_period ) ;

    so_called_platform_math :: sin ( vertical_offset , vertical_offset_phase ) ;
    so_called_platform_math :: mul_fract_by ( vertical_offset , vertical_offset_amplitude ) ;

    shy_guts :: logic_observer_animation_flight_transform_state :: vertical_offset = vertical_offset ;
}

void shy_guts :: compute_horizontal_offset ( )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract horizontal_offset ;
    so_called_type_platform_math_num_fract horizontal_offset_period ;
    so_called_type_platform_math_num_fract horizontal_offset_amplitude ;
    so_called_type_platform_math_num_fract horizontal_offset_phase ;

    time = shy_guts :: logic_observer_update_state :: time ;
    horizontal_offset_period = so_called_common_logic_observer_animation_consts :: flight_horizontal_offset_period ;
    horizontal_offset_amplitude = so_called_common_logic_observer_animation_consts :: flight_horizontal_offset_amplitude ;

    so_called_platform_math :: mul_fracts ( horizontal_offset_phase , time , so_called_platform_math_consts :: fract_2pi ) ;
    so_called_platform_math :: div_fract_by ( horizontal_offset_phase , horizontal_offset_period ) ;

    so_called_platform_math :: sin ( horizontal_offset , horizontal_offset_phase ) ;
    so_called_platform_math :: mul_fract_by ( horizontal_offset , horizontal_offset_amplitude ) ;

    shy_guts :: logic_observer_animation_flight_transform_state :: horizontal_offset = horizontal_offset ;
}

void shy_guts :: compute_eye ( )
{
    so_called_type_platform_math_num_fract vertical_offset ;
    so_called_type_platform_math_num_fract horizontal_offset ;
    so_called_type_platform_math_num_fract zero ;
    so_called_type_platform_vector_data eye ;

    vertical_offset = shy_guts :: logic_observer_animation_flight_transform_state :: vertical_offset ;
    horizontal_offset = shy_guts :: logic_observer_animation_flight_transform_state :: horizontal_offset ;
    zero = so_called_platform_math_consts :: fract_0 ;

    so_called_platform_vector :: xyz ( eye , horizontal_offset , vertical_offset , zero ) ;

    shy_guts :: logic_observer_animation_flight_transform_state :: eye = eye ;
}

void shy_guts :: compute_target ( )
{
    so_called_type_platform_math_num_fract vertical_offset ;
    so_called_type_platform_math_num_fract horizontal_offset ;
    so_called_type_platform_math_num_fract const_target_z ;
    so_called_type_platform_math_num_fract target_x ;
    so_called_type_platform_math_num_fract target_y ;
    so_called_type_platform_math_num_fract target_z ;
    so_called_type_platform_vector_data target ;

    vertical_offset = shy_guts :: logic_observer_animation_flight_transform_state :: vertical_offset ;
    horizontal_offset = shy_guts :: logic_observer_animation_flight_transform_state :: horizontal_offset ;
    const_target_z = so_called_common_logic_observer_animation_consts :: flight_target_z ;

    target_x = horizontal_offset ;
    target_y = vertical_offset ;
    target_z = const_target_z ;

    so_called_platform_vector :: xyz ( target , target_x , target_y , target_z ) ;

    shy_guts :: logic_observer_animation_flight_transform_state :: target = target ;
}

void shy_guts :: reply_transform ( )
{
    so_called_message_common_logic_observer_animation_flight_transform_reply msg ;
    msg . eye = shy_guts :: logic_observer_animation_flight_transform_state :: eye ;
    msg . target = shy_guts :: logic_observer_animation_flight_transform_state :: target ;
    so_called_sender_common_logic_observer_animation_flight_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_observer_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_logic_observer_animation_flight_transform_request )
{
    shy_guts :: compute_vertical_offset ( ) ;
    shy_guts :: compute_horizontal_offset ( ) ;
    shy_guts :: compute_eye ( ) ;
    shy_guts :: compute_target ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_observer_animation_flight :: receive ( so_called_message_common_logic_observer_update )
{
    so_called_type_platform_math_num_fract time_step ;
    so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
    so_called_platform_math :: add_to_fract ( shy_guts :: logic_observer_update_state :: time , time_step ) ;
}

void _shy_common_logic_observer_animation_flight :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

