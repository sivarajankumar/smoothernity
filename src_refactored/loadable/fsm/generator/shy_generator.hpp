namespace shy_guts
{
    typedef so_called_std_set < so_called_std_string > type_action_command_name_container ;
    typedef so_called_std_set < so_called_std_string > type_condition_state_name_container ;
    typedef so_called_std_map < so_called_std_string , type_action_command_name_container > type_machine_action_command_name_container ;
    typedef so_called_std_map < so_called_std_string , type_condition_state_name_container > type_machine_condition_state_name_container ;
    typedef so_called_std_map < so_called_std_string , type_machine_action_command_name_container > type_system_machine_action_command_name_container ;
    typedef so_called_std_map < so_called_std_string , type_machine_condition_state_name_container > type_system_machine_condition_state_name_container ;

    namespace consts
    {
        static void hpp_guts ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_class_type_behaviour_inputs ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_class_type_behaviour_inputs_action_command_variable ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void hpp_guts_class_type_behaviour_inputs_condition_state_variable ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void hpp_guts_namespace_behaviour_actions ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_behaviour_actions_action_command ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void hpp_guts_namespace_state_environment ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_states ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_states_state_variable ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void hpp_guts_variable_machine ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_variables ( so_called_std_string & ) ;
        static void hpp_path ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_contents ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_path ( so_called_std_string & , so_called_std_string ) ;
    }

    namespace hpp
    {
        static void contents 
            ( so_called_std_string & 
            , so_called_type_loadable_fsm_content_system_container :: const_iterator 
            ) ;
        static void guts_class_type_behaviour_inputs
            ( so_called_std_string &
            , so_called_type_loadable_fsm_content_system_container :: const_iterator
            ) ;
        static void guts_namespace_behaviour_actions 
            ( so_called_std_string &
            , so_called_type_loadable_fsm_content_system_container :: const_iterator 
            ) ;
        static void guts_namespace_states
            ( so_called_std_string &
            , so_called_type_loadable_fsm_content_system_container :: const_iterator
            ) ;
        static void guts_variables_machines 
            ( so_called_std_string & 
            , so_called_type_loadable_fsm_content_system_container :: const_iterator 
            ) ;
    }

    namespace lookup
    {
        static type_system_machine_action_command_name_container system_machine_action_command_name_container ;
        static type_system_machine_condition_state_name_container system_machine_condition_state_name_container ;

        static void save_system_machine_action_command
            ( so_called_std_string
            , so_called_std_string
            , so_called_std_string
            ) ;
        static void save_system_machine_condition_state
            ( so_called_std_string
            , so_called_std_string
            , so_called_std_string
            ) ;
        static void get_machine_action_command_names 
            ( shy_guts :: type_action_command_name_container & 
            , so_called_type_loadable_fsm_content_system_container :: const_iterator 
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
            ) ;
        static void get_machine_condition_state_names 
            ( shy_guts :: type_condition_state_name_container & 
            , so_called_type_loadable_fsm_content_system_container :: const_iterator 
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
            ) ;
    }

    namespace prepare
    {
        static void prepare ( ) ;
        static void system
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
            ) ;
        static void system_machine
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
            ) ;
        static void system_machine_state
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            ) ;
        static void system_machine_state_action_do
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_action_do_container :: const_iterator
            ) ;
        static void system_machine_state_action_command
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_action_command_container :: const_iterator
            ) ;
        static void system_machine_state_actions
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , const so_called_type_loadable_fsm_content_actions &
            ) ;
        static void system_machine_state_condition_command
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_condition_command_container :: const_iterator
            ) ;
        static void system_machine_state_condition_group
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_condition_group_container :: const_iterator
            ) ;
        static void system_machine_state_condition_input
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_condition_input_container :: const_iterator
            ) ;
        static void system_machine_state_condition_state
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_condition_state_container :: const_iterator
            ) ;
        static void system_machine_state_on_input
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_on_input_container :: const_iterator
            ) ;
        static void system_machine_state_transition
            ( so_called_type_loadable_fsm_content_system_container :: const_iterator
            , so_called_type_loadable_fsm_content_machine_container :: const_iterator
            , so_called_type_loadable_fsm_content_state_container :: const_iterator
            , so_called_type_loadable_fsm_content_transition_container :: const_iterator
            ) ;
    }
}

void shy_guts :: consts :: hpp_guts
    ( so_called_std_string & result
    , so_called_std_string contents
    )
{
    result . clear ( ) ;
    result += "namespace shy_guts\n" ;
    result += "{\n" ;
    result += contents ;
    result += "}\n" ;
}

void shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs 
    ( so_called_std_string & result 
    , so_called_std_string inputs
    )
{
    result . clear ( ) ;
    result += "    class type_behaviour_inputs\n" ;
    result += "    {\n" ;
    result += "    public :\n" ;
    result += inputs ;
    result += "    } ;\n" ;
}

void shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs_action_command_variable
    ( so_called_std_string & result 
    , so_called_std_string machine
    , so_called_std_string command
    )
{
    result . clear ( ) ;
    result += "        so_called_type_platform_math_num_whole machine_" ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs_condition_state_variable
    ( so_called_std_string & result
    , so_called_std_string machine
    , so_called_std_string state
    )
{
    result . clear ( ) ;
    result += "        so_called_type_platform_math_num_whole machine_" ;
    result += machine ;
    result += "_state_is_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_namespace_behaviour_actions ( so_called_std_string & result , so_called_std_string actions )
{
    result . clear ( ) ;
    result += "    namespace behaviour_actions\n" ;
    result += "    {\n" ;
    result += actions ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_namespace_behaviour_actions_action_command 
    ( so_called_std_string & result 
    , so_called_std_string machine 
    , so_called_std_string command
    )
{
    result . clear ( ) ;
    result += "        static void " ;
    result += machine ;
    result += "_command_" ;
    result += command ;
    result += " ( ) ;\n" ;
}

void shy_guts :: consts :: hpp_guts_namespace_state_environment ( so_called_std_string & result , so_called_std_string system )
{
    result . clear ( ) ;
    result += "    namespace state_environment\n" ;
    result += "    {\n" ;
    result += "        static so_called_type_platform_pointer_data < shy_guts :: type_behaviour_inputs > behaviour_inputs ;\n" ;
    result += "        static so_called_type_platform_pointer_data < so_called_type_common_" ;
    result += system ;
    result += "_fsm_inputs > inputs ;\n" ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_namespace_states ( so_called_std_string & result , so_called_std_string states )
{
    result . clear ( ) ;
    result += "    namespace states\n" ;
    result += "    {\n" ;
    result += states ;
    result += "    }\n" ;
}

void shy_guts :: consts :: hpp_guts_namespace_states_state_variable ( so_called_std_string & result , so_called_std_string machine , so_called_std_string state )
{
    result . clear ( ) ;
    result += "       static type_machine_" ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " " ;
    result += machine ;
    result += "_state_" ;
    result += state ;
    result += " ;\n" ;
}

void shy_guts :: consts :: hpp_guts_variable_machine ( so_called_std_string & result , so_called_std_string machine )
{
    result . clear ( ) ;
    result += "    static so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > machine_" ;
    result += machine ;
    result += "_state ;\n" ;
}

void shy_guts :: consts :: hpp_guts_variables ( so_called_std_string & result )
{
    result . clear ( ) ;
    result += "    static so_called_type_platform_math_num_whole fsm_running ;\n" ;
    result += "    static type_behaviour_inputs current_behaviour_inputs ;\n" ;
    result += "    static type_behaviour_inputs fixed_behaviour_inputs ;\n" ;
}

void shy_guts :: consts :: injections_hpp_path ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour_injections.hpp" ;
}

void shy_guts :: consts :: hpp_path ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour.hpp" ;
}

void shy_guts :: consts :: injections_hpp_contents ( so_called_std_string & result , so_called_std_string system )
{
    result . clear ( ) ;
    result += "#include \"../../engine/fsm/stateless/shy_stateless_injections.h\"\n" ;
    result += "\n" ;
    result += "#include \"../../../injections/platform/math/shy_math.h\"\n" ;
    result += "\n" ;
    result += "#include \"./shy_" ;
    result += system ;
    result += "_fsm_behaviour.hpp\"\n" ;
}

void shy_guts :: hpp :: contents 
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    )
{
    so_called_std_string guts ;
    so_called_std_string guts_class_type_behaviour_inputs ;
    so_called_std_string guts_namespace_behaviour_actions ;
    so_called_std_string guts_namespace_state_environment ;
    so_called_std_string guts_namespace_states ;
    so_called_std_string guts_variables ;
    so_called_std_string guts_variables_machines ;

    shy_guts :: hpp :: guts_class_type_behaviour_inputs
        ( guts_class_type_behaviour_inputs
        , system_i
        ) ;

    shy_guts :: hpp :: guts_namespace_states
        ( guts_namespace_states
        , system_i
        ) ;

    shy_guts :: hpp :: guts_namespace_behaviour_actions
        ( guts_namespace_behaviour_actions
        , system_i
        ) ;

    shy_guts :: consts :: hpp_guts_namespace_state_environment
        ( guts_namespace_state_environment
        , system_i -> first
        ) ;

    shy_guts :: consts :: hpp_guts_variables ( guts_variables ) ;

    shy_guts :: hpp :: guts_variables_machines
        ( guts_variables_machines
        , system_i
        ) ;

    shy_guts :: consts :: hpp_guts
        ( guts
        , guts_class_type_behaviour_inputs
        + so_called_loadable_generator_consts :: new_line
        + guts_namespace_states
        + so_called_loadable_generator_consts :: new_line
        + guts_namespace_behaviour_actions
        + so_called_loadable_generator_consts :: new_line
        + guts_namespace_state_environment
        + so_called_loadable_generator_consts :: new_line
        + guts_variables_machines
        + so_called_loadable_generator_consts :: new_line
        + guts_variables
        ) ;

    result . clear ( ) ;
    result += guts ;
}

void shy_guts :: hpp :: guts_class_type_behaviour_inputs
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i 
    )
{
    so_called_std_string inputs ;
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: type_action_command_name_container action_command_names ;
        shy_guts :: type_condition_state_name_container condition_state_names ;

        shy_guts :: lookup :: get_machine_action_command_names ( action_command_names , system_i , machine_i ) ;
        shy_guts :: lookup :: get_machine_condition_state_names ( condition_state_names , system_i , machine_i ) ;

        for ( shy_guts :: type_action_command_name_container :: const_iterator action_command_name_i = action_command_names . begin ( )
            ; action_command_name_i != action_command_names . end ( )
            ; ++ action_command_name_i
            )
        {
            so_called_std_string input_variable ;
            shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs_action_command_variable ( input_variable , machine_i -> first , * action_command_name_i ) ;
            inputs += input_variable ;
        }

        for ( shy_guts :: type_condition_state_name_container :: const_iterator condition_state_name_i = condition_state_names . begin ( )
            ; condition_state_name_i != condition_state_names . end ( )
            ; ++ condition_state_name_i
            )
        {
            so_called_std_string input_variable ;
            shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs_condition_state_variable ( input_variable , machine_i -> first , * condition_state_name_i ) ;
            inputs += input_variable ;
        }
    }

    shy_guts :: consts :: hpp_guts_class_type_behaviour_inputs ( result , inputs ) ;
}

void shy_guts :: hpp :: guts_namespace_states
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i 
    )
{
    so_called_std_string states ;
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        for ( so_called_type_loadable_fsm_content_state_container :: const_iterator state_i = machine_i -> second . states . begin ( )
            ; state_i != machine_i -> second . states . end ( )
            ; ++ state_i
            )
        {
            so_called_std_string state_variable ;
            shy_guts :: consts :: hpp_guts_namespace_states_state_variable ( state_variable , machine_i -> first , state_i -> first ) ;
            states += state_variable ;
        }
    }
    shy_guts :: consts :: hpp_guts_namespace_states ( result , states ) ;
}

void shy_guts :: hpp :: guts_namespace_behaviour_actions
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i 
    )
{
    so_called_std_string actions ;
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: type_action_command_name_container command_action_names ;
        shy_guts :: lookup :: get_machine_action_command_names ( command_action_names , system_i , machine_i ) ;

        for ( shy_guts :: type_action_command_name_container :: const_iterator command_i = command_action_names . begin ( )
            ; command_i != command_action_names . end ( )
            ; ++ command_i
            )
        {
            so_called_std_string action_command ;
            shy_guts :: consts :: hpp_guts_namespace_behaviour_actions_action_command
                ( action_command
                , machine_i -> first
                , * command_i
                ) ;
            actions += action_command ;
        }
    }
    shy_guts :: consts :: hpp_guts_namespace_behaviour_actions ( result , actions ) ;
}

void shy_guts :: hpp :: guts_variables_machines
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i 
    )
{
    result . clear ( ) ;
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        so_called_std_string variable_machine ;
        shy_guts :: consts :: hpp_guts_variable_machine ( variable_machine , machine_i -> first ) ;
        result += variable_machine ;
    }
}

void shy_guts :: prepare :: prepare ( )
{
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        shy_guts :: prepare :: system ( system_i ) ;
    }
}

void shy_guts :: prepare :: system
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    )
{
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: prepare :: system_machine ( system_i , machine_i ) ;
    }
}

void shy_guts :: prepare :: system_machine
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    for ( so_called_type_loadable_fsm_content_state_container :: const_iterator state_i = machine_i -> second . states . begin ( )
        ; state_i != machine_i -> second . states . end ( )
        ; ++ state_i
        )
    {
        shy_guts :: prepare :: system_machine_state ( system_i , machine_i , state_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    )
{
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_entry ) ;
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_exit ) ;

    for ( so_called_type_loadable_fsm_content_on_input_container :: const_iterator on_input_i = state_i -> second . on_input . begin ( )
        ; on_input_i != state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        shy_guts :: prepare :: system_machine_state_on_input ( system_i , machine_i , state_i , on_input_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_transition_container :: const_iterator transition_i = state_i -> second . transitions . begin ( )
        ; transition_i != state_i -> second . transitions . end ( )
        ; ++ transition_i
        )
    {
        shy_guts :: prepare :: system_machine_state_transition ( system_i , machine_i , state_i , transition_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_actions
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , const so_called_type_loadable_fsm_content_actions & actions
    )
{
    for ( so_called_type_loadable_fsm_content_action_do_container :: const_iterator action_do_i = actions . actions . begin ( )
        ; action_do_i != actions . actions . end ( )
        ; ++ action_do_i
        )
    {
        shy_guts :: prepare :: system_machine_state_action_do ( system_i , machine_i , state_i , action_do_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_action_command_container :: const_iterator action_command_i = actions . commands . begin ( )
        ; action_command_i != actions . commands . end ( )
        ; ++ action_command_i
        )
    {
        shy_guts :: prepare :: system_machine_state_action_command ( system_i , machine_i , state_i , action_command_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_action_do
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_action_do_container :: const_iterator action_do_i
    )
{
}

void shy_guts :: prepare :: system_machine_state_action_command
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_action_command_container :: const_iterator action_command_i
    )
{
    shy_guts :: lookup :: save_system_machine_action_command ( system_i -> first , action_command_i -> machine , action_command_i -> command ) ;
}

void shy_guts :: prepare :: system_machine_state_on_input
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_on_input_container :: const_iterator on_input_i
    )
{
    shy_guts :: prepare :: system_machine_state_actions ( system_i , machine_i , state_i , on_input_i -> actions ) ;
    for ( so_called_type_loadable_fsm_content_condition_group_container :: const_iterator condition_group_i = on_input_i -> condition_groups . begin ( )
        ; condition_group_i != on_input_i -> condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_group ( system_i , machine_i , state_i , condition_group_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_condition_group
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_condition_group_container :: const_iterator condition_group_i
    )
{
    for ( so_called_type_loadable_fsm_content_condition_input_container :: const_iterator condition_input_i = condition_group_i -> inputs . begin ( )
        ; condition_input_i != condition_group_i -> inputs . end ( )
        ; ++ condition_input_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_input ( system_i , machine_i , state_i , condition_input_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_condition_state_container :: const_iterator condition_state_i = condition_group_i -> states . begin ( )
        ; condition_state_i != condition_group_i -> states . end ( )
        ; ++ condition_state_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_state ( system_i , machine_i , state_i , condition_state_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_condition_command_container :: const_iterator condition_command_i = condition_group_i -> commands . begin ( )
        ; condition_command_i != condition_group_i -> commands . end ( )
        ; ++ condition_command_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_command ( system_i , machine_i , state_i , condition_command_i ) ;
    }
}

void shy_guts :: prepare :: system_machine_state_condition_input
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_condition_input_container :: const_iterator condition_input_i
    )
{
}

void shy_guts :: prepare :: system_machine_state_condition_state
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_condition_state_container :: const_iterator condition_state_i
    )
{
    shy_guts :: lookup :: save_system_machine_condition_state ( system_i -> first , condition_state_i -> machine , condition_state_i -> state ) ;
}

void shy_guts :: prepare :: system_machine_state_condition_command
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_condition_command_container :: const_iterator condition_command_i
    )
{
    shy_guts :: lookup :: save_system_machine_action_command ( system_i -> first , machine_i -> first , condition_command_i -> command ) ;
}

void shy_guts :: prepare :: system_machine_state_transition
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_transition_container :: const_iterator transition_i
    )
{
    for ( so_called_type_loadable_fsm_content_condition_group_container :: const_iterator condition_group_i = transition_i -> condition_groups . begin ( )
        ; condition_group_i != transition_i -> condition_groups . end ( )
        ; ++ condition_group_i
        )
    {
        shy_guts :: prepare :: system_machine_state_condition_group ( system_i , machine_i , state_i , condition_group_i ) ;
    }
}

void shy_guts :: lookup :: get_machine_action_command_names 
    ( shy_guts :: type_action_command_name_container & command_names
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    command_names = shy_guts :: lookup :: system_machine_action_command_name_container [ system_i -> first ] [ machine_i -> first ] ;
}

void shy_guts :: lookup :: get_machine_condition_state_names 
    ( shy_guts :: type_condition_state_name_container & state_names
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    state_names = shy_guts :: lookup :: system_machine_condition_state_name_container [ system_i -> first ] [ machine_i -> first ] ;
}

void shy_guts :: lookup :: save_system_machine_action_command
    ( so_called_std_string system
    , so_called_std_string machine
    , so_called_std_string command
    )
{
    shy_guts :: lookup :: system_machine_action_command_name_container [ system ] [ machine ] . insert ( command ) ;
}

void shy_guts :: lookup :: save_system_machine_condition_state
    ( so_called_std_string system
    , so_called_std_string machine
    , so_called_std_string state
    )
{
    shy_guts :: lookup :: system_machine_condition_state_name_container [ system ] [ machine ] . insert ( state ) ;
}

void shy_loadable_fsm_generator :: generate ( so_called_std_string & result )
{
    shy_guts :: prepare :: prepare ( ) ;

    result . clear ( ) ;
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        so_called_std_string system_name ;
        so_called_std_string fsm_hpp_path ;
        so_called_std_string fsm_injections_hpp_path ;
        so_called_std_string generate_fsm_hpp ;
        so_called_std_string generate_fsm_injections_hpp ;
        so_called_std_string fsm_hpp_contents ;
        so_called_std_string fsm_injections_hpp_contents ;

        system_name = system_i -> first ;

        shy_guts :: consts :: hpp_path
            ( fsm_hpp_path 
            , system_name 
            ) ;
        shy_guts :: consts :: injections_hpp_path
            ( fsm_injections_hpp_path 
            , system_name 
            ) ;

        shy_guts :: hpp :: contents
            ( fsm_hpp_contents
            , system_i
            ) ;
        shy_guts :: consts :: injections_hpp_contents
            ( fsm_injections_hpp_contents
            , system_name
            ) ;

        so_called_loadable_generator_python :: generate_file 
            ( generate_fsm_hpp 
            , so_called_loadable_generator_consts :: autogenerated_folder_path + fsm_hpp_path 
            , fsm_hpp_contents 
            ) ;
        so_called_loadable_generator_python :: generate_file 
            ( generate_fsm_injections_hpp 
            , so_called_loadable_generator_consts :: autogenerated_folder_path + fsm_injections_hpp_path 
            , fsm_injections_hpp_contents 
            ) ;

        result += generate_fsm_hpp ;
        result += generate_fsm_injections_hpp ;
    }
}

