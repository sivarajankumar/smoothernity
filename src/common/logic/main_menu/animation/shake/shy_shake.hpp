namespace shy_guts
{
    namespace logic_main_menu_animation_shake_transform_state
    {
        so_called_platform_math_num_fract_type shift_x ;
    }

    namespace logic_main_menu_update_state
    {
        so_called_platform_math_num_whole_type started ;
        so_called_platform_math_num_fract_type time ;
    }

    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_animation_shake > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_to_begin ;
    so_called_platform_math_num_fract_type time_from_begin_to_end ;
    so_called_platform_math_num_fract_type time_begin ;
    so_called_platform_math_num_fract_type time_end ;
    so_called_platform_math_num_fract_type shift_x_amplitude_begin ;
    so_called_platform_math_num_fract_type shift_x_amplitude_end ;
    so_called_platform_math_num_fract_type shift_x_amplitude ;
    so_called_platform_math_num_fract_type shift_x_period_in_seconds ;
    so_called_platform_math_num_fract_type shift_x_phase ;
    so_called_platform_math_num_fract_type shift_x ;

    time = shy_guts :: logic_main_menu_update_state :: time ;
    time_to_begin = so_called_common_logic_main_menu_animation_consts :: shake_time_to_begin ;
    time_from_begin_to_end = so_called_common_logic_main_menu_animation_consts :: shake_time_from_begin_to_end ;
    shift_x_amplitude_begin = so_called_common_logic_main_menu_animation_consts :: shake_shift_x_amplitude_begin ;
    shift_x_amplitude_end = so_called_common_logic_main_menu_animation_consts :: shake_shift_x_amplitude_end ;
    shift_x_period_in_seconds = so_called_common_logic_main_menu_animation_consts :: shake_shift_x_period_in_seconds ;

    time_begin = time_to_begin ;
    so_called_platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;

    so_called_common_engine_math_stateless :: easy_in_easy_out
        ( shift_x_amplitude
        , time
        , shift_x_amplitude_begin
        , time_begin
        , shift_x_amplitude_end
        , time_end
        ) ;

    so_called_platform_math :: mul_fracts ( shift_x_phase , time , so_called_platform_math_consts :: fract_2pi ) ;
    so_called_platform_math :: div_fract_by ( shift_x_phase , shift_x_period_in_seconds ) ;

    so_called_platform_math :: sin ( shift_x , shift_x_phase ) ;
    so_called_platform_math :: mul_fract_by ( shift_x , shift_x_amplitude ) ;

    shy_guts :: logic_main_menu_animation_shake_transform_state :: shift_x = shift_x ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_main_menu_animation_shake_transform_reply_message msg ;
    msg . shift_x = shy_guts :: logic_main_menu_animation_shake_transform_state :: shift_x ;
    so_called_common_logic_main_menu_animation_shake_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_common_logic_main_menu_animation_shake_transform_request_message )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_common_logic_main_menu_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_update_state :: started ) )
    {
        so_called_platform_math_num_fract_type time ;
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math_num_fract_type time_total ;
        so_called_platform_math_num_fract_type time_to_begin ;
        so_called_platform_math_num_fract_type time_from_begin_to_end ;

        time = shy_guts :: logic_main_menu_update_state :: time ;
        time_to_begin = so_called_common_logic_main_menu_animation_consts :: shake_time_to_begin ;
        time_from_begin_to_end = so_called_common_logic_main_menu_animation_consts :: shake_time_from_begin_to_end ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;

        so_called_platform_math :: add_fracts ( time_total , time_to_begin , time_from_begin_to_end ) ;
        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_total ) )
            shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_false ;

        shy_guts :: logic_main_menu_update_state :: time = time ;
    }
}

void _shy_common_logic_main_menu_animation_shake :: receive ( so_called_common_logic_main_menu_void_chosen_message )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: logic_main_menu_update_state :: started ) )
    {
        shy_guts :: logic_main_menu_update_state :: time = so_called_platform_math_consts :: fract_0 ;
        shy_guts :: logic_main_menu_update_state :: started = so_called_platform_math_consts :: whole_true ;
    }
}

void _shy_common_logic_main_menu_animation_shake :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
