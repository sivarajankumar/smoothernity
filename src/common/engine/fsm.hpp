template < typename mediator >
class shy_engine_fsm
{
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    template < typename fsm_state_environment_type >
    class fsm_state_type
    {
    public :
        virtual void on_entry ( fsm_state_environment_type & ) ;
        virtual void on_exit ( fsm_state_environment_type & ) ;
        virtual void on_input ( fsm_state_environment_type & ) ;
        virtual fsm_state_type < fsm_state_environment_type > & transition ( fsm_state_environment_type & ) ; 
    } ;
public :
    template < typename fsm_type , typename fsm_autogenerated_type >
    static void run_fsm ( fsm_type & , fsm_autogenerated_type & ) ;

    template < typename fsm_state_environment_type >
    static void tick_single_fsm 
        ( fsm_state_environment_type & 
        , typename platform_pointer :: template pointer < fsm_state_type < fsm_state_environment_type > > & 
        ) ;
private :
    template < typename fsm_type , typename fsm_autogenerated_type >
    static void _stabilize_fsm ( fsm_type & , fsm_autogenerated_type & ) ;
} ;

template < typename mediator >
template < typename fsm_state_environment_type >
void shy_engine_fsm < mediator > :: fsm_state_type < fsm_state_environment_type > :: on_entry ( fsm_state_environment_type & )
{
}

template < typename mediator >
template < typename fsm_state_environment_type >
void shy_engine_fsm < mediator > :: fsm_state_type < fsm_state_environment_type > :: on_exit ( fsm_state_environment_type & )
{
}

template < typename mediator >
template < typename fsm_state_environment_type >
void shy_engine_fsm < mediator > :: fsm_state_type < fsm_state_environment_type > :: on_input ( fsm_state_environment_type & )
{
}

template < typename mediator >
template < typename fsm_state_environment_type >
typename shy_engine_fsm < mediator > :: template fsm_state_type < fsm_state_environment_type > &
shy_engine_fsm < mediator > :: fsm_state_type < fsm_state_environment_type > :: transition ( fsm_state_environment_type & )
{
    return * this ;
}

template < typename mediator >
template < typename fsm_type , typename fsm_autogenerated_type >
void shy_engine_fsm < mediator > :: run_fsm ( fsm_type & fsm , fsm_autogenerated_type & fsm_autogenerated )
{
    num_whole is_running ;
    fsm_autogenerated . is_fsm_running ( is_running ) ;
    if ( platform_conditions :: whole_is_false ( is_running ) )
    {
        fsm_autogenerated . run_fsm_begin ( ) ;
        _stabilize_fsm ( fsm , fsm_autogenerated ) ;
        fsm_autogenerated . reset_autogenerated_input_events ( ) ;
        fsm . reset_input_events ( ) ;
        _stabilize_fsm ( fsm , fsm_autogenerated ) ;
        fsm_autogenerated . run_fsm_end ( ) ;
    }
}

template < typename mediator >
template < typename fsm_state_environment_type >
void shy_engine_fsm < mediator > :: tick_single_fsm 
    ( fsm_state_environment_type & env 
    , typename platform_pointer :: template pointer < fsm_state_type < fsm_state_environment_type > > & state 
    )
{
    typename platform_pointer :: template pointer < fsm_state_type < fsm_state_environment_type > > next_state ;
    num_whole states_are_equal ;

    state . get ( ) . on_input ( env ) ;
    for ( ; ; )
    {
        platform_pointer :: bind ( next_state , state . get ( ) . transition ( env ) ) ;
        platform_pointer :: are_equal ( states_are_equal , state , next_state ) ;
        if ( platform_conditions :: whole_is_true ( states_are_equal ) )
            break ;
        else
        {
            state . get ( ) . on_exit ( env ) ;
            state = next_state ;
            state . get ( ) . on_entry ( env ) ;
        }
    }
}

template < typename mediator >
template < typename fsm_type , typename fsm_autogenerated_type >
void shy_engine_fsm < mediator > :: _stabilize_fsm ( fsm_type & fsm , fsm_autogenerated_type & fsm_autogenerated )
{
    num_whole autogenerated_inputs_changed ;
    num_whole inputs_changed ;
    for ( ; ; )
    {
        fsm_autogenerated . recalc_current_autogenerated_inputs ( ) ;
        fsm . recalc_current_inputs ( ) ;
        fsm_autogenerated . determine_autogenerated_inputs_change ( autogenerated_inputs_changed ) ;
        fsm . determine_inputs_change ( inputs_changed ) ;
        if ( platform_conditions :: whole_is_true ( autogenerated_inputs_changed )
          || platform_conditions :: whole_is_true ( inputs_changed )
           )
        {
            fsm_autogenerated . update_fixed_autogenerated_inputs ( ) ;
            fsm . update_fixed_inputs ( ) ;
            fsm_autogenerated . tick_all_fsms ( ) ;
        }
        else
            break ;
    }
}

