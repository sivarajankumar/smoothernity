class shy_common_logic_application_fsm_behaviour_loadable
{
public :
    static void determine_behaviour_inputs_change ( so_called_type_platform_math_num_whole & ) ;
    static void init ( ) ;
    static void is_fsm_running ( so_called_type_platform_math_num_whole & ) ;
    static void recalc_current_behaviour_inputs ( ) ;
    static void reset_behaviour_input_events ( ) ;
    static void run_fsm_begin ( ) ;
    static void run_fsm_end ( ) ;
    static void set_inputs 
        ( so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > 
        , so_called_type_platform_pointer_data < so_called_type_common_logic_application_fsm_inputs > 
        ) ;
    static void tick_all_fsms ( ) ;
    static void update_fixed_behaviour_inputs ( ) ;
} ;
