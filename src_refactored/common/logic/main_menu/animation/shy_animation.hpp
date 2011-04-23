namespace shy_guts
{
    namespace logic_main_menu_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data view ;
    }
    
    namespace logic_main_menu_animation_shake_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract shift_x ;
    }

    static void proceed_with_transform ( ) ;
    static void obtain_shake_transform ( ) ;
    static void compute_and_reply_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_shake_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_animation_shake_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_animation_shake_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: compute_and_reply_transform ( ) ;
    }
}

void shy_guts :: obtain_shake_transform ( )
{
    shy_guts :: logic_main_menu_animation_shake_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_main_menu_animation_shake_transform_request :: send ( so_called_message_common_logic_main_menu_animation_shake_transform_request ( ) ) ;
}

void shy_guts :: compute_and_reply_transform ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_type_platform_matrix_data view ;
    so_called_type_platform_math_num_fract shake_shift_x ;
    so_called_type_platform_math_num_fract origin_x ;
    so_called_type_platform_math_num_fract origin_y ;
    so_called_type_platform_math_num_fract origin_z ;

    shake_shift_x = shy_guts :: logic_main_menu_animation_shake_transform_state :: shift_x ;

    origin_x = so_called_platform_math_consts :: fract_0 ;
    origin_y = so_called_platform_math_consts :: fract_0 ;
    origin_z = so_called_platform_math_consts :: fract_0 ;

    so_called_platform_math :: add_to_fract ( origin_x , shake_shift_x ) ;

    so_called_platform_matrix :: identity ( view ) ;
    so_called_platform_matrix :: set_origin ( view , origin_x , origin_y , origin_z ) ;

    shy_guts :: logic_main_menu_animation_transform_state :: view = view ;
}

void shy_guts :: reply_transform ( )
{
    so_called_message_common_logic_main_menu_animation_transform_reply msg ;
    msg . view = shy_guts :: logic_main_menu_animation_transform_state :: view ;
    so_called_sender_common_logic_main_menu_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_main_menu_animation :: receive ( so_called_message_common_logic_main_menu_animation_shake_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_animation_shake_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_animation_shake_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_animation_shake_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_animation_shake_transform_state :: shift_x = msg . shift_x ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_animation :: receive ( so_called_message_common_logic_main_menu_animation_transform_request )
{
    shy_guts :: logic_main_menu_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
