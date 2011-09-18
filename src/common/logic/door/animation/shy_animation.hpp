namespace shy_guts
{
    namespace logic_door_animation_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_door_animation_appear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }

    static void proceed_with_transform ( ) ;
    static void request_appear_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_door_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_appear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_animation_appear_transform_state :: replied ) )
    {
        shy_guts :: logic_door_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_computed_transform ( ) ;
    }
}

void shy_guts :: request_appear_transform ( )
{
    shy_guts :: logic_door_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_door_animation_appear_transform_request_sender :: send ( so_called_common_logic_door_animation_appear_transform_request_message ( ) ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type origin_x ;
    so_called_platform_math_num_fract_type origin_y ;
    so_called_platform_math_num_fract_type origin_z ;
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_matrix_data_type transform ;

    origin_x = so_called_common_logic_door_animation_consts :: animation_origin_x ;
    origin_y = so_called_common_logic_door_animation_consts :: animation_origin_y ;
    origin_z = so_called_common_logic_door_animation_consts :: animation_origin_z ;
    scale = shy_guts :: logic_door_animation_appear_transform_state :: scale ;
    zero = so_called_platform_math_consts :: fract_0 ;

    so_called_platform_matrix :: identity ( transform ) ;
    so_called_platform_matrix :: set_axis_x ( transform , scale , zero , zero ) ;
    so_called_platform_matrix :: set_axis_y ( transform , zero , scale , zero ) ;
    so_called_platform_matrix :: set_axis_z ( transform , zero , zero , scale ) ;
    so_called_platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    shy_guts :: logic_door_animation_transform_state :: transform = transform ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_door_animation_transform_reply_message msg ;
    msg . transform = shy_guts :: logic_door_animation_transform_state :: transform ;
    so_called_common_logic_door_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_door_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_door_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_door_animation :: receive ( so_called_common_logic_door_animation_appear_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_animation_appear_transform_state :: requested ) )
    {
        shy_guts :: logic_door_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_door_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_door_animation_appear_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_door_animation :: receive ( so_called_common_logic_door_animation_transform_request_message )
{
    shy_guts :: logic_door_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_door_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
