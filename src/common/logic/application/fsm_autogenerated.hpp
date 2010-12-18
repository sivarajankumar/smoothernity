template < typename logic_application_fsm >
shy_logic_application_fsm_autogenerated < logic_application_fsm > :: shy_logic_application_fsm_autogenerated ( )
{
    typename platform_pointer :: template pointer < logic_application_fsm_autogenerated > fsm ;
    platform_pointer :: bind ( fsm , * this ) ;
    _autogenerated_actions . set_fsm ( fsm ) ;

    platform_pointer :: bind ( _state_environment . autogenerated_actions , _autogenerated_actions ) ;
    platform_pointer :: bind ( _state_environment . autogenerated_inputs , _fixed_autogenerated_inputs ) ;
    platform_pointer :: bind ( _state_environment . states , _states ) ;

    platform_pointer :: bind ( _machine_amusement_generator_state , _states . amusement_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_amusement_performer_state , _states . amusement_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_game_performer_state , _states . game_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_generator_state , _states . generator_state_initial ) ;
    platform_pointer :: bind ( _machine_main_menu_generator_state , _states . main_menu_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_main_menu_performer_state , _states . main_menu_performer_state_initial ) ;
    platform_pointer :: bind ( _machine_performer_state , _states . performer_state_initial ) ;
    platform_pointer :: bind ( _machine_text_generator_state , _states . text_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_title_generator_state , _states . title_generator_state_initial ) ;
    platform_pointer :: bind ( _machine_title_performer_state , _states . title_performer_state_initial ) ;

    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: set_actions ( typename platform_pointer :: template pointer < actions_type > actions )
{
    _state_environment . actions = actions ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: set_inputs ( typename platform_pointer :: template pointer < inputs_type > inputs )
{
    _state_environment . inputs = inputs ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: reset_autogenerated_input_events ( )
{
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_amusement_generator_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_amusement_performer_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_game_performer_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_main_menu_generator_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_main_menu_performer_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_text_generator_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_title_generator_command_start , false ) ;
    platform_math :: make_num_whole ( _current_autogenerated_inputs . machine_title_performer_command_start , false ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: determine_autogenerated_inputs_change ( num_whole & inputs_changed )
{
    if ( platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_amusement_generator_command_start , _fixed_autogenerated_inputs . machine_amusement_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_amusement_generator_state_is_finished , _fixed_autogenerated_inputs . machine_amusement_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_amusement_performer_command_start , _fixed_autogenerated_inputs . machine_amusement_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_amusement_performer_state_is_finished , _fixed_autogenerated_inputs . machine_amusement_performer_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_game_performer_command_start , _fixed_autogenerated_inputs . machine_game_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_main_menu_generator_command_start , _fixed_autogenerated_inputs . machine_main_menu_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_main_menu_generator_state_is_finished , _fixed_autogenerated_inputs . machine_main_menu_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_main_menu_performer_command_start , _fixed_autogenerated_inputs . machine_main_menu_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_main_menu_performer_state_is_finished , _fixed_autogenerated_inputs . machine_main_menu_performer_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_text_generator_command_start , _fixed_autogenerated_inputs . machine_text_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_text_generator_state_is_finished , _fixed_autogenerated_inputs . machine_text_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_title_generator_command_start , _fixed_autogenerated_inputs . machine_title_generator_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_title_generator_state_is_finished , _fixed_autogenerated_inputs . machine_title_generator_state_is_finished )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_title_performer_command_start , _fixed_autogenerated_inputs . machine_title_performer_command_start )
      && platform_conditions :: wholes_are_equal ( _current_autogenerated_inputs . machine_title_performer_state_is_finished , _fixed_autogenerated_inputs . machine_title_performer_state_is_finished )
       )
    {
        platform_math :: make_num_whole ( inputs_changed , false ) ;
    }
    else
        platform_math :: make_num_whole ( inputs_changed , true ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: recalc_current_autogenerated_inputs ( )
{
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_amusement_generator_state_is_finished , _machine_amusement_generator_state , _states . amusement_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_amusement_performer_state_is_finished , _machine_amusement_performer_state , _states . amusement_performer_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_main_menu_generator_state_is_finished , _machine_main_menu_generator_state , _states . main_menu_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_main_menu_performer_state_is_finished , _machine_main_menu_performer_state , _states . main_menu_performer_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_text_generator_state_is_finished , _machine_text_generator_state , _states . text_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_title_generator_state_is_finished , _machine_title_generator_state , _states . title_generator_state_finished ) ;
    platform_pointer :: is_bound_to ( _current_autogenerated_inputs . machine_title_performer_state_is_finished , _machine_title_performer_state , _states . title_performer_state_finished ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: update_fixed_autogenerated_inputs ( )
{
    _fixed_autogenerated_inputs = _current_autogenerated_inputs ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: tick_all_fsms ( )
{
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_amusement_generator_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_amusement_performer_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_game_performer_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_generator_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_main_menu_generator_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_main_menu_performer_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_performer_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_text_generator_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_title_generator_state ) ;
    engine_fsm :: tick_single_fsm ( _state_environment , _machine_title_performer_state ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: is_fsm_running ( num_whole & result )
{
    result = _fsm_running ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: run_fsm_begin ( )
{
    platform_math :: make_num_whole ( _fsm_running , true ) ;
}

template < typename logic_application_fsm >
void shy_logic_application_fsm_autogenerated < logic_application_fsm > :: run_fsm_end ( )
{
    platform_math :: make_num_whole ( _fsm_running , false ) ;
}

