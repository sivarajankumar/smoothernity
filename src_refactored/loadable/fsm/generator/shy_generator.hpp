namespace shy_guts
{
    typedef so_called_std_set < so_called_std_string > type_action_command_name_container ;
    typedef so_called_std_map < so_called_std_string , type_action_command_name_container > type_machine_action_command_name_container ;
    typedef so_called_std_map < so_called_std_string , type_machine_action_command_name_container > type_system_machine_action_command_name_container ;

    namespace consts
    {
        static void hpp_guts ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_behaviour_actions ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_behaviour_actions_action_command ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
        static void hpp_guts_namespace_state_environment ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_variable_machine ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_variables ( so_called_std_string & ) ;
        static void hpp_path ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_contents ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_path ( so_called_std_string & , so_called_std_string ) ;
    }

    static type_system_machine_action_command_name_container system_machine_action_command_name_container ;

    static void hpp_contents 
        ( so_called_std_string & 
        , so_called_type_loadable_fsm_content_system_container :: const_iterator 
        ) ;
    static void hpp_guts_namespace_behaviour_actions 
        ( so_called_std_string &
        , so_called_type_loadable_fsm_content_system_container :: const_iterator 
        ) ;
    static void hpp_guts_variables_machines 
        ( so_called_std_string & 
        , so_called_type_loadable_fsm_content_system_container :: const_iterator 
        ) ;
    static void get_machine_action_command_names 
        ( shy_guts :: type_action_command_name_container & 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        ) ;
    static void prepare ( ) ;
    static void prepare_system
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        ) ;
    static void prepare_system_machine
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator 
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator 
        ) ;
    static void prepare_system_machine_state
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        ) ;
    static void prepare_system_machine_state_action_do
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        , so_called_type_loadable_fsm_content_action_do_container :: const_iterator
        ) ;
    static void prepare_system_machine_state_action_command
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        , so_called_type_loadable_fsm_content_action_command_container :: const_iterator
        ) ;
    static void prepare_system_machine_state_actions
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        , const so_called_type_loadable_fsm_content_actions &
        ) ;
    static void prepare_system_machine_state_on_input
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        , so_called_type_loadable_fsm_content_on_input_container :: const_iterator
        ) ;
    static void prepare_system_machine_state_transition
        ( so_called_type_loadable_fsm_content_system_container :: const_iterator
        , so_called_type_loadable_fsm_content_machine_container :: const_iterator
        , so_called_type_loadable_fsm_content_state_container :: const_iterator
        , so_called_type_loadable_fsm_content_transition_container :: const_iterator
        ) ;
    static void save_system_machine_action_command
        ( so_called_std_string
        , so_called_std_string
        , so_called_std_string
        ) ;
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

void shy_guts :: hpp_contents 
    ( so_called_std_string & result
    , so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    )
{
    so_called_std_string guts ;
    so_called_std_string guts_namespace_behaviour_actions ;
    so_called_std_string guts_namespace_state_environment ;
    so_called_std_string guts_variables ;
    so_called_std_string guts_variables_machines ;

    shy_guts :: hpp_guts_namespace_behaviour_actions
        ( guts_namespace_behaviour_actions
        , system_i
        ) ;

    shy_guts :: consts :: hpp_guts_namespace_state_environment
        ( guts_namespace_state_environment
        , system_i -> first
        ) ;

    shy_guts :: consts :: hpp_guts_variables ( guts_variables ) ;

    shy_guts :: hpp_guts_variables_machines
        ( guts_variables_machines
        , system_i
        ) ;

    shy_guts :: consts :: hpp_guts
        ( guts
        , guts_namespace_behaviour_actions
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

void shy_guts :: hpp_guts_namespace_behaviour_actions
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
        shy_guts :: get_machine_action_command_names ( command_action_names , machine_i ) ;

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
    shy_guts :: consts :: hpp_guts_namespace_behaviour_actions
        ( result
        , actions
        ) ;
}

void shy_guts :: hpp_guts_variables_machines
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

void shy_guts :: get_machine_action_command_names 
    ( shy_guts :: type_action_command_name_container & command_names
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
}

void shy_guts :: prepare ( )
{
    so_called_type_loadable_fsm_content_system_container * system_container = 0 ;
    so_called_loadable_fsm_content :: get_system_container ( system_container ) ;
    for ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i = system_container -> begin ( )
        ; system_i != system_container -> end ( )
        ; ++ system_i
        )
    {
        shy_guts :: prepare_system ( system_i ) ;
    }
}

void shy_guts :: prepare_system
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    )
{
    for ( so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i = system_i -> second . machines . begin ( )
        ; machine_i != system_i -> second . machines . end ( )
        ; ++ machine_i
        )
    {
        shy_guts :: prepare_system_machine ( system_i , machine_i ) ;
    }
}

void shy_guts :: prepare_system_machine
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    )
{
    for ( so_called_type_loadable_fsm_content_state_container :: const_iterator state_i = machine_i -> second . states . begin ( )
        ; state_i != machine_i -> second . states . end ( )
        ; ++ state_i
        )
    {
        shy_guts :: prepare_system_machine_state ( system_i , machine_i , state_i ) ;
    }
}

void shy_guts :: prepare_system_machine_state
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    )
{
    shy_guts :: prepare_system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_entry ) ;
    shy_guts :: prepare_system_machine_state_actions ( system_i , machine_i , state_i , state_i -> second . on_exit ) ;

    for ( so_called_type_loadable_fsm_content_on_input_container :: const_iterator on_input_i = state_i -> second . on_input . begin ( )
        ; on_input_i != state_i -> second . on_input . end ( )
        ; ++ on_input_i
        )
    {
        shy_guts :: prepare_system_machine_state_on_input ( system_i , machine_i , state_i , on_input_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_transition_container :: const_iterator transition_i = state_i -> second . transitions . begin ( )
        ; transition_i != state_i -> second . transitions . end ( )
        ; ++ transition_i
        )
    {
        shy_guts :: prepare_system_machine_state_transition ( system_i , machine_i , state_i , transition_i ) ;
    }
}

void shy_guts :: prepare_system_machine_state_actions
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
        shy_guts :: prepare_system_machine_state_action_do ( system_i , machine_i , state_i , action_do_i ) ;
    }

    for ( so_called_type_loadable_fsm_content_action_command_container :: const_iterator action_command_i = actions . commands . begin ( )
        ; action_command_i != actions . commands . end ( )
        ; ++ action_command_i
        )
    {
        shy_guts :: prepare_system_machine_state_action_command ( system_i , machine_i , state_i , action_command_i ) ;
    }
}

void shy_guts :: prepare_system_machine_state_action_do
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_action_do_container :: const_iterator action_do_i
    )
{
}

void shy_guts :: prepare_system_machine_state_action_command
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_action_command_container :: const_iterator action_command_i
    )
{
    shy_guts :: save_system_machine_action_command ( system_i -> first , action_command_i -> machine , action_command_i -> command ) ;
}

void shy_guts :: prepare_system_machine_state_on_input
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_on_input_container :: const_iterator on_input_i
    )
{
}

void shy_guts :: prepare_system_machine_state_transition
    ( so_called_type_loadable_fsm_content_system_container :: const_iterator system_i
    , so_called_type_loadable_fsm_content_machine_container :: const_iterator machine_i
    , so_called_type_loadable_fsm_content_state_container :: const_iterator state_i
    , so_called_type_loadable_fsm_content_transition_container :: const_iterator transition_i
    )
{
}

void shy_guts :: save_system_machine_action_command
    ( so_called_std_string system
    , so_called_std_string machine
    , so_called_std_string command
    )
{
    shy_guts :: system_machine_action_command_name_container [ system ] [ machine ] . insert ( command ) ;
}

void shy_loadable_fsm_generator :: generate ( so_called_std_string & result )
{
    shy_guts :: prepare ( ) ;

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

        shy_guts :: hpp_contents
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

