void shy_loadable_fsm_behaviour_trace :: machine_state_action_command 
    ( so_called_std_string machine 
    , so_called_std_string state
    , so_called_std_string command_name
    , so_called_std_string command_machine
    )
{
    so_called_lib_std_cerr << "machine " ;
    so_called_lib_std_cerr << machine ;
    so_called_lib_std_cerr << " state " ;
    so_called_lib_std_cerr << state ;
    so_called_lib_std_cerr << " action command " ;
    so_called_lib_std_cerr << command_name ;
    so_called_lib_std_cerr << " to machine " ;
    so_called_lib_std_cerr << command_machine ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_loadable_fsm_behaviour_trace :: machine_state_action_do 
    ( so_called_std_string machine
    , so_called_std_string state
    , so_called_std_string action
    )
{
    so_called_lib_std_cerr << "machine " ;
    so_called_lib_std_cerr << machine ;
    so_called_lib_std_cerr << " state " ;
    so_called_lib_std_cerr << state ;
    so_called_lib_std_cerr << " action do " ;
    so_called_lib_std_cerr << action ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_loadable_fsm_behaviour_trace :: machine_state_on_entry ( so_called_std_string machine , so_called_std_string state )
{
    so_called_lib_std_cerr << "machine " ;
    so_called_lib_std_cerr << machine ;
    so_called_lib_std_cerr << " state " ;
    so_called_lib_std_cerr << state ;
    so_called_lib_std_cerr << " on_entry" ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_loadable_fsm_behaviour_trace :: machine_state_on_exit ( so_called_std_string machine , so_called_std_string state )
{
    so_called_lib_std_cerr << "machine " ;
    so_called_lib_std_cerr << machine ;
    so_called_lib_std_cerr << " state " ;
    so_called_lib_std_cerr << state ;
    so_called_lib_std_cerr << " on_exit" ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_loadable_fsm_behaviour_trace :: machine_state_on_input ( so_called_std_string machine , so_called_std_string state )
{
    so_called_lib_std_cerr << "machine " ;
    so_called_lib_std_cerr << machine ;
    so_called_lib_std_cerr << " state " ;
    so_called_lib_std_cerr << state ;
    so_called_lib_std_cerr << " on_input" ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_loadable_fsm_behaviour_trace :: tick_all_fsms ( )
{
    so_called_lib_std_cerr << so_called_lib_std_endl ;
    so_called_lib_std_cerr << "tick all fsms" ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

