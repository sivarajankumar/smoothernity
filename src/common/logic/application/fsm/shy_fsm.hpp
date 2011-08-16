namespace shy_guts
{
    static so_called_type_common_logic_application_fsm_inputs inputs_current ;
    static so_called_type_common_logic_application_fsm_inputs inputs_fixed ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_application_fsm > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_application_fsm :: reset_input_events ( )
{
    shy_guts :: inputs_current . logic_amusement_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_amusement_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_application_render = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_application_update = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_main_menu_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_main_menu_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_meshes_cleaner_clean_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_meshes_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_text_cleaner_clean_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_letters_text_generator_generate_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_timer_appear_run_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_salutation_timer_disappear_run_finished = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_text_prepared = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_title_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: inputs_current . logic_title_finished = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_application_fsm :: recalc_current_inputs ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_application_consts :: skip_amusement ) )
    {
        shy_guts :: inputs_current . stage_amusement_disabled = so_called_platform_math_consts :: whole_true ;
        shy_guts :: inputs_current . stage_amusement_enabled = so_called_platform_math_consts :: whole_false ;
    }
    else
    {
        shy_guts :: inputs_current . stage_amusement_disabled = so_called_platform_math_consts :: whole_false ;
        shy_guts :: inputs_current . stage_amusement_enabled = so_called_platform_math_consts :: whole_true ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_application_consts :: skip_main_menu ) )
    {
        shy_guts :: inputs_current . stage_main_menu_disabled = so_called_platform_math_consts :: whole_true ;
        shy_guts :: inputs_current . stage_main_menu_enabled = so_called_platform_math_consts :: whole_false ;
    }
    else
    {
        shy_guts :: inputs_current . stage_main_menu_disabled = so_called_platform_math_consts :: whole_false ;
        shy_guts :: inputs_current . stage_main_menu_enabled = so_called_platform_math_consts :: whole_true ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_application_consts :: skip_salutation ) )
    {
        shy_guts :: inputs_current . stage_salutation_disabled = so_called_platform_math_consts :: whole_true ;
        shy_guts :: inputs_current . stage_salutation_enabled = so_called_platform_math_consts :: whole_false ;
    }
    else
    {
        shy_guts :: inputs_current . stage_salutation_disabled = so_called_platform_math_consts :: whole_false ;
        shy_guts :: inputs_current . stage_salutation_enabled = so_called_platform_math_consts :: whole_true ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( so_called_common_logic_application_consts :: skip_title ) )
    {
        shy_guts :: inputs_current . stage_title_disabled = so_called_platform_math_consts :: whole_true ;
        shy_guts :: inputs_current . stage_title_enabled = so_called_platform_math_consts :: whole_false ;
    }
    else
    {
        shy_guts :: inputs_current . stage_title_disabled = so_called_platform_math_consts :: whole_false ;
        shy_guts :: inputs_current . stage_title_enabled = so_called_platform_math_consts :: whole_true ;
    }
}

void _shy_common_logic_application_fsm :: determine_inputs_change ( so_called_type_platform_math_num_whole & inputs_changed )
{
    if ( so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_amusement_created 
            , shy_guts :: inputs_fixed . logic_amusement_created 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_amusement_finished 
            , shy_guts :: inputs_fixed . logic_amusement_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_application_render 
            , shy_guts :: inputs_fixed . logic_application_render 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_application_update 
            , shy_guts :: inputs_fixed . logic_application_update 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_main_menu_created 
            , shy_guts :: inputs_fixed . logic_main_menu_created 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_main_menu_finished 
            , shy_guts :: inputs_fixed . logic_main_menu_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_letters_meshes_cleaner_clean_finished 
            , shy_guts :: inputs_fixed . logic_salutation_letters_meshes_cleaner_clean_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_letters_meshes_generator_generate_finished 
            , shy_guts :: inputs_fixed . logic_salutation_letters_meshes_generator_generate_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_letters_text_cleaner_clean_finished 
            , shy_guts :: inputs_fixed . logic_salutation_letters_text_cleaner_clean_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_letters_text_generator_generate_finished 
            , shy_guts :: inputs_fixed . logic_salutation_letters_text_generator_generate_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_timer_appear_run_finished 
            , shy_guts :: inputs_fixed . logic_salutation_timer_appear_run_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_salutation_timer_disappear_run_finished 
            , shy_guts :: inputs_fixed . logic_salutation_timer_disappear_run_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_text_prepared 
            , shy_guts :: inputs_fixed . logic_text_prepared 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_title_created 
            , shy_guts :: inputs_fixed . logic_title_created 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . logic_title_finished 
            , shy_guts :: inputs_fixed . logic_title_finished 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_amusement_disabled 
            , shy_guts :: inputs_fixed . stage_amusement_disabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_amusement_enabled 
            , shy_guts :: inputs_fixed . stage_amusement_enabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_main_menu_disabled 
            , shy_guts :: inputs_fixed . stage_main_menu_disabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_main_menu_enabled 
            , shy_guts :: inputs_fixed . stage_main_menu_enabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_salutation_disabled 
            , shy_guts :: inputs_fixed . stage_salutation_disabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_salutation_enabled 
            , shy_guts :: inputs_fixed . stage_salutation_enabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_title_disabled 
            , shy_guts :: inputs_fixed . stage_title_disabled 
            )
      && so_called_platform_conditions :: wholes_are_equal 
            ( shy_guts :: inputs_current . stage_title_enabled 
            , shy_guts :: inputs_fixed . stage_title_enabled 
            )
       )
    {
        inputs_changed = so_called_platform_math_consts :: whole_false ;
    }
    else
        inputs_changed = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_application_fsm :: update_fixed_inputs ( )
{
    shy_guts :: inputs_fixed = shy_guts :: inputs_current ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_init )
{
    reset_input_events ( ) ;

    so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > inputs_current ;
    so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > inputs_fixed ;

    so_called_platform_pointer :: bind ( inputs_current , shy_guts :: inputs_current ) ;
    so_called_platform_pointer :: bind ( inputs_fixed , shy_guts :: inputs_fixed ) ;

    so_called_common_logic_application_fsm_behaviour :: set_inputs ( inputs_current , inputs_fixed ) ;
    so_called_common_logic_application_fsm_behaviour :: init ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_created )
{
    shy_guts :: inputs_current . logic_amusement_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_amusement_finished )
{
    shy_guts :: inputs_current . logic_amusement_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_render )
{
    shy_guts :: inputs_current . logic_application_render = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_application_update )
{
    shy_guts :: inputs_current . logic_application_update = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_created )
{
    shy_guts :: inputs_current . logic_main_menu_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_main_menu_finished )
{
    shy_guts :: inputs_current . logic_main_menu_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_letters_meshes_cleaner_clean_finished )
{
    shy_guts :: inputs_current . logic_salutation_letters_meshes_cleaner_clean_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished )
{
    shy_guts :: inputs_current . logic_salutation_letters_meshes_generator_generate_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_letters_text_cleaner_clean_finished )
{
    shy_guts :: inputs_current . logic_salutation_letters_text_cleaner_clean_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_letters_text_generator_generate_finished )
{
    shy_guts :: inputs_current . logic_salutation_letters_text_generator_generate_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_timer_appear_run_finished )
{
    shy_guts :: inputs_current . logic_salutation_timer_appear_run_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_salutation_timer_disappear_run_finished )
{
    shy_guts :: inputs_current . logic_salutation_timer_disappear_run_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_text_prepared )
{
    shy_guts :: inputs_current . logic_text_prepared = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_created )
{
    shy_guts :: inputs_current . logic_title_created = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: receive ( so_called_message_common_logic_title_finished )
{
    shy_guts :: inputs_current . logic_title_finished = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_fsm_stateless :: run_fsm < _shy_common_logic_application_fsm , so_called_common_logic_application_fsm_behaviour > ( ) ;
}

void _shy_common_logic_application_fsm :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
