void shy_common_engine_fsm_stateless :: tick_single_fsm ( so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > & state )
{
    so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > next_state ;
    so_called_type_platform_math_num_whole states_are_equal ;

    state . get ( ) . on_input ( ) ;
    for ( ; ; )
    {
        so_called_platform_pointer :: bind ( next_state , state . get ( ) . transition ( ) ) ;
        so_called_platform_pointer :: are_equal ( states_are_equal , state , next_state ) ;
        if ( so_called_platform_conditions :: whole_is_true ( states_are_equal ) )
            break ;
        else
        {
            state . get ( ) . on_exit ( ) ;
            state = next_state ;
            state . get ( ) . on_entry ( ) ;
        }
    }
}

