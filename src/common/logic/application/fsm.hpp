template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef shy_logic_application_fsm < mediator > logic_application_fsm ;

    class _logic_application_fsm_inputs_type
    {
    public :
        num_whole logic_amusement_finished ;
        num_whole logic_application_render ;
        num_whole logic_application_update ;
        num_whole logic_text_prepared ;
        num_whole logic_title_created ;
        num_whole logic_title_finished ;
        num_whole logic_main_menu_created ;
        num_whole logic_main_menu_finished ;
    } ;

    class _logic_application_fsm_state_type
    {
    public :
        virtual void on_entry ( logic_application_fsm & ) ;
        virtual void on_exit ( logic_application_fsm & ) ;
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ; 
    } ;

    class _machine_application_state_initial_type
    : public _logic_application_fsm_state_type
    {
    public :
        virtual void on_input ( logic_application_fsm & ) ;
        virtual _logic_application_fsm_state_type & transition ( logic_application_fsm & ) ;
    } ;

    class _machine_application_state_launched_type
    : public _logic_application_fsm_state_type
    {
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_amusement_finished ) ;
    void receive ( typename messages :: logic_application_render ) ;
    void receive ( typename messages :: logic_application_update ) ;
    void receive ( typename messages :: logic_text_prepared ) ;
    void receive ( typename messages :: logic_title_created ) ;
    void receive ( typename messages :: logic_title_finished ) ;
    void receive ( typename messages :: logic_main_menu_created ) ;
    void receive ( typename messages :: logic_main_menu_finished ) ;
private :
    void _run_fsm ( ) ;
    void _stabilize_fsm ( ) ;
    void _reset_input_events ( ) ;
    void _determine_inputs_change ( ) ;
    void _update_fixed_inputs ( ) ;
    void _tick_all_fsms ( ) ;
    void _tick_single_fsm ( typename platform_pointer :: template pointer < _logic_application_fsm_state_type > & ) ;
public :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _machine_application_state_initial_type _machine_application_state_initial ;
    _machine_application_state_launched_type _machine_application_state_launched ;

    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > _machine_application_state ;

    num_whole _inputs_changed ;
    num_whole _fsm_running ;
    _logic_application_fsm_inputs_type _current_inputs ;
    _logic_application_fsm_inputs_type _fixed_inputs ;
} ;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _machine_application_state_initial_type :: on_input ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        fsm . _mediator . get ( ) . send ( typename messages :: logic_text_prepare_permit ( ) ) ;
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _machine_application_state_initial_type :: transition ( logic_application_fsm & fsm )
{
    if ( platform_conditions :: whole_is_true ( fsm . _fixed_inputs . logic_application_update ) )
        return fsm . _machine_application_state_launched ;
    else
        return _logic_application_fsm_state_type :: transition ( fsm ) ;
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_entry ( logic_application_fsm & )
{
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_exit ( logic_application_fsm & )
{
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: on_input ( logic_application_fsm & )
{
}

template < typename mediator >
typename shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type &
shy_logic_application_fsm < mediator > :: _logic_application_fsm_state_type :: transition ( logic_application_fsm & )
{
    return * this ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _inputs_changed = _platform_math_consts . get ( ) . whole_false ;
    _fsm_running = _platform_math_consts . get ( ) . whole_false ;

    platform_pointer :: bind ( _machine_application_state , _machine_application_state_initial ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_finished )
{
    _current_inputs . logic_amusement_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_render )
{
    _current_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_update )
{
    _current_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_text_prepared )
{
    _current_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_created )
{
    _current_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_finished )
{
    _current_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_created )
{
    _current_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_finished )
{
    _current_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _reset_input_events ( )
{
    _current_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_false ;
    _current_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _determine_inputs_change ( )
{
    if ( platform_conditions :: wholes_are_equal ( _current_inputs . logic_application_render , _fixed_inputs . logic_application_render )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_application_update , _fixed_inputs . logic_application_update )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_main_menu_created , _fixed_inputs . logic_main_menu_created )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_main_menu_finished , _fixed_inputs . logic_main_menu_finished )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_text_prepared , _fixed_inputs . logic_text_prepared )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_title_created , _fixed_inputs . logic_title_created )
      && platform_conditions :: wholes_are_equal ( _current_inputs . logic_title_finished , _fixed_inputs . logic_title_finished )
       )
    {
        _inputs_changed = _platform_math_consts . get ( ) . whole_false ;
    }
    else
        _inputs_changed = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _update_fixed_inputs ( )
{
    _fixed_inputs = _current_inputs ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _run_fsm ( )
{
    if ( platform_conditions :: whole_is_false ( _fsm_running ) )
    {
        _fsm_running = _platform_math_consts . get ( ) . whole_true ;
        _stabilize_fsm ( ) ;
        _reset_input_events ( ) ;
        _stabilize_fsm ( ) ;
        _fsm_running = _platform_math_consts . get ( ) . whole_false ;
    }
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _stabilize_fsm ( )
{
    while ( true )
    {
        _determine_inputs_change ( ) ;
        if ( platform_conditions :: whole_is_true ( _inputs_changed ) )
        {
            _update_fixed_inputs ( ) ;
            _tick_all_fsms ( ) ;
        }
        else
            break ;
    }
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _tick_all_fsms ( )
{
    _tick_single_fsm ( _machine_application_state ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _tick_single_fsm ( typename platform_pointer :: template pointer < _logic_application_fsm_state_type > & state )
{
    typename platform_pointer :: template pointer < _logic_application_fsm_state_type > next_state ;
    num_whole states_are_equal ;

    state . get ( ) . on_input ( * this ) ;
    while ( true )
    {
        platform_pointer :: bind ( next_state , state . get ( ) . transition ( * this ) ) ;
        platform_pointer :: are_equal ( states_are_equal , state , next_state ) ;
        if ( platform_conditions :: whole_is_true ( states_are_equal ) )
            break ;
        else
        {
            state . get ( ) . on_exit ( * this ) ;
            state = next_state ;
            state . get ( ) . on_entry ( * this ) ;
        }
    }
}

