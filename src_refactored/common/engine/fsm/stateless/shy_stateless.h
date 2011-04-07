class shy_common_engine_fsm_stateless
{
public :
    template < typename fsm_state_environment_type >
    class fsm_state_type
    {
    public :
        virtual ~ fsm_state_type ( ) ;
        virtual void on_entry ( fsm_state_environment_type & ) ;
        virtual void on_exit ( fsm_state_environment_type & ) ;
        virtual void on_input ( fsm_state_environment_type & ) ;
        virtual fsm_state_type < fsm_state_environment_type > & transition ( fsm_state_environment_type & )
        {
            // MSVC 2010 COMPILER THROWS ERROR C2244 IF THIS METHOD IS IMPLEMENTED EXTERNALLY
            return * this ;
        }
    } ;
public :
    template < typename fsm , typename fsm_behaviour >
    static void run_fsm ( ) ;

    template < typename fsm_state_environment_type >
    static void tick_single_fsm 
        ( fsm_state_environment_type & 
        , so_called_type_platform_pointer_data < fsm_state_type < fsm_state_environment_type > > & 
        ) ;
private :
    template < typename fsm , typename fsm_behaviour >
    static void _stabilize_fsm ( ) ;
} ;

template < typename fsm_state_environment_type >
shy_common_engine_fsm_stateless :: fsm_state_type < fsm_state_environment_type > :: ~ fsm_state_type ( )
{
}

template < typename fsm_state_environment_type >
void shy_common_engine_fsm_stateless :: fsm_state_type < fsm_state_environment_type > :: on_entry ( fsm_state_environment_type & )
{
}

template < typename fsm_state_environment_type >
void shy_common_engine_fsm_stateless :: fsm_state_type < fsm_state_environment_type > :: on_exit ( fsm_state_environment_type & )
{
}

template < typename fsm_state_environment_type >
void shy_common_engine_fsm_stateless :: fsm_state_type < fsm_state_environment_type > :: on_input ( fsm_state_environment_type & )
{
}

template < typename fsm, typename fsm_behaviour >
void shy_common_engine_fsm_stateless :: run_fsm ( )
{
    so_called_type_platform_math_num_whole is_running ;
    fsm_behaviour :: is_fsm_running ( is_running ) ;
    if ( so_called_platform_conditions :: whole_is_false ( is_running ) )
    {
        fsm_behaviour :: run_fsm_begin ( ) ;
        _stabilize_fsm < fsm , fsm_behaviour > ( ) ;
        fsm_behaviour :: reset_behaviour_input_events ( ) ;
        fsm :: reset_input_events ( ) ;
        fsm_behaviour :: run_fsm_end ( ) ;
    }
}

template < typename fsm_state_environment_type >
void shy_common_engine_fsm_stateless :: tick_single_fsm 
    ( fsm_state_environment_type & env 
    , so_called_type_platform_pointer_data < fsm_state_type < fsm_state_environment_type > > & state 
    )
{
    so_called_type_platform_pointer_data < fsm_state_type < fsm_state_environment_type > > next_state ;
    so_called_type_platform_math_num_whole states_are_equal ;

    state . get ( ) . on_input ( env ) ;
    for ( ; ; )
    {
        so_called_platform_pointer :: bind ( next_state , state . get ( ) . transition ( env ) ) ;
        so_called_platform_pointer :: are_equal ( states_are_equal , state , next_state ) ;
        if ( so_called_platform_conditions :: whole_is_true ( states_are_equal ) )
            break ;
        else
        {
            state . get ( ) . on_exit ( env ) ;
            state = next_state ;
            state . get ( ) . on_entry ( env ) ;
        }
    }
}

template < typename fsm , typename fsm_behaviour >
void shy_common_engine_fsm_stateless :: _stabilize_fsm ( )
{
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
}
