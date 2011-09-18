namespace shy_guts
{
    namespace logic_blanket_animation_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_blanket_animation_appear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
        static so_called_platform_math_num_fract_type rotation ;
    }

    namespace logic_blanket_animation_disappear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
        static so_called_platform_math_num_fract_type rotation ;
    }

    namespace logic_blanket_animation_fit_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale ;
    }

    static void proceed_with_transform ( ) ;
    static void request_appear_transform ( ) ;
    static void request_disappear_transform ( ) ;
    static void request_fit_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_fit_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_fit_transform_state :: replied ) )
    {
        shy_guts :: logic_blanket_animation_fit_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_appear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_appear_transform_state :: replied ) )
    {
        shy_guts :: logic_blanket_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_disappear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_disappear_transform_state :: replied ) )
    {
        shy_guts :: logic_blanket_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_computed_transform ( ) ;
    }
}

void shy_guts :: request_appear_transform ( )
{
    shy_guts :: logic_blanket_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_blanket_animation_appear_transform_request_sender :: send ( so_called_common_logic_blanket_animation_appear_transform_request_message ( ) ) ;
}

void shy_guts :: request_disappear_transform ( )
{
    shy_guts :: logic_blanket_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_blanket_animation_disappear_transform_request_sender :: send ( so_called_common_logic_blanket_animation_disappear_transform_request_message ( ) ) ;
}

void shy_guts :: request_fit_transform ( )
{
    shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_blanket_animation_fit_transform_request_sender :: send ( so_called_common_logic_blanket_animation_fit_transform_request_message ( ) ) ;
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
    so_called_platform_math_num_fract_type appear_scale ;
    so_called_platform_math_num_fract_type appear_rotation ;
    so_called_platform_math_num_fract_type disappear_scale ;
    so_called_platform_math_num_fract_type disappear_rotation ;
    so_called_platform_math_num_fract_type fit_scale ;
    so_called_platform_math_num_fract_type one ;
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_math_num_fract_type scale ;
    so_called_platform_math_num_fract_type rotation ;
    so_called_platform_vector_data_type axis_x ;
    so_called_platform_vector_data_type axis_y ;
    so_called_platform_vector_data_type axis_z ;
    so_called_platform_matrix_data_type transform ;

    origin_x = so_called_common_logic_blanket_animation_consts :: animation_origin_x ;
    origin_y = so_called_common_logic_blanket_animation_consts :: animation_origin_y ;
    origin_z = so_called_common_logic_blanket_animation_consts :: animation_origin_z ;
    one = so_called_platform_math_consts :: fract_1 ;
    zero = so_called_platform_math_consts :: fract_0 ;
    appear_scale = shy_guts :: logic_blanket_animation_appear_transform_state :: scale ;
    appear_rotation = shy_guts :: logic_blanket_animation_appear_transform_state :: rotation ;
    disappear_scale = shy_guts :: logic_blanket_animation_disappear_transform_state :: scale ;
    disappear_rotation = shy_guts :: logic_blanket_animation_disappear_transform_state :: rotation ;
    fit_scale = shy_guts :: logic_blanket_animation_fit_transform_state :: scale ;

    so_called_platform_math :: add_fracts ( scale , appear_scale , disappear_scale ) ;
    so_called_platform_math :: mul_fract_by ( scale , fit_scale ) ;
    so_called_platform_math :: add_fracts ( rotation , appear_rotation , disappear_rotation ) ;

    so_called_common_engine_math_stateless :: rotation_z ( axis_x , axis_y , rotation ) ;
    so_called_platform_vector :: xyz ( axis_z , zero , zero , one ) ;

    so_called_platform_vector :: mul_by ( axis_x , scale ) ;
    so_called_platform_vector :: mul_by ( axis_y , scale ) ;

    so_called_platform_matrix :: identity ( transform ) ;
    so_called_platform_matrix :: set_axis_x ( transform , axis_x ) ;
    so_called_platform_matrix :: set_axis_y ( transform , axis_y ) ;
    so_called_platform_matrix :: set_axis_z ( transform , axis_z ) ;
    so_called_platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    shy_guts :: logic_blanket_animation_transform_state :: transform = transform ;
}

void shy_guts :: reply_transform ( )
{
    so_called_common_logic_blanket_animation_transform_reply_message msg ;
    msg . transform = shy_guts :: logic_blanket_animation_transform_state :: transform ;
    so_called_common_logic_blanket_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_blanket_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_blanket_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_fit_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_blanket_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_blanket_animation :: receive ( so_called_common_logic_blanket_animation_appear_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_appear_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_blanket_animation_appear_transform_state :: scale = msg . scale ;
        shy_guts :: logic_blanket_animation_appear_transform_state :: rotation = msg . rotation ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_blanket_animation :: receive ( so_called_common_logic_blanket_animation_disappear_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_disappear_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_blanket_animation_disappear_transform_state :: scale = msg . scale ;
        shy_guts :: logic_blanket_animation_disappear_transform_state :: rotation = msg . rotation ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_blanket_animation :: receive ( so_called_common_logic_blanket_animation_fit_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_fit_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_fit_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_animation_fit_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_blanket_animation_fit_transform_state :: scale = msg . scale ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_blanket_animation :: receive ( so_called_common_logic_blanket_animation_transform_request_message )
{
    shy_guts :: logic_blanket_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_blanket_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

