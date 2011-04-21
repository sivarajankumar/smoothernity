namespace shy_guts
{
    namespace consts
    {
        static void hpp_guts ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_namespace_state_environment ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_guts_variables ( so_called_std_string & ) ;
        static void hpp_path ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_contents ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_path ( so_called_std_string & , so_called_std_string ) ;
    }

    static void hpp_contents ( so_called_std_string & , so_called_type_loadable_fsm_content_system_container :: const_iterator ) ;
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
    so_called_std_string guts_namespace_state_environment ;
    so_called_std_string guts_variables ;

    shy_guts :: consts :: hpp_guts_namespace_state_environment
        ( guts_namespace_state_environment
        , system_i -> first
        ) ;

    shy_guts :: consts :: hpp_guts_variables ( guts_variables ) ;

    shy_guts :: consts :: hpp_guts
        ( guts
        , guts_namespace_state_environment
        + so_called_loadable_generator_consts :: new_line
        + guts_variables
        ) ;

    result . clear ( ) ;
    result += guts ;
}

void shy_loadable_fsm_generator :: generate ( so_called_std_string & result )
{
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

