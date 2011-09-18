namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_roll_out > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_rewind_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_step_message )
{
    so_called_common_engine_math_stateless :: add_frame_to_time ( shy_guts :: time ) ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_transform_request_message msg )
{
    so_called_platform_math_num_fract_type position_radius ;
    so_called_platform_math_num_fract_type position_spin_periods ;
    so_called_platform_math_num_fract_type rotation_periods ;
    so_called_platform_math_num_fract_type shifted_time ;

    so_called_common_engine_math_stateless :: shift
        ( shifted_time
        , shy_guts :: time
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_time_shift_per_letter
        , msg . letter
        ) ;

    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( position_radius
        , shifted_time
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_position_radius_begin
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_position_radius_end
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_time
        ) ;

    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( position_spin_periods
        , shifted_time
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_position_spin_periods_begin
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_position_spin_periods_end
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_time
        ) ;

    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( rotation_periods
        , shifted_time
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_rotation_periods_begin
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_rotation_periods_end
        , so_called_common_logic_salutation_letters_animation_consts :: roll_out_time
        ) ;

    so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_message msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . position_radius = position_radius ;
    msg_reply . position_spin_periods = position_spin_periods ;
    msg_reply . rotation_periods = rotation_periods ;
    so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_sender :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_roll_out :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
