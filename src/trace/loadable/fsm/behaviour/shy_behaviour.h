class shy_trace_loadable_fsm_behaviour
{
public :
    static void machine_state_action_command 
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        , const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void machine_state_action_discard
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void machine_state_action_do 
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void machine_state_on_entry
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void machine_state_on_exit
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void machine_state_on_input
        ( const so_called_lib_std_char *
        , const so_called_lib_std_char *
        ) ;
    static void tick_all_fsms ( ) ;
} ;
