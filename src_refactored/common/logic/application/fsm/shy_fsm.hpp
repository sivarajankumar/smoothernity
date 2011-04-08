namespace shy_guts
{
    static so_called_type_common_logic_application_fsm_inputs current_inputs ;
    static so_called_type_common_logic_application_fsm_inputs fixed_inputs ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_application_fsm :: reset_input_events ( )
{
    shy_guts :: current_inputs . logic_amusement_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_amusement_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_application_render = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_application_update = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_main_menu_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_main_menu_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_text_prepared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_title_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: current_inputs . logic_title_finished = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_application_fsm :: recalc_current_inputs ( )
{
}

void _shy_common_logic_application_fsm :: determine_inputs_change ( so_called_type_platform_math_num_whole & )
{
}

void _shy_common_logic_application_fsm :: update_fixed_inputs ( )
{
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_init )
{
    so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > inputs ;
    so_called_platform_pointer :: bind ( inputs , shy_guts :: fixed_inputs ) ;
    so_called_common_logic_application_fsm_behaviour :: set_inputs ( inputs ) ;
    so_called_common_logic_application_fsm_behaviour :: init ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_created )
{
    shy_guts :: current_inputs . logic_amusement_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_finished )
{
    shy_guts :: current_inputs . logic_amusement_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_render )
{
    shy_guts :: current_inputs . logic_application_render = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_update )
{
    shy_guts :: current_inputs . logic_application_update = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_created )
{
    shy_guts :: current_inputs . logic_main_menu_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_finished )
{
    shy_guts :: current_inputs . logic_main_menu_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_text_prepared )
{
    shy_guts :: current_inputs . logic_text_prepared = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_created )
{
    shy_guts :: current_inputs . logic_title_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_finished )
{
    shy_guts :: current_inputs . logic_title_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}
