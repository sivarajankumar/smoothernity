namespace shy_guts
{
    class action_command_name_container_type
    {
    public :
        typedef so_called_lib_std_set < so_called_lib_std_string > contents_type ;
        contents_type contents ;
    } ;

    class condition_state_name_container_type
    {
    public :
        typedef so_called_lib_std_set < so_called_lib_std_string > contents_type ;
        contents_type contents ;
    } ;

    class machine_action_command_name_container_type
    {
    public :
        typedef so_called_lib_std_map < so_called_lib_std_string , action_command_name_container_type > contents_type ;
        contents_type contents ;
    } ;

    class machine_condition_state_name_container_type
    {
    public :
        typedef so_called_lib_std_map < so_called_lib_std_string , condition_state_name_container_type > contents_type ;
        contents_type contents ;
    } ;

    class system_machine_action_command_name_container_type
    {
    public :
        typedef so_called_lib_std_map < so_called_lib_std_string , machine_action_command_name_container_type > contents_type ;
        contents_type contents ;
    } ;

    class system_machine_condition_state_name_container_type
    {
    public :
        typedef so_called_lib_std_map < so_called_lib_std_string , machine_condition_state_name_container_type > contents_type ;
        contents_type contents ;
    } ;

    namespace consts
    {
        static void h_contents ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void h_path ( so_called_lib_std_string & ) ;
        static void hpp_behaviour_determine_behaviour_inputs_change ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_determine_behaviour_inputs_change_condition_command ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_determine_behaviour_inputs_change_condition_state ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_determine_behaviour_inputs_change_else_if ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_determine_behaviour_inputs_change_if ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_init ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_init_bind_initial_state ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_is_fsm_running ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_recalc_current_behaviour_inputs ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_recalc_current_behaviour_inputs_check_machine_state ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_reset_behaviour_input_events ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_reset_behaviour_input_events_reset_machine_command ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_reset_behaviour_input_events_reset_machine_state_is ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_run_fsm_begin ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_run_fsm_end ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_set_inputs ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_tick_all_fsms ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_behaviour_tick_all_fsms_tick_machine ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_behaviour_update_fixed_behaviour_inputs ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_behaviour_actions ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_behaviour_actions_action_command_declare ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_behaviour_actions_action_command_implement ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_machine_variable ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_states ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_states_state_variable ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_behaviour_inputs ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_behaviour_inputs_action_command_variable ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_behaviour_inputs_condition_state_variable ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_action_command ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_action_discard ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_action_do ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_command ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_first_group_first ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_first_group_next ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_first_group_single ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_input ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_last_group_first ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_last_group_next ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_next_group_first ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_next_group_next ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_next_group_single ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_single_group_first ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_single_group_next ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_single_group_single ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_condition_state ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_entry_action ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_entry_declare ( so_called_lib_std_string & ) ;
        static void hpp_guts_type_machine_state_on_entry_implement ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_exit_action ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_exit_declare ( so_called_lib_std_string & ) ;
        static void hpp_guts_type_machine_state_on_exit_implement ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_input_action ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_input_declare ( so_called_lib_std_string & ) ;
        static void hpp_guts_type_machine_state_on_input_if_fat ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_input_if_slim_multi_actions ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_input_if_slim_single_action ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_on_input_implement ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_conditionless ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_declare ( so_called_lib_std_string & ) ;
        static void hpp_guts_type_machine_state_transition_else ( so_called_lib_std_string & result ) ;
        static void hpp_guts_type_machine_state_transition_if_fat_first ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_if_fat_next ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_if_slim_first ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_if_slim_next ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_transition_implement ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void hpp_guts_type_machine_state_public ( so_called_lib_std_string & ) ;
        static void hpp_guts_variables ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void hpp_path ( so_called_lib_std_string & ) ;
        static void injections_h_contents ( so_called_lib_std_string & , so_called_lib_std_string ) ;
        static void injections_h_path ( so_called_lib_std_string & ) ;
        static void injections_hpp_contents ( so_called_lib_std_string & ) ;
        static void injections_hpp_path ( so_called_lib_std_string & ) ;
    }

    namespace hpp
    {
        static void behaviour_determine_behaviour_inputs_change
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void behaviour_init
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void behaviour_recalc_current_behaviour_inputs
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void behaviour_reset_behaviour_input_events
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void behaviour_tick_all_fsms
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void contents 
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void every_guts_behaviour_actions_action_command
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void every_guts_machine_variable 
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void every_guts_type_machine_state_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void every_guts_type_machine_state_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void guts 
            ( so_called_lib_std_string & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void guts_behaviour_actions 
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void guts_states
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void guts_type_behaviour_inputs
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_condition_line
            ( so_called_lib_std_string &
            , so_called_lib_std_string
            , so_called_lib_std_bool
            , so_called_lib_std_bool
            , so_called_lib_std_bool
            , so_called_lib_std_bool
            , so_called_lib_std_bool
            , so_called_lib_std_bool
            ) ;
        static void guts_type_machine_state_conditions
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , const so_called_loadable_fsm_content_condition_group_container_type &
            ) ;
        static void guts_type_machine_state_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_entry_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_entry_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_exit_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_exit_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_input_actions
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_on_input_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_input_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_input_if
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_on_input_container_type :: const_iterator
            , so_called_lib_std_string
            , so_called_lib_std_string
            ) ;
        static void guts_type_machine_state_on_input_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_on_input_on_input 
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_on_input_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_transition_declare
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void guts_type_machine_state_transition_implement
            ( so_called_lib_std_string &
            , so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
    }

    namespace lookup
    {
        static system_machine_action_command_name_container_type system_machine_action_command_name_container ;
        static system_machine_condition_state_name_container_type system_machine_condition_state_name_container ;

        static void single_action 
            ( so_called_lib_std_bool &
            , const so_called_loadable_fsm_content_actions_type &
            ) ;
        static void single_condition_single_group
            ( so_called_lib_std_bool &
            , const so_called_loadable_fsm_content_condition_group_container_type &
            ) ;
        static void get_machine_action_command_names 
            ( shy_guts :: action_command_name_container_type & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
            ) ;
        static void get_machine_condition_state_names 
            ( shy_guts :: condition_state_name_container_type & 
            , so_called_loadable_fsm_content_system_container_type :: const_iterator 
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
            ) ;
        static void save_system_machine_action_command
            ( so_called_lib_std_string
            , so_called_lib_std_string
            , so_called_lib_std_string
            ) ;
        static void save_system_machine_condition_state
            ( so_called_lib_std_string
            , so_called_lib_std_string
            , so_called_lib_std_string
            ) ;
    }

    namespace prepare
    {
        static void prepare ( ) ;
        static void system
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
            ) ;
        static void system_machine
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator 
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator 
            ) ;
        static void system_machine_state
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            ) ;
        static void system_machine_state_action_command
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_action_command_container_type :: const_iterator
            ) ;
        static void system_machine_state_action_discard
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_action_discard_container_type :: const_iterator
            ) ;
        static void system_machine_state_action_do
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_action_do_container_type :: const_iterator
            ) ;
        static void system_machine_state_actions
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , const so_called_loadable_fsm_content_actions_type &
            ) ;
        static void system_machine_state_condition_command
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_condition_command_container_type :: const_iterator
            ) ;
        static void system_machine_state_condition_group
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_condition_group_container_type :: const_iterator
            ) ;
        static void system_machine_state_condition_input
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_condition_input_container_type :: const_iterator
            ) ;
        static void system_machine_state_condition_state
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_condition_state_container_type :: const_iterator
            ) ;
        static void system_machine_state_on_input
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_on_input_container_type :: const_iterator
            ) ;
        static void system_machine_state_transition
            ( so_called_loadable_fsm_content_system_container_type :: const_iterator
            , so_called_loadable_fsm_content_machine_container_type :: const_iterator
            , so_called_loadable_fsm_content_state_container_type :: const_iterator
            , so_called_loadable_fsm_content_transition_container_type :: const_iterator
            ) ;
    }
}

void shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string conditions
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: determine_behaviour_inputs_change ( so_called_platform_math_num_whole_type & inputs_changed )\n" ;
    result += "{\n" ;
    result += conditions ;
    result += "    else\n" ;
    result += "        inputs_changed = so_called_platform_math_consts :: whole_false ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_else_if ( so_called_lib_std_string & result , so_called_lib_std_string condition )
{
    result . clear ( ) ;
    result += "    else if ( ! " ;
    result += condition ;
    result += " )\n" ;
    result += "        inputs_changed = so_called_platform_math_consts :: whole_true ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_if ( so_called_lib_std_string & result , so_called_lib_std_string condition )
{
    result . clear ( ) ;
    result += "    if ( ! " ;
    result += condition ;
    result += " )\n" ;
    result += "        inputs_changed = so_called_platform_math_consts :: whole_true ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_condition_command
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "so_called_platform_conditions :: wholes_are_equal ( shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " , shy_guts :: behaviour_inputs_fixed . machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " )" ;
}

void shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_condition_state
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "so_called_platform_conditions :: wholes_are_equal ( shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " , shy_guts :: behaviour_inputs_fixed . machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " )" ;
}

void shy_guts :: consts :: hpp_behaviour_init 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string bindings
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: init ( )\n" ;
    result += "{\n" ;
    result += "    reset_behaviour_input_events ( ) ;\n" ;
    result += "    update_fixed_behaviour_inputs ( ) ;\n" ;
    result += "\n" ;
    result += "    shy_guts :: fsm_running = so_called_platform_math_consts :: whole_false ;\n" ;
    result += "\n" ;
    result += bindings ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_init_bind_initial_state 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    )
{
    result . clear ( ) ;
    result += "    so_called_platform_pointer :: bind\n" ;
    result += "        ( shy_guts :: machine_" ;
    result += machine ;
    result += "_state\n" ;
    result += "        , shy_guts :: states :: " ;
    result += machine ;
    result += "_state_initial\n" ;
    result += "        ) ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_is_fsm_running
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: is_fsm_running ( so_called_platform_math_num_whole_type & result )\n" ;
    result += "{\n" ;
    result += "    result = shy_guts :: fsm_running ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_recalc_current_behaviour_inputs
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string checkers
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: recalc_current_behaviour_inputs ( )\n" ;
    result += "{\n" ;
    result += checkers ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_recalc_current_behaviour_inputs_check_machine_state
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    so_called_platform_pointer :: is_bound_to\n" ;
    result += "        ( shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += "\n" ;
    result += "        , shy_guts :: machine_" ;
    result += machine ;
    result += "_state\n" ;
    result += "        , shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "\n" ;
    result += "        ) ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string resetters
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: reset_behaviour_input_events ( )\n" ;
    result += "{\n" ;
    result += resetters ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events_reset_machine_command
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "    shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " = so_called_platform_math_consts :: whole_false ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events_reset_machine_state_is
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " = so_called_platform_math_consts :: whole_false ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_run_fsm_begin 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: run_fsm_begin ( )\n" ;
    result += "{\n" ;
    result += "    shy_guts :: fsm_running = so_called_platform_math_consts :: whole_true ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_run_fsm_end 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: run_fsm_end ( )\n" ;
    result += "{\n" ;
    result += "    shy_guts :: fsm_running = so_called_platform_math_consts :: whole_false ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_set_inputs
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: set_inputs\n" ;
    result += "    ( so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type > inputs_current\n" ;
    result += "    , so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type > inputs_fixed\n" ;
    result += "    )\n" ;
    result += "{\n" ;
    result += "    shy_guts :: inputs_current = inputs_current ;\n" ;
    result += "    shy_guts :: inputs_fixed = inputs_fixed ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_tick_all_fsms
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string tickers
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: tick_all_fsms ( )\n" ;
    result += "{\n" ;
    result += tickers ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_behaviour_tick_all_fsms_tick_machine 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    )
{
    result . clear ( ) ;
    result += "    so_called_common_engine_fsm_stateless :: tick_single_fsm ( shy_guts :: machine_" ;
    result += machine ;
    result += "_state ) ;\n" ;
}

void shy_guts :: consts :: hpp_behaviour_update_fixed_behaviour_inputs 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    )
{
    result . clear ( ) ;
    result += "void so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static :: update_fixed_behaviour_inputs ( )\n" ;
    result += "{\n" ;
    result += "    shy_guts :: behaviour_inputs_fixed = shy_guts :: behaviour_inputs_current ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts
    ( so_called_lib_std_string & result
    , so_called_lib_std_string contents
    )
{
    result . clear ( ) ;
    result += "namespace shy_guts\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    , so_called_lib_std_string methods
    )
{
    result . clear ( ) ;
    result += "    class machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += "\n" ;
    result += "    : public so_called_common_engine_fsm_state_type\n" ;
    result += "    {\n" ;
    result += methods ;
    result += "    } ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_declare ( so_called_lib_std_string & result )
{
    result = "        virtual void on_entry ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_declare ( so_called_lib_std_string & result )
{
    result = "        virtual void on_exit ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_declare ( so_called_lib_std_string & result )
{
    result = "        virtual void on_input ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_declare ( so_called_lib_std_string & result )
{
    result = "        virtual so_called_common_engine_fsm_state_type & transition ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_public ( so_called_lib_std_string & result )
{
    result = "    public :\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_action_command
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "shy_guts :: behaviour_actions :: " ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_action_discard
    ( so_called_lib_std_string & result
    , so_called_lib_std_string input
    )
{
    result . clear ( ) ;
    result += "shy_guts :: inputs_current . get ( ) . " ;
    result += input ;
    result += " = so_called_platform_math_consts :: whole_false ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_action_do
    ( so_called_lib_std_string & result
    , so_called_lib_std_string system
    , so_called_lib_std_string action
    )
{
    result . clear ( ) ;
    result += "so_called_common_" ;
    result += system ;
    result += "_fsm_actions :: " ;
    result += action ;
    result += " ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_input
    ( so_called_lib_std_string & result
    , so_called_lib_std_string input
    )
{
    result . clear ( ) ;
    result += "so_called_platform_conditions :: whole_is_true ( shy_guts :: inputs_fixed . get ( ) . " ;
    result += input ;
    result += " )" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_state
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "so_called_platform_conditions :: whole_is_true ( shy_guts :: behaviour_inputs_fixed . machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " )" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_command
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "so_called_platform_conditions :: whole_is_true ( shy_guts :: behaviour_inputs_fixed . machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " )" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += " (  " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "       && " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += " " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_last_group_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "       && " ;
    result += condition ;
    result += "\n" ;
    result += "       )\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "    || (  " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "       && " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_last_group_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "       && " ;
    result += condition ;
    result += "\n" ;
    result += "       )\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "    || " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_single
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += " " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_single
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += "    && " ;
    result += condition ;
    result += "\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_single
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    )
{
    result . clear ( ) ;
    result += condition ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_implement
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    , so_called_lib_std_string contents
    )
{
    result . clear ( ) ;
    result += "void shy_guts :: machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += " :: on_entry ( )\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_action
    ( so_called_lib_std_string & result
    , so_called_lib_std_string action
    )
{
    result . clear ( ) ;
    result += "    " ;
    result += action ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_implement
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    , so_called_lib_std_string contents
    )
{
    result . clear ( ) ;
    result += "void shy_guts :: machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += " :: on_exit ( )\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_action
    ( so_called_lib_std_string & result
    , so_called_lib_std_string action
    )
{
    result . clear ( ) ;
    result += "    " ;
    result += action ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_implement
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    , so_called_lib_std_string contents
    )
{
    result . clear ( ) ;
    result += "void shy_guts :: machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += " :: on_input ( )\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_action
    ( so_called_lib_std_string & result
    , so_called_lib_std_string action
    )
{
    result . clear ( ) ;
    result += "        " ;
    result += action ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_fat
    ( so_called_lib_std_string & result
    , so_called_lib_std_string conditions
    , so_called_lib_std_string actions
    )
{
    result . clear ( ) ;
    result += "    if\n" ;
    result += "    ( " ;
    result += conditions ;
    result += "    )\n" ;
    result += "    {\n" ;
    result += actions ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_slim_single_action
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    , so_called_lib_std_string action
    )
{
    result . clear ( ) ;
    result += "    if ( " ;
    result += condition ;
    result += " )\n" ;
    result += action ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_slim_multi_actions
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    , so_called_lib_std_string actions
    )
{
    result . clear ( ) ;
    result += "    if ( " ;
    result += condition ;
    result += " )\n" ;
    result += "    {\n" ;
    result += actions ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_implement
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    , so_called_lib_std_string contents
    )
{
    result . clear ( ) ;
    result += "so_called_common_engine_fsm_state_type & shy_guts :: machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += " :: transition ( )\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_fat_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string conditions
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    if\n" ;
    result += "    ( " ;
    result += conditions ;
    result += "    )\n" ;
    result += "    {\n" ;
    result += "        return shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_fat_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string conditions
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    else if\n" ;
    result += "    ( " ;
    result += conditions ;
    result += "    )\n" ;
    result += "    {\n" ;
    result += "        return shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_slim_first
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    if ( " ;
    result += condition ;
    result += " )\n" ;
    result += "        return shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_slim_next
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    else if ( " ;
    result += condition ;
    result += " )\n" ;
    result += "        return shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_conditionless 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "    return shy_guts :: states :: " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_machine_state_transition_else ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += "    else\n" ;
    result += "        return so_called_common_engine_fsm_state_type :: transition ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_behaviour_inputs 
    ( so_called_lib_std_string & result 
    , so_called_lib_std_string inputs
    )
{
    result . clear ( ) ;
    result += "    class behaviour_inputs_type\n" ;
    result += "    {\n" ;
    result += "    public :\n" ;
    result += inputs ;
    result += "    } ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_behaviour_inputs_action_command_variable
    ( so_called_lib_std_string & result 
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "        so_called_platform_math_num_whole_type machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_type_behaviour_inputs_condition_state_variable
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    result . clear ( ) ;
    result += "        so_called_platform_math_num_whole_type machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_behaviour_actions ( so_called_lib_std_string & result , so_called_lib_std_string actions )
{
    result . clear ( ) ;
    result += "    namespace behaviour_actions\n" ;
    result += "    {\n" ;
    result += actions ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_behaviour_actions_action_command_declare
    ( so_called_lib_std_string & result 
    , so_called_lib_std_string machine 
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "        static void " ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_behaviour_actions_action_command_implement
    ( so_called_lib_std_string & result
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    result . clear ( ) ;
    result += "void shy_guts :: behaviour_actions :: " ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ( )\n" ;
    result += "{\n" ;
    result += "    shy_guts :: behaviour_inputs_current . machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " = so_called_platform_math_consts :: whole_true ;\n" ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_states ( so_called_lib_std_string & result , so_called_lib_std_string states )
{
    result . clear ( ) ;
    result += "    namespace states\n" ;
    result += "    {\n" ;
    result += states ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_states_state_variable ( so_called_lib_std_string & result , so_called_lib_std_string machine , so_called_lib_std_string state )
{
    result . clear ( ) ;
    result += "       static machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += "_type" ;
    result += " " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_machine_variable ( so_called_lib_std_string & result , so_called_lib_std_string machine )
{
    result . clear ( ) ;
    result += "    static so_called_platform_pointer_data_type < so_called_common_engine_fsm_state_type > machine_" ;
    result += machine ;
    result += "_state ;\n" ;
}

void shy_guts :: consts :: hpp_guts_variables ( so_called_lib_std_string & result , so_called_lib_std_string system )
{
    result . clear ( ) ;
    result += "    static so_called_platform_math_num_whole_type fsm_running ;\n" ;
    result += "    static behaviour_inputs_type behaviour_inputs_current ;\n" ;
    result += "    static behaviour_inputs_type behaviour_inputs_fixed ;\n" ;
    result += "    static so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type > inputs_current ;\n" ;
    result += "    static so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type > inputs_fixed ;\n" ;
}

void shy_guts :: consts :: injections_h_path ( so_called_lib_std_string & path )
{
    path = "/fsm/behaviour/static/autogenerated/shy_autogenerated_injections.h" ;
}

void shy_guts :: consts :: injections_hpp_path ( so_called_lib_std_string & path )
{
    path = "/fsm/behaviour/static/autogenerated/shy_autogenerated_injections.hpp" ;
}

void shy_guts :: consts :: h_path ( so_called_lib_std_string & path )
{
    path = "/fsm/behaviour/static/autogenerated/shy_autogenerated.h" ;
}

void shy_guts :: consts :: hpp_path ( so_called_lib_std_string & path )
{
    path = "/fsm/behaviour/static/autogenerated/shy_autogenerated.hpp" ;
}

void shy_guts :: consts :: h_contents ( so_called_lib_std_string & result , so_called_lib_std_string system )
{
    result . clear ( ) ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_begin ;
    result += "\n" ;
    result += "class shy_common_" ;
    result += system ;
    result += "_fsm_behaviour_static\n" ;
    result += "{\n" ;
    result += "public :\n" ;
    result += "    static void determine_behaviour_inputs_change ( so_called_platform_math_num_whole_type & ) ;\n" ;
    result += "    static void init ( ) ;\n" ;
    result += "    static void is_fsm_running ( so_called_platform_math_num_whole_type & ) ;\n" ;
    result += "    static void recalc_current_behaviour_inputs ( ) ;\n" ;
    result += "    static void reset_behaviour_input_events ( ) ;\n" ;
    result += "    static void run_fsm_begin ( ) ;\n" ;
    result += "    static void run_fsm_end ( ) ;\n" ;
    result += "    static void set_inputs\n" ;
    result += "        ( so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type >\n" ;
    result += "        , so_called_platform_pointer_data_type < so_called_common_" ;
    result += system ;
    result += "_fsm_inputs_type >\n" ;
    result += "        ) ;\n" ;
    result += "    static void tick_all_fsms ( ) ;\n" ;
    result += "    static void update_fixed_behaviour_inputs ( ) ;\n" ;
    result += "} ;\n" ;
    result += "\n" ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_end ;
}

void shy_guts :: consts :: injections_h_contents ( so_called_lib_std_string & result , so_called_lib_std_string system )
{
    result . clear ( ) ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_begin ;
    result += "\n" ;
    result += "#ifndef _shy_common_" ;
    result += system ;
    result += "_fsm_behaviour_static_autogenerated_injections_included\n" ;
    result += "#define _shy_common_" ;
    result += system ;
    result += "_fsm_behaviour_static_autogenerated_injections_included\n" ;
    result += "\n" ;
    result += "#include \"src/injections/platform/pointer/data/type/shy_type.h\"\n" ;
    result += "\n" ;
    result += "#include \"./shy_autogenerated.h\"\n" ;
    result += "\n" ;
    result += "typedef shy_common_" ;
    result += system ;
    result += "_fsm_behaviour_static so_called_common_" ;
    result += system ;
    result += "_fsm_behaviour_static ;\n" ;
    result += "\n" ;
    result += "#endif\n" ;
    result += "\n" ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_end ;
}

void shy_guts :: consts :: injections_hpp_contents ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_begin ;
    result += "\n" ;
    result += "#include \"src/common/engine/fsm/stateless/shy_stateless_injections.h\"\n" ;
    result += "\n" ;
    result += "#include \"src/injections/platform/math/consts/shy_consts.h\"\n" ;
    result += "\n" ;
    result += "#include \"./shy_autogenerated.hpp\"\n" ;
    result += "\n" ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_end ;
}

void shy_guts :: hpp :: contents 
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string behaviour_determine_behaviour_inputs_change ;
    so_called_lib_std_string behaviour_init ;
    so_called_lib_std_string behaviour_is_fsm_running ;
    so_called_lib_std_string behaviour_recalc_current_behaviour_inputs ;
    so_called_lib_std_string behaviour_reset_behaviour_input_events ;
    so_called_lib_std_string behaviour_run_fsm_begin ;
    so_called_lib_std_string behaviour_run_fsm_end ;
    so_called_lib_std_string behaviour_set_inputs ;
    so_called_lib_std_string behaviour_tick_all_fsms ;
    so_called_lib_std_string behaviour_update_fixed_behaviour_inputs ;
    so_called_lib_std_string every_guts_behaviour_actions_action_command ;
    so_called_lib_std_string every_guts_type_machine_state_implement ;
    so_called_lib_std_string guts ;

    shy_guts :: consts :: hpp_behaviour_is_fsm_running ( behaviour_is_fsm_running , system_i -> first ) ;
    shy_guts :: consts :: hpp_behaviour_run_fsm_begin ( behaviour_run_fsm_begin , system_i -> first ) ;
    shy_guts :: consts :: hpp_behaviour_run_fsm_end ( behaviour_run_fsm_end , system_i -> first ) ;
    shy_guts :: consts :: hpp_behaviour_set_inputs ( behaviour_set_inputs , system_i -> first ) ;
    shy_guts :: consts :: hpp_behaviour_update_fixed_behaviour_inputs ( behaviour_update_fixed_behaviour_inputs , system_i -> first ) ;
    shy_guts :: hpp :: behaviour_determine_behaviour_inputs_change ( behaviour_determine_behaviour_inputs_change , system_i ) ;
    shy_guts :: hpp :: behaviour_init ( behaviour_init , system_i ) ;
    shy_guts :: hpp :: behaviour_recalc_current_behaviour_inputs ( behaviour_recalc_current_behaviour_inputs , system_i ) ;
    shy_guts :: hpp :: behaviour_reset_behaviour_input_events ( behaviour_reset_behaviour_input_events , system_i ) ;
    shy_guts :: hpp :: behaviour_tick_all_fsms ( behaviour_tick_all_fsms , system_i ) ;
    shy_guts :: hpp :: every_guts_behaviour_actions_action_command ( every_guts_behaviour_actions_action_command , system_i ) ;
    shy_guts :: hpp :: every_guts_type_machine_state_implement ( every_guts_type_machine_state_implement , system_i ) ;
    shy_guts :: hpp :: guts ( guts , system_i ) ;

    result . clear ( ) ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_begin ;
    result += so_called_platform_generator_consts :: new_line ;
    result += guts ;
    result += so_called_platform_generator_consts :: new_line ;
    result += every_guts_type_machine_state_implement ;
    result += so_called_platform_generator_consts :: new_line ;
    result += every_guts_behaviour_actions_action_command ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_determine_behaviour_inputs_change ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_init ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_is_fsm_running ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_recalc_current_behaviour_inputs ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_reset_behaviour_input_events ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_run_fsm_begin ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_run_fsm_end ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_set_inputs ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_tick_all_fsms ;
    result += so_called_platform_generator_consts :: new_line ;
    result += behaviour_update_fixed_behaviour_inputs ;
    result += so_called_platform_generator_consts :: new_line ;
    result += so_called_platform_generator_consts :: autogenerated_cpp_file_end ;
}

void shy_guts :: hpp :: every_guts_type_machine_state_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    result . clear ( ) ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        for ( so_called_loadable_fsm_content_state_container_type :: const_iterator state_i = machine_i -> second . states . begin ( )
            ; state_i != machine_i -> second . states . end ( )
            ; ++ state_i
            )
        {
            so_called_lib_std_string state_implement ;
            shy_guts :: hpp :: guts_type_machine_state_implement ( state_implement , system_i , machine_i , state_i ) ;
            if ( ! state_implement . empty ( ) )
            {
                if ( ! result . empty ( ) )
                    result += so_called_platform_generator_consts :: new_line ;
                result += state_implement ;
            }
        }
    }
}

void shy_guts :: hpp :: guts_type_machine_state_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string guts_type_machine_state_on_entry_implement ;
    so_called_lib_std_string guts_type_machine_state_on_exit_implement ;
    so_called_lib_std_string guts_type_machine_state_on_input_implement ;
    so_called_lib_std_string guts_type_machine_state_transition_implement ;

    shy_guts :: hpp :: guts_type_machine_state_on_entry_implement ( guts_type_machine_state_on_entry_implement , system_i , machine_i , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_on_exit_implement ( guts_type_machine_state_on_exit_implement , system_i , machine_i , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_on_input_implement ( guts_type_machine_state_on_input_implement , system_i , machine_i , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_transition_implement ( guts_type_machine_state_transition_implement , system_i , machine_i , state_i ) ;

    result . clear ( ) ;

    if ( ! guts_type_machine_state_on_entry_implement . empty ( ) )
    {
        if ( ! result . empty ( ) )
            result += so_called_platform_generator_consts :: new_line ;
        result += guts_type_machine_state_on_entry_implement ;
    }

    if ( ! guts_type_machine_state_on_exit_implement . empty ( ) )
    {
        if ( ! result . empty ( ) )
            result += so_called_platform_generator_consts :: new_line ;
        result += guts_type_machine_state_on_exit_implement ;
    }

    if ( ! guts_type_machine_state_on_input_implement . empty ( ) )
    {
        if ( ! result . empty ( ) )
            result += so_called_platform_generator_consts :: new_line ;
        result += guts_type_machine_state_on_input_implement ;
    }

    if ( ! guts_type_machine_state_transition_implement . empty ( ) )
    {
        if ( ! result . empty ( ) )
            result += so_called_platform_generator_consts :: new_line ;
        result += guts_type_machine_state_transition_implement ;
    }
}

void shy_guts :: hpp :: guts_type_machine_state_on_entry_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string actions ;

    for ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i = state_i -> second . on_entry . actions . begin ( )
        ; action_do_i != state_i -> second . on_entry . actions . end ( )
        ; ++ action_do_i
        )
    {
        so_called_lib_std_string action_do ;
        so_called_lib_std_string on_entry_action_do ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_do ( action_do , system_i -> first , action_do_i -> action ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_action ( on_entry_action_do , action_do ) ;
        actions += on_entry_action_do ;
    }

    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i = state_i -> second . on_entry . commands . begin ( )
        ; action_command_i != state_i -> second . on_entry . commands . end ( )
        ; ++ action_command_i
        )
    {
        so_called_lib_std_string action_command ;
        so_called_lib_std_string on_entry_action_command ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_command ( action_command , action_command_i -> machine , action_command_i -> command ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_action ( on_entry_action_command , action_command ) ;
        actions += on_entry_action_command ;
    }

    for ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i = state_i -> second . on_entry . discards . begin ( )
        ; action_discard_i != state_i -> second . on_entry . discards . end ( )
        ; ++ action_discard_i
        )
    {
        so_called_lib_std_string action_discard ;
        so_called_lib_std_string on_entry_action_discard ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_discard ( action_discard , action_discard_i -> input ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_action ( on_entry_action_discard , action_discard ) ;
        actions += on_entry_action_discard ;
    }

    if ( ! actions . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_implement ( result , machine_i -> first , state_i -> first , actions ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_on_exit_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string actions ;

    for ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i = state_i -> second . on_exit . actions . begin ( )
        ; action_do_i != state_i -> second . on_exit . actions . end ( )
        ; ++ action_do_i
        )
    {
        so_called_lib_std_string action_do ;
        so_called_lib_std_string on_exit_action_do ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_do ( action_do , system_i -> first , action_do_i -> action ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_action ( on_exit_action_do , action_do ) ;
        actions += on_exit_action_do ;
    }

    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i = state_i -> second . on_exit . commands . begin ( )
        ; action_command_i != state_i -> second . on_exit . commands . end ( )
        ; ++ action_command_i
        )
    {
        so_called_lib_std_string action_command ;
        so_called_lib_std_string on_exit_action_command ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_command ( action_command , action_command_i -> machine , action_command_i -> command ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_action ( on_exit_action_command , action_command ) ;
        actions += on_exit_action_command ;
    }

    for ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i = state_i -> second . on_exit . discards . begin ( )
        ; action_discard_i != state_i -> second . on_exit . discards . end ( )
        ; ++ action_discard_i
        )
    {
        so_called_lib_std_string action_discard ;
        so_called_lib_std_string on_exit_action_discard ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_discard ( action_discard , action_discard_i -> input ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_action ( on_exit_action_discard , action_discard ) ;
        actions += on_exit_action_discard ;
    }

    if ( ! actions . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_implement ( result , machine_i -> first , state_i -> first , actions ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_on_input_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string all_inputs ;

    for ( so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i = state_i -> second . on_input . begin ( )
        ; on_input_i != state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        so_called_lib_std_string single_input ;
        shy_guts :: hpp :: guts_type_machine_state_on_input_on_input ( single_input , system_i , machine_i , on_input_i ) ;
        all_inputs += single_input ;
    }

    if ( ! all_inputs . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_implement ( result , machine_i -> first , state_i -> first , all_inputs ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_on_input_on_input 
    ( so_called_lib_std_string & result 
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i 
    )
{
    so_called_lib_std_string actions ;
    so_called_lib_std_string conditions ;

    shy_guts :: hpp :: guts_type_machine_state_on_input_actions ( actions , system_i , on_input_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_conditions ( conditions , machine_i , on_input_i -> condition_groups ) ;
    shy_guts :: hpp :: guts_type_machine_state_on_input_if ( result , on_input_i , conditions , actions ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_on_input_actions
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i
    )
{
    result . clear ( ) ;

    for ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i = on_input_i -> actions . actions . begin ( )
        ; action_do_i != on_input_i -> actions . actions . end ( )
        ; ++ action_do_i
        )
    {
        so_called_lib_std_string action_do ;
        so_called_lib_std_string on_input_action_do ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_do ( action_do , system_i -> first , action_do_i -> action ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_action ( on_input_action_do , action_do ) ;
        result += on_input_action_do ;
    }

    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i = on_input_i -> actions . commands . begin ( )
        ; action_command_i != on_input_i -> actions . commands . end ( )
        ; ++ action_command_i
        )
    {
        so_called_lib_std_string action_command ;
        so_called_lib_std_string on_input_action_command ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_command ( action_command , action_command_i -> machine , action_command_i -> command ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_action ( on_input_action_command , action_command ) ;
        result += on_input_action_command ;
    }

    for ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i = on_input_i -> actions . discards . begin ( )
        ; action_discard_i != on_input_i -> actions . discards . end ( )
        ; ++ action_discard_i
        )
    {
        so_called_lib_std_string action_discard ;
        so_called_lib_std_string on_input_action_discard ;
        shy_guts :: consts :: hpp_guts_type_machine_state_action_discard ( action_discard , action_discard_i -> input ) ;
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_action ( on_input_action_discard , action_discard ) ;
        result += on_input_action_discard ;
    }
}

void shy_guts :: hpp :: guts_type_machine_state_condition_line
    ( so_called_lib_std_string & result
    , so_called_lib_std_string condition
    , so_called_lib_std_bool group_first
    , so_called_lib_std_bool group_last
    , so_called_lib_std_bool group_single
    , so_called_lib_std_bool condition_first
    , so_called_lib_std_bool condition_last
    , so_called_lib_std_bool condition_single
    )
{
    if ( group_single )
    {
        if ( condition_single )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_single ( result , condition ) ;
        else if ( condition_first )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_single ( result , condition ) ;
        else
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_single ( result , condition ) ;
    }
    else if ( group_first )
    {
        if ( condition_single )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_first ( result , condition ) ;
        else if ( condition_first )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_first ( result , condition ) ;
        else if ( condition_last )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_last_group_first ( result , condition ) ;
        else
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_first ( result , condition ) ;
    }
    else
    {
        if ( condition_single )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_single_group_next ( result , condition ) ;
        else if ( condition_first )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_first_group_next ( result , condition ) ;
        else if ( condition_last )
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_last_group_next ( result , condition ) ;
        else
            shy_guts :: consts :: hpp_guts_type_machine_state_condition_next_group_next ( result , condition ) ;
    }
}

void shy_guts :: hpp :: guts_type_machine_state_conditions
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , const so_called_loadable_fsm_content_condition_group_container_type & condition_group_container
    )
{
    result . clear ( ) ;
    for ( so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i = condition_group_container . begin ( )
        ; condition_group_i != condition_group_container . end ( )
        ; ++ condition_group_i
        )
    {
        so_called_lib_std_bool group_first = so_called_lib_std_true ;
        so_called_lib_std_bool group_last = so_called_lib_std_true ;
        so_called_lib_std_bool group_single = so_called_lib_std_true ;

        group_first &= condition_group_i == condition_group_container . begin ( ) ;
        group_last &= condition_group_i == condition_group_container . end ( ) - 1 ;
        group_single &= group_first ;
        group_single &= group_last ;

        for ( so_called_loadable_fsm_content_condition_input_container_type :: const_iterator condition_input_i = condition_group_i -> inputs . begin ( )
            ; condition_input_i != condition_group_i -> inputs . end ( )
            ; ++ condition_input_i
            )
        {
            so_called_lib_std_string condition_line ;
            so_called_lib_std_string condition_input ;
            so_called_lib_std_bool condition_first = so_called_lib_std_true ;
            so_called_lib_std_bool condition_last = so_called_lib_std_true ;
            so_called_lib_std_bool condition_single = so_called_lib_std_true ;

            shy_guts :: consts :: hpp_guts_type_machine_state_condition_input ( condition_input , condition_input_i -> input ) ;

            condition_first &= condition_input_i == condition_group_i -> inputs . begin ( ) ;
            condition_last &= condition_input_i == condition_group_i -> inputs . end ( ) - 1 ;
            condition_last &= condition_group_i -> states . empty ( ) ;
            condition_last &= condition_group_i -> commands . empty ( ) ;
            condition_single &= condition_first ;
            condition_single &= condition_last ;

            shy_guts :: hpp :: guts_type_machine_state_condition_line
                ( condition_line
                , condition_input
                , group_first
                , group_last
                , group_single
                , condition_first
                , condition_last
                , condition_single
                ) ;

            result += condition_line ;
        }

        for ( so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i = condition_group_i -> states . begin ( )
            ; condition_state_i != condition_group_i -> states . end ( )
            ; ++ condition_state_i
            )
        {
            so_called_lib_std_string condition_line ;
            so_called_lib_std_string condition_state ;
            so_called_lib_std_bool condition_first = so_called_lib_std_true ;
            so_called_lib_std_bool condition_last = so_called_lib_std_true ;
            so_called_lib_std_bool condition_single = so_called_lib_std_true ;

            shy_guts :: consts :: hpp_guts_type_machine_state_condition_state ( condition_state , condition_state_i -> machine , condition_state_i -> state ) ;

            condition_first &= condition_group_i -> inputs . empty ( ) ;
            condition_first &= condition_state_i == condition_group_i -> states . begin ( ) ;
            condition_last &= condition_state_i == condition_group_i -> states . end ( ) - 1 ;
            condition_last &= condition_group_i -> commands . empty ( ) ;
            condition_single &= condition_first ;
            condition_single &= condition_last ;

            shy_guts :: hpp :: guts_type_machine_state_condition_line
                ( condition_line
                , condition_state
                , group_first
                , group_last
                , group_single
                , condition_first
                , condition_last
                , condition_single
                ) ;

            result += condition_line ;
        }

        for ( so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i = condition_group_i -> commands . begin ( )
            ; condition_command_i != condition_group_i -> commands . end ( )
            ; ++ condition_command_i
            )
        {
            so_called_lib_std_string condition_line ;
            so_called_lib_std_string condition_command ;
            so_called_lib_std_bool condition_first = so_called_lib_std_true ;
            so_called_lib_std_bool condition_last = so_called_lib_std_true ;
            so_called_lib_std_bool condition_single = so_called_lib_std_true ;

            shy_guts :: consts :: hpp_guts_type_machine_state_condition_command ( condition_command , machine_i -> first , condition_command_i -> command ) ;

            condition_first &= condition_group_i -> inputs . empty ( ) ;
            condition_first &= condition_group_i -> states . empty ( ) ;
            condition_first &= condition_command_i == condition_group_i -> commands . begin ( ) ;
            condition_last &= condition_command_i == condition_group_i -> commands . end ( ) - 1 ;
            condition_single &= condition_first ;
            condition_single &= condition_last ;

            shy_guts :: hpp :: guts_type_machine_state_condition_line
                ( condition_line
                , condition_command
                , group_first
                , group_last
                , group_single
                , condition_first
                , condition_last
                , condition_single
                ) ;

            result += condition_line ;
        }
    }
}

void shy_guts :: hpp :: guts_type_machine_state_on_input_if
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i
    , so_called_lib_std_string conditions
    , so_called_lib_std_string actions
    )
{
    so_called_lib_std_bool single_condition = so_called_lib_std_false ;
    so_called_lib_std_bool single_action = so_called_lib_std_false ;

    shy_guts :: lookup :: single_condition_single_group ( single_condition , on_input_i -> condition_groups ) ;
    shy_guts :: lookup :: single_action ( single_action , on_input_i -> actions ) ;

    if ( single_condition )
    {
        if ( single_action )
            shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_slim_single_action ( result , conditions , actions ) ;
        else
            shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_slim_multi_actions ( result , conditions , actions ) ;
    }
    else
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_if_fat ( result , conditions , actions ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_transition_implement
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string all_transitions ;

    so_called_lib_std_bool conditionless = so_called_lib_std_true ;
    if ( conditionless )
        conditionless &= state_i -> second . transitions . size ( ) == 1 ;
    if ( conditionless )
        conditionless &= state_i -> second . transitions . begin ( ) -> condition_groups . empty ( ) ;
    
    if ( conditionless )
    {
        shy_guts :: consts :: hpp_guts_type_machine_state_transition_conditionless
            ( all_transitions
            , machine_i -> first
            , state_i -> second . transitions . begin ( ) -> state
            ) ;
    }
    else
    {
        for ( so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i = state_i -> second . transitions . begin ( )
            ; transition_i != state_i -> second . transitions . end ( )
            ; ++ transition_i
            )
        {
            so_called_lib_std_string conditions ;
            so_called_lib_std_string transition ;
            so_called_lib_std_bool single_condition = so_called_lib_std_false ;
            so_called_lib_std_bool first_transition = so_called_lib_std_false ;

            first_transition = transition_i == state_i -> second . transitions . begin ( ) ;
            shy_guts :: lookup :: single_condition_single_group ( single_condition , transition_i -> condition_groups ) ;
            shy_guts :: hpp :: guts_type_machine_state_conditions ( conditions , machine_i , transition_i -> condition_groups ) ;

            if ( single_condition )
            {
                if ( first_transition )
                {
                    shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_slim_first
                        ( transition
                        , conditions
                        , machine_i -> first
                        , transition_i -> state
                        ) ;
                }
                else
                {
                    shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_slim_next
                        ( transition
                        , conditions
                        , machine_i -> first
                        , transition_i -> state
                        ) ;
                }
            }
            else
            {
                if ( first_transition )
                {
                    shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_fat_first
                        ( transition
                        , conditions
                        , machine_i -> first
                        , transition_i -> state
                        ) ;
                }
                else
                {
                    shy_guts :: consts :: hpp_guts_type_machine_state_transition_if_fat_next
                        ( transition
                        , conditions
                        , machine_i -> first
                        , transition_i -> state
                        ) ;
                }
            }

            all_transitions += transition ;
        }

        if ( ! all_transitions . empty ( ) )
        {
            so_called_lib_std_string else_part ;
            shy_guts :: consts :: hpp_guts_type_machine_state_transition_else ( else_part ) ;
            all_transitions += else_part ;
        }
    }

    if ( ! all_transitions . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_transition_implement ( result , machine_i -> first , state_i -> first , all_transitions ) ;
}

void shy_guts :: hpp :: behaviour_tick_all_fsms
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string tickers ;

    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_lib_std_string tick_machine ;
        shy_guts :: consts :: hpp_behaviour_tick_all_fsms_tick_machine ( tick_machine , machine_i -> first ) ;
        tickers += tick_machine ;
    }

    shy_guts :: consts :: hpp_behaviour_tick_all_fsms
        ( result
        , system_i -> first
        , tickers
        ) ;
}

void shy_guts :: hpp :: behaviour_reset_behaviour_input_events
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string resetters ;

    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: action_command_name_container_type action_command_names ;
        shy_guts :: condition_state_name_container_type condition_state_names ;
        shy_guts :: lookup :: get_machine_action_command_names ( action_command_names , system_i , machine_i ) ;
        shy_guts :: lookup :: get_machine_condition_state_names ( condition_state_names , system_i , machine_i ) ;

        for ( shy_guts :: action_command_name_container_type :: contents_type :: const_iterator action_command_name_i = action_command_names . contents . begin ( )
            ; action_command_name_i != action_command_names . contents . end ( )
            ; ++ action_command_name_i
            )
        {
            so_called_lib_std_string input_command_reset ;
            shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events_reset_machine_command ( input_command_reset , machine_i -> first , * action_command_name_i ) ;
            resetters += input_command_reset ;
        }

        for ( shy_guts :: condition_state_name_container_type :: contents_type :: const_iterator condition_state_name_i = condition_state_names . contents . begin ( )
            ; condition_state_name_i != condition_state_names . contents . end ( )
            ; ++ condition_state_name_i
            )
        {
            so_called_lib_std_string input_state_is_reset ;
            shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events_reset_machine_state_is ( input_state_is_reset , machine_i -> first , * condition_state_name_i ) ;
            resetters += input_state_is_reset ;
        }
    }

    shy_guts :: consts :: hpp_behaviour_reset_behaviour_input_events
        ( result
        , system_i -> first
        , resetters
        ) ;
}

void shy_guts :: hpp :: behaviour_recalc_current_behaviour_inputs
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string checkers ;

    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: condition_state_name_container_type condition_state_names ;
        shy_guts :: lookup :: get_machine_condition_state_names ( condition_state_names , system_i , machine_i ) ;

        for ( shy_guts :: condition_state_name_container_type :: contents_type :: const_iterator condition_state_name_i = condition_state_names . contents . begin ( )
            ; condition_state_name_i != condition_state_names . contents . end ( )
            ; ++ condition_state_name_i
            )
        {
            so_called_lib_std_string state_checker ;
            shy_guts :: consts :: hpp_behaviour_recalc_current_behaviour_inputs_check_machine_state ( state_checker , machine_i -> first , * condition_state_name_i ) ;
            checkers += state_checker ;
        }
    }

    shy_guts :: consts :: hpp_behaviour_recalc_current_behaviour_inputs
        ( result
        , system_i -> first
        , checkers
        ) ;
}

void shy_guts :: hpp :: behaviour_determine_behaviour_inputs_change
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_bool first_condition = so_called_lib_std_true ;
    so_called_lib_std_string conditions ;

    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: action_command_name_container_type action_command_names ;
        shy_guts :: condition_state_name_container_type condition_state_names ;

        shy_guts :: lookup :: get_machine_action_command_names ( action_command_names , system_i , machine_i ) ;
        shy_guts :: lookup :: get_machine_condition_state_names ( condition_state_names , system_i , machine_i ) ;

        for ( shy_guts :: action_command_name_container_type :: contents_type :: const_iterator action_command_name_i = action_command_names . contents . begin ( )
            ; action_command_name_i != action_command_names . contents . end ( )
            ; ++ action_command_name_i
            )
        {
            so_called_lib_std_string condition ;
            shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_condition_command ( condition , machine_i -> first , * action_command_name_i ) ;
            if ( first_condition )
            {
                first_condition = so_called_lib_std_false ;
                so_called_lib_std_string condition_if ;
                shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_if ( condition_if , condition ) ;
                conditions += condition_if ;
            }
            else
            {
                so_called_lib_std_string condition_else_if ;
                shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_else_if ( condition_else_if , condition ) ;
                conditions += condition_else_if ;
            }
        }

        for ( shy_guts :: condition_state_name_container_type :: contents_type :: const_iterator condition_state_name_i = condition_state_names . contents . begin ( )
            ; condition_state_name_i != condition_state_names . contents . end ( )
            ; ++ condition_state_name_i
            )
        {
            so_called_lib_std_string condition ;
            shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_condition_state ( condition , machine_i -> first , * condition_state_name_i ) ;

            if ( first_condition )
            {
                first_condition = so_called_lib_std_false ;
                so_called_lib_std_string condition_if ;
                shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_if ( condition_if , condition ) ;
                conditions += condition_if ;
            }
            else
            {
                so_called_lib_std_string condition_else_if ;
                shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change_else_if ( condition_else_if , condition ) ;
                conditions += condition_else_if ;
            }
        }
    }

    shy_guts :: consts :: hpp_behaviour_determine_behaviour_inputs_change
        ( result
        , system_i -> first
        , conditions
        ) ;
}

void shy_guts :: hpp :: behaviour_init
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string states ;

    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_lib_std_string state_binding ;
        shy_guts :: consts :: hpp_behaviour_init_bind_initial_state ( state_binding , machine_i -> first ) ;
        states += state_binding ;
    }

    shy_guts :: consts :: hpp_behaviour_init
        ( result
        , system_i -> first
        , states
        ) ;
}

void shy_guts :: hpp :: guts 
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    so_called_lib_std_string every_guts_machine_variable ;
    so_called_lib_std_string every_guts_type_machine_state_declare ;
    so_called_lib_std_string guts_behaviour_actions ;
    so_called_lib_std_string guts_states ;
    so_called_lib_std_string guts_type_behaviour_inputs ;
    so_called_lib_std_string guts_variables ;

    shy_guts :: hpp :: every_guts_machine_variable ( every_guts_machine_variable , system_i ) ;
    shy_guts :: hpp :: every_guts_type_machine_state_declare ( every_guts_type_machine_state_declare , system_i ) ;
    shy_guts :: hpp :: guts_behaviour_actions ( guts_behaviour_actions , system_i ) ;
    shy_guts :: hpp :: guts_states ( guts_states , system_i ) ;
    shy_guts :: hpp :: guts_type_behaviour_inputs ( guts_type_behaviour_inputs , system_i ) ;
    shy_guts :: consts :: hpp_guts_variables ( guts_variables , system_i -> first ) ;

    shy_guts :: consts :: hpp_guts
        ( result
        , every_guts_type_machine_state_declare
        + so_called_platform_generator_consts :: new_line
        + guts_type_behaviour_inputs
        + so_called_platform_generator_consts :: new_line
        + guts_states
        + so_called_platform_generator_consts :: new_line
        + guts_behaviour_actions
        + so_called_platform_generator_consts :: new_line
        + every_guts_machine_variable
        + so_called_platform_generator_consts :: new_line
        + guts_variables
        ) ;
}

void shy_guts :: hpp :: every_guts_type_machine_state_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i 
    )
{
    result . clear ( ) ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        for ( so_called_loadable_fsm_content_state_container_type :: const_iterator state_i = machine_i -> second . states . begin ( )
            ; state_i != machine_i -> second . states . end ( )
            ; ++ state_i
            )
        {
            if ( machine_i != system_i -> second . machines . begin ( ) || state_i != machine_i -> second . states . begin ( ) )
                result += so_called_platform_generator_consts :: new_line ;
            so_called_lib_std_string state_type ;
            shy_guts :: hpp :: guts_type_machine_state_declare ( state_type , machine_i , state_i ) ;
            result += state_type ;
        }
    }
}

void shy_guts :: hpp :: guts_type_machine_state_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    so_called_lib_std_string on_entry ;
    so_called_lib_std_string on_exit ;
    so_called_lib_std_string on_input ;
    so_called_lib_std_string transition ;

    shy_guts :: hpp :: guts_type_machine_state_on_entry_declare ( on_entry , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_on_exit_declare ( on_exit , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_on_input_declare ( on_input , state_i ) ;
    shy_guts :: hpp :: guts_type_machine_state_transition_declare ( transition , state_i ) ;

    so_called_lib_std_string methods ;
    methods = on_entry + on_exit + on_input + transition ;

    if ( ! methods . empty ( ) )
    {
        so_called_lib_std_string public_area ;
        shy_guts :: consts :: hpp_guts_type_machine_state_public ( public_area ) ;
        methods = public_area + methods ;
    }

    shy_guts :: consts :: hpp_guts_type_machine_state 
        ( result 
        , machine_i -> first
        , state_i -> first
        , methods 
        ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_on_entry_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    if ( ! state_i -> second . on_entry . actions . empty ( )
      || ! state_i -> second . on_entry . commands . empty ( )
      || ! state_i -> second . on_entry . discards . empty ( )
       )
    {
        shy_guts :: consts :: hpp_guts_type_machine_state_on_entry_declare ( result ) ;
    }
}

void shy_guts :: hpp :: guts_type_machine_state_on_exit_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    if ( ! state_i -> second . on_exit . actions . empty ( ) 
      || ! state_i -> second . on_exit . commands . empty ( ) 
      || ! state_i -> second . on_exit . discards . empty ( ) 
       )
    {
        shy_guts :: consts :: hpp_guts_type_machine_state_on_exit_declare ( result ) ;
    }
}

void shy_guts :: hpp :: guts_type_machine_state_on_input_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    if ( ! state_i -> second . on_input . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_on_input_declare ( result ) ;
}

void shy_guts :: hpp :: guts_type_machine_state_transition_declare
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    if ( ! state_i -> second . transitions . empty ( ) )
        shy_guts :: consts :: hpp_guts_type_machine_state_transition_declare ( result ) ;
}

void shy_guts :: hpp :: guts_type_behaviour_inputs
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i 
    )
{
    so_called_lib_std_string inputs ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: action_command_name_container_type action_command_names ;
        shy_guts :: condition_state_name_container_type condition_state_names ;

        shy_guts :: lookup :: get_machine_action_command_names ( action_command_names , system_i , machine_i ) ;
        shy_guts :: lookup :: get_machine_condition_state_names ( condition_state_names , system_i , machine_i ) ;

        for ( shy_guts :: action_command_name_container_type :: contents_type :: const_iterator action_command_name_i = action_command_names . contents . begin ( )
            ; action_command_name_i != action_command_names . contents . end ( )
            ; ++ action_command_name_i
            )
        {
            so_called_lib_std_string input_variable ;
            shy_guts :: consts :: hpp_guts_type_behaviour_inputs_action_command_variable ( input_variable , machine_i -> first , * action_command_name_i ) ;
            inputs += input_variable ;
        }

        for ( shy_guts :: condition_state_name_container_type :: contents_type :: const_iterator condition_state_name_i = condition_state_names . contents . begin ( )
            ; condition_state_name_i != condition_state_names . contents . end ( )
            ; ++ condition_state_name_i
            )
        {
            so_called_lib_std_string input_variable ;
            shy_guts :: consts :: hpp_guts_type_behaviour_inputs_condition_state_variable ( input_variable , machine_i -> first , * condition_state_name_i ) ;
            inputs += input_variable ;
        }
    }

    shy_guts :: consts :: hpp_guts_type_behaviour_inputs ( result , inputs ) ;
}

void shy_guts :: hpp :: guts_states
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i 
    )
{
    so_called_lib_std_string states ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        for ( so_called_loadable_fsm_content_state_container_type :: const_iterator state_i = machine_i -> second . states . begin ( )
            ; state_i != machine_i -> second . states . end ( )
            ; ++ state_i
            )
        {
            so_called_lib_std_string state_variable ;
            shy_guts :: consts :: hpp_guts_states_state_variable ( state_variable , machine_i -> first , state_i -> first ) ;
            states += state_variable ;
        }
    }
    shy_guts :: consts :: hpp_guts_states ( result , states ) ;
}

void shy_guts :: hpp :: guts_behaviour_actions
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i 
    )
{
    so_called_lib_std_string actions ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: action_command_name_container_type command_action_names ;
        shy_guts :: lookup :: get_machine_action_command_names ( command_action_names , system_i , machine_i ) ;

        for ( shy_guts :: action_command_name_container_type :: contents_type :: const_iterator command_i = command_action_names . contents . begin ( )
            ; command_i != command_action_names . contents . end ( )
            ; ++ command_i
            )
        {
            so_called_lib_std_string action_command ;
            shy_guts :: consts :: hpp_guts_behaviour_actions_action_command_declare
                ( action_command
                , machine_i -> first
                , * command_i
                ) ;
            actions += action_command ;
        }
    }
    shy_guts :: consts :: hpp_guts_behaviour_actions ( result , actions ) ;
}

void shy_guts :: hpp :: every_guts_behaviour_actions_action_command
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: action_command_name_container_type command_action_names ;
        shy_guts :: lookup :: get_machine_action_command_names ( command_action_names , system_i , machine_i ) ;

        for ( shy_guts :: action_command_name_container_type :: contents_type :: const_iterator command_i = command_action_names . contents . begin ( )
            ; command_i != command_action_names . contents . end ( )
            ; ++ command_i
            )
        {
            so_called_lib_std_string action_command ;
            shy_guts :: consts :: hpp_guts_behaviour_actions_action_command_implement
                ( action_command
                , machine_i -> first
                , * command_i
                ) ;
            if ( machine_i != system_i -> second . machines . begin ( ) || command_i != command_action_names . contents . begin ( ) )
                result += so_called_platform_generator_consts :: new_line ;
            result += action_command ;
        }
    }
}

void shy_guts :: hpp :: every_guts_machine_variable
    ( so_called_lib_std_string & result
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i 
    )
{
    result . clear ( ) ;
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_lib_std_string variable_machine ;
        shy_guts :: consts :: hpp_guts_machine_variable ( variable_machine , machine_i -> first ) ;
        result += variable_machine ;
    }
}

void shy_guts :: prepare :: prepare ( )
{
    so_called_loadable_fsm_content_system_container_type * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        shy_guts :: prepare :: system ( system_i ) ;
    }
}

void shy_guts :: prepare :: system
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    )
{
    for ( so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: prepare :: system_machine ( system_i , machine_i ) ;
    }
}

void shy_guts :: prepare :: system_machine
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    for ( so_called_loadable_fsm_content_state_container_type :: const_iterator state_i = machine_i -> second . states . begin ( )
        ; state_i != machine_i -> second . states . end ( )
        ; ++ state_i
        )
    {
        shy_guts :: prepare :: system_machine_state ( system_i , machine_i , state_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    )
{
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_entry ) ;
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_exit ) ;

    for ( so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i = state_i -> second . on_input . begin ( )
        ; on_input_i != state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        shy_guts :: prepare :: system_machine_state_on_input ( system_i , machine_i , state_i , on_input_i ) ;
    }

    for ( so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i = state_i -> second . transitions . begin ( )
        ; transition_i != state_i -> second . transitions . end ( )
        ; ++ transition_i
        )
    {
        shy_guts :: prepare :: system_machine_state_transition ( system_i , machine_i , state_i , transition_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_actions
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , const so_called_loadable_fsm_content_actions_type & actions
    )
{
    for ( so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i = actions . actions . begin ( )
        ; action_do_i != actions . actions . end ( )
        ; ++ action_do_i
        )
    {
        shy_guts :: prepare :: system_machine_state_action_do ( system_i , machine_i , state_i , action_do_i ) ;
    }

    for ( so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i = actions . commands . begin ( )
        ; action_command_i != actions . commands . end ( )
        ; ++ action_command_i
        )
    {
        shy_guts :: prepare :: system_machine_state_action_command ( system_i , machine_i , state_i , action_command_i ) ;
    }

    for ( so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i = actions . discards . begin ( )
        ; action_discard_i != actions . discards . end ( )
        ; ++ action_discard_i
        )
    {
        shy_guts :: prepare :: system_machine_state_action_discard ( system_i , machine_i , state_i , action_discard_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_action_do
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_action_do_container_type :: const_iterator action_do_i
    )
{
}

void shy_guts :: prepare :: system_machine_state_action_discard
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_action_discard_container_type :: const_iterator action_discard_i
    )
{
}

void shy_guts :: prepare :: system_machine_state_action_command
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_action_command_container_type :: const_iterator action_command_i
    )
{
    shy_guts :: lookup :: save_system_machine_action_command ( system_i -> first , action_command_i -> machine , action_command_i -> command ) ;
}

void shy_guts :: prepare :: system_machine_state_on_input
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_on_input_container_type :: const_iterator on_input_i
    )
{
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , on_input_i -> actions ) ;
    for ( so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i = on_input_i -> condition_groups . begin ( )
        ; condition_group_i != on_input_i -> condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_group ( system_i , machine_i , state_i , condition_group_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_condition_group
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i
    )
{
    for ( so_called_loadable_fsm_content_condition_input_container_type :: const_iterator condition_input_i = condition_group_i -> inputs . begin ( )
        ; condition_input_i != condition_group_i -> inputs . end ( )
        ; ++ condition_input_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_input ( system_i , machine_i , state_i , condition_input_i ) ;
    }

    for ( so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i = condition_group_i -> states . begin ( )
        ; condition_state_i != condition_group_i -> states . end ( )
        ; ++ condition_state_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_state ( system_i , machine_i , state_i , condition_state_i ) ;
    }

    for ( so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i = condition_group_i -> commands . begin ( )
        ; condition_command_i != condition_group_i -> commands . end ( )
        ; ++ condition_command_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_command ( system_i , machine_i , state_i , condition_command_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_condition_input
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_input_container_type :: const_iterator condition_input_i
    )
{
}

void shy_guts :: prepare :: system_machine_state_condition_state
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_state_container_type :: const_iterator condition_state_i
    )
{
    shy_guts :: lookup :: save_system_machine_condition_state ( system_i -> first , condition_state_i -> machine , condition_state_i -> state ) ;
}

void shy_guts :: prepare :: system_machine_state_condition_command
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_condition_command_container_type :: const_iterator condition_command_i
    )
{
    shy_guts :: lookup :: save_system_machine_action_command ( system_i -> first , machine_i -> first , condition_command_i -> command ) ;
}

void shy_guts :: prepare :: system_machine_state_transition
    ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    , so_called_loadable_fsm_content_state_container_type :: const_iterator state_i
    , so_called_loadable_fsm_content_transition_container_type :: const_iterator transition_i
    )
{
    for ( so_called_loadable_fsm_content_condition_group_container_type :: const_iterator condition_group_i = transition_i -> condition_groups . begin ( )
        ; condition_group_i != transition_i -> condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_group ( system_i , machine_i , state_i , condition_group_i ) ;
    }
}

void shy_guts :: lookup :: single_action
    ( so_called_lib_std_bool & result
    , const so_called_loadable_fsm_content_actions_type & actions
    )
{
    so_called_lib_std_int32_t count = 0;
    count += so_called_lib_std_int32_t ( actions . actions . size ( ) ) ;
    count += so_called_lib_std_int32_t ( actions . commands . size ( ) ) ;
    count += so_called_lib_std_int32_t ( actions . discards . size ( ) ) ;
    if ( count == 1 )
        result = so_called_lib_std_true ;
    else
        result = so_called_lib_std_false ;
}

void shy_guts :: lookup :: single_condition_single_group
    ( so_called_lib_std_bool & result
    , const so_called_loadable_fsm_content_condition_group_container_type & condition_groups
    )
{
    result = so_called_lib_std_false ;
    if ( condition_groups . size ( ) == 1 )
    {
        so_called_lib_std_int32_t count = 0 ;
        count += so_called_lib_std_int32_t ( condition_groups . begin ( ) -> inputs . size ( ) ) ;
        count += so_called_lib_std_int32_t ( condition_groups . begin ( ) -> states . size ( ) ) ;
        count += so_called_lib_std_int32_t ( condition_groups . begin ( ) -> commands . size ( ) ) ;
        if ( count == 1 )
            result = so_called_lib_std_true ;
    }
}

void shy_guts :: lookup :: get_machine_action_command_names 
    ( shy_guts :: action_command_name_container_type & command_names
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    command_names = shy_guts :: lookup :: system_machine_action_command_name_container . contents [ system_i -> first ] . contents [ machine_i -> first ] ;
}

void shy_guts :: lookup :: get_machine_condition_state_names 
    ( shy_guts :: condition_state_name_container_type & state_names
    , so_called_loadable_fsm_content_system_container_type :: const_iterator system_i
    , so_called_loadable_fsm_content_machine_container_type :: const_iterator machine_i
    )
{
    state_names = shy_guts :: lookup :: system_machine_condition_state_name_container . contents [ system_i -> first ] . contents [ machine_i -> first ] ;
}

void shy_guts :: lookup :: save_system_machine_action_command
    ( so_called_lib_std_string system
    , so_called_lib_std_string machine
    , so_called_lib_std_string command
    )
{
    shy_guts :: lookup :: system_machine_action_command_name_container . contents [ system ] . contents [ machine ] . contents . insert ( command ) ;
}

void shy_guts :: lookup :: save_system_machine_condition_state
    ( so_called_lib_std_string system
    , so_called_lib_std_string machine
    , so_called_lib_std_string state
    )
{
    shy_guts :: lookup :: system_machine_condition_state_name_container . contents [ system ] . contents [ machine ] . contents . insert ( state ) ;
}

void shy_loadable_fsm_generator :: generate ( )
{
    shy_guts :: prepare :: prepare ( ) ;

    so_called_loadable_fsm_content_system_container_type * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_loadable_fsm_content_system_container_type :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        so_called_lib_std_string system_name ;
        so_called_lib_std_string system_path ;
        so_called_lib_std_string fsm_h_path ;
        so_called_lib_std_string fsm_hpp_path ;
        so_called_lib_std_string fsm_injections_h_path ;
        so_called_lib_std_string fsm_injections_hpp_path ;
        so_called_lib_std_string fsm_h_contents ;
        so_called_lib_std_string fsm_hpp_contents ;
        so_called_lib_std_string fsm_injections_h_contents ;
        so_called_lib_std_string fsm_injections_hpp_contents ;

        system_name = system_i -> first ;

        so_called_loadable_reflection :: module_path ( system_path , system_name ) ;
        shy_guts :: consts :: h_path ( fsm_h_path ) ;
        shy_guts :: consts :: hpp_path ( fsm_hpp_path ) ;
        shy_guts :: consts :: injections_h_path ( fsm_injections_h_path ) ;
        shy_guts :: consts :: injections_hpp_path ( fsm_injections_hpp_path ) ;

        shy_guts :: consts :: h_contents
            ( fsm_h_contents
            , system_name
            ) ;
        shy_guts :: hpp :: contents
            ( fsm_hpp_contents
            , system_i
            ) ;
        shy_guts :: consts :: injections_h_contents
            ( fsm_injections_h_contents
            , system_name
            ) ;
        shy_guts :: consts :: injections_hpp_contents
            ( fsm_injections_hpp_contents
            ) ;

        so_called_platform_generator_python :: generate_file 
            ( so_called_platform_generator_consts :: common_folder_path + system_path + fsm_h_path 
            , fsm_h_contents 
            ) ;
        so_called_platform_generator_python :: generate_file 
            ( so_called_platform_generator_consts :: common_folder_path + system_path + fsm_hpp_path 
            , fsm_hpp_contents 
            ) ;
        so_called_platform_generator_python :: generate_file 
            ( so_called_platform_generator_consts :: common_folder_path + system_path + fsm_injections_h_path 
            , fsm_injections_h_contents 
            ) ;
        so_called_platform_generator_python :: generate_file 
            ( so_called_platform_generator_consts :: common_folder_path + system_path + fsm_injections_hpp_path 
            , fsm_injections_hpp_contents 
            ) ;
    }
}

