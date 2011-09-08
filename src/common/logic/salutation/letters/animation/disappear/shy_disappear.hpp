namespace shy_guts
{
    static so_called_platform_math_num_fract_type time ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation_disappear > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_init_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_logic_salutation_letters_animation_disappear_rewind_message )
{
    shy_guts :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_logic_salutation_letters_animation_disappear_step_message )
{
}

void _shy_common_logic_salutation_letters_animation_disappear :: receive ( so_called_common_logic_salutation_letters_animation_disappear_transform_request_message msg )
{
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type scale_cut_off ;
    so_called_platform_math_num_fract_type letter_index ;
    so_called_platform_math_num_fract_type letter_time_shift ;
    so_called_platform_math_num_fract_type shifted_time ;
    so_called_platform_math_num_fract_type time_shift_per_letter ;

    scale_cut_off = so_called_common_logic_salutation_letters_animation_consts :: disappear_scale_cut_off ;
    time_shift_per_letter = so_called_common_logic_salutation_letters_animation_consts :: disappear_time_shift_per_letter ;

    so_called_platform_math :: make_fract_from_whole ( letter_index , msg . letter ) ;
    so_called_platform_math :: mul_fracts ( letter_time_shift , letter_index , time_shift_per_letter ) ;
    so_called_platform_math :: sub_fracts ( shifted_time , shy_guts :: time , letter_time_shift ) ;

    so_called_common_engine_math_stateless :: hard_in_easy_out
        ( scale
        , shifted_time
        , so_called_common_logic_salutation_letters_animation_consts :: disappear_scale_begin
        , so_called_platform_math_consts :: fract_0
        , so_called_common_logic_salutation_letters_animation_consts :: disappear_scale_end
        , so_called_common_logic_salutation_letters_animation_consts :: disappear_time
        ) ;

    if ( so_called_platform_conditions :: fract_less_than_fract ( scale , scale_cut_off ) )
        scale = so_called_platform_math_consts :: fract_0 ;

    so_called_common_logic_salutation_letters_animation_disappear_transform_reply_message msg_reply ;
    msg_reply . letter = msg . letter ;
    msg_reply . scale = scale ;
    so_called_common_logic_salutation_letters_animation_disappear_transform_reply_sender :: send ( msg_reply ) ;
}

void _shy_common_logic_salutation_letters_animation_disappear :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
