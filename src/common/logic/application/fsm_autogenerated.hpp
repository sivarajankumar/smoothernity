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

