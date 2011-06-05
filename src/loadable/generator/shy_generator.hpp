void shy_loadable_generator :: generate ( so_called_lib_std_string & result )
{
    so_called_lib_std_string consts_logic ;
    so_called_lib_std_string fsm_logic ;

    so_called_loadable_consts_generator :: generate ( consts_logic ) ;
    so_called_loadable_fsm_generator :: generate ( fsm_logic ) ;

    so_called_loadable_generator_python :: main_script ( result , consts_logic + fsm_logic ) ;
}

