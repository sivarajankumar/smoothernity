namespace shy_guts
{
    namespace consts
    {
        static so_called_lib_std_char slash = '/' ;
        static so_called_lib_std_char underscore = '_' ;
    }
}

void shy_loadable_generator :: generate ( so_called_lib_std_string & result )
{
    so_called_lib_std_string consts_logic ;
    so_called_lib_std_string fsm_logic ;

    so_called_loadable_consts_generator :: generate ( consts_logic ) ;
    so_called_loadable_fsm_generator :: generate ( fsm_logic ) ;

    so_called_loadable_generator_python :: main_script ( result , consts_logic + fsm_logic ) ;
}

void shy_loadable_generator :: module_path ( so_called_lib_std_string & result , so_called_lib_std_string module_name )
{
    result . clear ( ) ;
    for ( so_called_lib_std_int32_t i = 0 ; i < so_called_lib_std_int32_t ( module_name . size ( ) ) ; ++ i )
    {
        if ( module_name [ i ] == shy_guts :: consts :: underscore )
            result += shy_guts :: consts :: slash ;
        else
            result += module_name [ i ] ;
    }
}
