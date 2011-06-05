class shy_common_engine_fsm_stateless
{
public :
    template < typename fsm , typename fsm_behaviour >
    static void run_fsm ( ) ;

    static void tick_single_fsm ( so_called_type_platform_pointer_data < so_called_type_common_engine_fsm_state > & ) ;
} ;

template < typename fsm, typename fsm_behaviour >
void shy_common_engine_fsm_stateless :: run_fsm ( )
{
    so_called_type_platform_math_num_whole is_running ;
    fsm_behaviour :: is_fsm_running ( is_running ) ;
    if ( so_called_platform_conditions :: whole_is_false ( is_running ) )
    {
        fsm_behaviour :: run_fsm_begin ( ) ;

        so_called_type_platform_math_num_whole behaviour_inputs_changed ;
        so_called_type_platform_math_num_whole inputs_changed ;
        for ( ; ; )
        {
            fsm_behaviour :: recalc_current_behaviour_inputs ( ) ;
            fsm :: recalc_current_inputs ( ) ;
            fsm_behaviour :: determine_behaviour_inputs_change ( behaviour_inputs_changed ) ;
            fsm :: determine_inputs_change ( inputs_changed ) ;
            if ( so_called_platform_conditions :: whole_is_true ( behaviour_inputs_changed )
              || so_called_platform_conditions :: whole_is_true ( inputs_changed )
               )
            {
                fsm_behaviour :: update_fixed_behaviour_inputs ( ) ;
                fsm :: update_fixed_inputs ( ) ;
                fsm_behaviour :: tick_all_fsms ( ) ;
            }
            else
                break ;
        }

        fsm_behaviour :: reset_behaviour_input_events ( ) ;
        fsm :: reset_input_events ( ) ;
        fsm_behaviour :: run_fsm_end ( ) ;
    }
}

