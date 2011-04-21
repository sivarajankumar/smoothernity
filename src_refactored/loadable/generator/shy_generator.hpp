namespace shy_guts
{
    namespace consts_consts
    {
        static void hpp_path ( so_called_std_string & , so_called_std_string ) ;
        static void hpp_value_fract ( so_called_std_string & , so_called_std_string , so_called_std_string , so_called_std_string , so_called_std_string ) ;
        static void hpp_value_whole ( so_called_std_string & , so_called_std_string , so_called_std_string , so_called_std_string ) ;
        static void injections_hpp_contents ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_path ( so_called_std_string & , so_called_std_string ) ;
    }

    namespace consts_fsm
    {
        static void hpp_path ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_contents ( so_called_std_string & , so_called_std_string ) ;
        static void injections_hpp_path ( so_called_std_string & , so_called_std_string ) ;
    }

    namespace generate_consts
    {
        static void hpp_contents ( so_called_std_string & , so_called_type_loadable_consts_content_module_container :: const_iterator ) ;
        static void hpp_values_fract ( so_called_std_string & , so_called_type_loadable_consts_content_module_container :: const_iterator ) ;
        static void hpp_values_whole ( so_called_std_string & , so_called_type_loadable_consts_content_module_container :: const_iterator ) ;
        static void python_script ( so_called_std_string & ) ;
        static void signed_value ( so_called_std_string & , so_called_std_string , so_called_std_string ) ;
    }

    namespace generate_fsm
    {
        static void python_script ( so_called_std_string & ) ;
    }
}

void shy_guts :: consts_consts :: hpp_path ( so_called_std_string & path , so_called_std_string module )
{
    path . clear ( ) ;
    path += module ;
    path += "_consts/shy_" ;
    path += module ;
    path += "_consts.hpp" ;
}

void shy_guts :: consts_consts :: injections_hpp_path ( so_called_std_string & path , so_called_std_string module )
{
    path . clear ( ) ;
    path += module ;
    path += "_consts/shy_" ;
    path += module ;
    path += "_consts_injections.hpp" ;
}

void shy_guts :: consts_consts :: injections_hpp_contents ( so_called_std_string & result , so_called_std_string module )
{
    result . clear ( ) ;
    result += "#include \"../../../injections/platform/math/shy_math.h\"\n" ;
    result += "\n" ;
    result += "#include \"./shy_" ;
    result += module ;
    result += "_consts.hpp\"\n" ;
}

void shy_guts :: consts_consts :: hpp_value_fract
    ( so_called_std_string & result 
    , so_called_std_string module 
    , so_called_std_string value 
    , so_called_std_string numerator 
    , so_called_std_string denominator 
    )
{
    result . clear ( ) ;
    result += "const so_called_type_platform_math_num_fract so_called_common_" ;
    result += module ;
    result += "_consts :: " ;
    result += value ;
    result += " = so_called_platform_math :: init_num_fract ( " ;
    result += numerator ;
    result += " , " ;
    result += denominator ;
    result += " ) ;\n" ;
}

void shy_guts :: consts_consts :: hpp_value_whole
    ( so_called_std_string & result 
    , so_called_std_string module 
    , so_called_std_string value 
    , so_called_std_string number
    )
{
    result . clear ( ) ;
    result += "const so_called_type_platform_math_num_whole so_called_common_" ;
    result += module ;
    result += "_consts :: " ;
    result += value ;
    result += " = so_called_platform_math :: init_num_whole ( " ;
    result += number ;
    result += " ) ;\n" ;
}

void shy_guts :: consts_fsm :: injections_hpp_path ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour_injections.hpp" ;
}

void shy_guts :: consts_fsm :: hpp_path ( so_called_std_string & path , so_called_std_string system )
{
    path . clear ( ) ;
    path += system ;
    path += "_fsm_behaviour/shy_" ;
    path += system ;
    path += "_fsm_behaviour.hpp" ;
}

void shy_guts :: consts_fsm :: injections_hpp_contents ( so_called_std_string & result , so_called_std_string system )
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

void shy_guts :: generate_consts :: python_script ( so_called_std_string & result )
{
    result . clear ( ) ;
    so_called_type_loadable_consts_content_module_container * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    for ( so_called_type_loadable_consts_content_module_container :: const_iterator module_i = module_container -> begin ( )
        ; module_i != module_container -> end ( )
        ; ++ module_i
        )
    {
        so_called_std_string module_name ;
        so_called_std_string consts_hpp_path ;
        so_called_std_string consts_injections_hpp_path ;
        so_called_std_string generate_consts_hpp ;
        so_called_std_string generate_consts_injections_hpp ;
        so_called_std_string consts_hpp_contents ;
        so_called_std_string consts_injections_hpp_contents ;

        module_name = module_i -> first ;

        shy_guts :: consts_consts :: hpp_path
            ( consts_hpp_path 
            , module_name 
            ) ;
        shy_guts :: consts_consts :: injections_hpp_path
            ( consts_injections_hpp_path 
            , module_name 
            ) ;

        shy_guts :: consts_consts :: injections_hpp_contents 
            ( consts_injections_hpp_contents 
            , module_name 
            ) ;
        shy_guts :: generate_consts :: hpp_contents
            ( consts_hpp_contents
            , module_i
            ) ;

        so_called_loadable_generator_python :: generate_file 
            ( generate_consts_hpp
            , so_called_loadable_generator_consts :: autogenerated_folder_path + consts_hpp_path
            , consts_hpp_contents
            ) ;
        so_called_loadable_generator_python :: generate_file 
            ( generate_consts_injections_hpp 
            , so_called_loadable_generator_consts :: autogenerated_folder_path + consts_injections_hpp_path 
            , consts_injections_hpp_contents 
            ) ;

        result += generate_consts_hpp ;
        result += generate_consts_injections_hpp ;
    }
}

void shy_guts :: generate_consts :: hpp_contents ( so_called_std_string & result , so_called_type_loadable_consts_content_module_container :: const_iterator module_i )
{
    so_called_std_string values_fract ;
    so_called_std_string values_whole ;

    shy_guts :: generate_consts :: hpp_values_fract ( values_fract , module_i ) ;
    shy_guts :: generate_consts :: hpp_values_whole ( values_whole , module_i ) ;

    result . clear ( ) ;
    result += values_fract ;
    result += values_whole ;
}

void shy_guts :: generate_consts :: hpp_values_fract ( so_called_std_string & result , so_called_type_loadable_consts_content_module_container :: const_iterator module_i )
{
    result . clear ( ) ;
    for ( so_called_type_loadable_consts_content_value_fract_container :: const_iterator value_i = module_i -> second . name_to_fract . begin ( )
        ; value_i != module_i -> second . name_to_fract . end ( )
        ; ++ value_i
        )
    {
        so_called_std_string numerator ;
        so_called_std_string denominator ;
        so_called_std_string value_cplusplus_code ;

        shy_guts :: generate_consts :: signed_value
            ( numerator
            , value_i -> second . numerator_sign
            , value_i -> second . numerator_value
            ) ;

        shy_guts :: generate_consts :: signed_value
            ( denominator
            , value_i -> second . denominator_sign
            , value_i -> second . denominator_value
            ) ;

        shy_guts :: consts_consts :: hpp_value_fract 
            ( value_cplusplus_code
            , module_i -> first
            , value_i -> first
            , numerator
            , denominator
            ) ;

        result += value_cplusplus_code ;
    }
}

void shy_guts :: generate_consts :: hpp_values_whole ( so_called_std_string & result , so_called_type_loadable_consts_content_module_container :: const_iterator module_i )
{
    result . clear ( ) ;
    for ( so_called_type_loadable_consts_content_value_whole_container :: const_iterator value_i = module_i -> second . name_to_whole . begin ( )
        ; value_i != module_i -> second . name_to_whole . end ( )
        ; ++ value_i
        )
    {
        so_called_std_string value_str ;
        so_called_std_string value_cplusplus_code ;

        shy_guts :: generate_consts :: signed_value
            ( value_str
            , value_i -> second . sign
            , value_i -> second . value
            ) ;

        shy_guts :: consts_consts :: hpp_value_whole 
            ( value_cplusplus_code
            , module_i -> first
            , value_i -> first
            , value_str
            ) ;

        result += value_cplusplus_code ;
    }
}

void shy_guts :: generate_consts :: signed_value ( so_called_std_string & result , so_called_std_string sign , so_called_std_string number )
{
    result . clear ( ) ;
    result += sign ;
    if ( ! sign . empty ( ) )
        result += so_called_loadable_generator_consts :: whitespace ;
    result += number ;
}

void shy_guts :: generate_fsm :: python_script ( so_called_std_string & result )
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

        shy_guts :: consts_fsm :: hpp_path
            ( fsm_hpp_path 
            , system_name 
            ) ;
        shy_guts :: consts_fsm :: injections_hpp_path
            ( fsm_injections_hpp_path 
            , system_name 
            ) ;

        shy_guts :: consts_fsm :: injections_hpp_contents
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

void shy_loadable_generator :: generate ( so_called_std_string & result )
{
    so_called_std_string consts_logic ;
    so_called_std_string fsm_logic ;
    shy_guts :: generate_consts :: python_script ( consts_logic ) ;
    shy_guts :: generate_fsm :: python_script ( fsm_logic ) ;
    so_called_loadable_generator_python :: main_script ( result , consts_logic + fsm_logic ) ;
}

