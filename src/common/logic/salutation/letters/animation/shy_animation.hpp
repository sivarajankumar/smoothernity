namespace shy_guts
{
    namespace logic_salutation_letters_animation_appear_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_appear_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_disappear_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_disappear_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_layout_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_roll_in_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_roll_in_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_roll_out_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_roll_out_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_transform_state
    {
        static so_called_common_logic_salutation_letters_animation_transform_request_message msg_request ;
        static so_called_platform_matrix_data_type transform ;
        static void on_request ( ) ;
    }

    static void compute_transform ( );
    static void request_animation_appear_transform ( ) ;
    static void request_animation_disappear_transform ( ) ;
    static void request_animation_roll_in_transform ( ) ;
    static void request_animation_roll_out_transform ( ) ;
    static void request_animation_layout_transform ( ) ;
    static void send_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_animation_transform_state :: on_request ( )
{
    shy_guts :: request_animation_layout_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_reply ( )
{
    shy_guts :: request_animation_appear_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_appear_transform_state :: on_reply ( )
{
    shy_guts :: request_animation_disappear_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: on_reply ( )
{
    shy_guts :: request_animation_roll_in_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: on_reply ( )
{
    shy_guts :: request_animation_roll_out_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: on_reply ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: send_computed_transform ( ) ;
}

void shy_guts :: request_animation_layout_transform ( )
{
    so_called_platform_math_num_whole_type letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_animation_appear_transform ( )
{
    so_called_platform_math_num_whole_type letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_appear_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_appear_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_animation_disappear_transform ( )
{
    so_called_platform_math_num_whole_type letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_animation_roll_in_transform ( )
{
    so_called_platform_math_num_whole_type letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . request ( ) ;
}

void shy_guts :: request_animation_roll_out_transform ( )
{
    so_called_platform_math_num_whole_type letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . request ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_vector_data_type final_origin ;
    so_called_platform_math_num_fract_type final_rotation ;
    so_called_platform_math_num_fract_type final_scale ;
    so_called_platform_vector_data_type layout_origin ;
    so_called_platform_math_num_fract_type layout_scale ;
    so_called_platform_math_num_fract_type appear_scale ;
    so_called_platform_math_num_fract_type disappear_scale ;
    so_called_platform_math_num_fract_type roll_in_position_radius ;
    so_called_platform_math_num_fract_type roll_in_position_spin_periods ;
    so_called_platform_math_num_fract_type roll_in_rotation_periods ;
    so_called_platform_math_num_fract_type roll_out_position_radius ;
    so_called_platform_math_num_fract_type roll_out_position_spin_periods ;
    so_called_platform_math_num_fract_type roll_out_rotation_periods ;
    so_called_platform_vector_data_type total_position ;
    so_called_platform_math_num_fract_type total_position_radius ;
    so_called_platform_math_num_fract_type total_position_spin_periods ;
    so_called_platform_math_num_fract_type total_position_spin_radians ;
    so_called_platform_math_num_fract_type total_rotation_radians ;
    so_called_platform_math_num_fract_type total_rotation_periods ;
    so_called_platform_math_num_fract_type total_scale ;
    so_called_platform_matrix_data_type transform ;

    layout_origin = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_reply . origin ;
    layout_scale = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_reply . scale ;
    appear_scale = shy_guts :: logic_salutation_letters_animation_appear_transform_state :: taker . msg_reply . scale ;
    disappear_scale = shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: taker . msg_reply . scale ;
    roll_in_position_radius = shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . msg_reply . position_radius ;
    roll_in_position_spin_periods = shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . msg_reply . position_spin_periods ;
    roll_in_rotation_periods = shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . msg_reply . rotation_periods ;
    roll_out_position_radius = shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . msg_reply . position_radius ;
    roll_out_position_spin_periods = shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . msg_reply . position_spin_periods ;
    roll_out_rotation_periods = shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . msg_reply . rotation_periods ;

    total_scale = so_called_platform_math_consts :: fract_1 ;
    so_called_platform_math :: mul_fract_by ( total_scale , layout_scale ) ;
    so_called_platform_math :: mul_fract_by ( total_scale , appear_scale ) ;
    so_called_platform_math :: mul_fract_by ( total_scale , disappear_scale ) ;

    so_called_platform_math :: add_fracts ( total_position_radius , roll_in_position_radius , roll_out_position_radius ) ;
    so_called_platform_math :: add_fracts ( total_position_spin_periods , roll_in_position_spin_periods , roll_out_position_spin_periods ) ;
    so_called_platform_math :: add_fracts ( total_rotation_periods , roll_in_rotation_periods , roll_out_rotation_periods ) ;

    so_called_common_engine_math_stateless :: make_radians_from_periods ( total_rotation_radians , total_rotation_periods ) ;
    so_called_common_engine_math_stateless :: make_radians_from_periods ( total_position_spin_radians , total_position_spin_periods ) ;

    so_called_common_engine_math_stateless :: make_cartesian_from_polar ( total_position , total_position_radius , total_position_spin_radians ) ;
    so_called_platform_vector :: mul_by ( total_position , layout_scale ) ;
    so_called_platform_vector :: add_to ( total_position , layout_origin ) ;

    final_origin = total_position ;
    final_rotation = total_rotation_radians ;
    final_scale = total_scale ;

    so_called_common_engine_math_stateless :: scale_rotation_z ( transform , final_scale , final_rotation ) ;
    so_called_platform_matrix :: set_origin ( transform , final_origin ) ;

    shy_guts :: logic_salutation_letters_animation_transform_state :: transform = transform ;
}

void shy_guts :: send_computed_transform ( )
{
    so_called_common_logic_salutation_letters_animation_transform_reply_message msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    msg . transform = shy_guts :: logic_salutation_letters_animation_transform_state :: transform ;
    so_called_common_logic_salutation_letters_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_animation_appear_transform_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_appear_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_appear_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_appear_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_disappear_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_disappear_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_roll_in_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_roll_in_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_roll_out_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_roll_out_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_layout_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_transform_request_message msg )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request = msg ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
