namespace shy_guts
{
    namespace logic_main_menu_selection_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_main_menu_selection_animation_idle_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data position ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_idle_attention_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_appear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_disappear_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_select_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_unselect_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_attention_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract scale_x ;
        static so_called_type_platform_math_num_fract scale_y ;
    }

    namespace logic_main_menu_selection_animation_push_weight_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract weight ;
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
}

void shy_guts :: obtain_idle_transform ( )
{
}

void shy_guts :: obtain_idle_attention_transform ( )
{
}

void shy_guts :: obtain_appear_transform ( )
{
}

void shy_guts :: obtain_disappear_transform ( )
{
}

void shy_guts :: obtain_select_transform ( )
{
}

void shy_guts :: obtain_unselect_transform ( )
{
}

void shy_guts :: obtain_push_transform ( )
{
}

void shy_guts :: obtain_push_attention_transform ( )
{
}

void shy_guts :: obtain_push_weight ( )
{
}

void shy_guts :: reply_transform ( )
{
}

void shy_guts :: reply_computed_transform ( )
{
}

void shy_guts :: compute_transform ( )
{
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_appear_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_disappear_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_idle_attention_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_idle_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_attention_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_push_weight_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested ) )
    {
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_selection_animation_push_weight_state :: weight = msg . weight ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_select_transform_reply msg )
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

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_transform_request )
{
    shy_guts :: logic_main_menu_selection_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}

void _shy_common_logic_main_menu_selection_animation :: receive ( so_called_message_common_logic_main_menu_selection_animation_unselect_transform_reply msg )
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
