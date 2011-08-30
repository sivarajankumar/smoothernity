namespace shy_guts
{
    namespace logic_main_menu_selection_animation_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_matrix_data_type transform ;
    }

    namespace logic_main_menu_selection_animation_idle_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_vector_data_type position ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_idle_attention_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_appear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_disappear_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_select_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_unselect_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_attention_transform_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type scale_x ;
        static so_called_platform_math_num_fract_type scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_weight_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_platform_math_num_fract_type weight ;
    }

    static void proceed_with_transform ( ) ;
    static void obtain_idle_transform ( ) ;
    static void obtain_idle_attention_transform ( ) ;
    static void obtain_appear_transform ( ) ;
    static void obtain_disappear_transform ( ) ;
    static void obtain_select_transform ( ) ;
    static void obtain_unselect_transform ( ) ;
    static void obtain_push_transform ( ) ;
    static void obtain_push_attention_transform ( ) ;
    static void obtain_push_weight ( ) ;
    static void reply_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_idle_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_idle_attention_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_appear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_disappear_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_select_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_select_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_select_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_unselect_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_push_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_push_attention_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: obtain_push_weight ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_weight_state :: replied ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_transform ( ) ;
    }
}

void shy_guts :: obtain_idle_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_idle_transform_request_sender :: send 
        ( so_called_common_logic_main_menu_selection_animation_idle_transform_request_message ( ) 
        ) ;
}

void shy_guts :: obtain_idle_attention_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_idle_attention_transform_request_sender :: send 
        ( so_called_common_logic_main_menu_selection_animation_idle_attention_transform_request_message ( ) 
        ) ;
}

void shy_guts :: obtain_appear_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_appear_transform_request_sender :: send 
        ( so_called_common_logic_main_menu_selection_animation_appear_transform_request_message ( ) 
        ) ;
}

void shy_guts :: obtain_disappear_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_disappear_transform_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_disappear_transform_request_message ( )
        ) ;
}

void shy_guts :: obtain_select_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_select_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_select_transform_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_select_transform_request_message ( )
        ) ;
}

void shy_guts :: obtain_unselect_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_unselect_transform_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_unselect_transform_request_message ( )
        ) ;
}

void shy_guts :: obtain_push_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_push_transform_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_push_transform_request_message ( ) 
        ) ;
}

void shy_guts :: obtain_push_attention_transform ( )
{
    shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_push_attention_transform_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_push_attention_transform_request_message ( ) 
        ) ;
}

void shy_guts :: obtain_push_weight ( )
{
    shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_push_weight_request_sender :: send
        ( so_called_common_logic_main_menu_selection_animation_push_weight_request_message ( ) 
        ) ;
}

void shy_guts :: reply_transform ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_computed_transform ( ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    so_called_common_logic_main_menu_selection_animation_transform_reply_message reply_msg ;
    reply_msg . transform = shy_guts :: logic_main_menu_selection_animation_transform_state :: transform ;
    so_called_common_logic_main_menu_selection_animation_transform_reply_sender :: send ( reply_msg ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_platform_math_num_fract_type zero ;
    so_called_platform_vector_data_type idle_position ;
    so_called_platform_math_num_fract_type idle_scale_x ;
    so_called_platform_math_num_fract_type idle_scale_y ;
    so_called_platform_math_num_fract_type idle_attention_scale_x ;
    so_called_platform_math_num_fract_type idle_attention_scale_y ;
    so_called_platform_math_num_fract_type appear_scale_x ;
    so_called_platform_math_num_fract_type appear_scale_y ;
    so_called_platform_math_num_fract_type disappear_scale_x ;
    so_called_platform_math_num_fract_type disappear_scale_y ;
    so_called_platform_math_num_fract_type select_scale_x ;
    so_called_platform_math_num_fract_type select_scale_y ;
    so_called_platform_math_num_fract_type unselect_scale_x ;
    so_called_platform_math_num_fract_type unselect_scale_y ;
    so_called_platform_math_num_fract_type push_scale_x ;
    so_called_platform_math_num_fract_type push_scale_y ;
    so_called_platform_math_num_fract_type push_attention_scale_x ;
    so_called_platform_math_num_fract_type push_attention_scale_y ;
    so_called_platform_math_num_fract_type push_weight ;
    so_called_platform_math_num_fract_type weighted_scale_x ;
    so_called_platform_math_num_fract_type weighted_scale_y ;
    so_called_platform_math_num_fract_type weight_0 ;
    so_called_platform_math_num_fract_type weight_1 ;
    so_called_platform_math_num_fract_type scale_x ;
    so_called_platform_math_num_fract_type scale_y ;
    so_called_platform_math_num_fract_type scale_z ;
    so_called_platform_vector_data_type position ;
    so_called_platform_matrix_data_type transform ;
    
    zero = so_called_platform_math_consts :: fract_0 ;
    idle_position = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: position ;
    idle_scale_x = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_x ;
    idle_scale_y = shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_y ;
    idle_attention_scale_x = shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: scale_x ;
    idle_attention_scale_y = shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: scale_y ;
    appear_scale_x = shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: scale_x ;
    appear_scale_y = shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: scale_y ;
    disappear_scale_x = shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: scale_x ;
    disappear_scale_y = shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: scale_y ;
    select_scale_x = shy_guts :: logic_main_menu_selection_animation_select_transform_state :: scale_x ;
    select_scale_y = shy_guts :: logic_main_menu_selection_animation_select_transform_state :: scale_y ;
    unselect_scale_x = shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: scale_x ;
    unselect_scale_y = shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: scale_y ;
    push_scale_x = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: scale_x ;
    push_scale_y = shy_guts :: logic_main_menu_selection_animation_push_transform_state :: scale_y ;
    push_attention_scale_x = shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: scale_x ;
    push_attention_scale_y = shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: scale_y ;
    push_weight = shy_guts :: logic_main_menu_selection_animation_push_weight_state :: weight ;
    weight_0 = so_called_platform_math_consts :: fract_0 ;
    weight_1 = so_called_platform_math_consts :: fract_1 ;

    so_called_common_engine_math_stateless :: lerp ( weighted_scale_x , push_weight , idle_attention_scale_x , weight_0 , push_attention_scale_x , weight_1 ) ;
    so_called_common_engine_math_stateless :: lerp ( weighted_scale_y , push_weight , idle_attention_scale_y , weight_0 , push_attention_scale_y , weight_1 ) ;
    
    position = idle_position ;
    so_called_platform_math :: mul_fracts ( scale_x , idle_scale_x , appear_scale_x ) ;
    so_called_platform_math :: mul_fracts ( scale_y , idle_scale_y , appear_scale_y ) ;
    so_called_platform_math :: mul_fract_by ( scale_x , disappear_scale_x ) ;
    so_called_platform_math :: mul_fract_by ( scale_y , disappear_scale_y ) ;
    so_called_platform_math :: mul_fract_by ( scale_x , select_scale_x ) ;
    so_called_platform_math :: mul_fract_by ( scale_y , select_scale_y ) ;
    so_called_platform_math :: mul_fract_by ( scale_x , unselect_scale_x ) ;
    so_called_platform_math :: mul_fract_by ( scale_y , unselect_scale_y ) ;
    so_called_platform_math :: mul_fract_by ( scale_x , push_scale_x ) ;
    so_called_platform_math :: mul_fract_by ( scale_y , push_scale_y ) ;
    so_called_platform_math :: mul_fract_by ( scale_x , weighted_scale_x ) ;
    so_called_platform_math :: mul_fract_by ( scale_y , weighted_scale_y ) ;
    scale_z = so_called_platform_math_consts :: fract_1 ;
    
    so_called_platform_matrix :: set_origin ( transform , position ) ;
    so_called_platform_matrix :: set_axis_x ( transform , scale_x , zero , zero ) ;
    so_called_platform_matrix :: set_axis_y ( transform , zero , scale_y , zero ) ;
    so_called_platform_matrix :: set_axis_z ( transform , zero , zero , scale_z ) ;
    
    shy_guts :: logic_main_menu_selection_animation_transform_state :: transform = transform ;
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_weight_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_select_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_select_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_appear_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_appear_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_disappear_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_disappear_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_idle_attention_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_idle_attention_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_idle_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: position = msg . position ;
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_idle_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_push_attention_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_push_attention_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_push_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_push_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_push_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_push_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_push_weight_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: weight = msg . weight ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_select_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_select_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_select_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_select_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_select_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_select_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_transform_request_message )
{
    shy_guts :: logic_main_menu_selection_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_common_logic_main_menu_selection_animation_unselect_transform_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: scale_x = msg . scale_x ;
        shy_guts :: logic_main_menu_selection_animation_unselect_transform_state :: scale_y = msg . scale_y ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

