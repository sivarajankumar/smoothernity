template 
    < typename _actions
    , typename _contents
    , typename _executor
    , typename _inputs 
    , typename _platform
    , typename _state
    >
class shy_fsm_contents_types
{
public :
    typedef _actions actions ;
    typedef _contents contents ;
    typedef _executor executor ;
    typedef _inputs inputs ;
    typedef _platform platform ;
    typedef _state state ;
} ;

template < typename fsm_contents_types >
class shy_logic_application_fsm_contents
: public fsm_contents_types :: contents
{
    typedef typename fsm_contents_types :: actions actions ;
    typedef typename fsm_contents_types :: executor executor ;
    typedef typename fsm_contents_types :: inputs inputs ;
    typedef typename fsm_contents_types :: platform platform ;
    typedef typename fsm_contents_types :: platform :: platform_pointer platform_pointer ;
    typedef typename fsm_contents_types :: state state ;

public :
    class all_states ;

private :
    class _machine_main_state_initial_type
    : public state
    {
    public :
        virtual void transition ( typename platform_pointer :: template pointer < state > & , typename platform_pointer :: template pointer < all_states > ) ;
    } ;

    class _machine_main_state_application_launched_type
    : public state
    {
    public :
        virtual void entry_actions ( typename platform_pointer :: template pointer < actions > ) ;
        virtual void input_actions ( typename platform_pointer :: template pointer < const inputs > , typename platform_pointer :: template pointer < actions > ) ;
        virtual void transition ( typename platform_pointer :: template pointer < state > & , typename platform_pointer :: template pointer < all_states > ) ;
    } ;

    class _machine_main_state_generating_title_type
    : public state
    {
    public :
        virtual void entry_actions ( typename platform_pointer :: template pointer < actions > ) ;
        virtual void input_actions ( typename platform_pointer :: template pointer < const inputs > , typename platform_pointer :: template pointer < actions > ) ;
        virtual void transition ( typename platform_pointer :: template pointer < state > & , typename platform_pointer :: template pointer < all_states > ) ;
    } ;

    class _machine_slave_state_initial_type
    : public state
    {
    } ;

public :
    class all_states
    {
    public :
        _machine_main_state_application_launched_type machine_main_state_application_launched ;
        _machine_main_state_generating_title_type machine_main_state_generating_title ;
        _machine_main_state_initial_type machine_main_state_initial ;
        _machine_slave_state_initial_type machine_slave_state_initial ;
    } ;
    class all_machines
    {
    public :
        typename platform_pointer :: template pointer < state > machine_main ;
        typename platform_pointer :: template pointer < state > machine_slave ;
    } ;
public :
    shy_logic_application_fsm_contents ( ) ;
    virtual void tick ( typename platform_pointer :: template pointer < executor > ) ;
private :
    all_states _all_states ;
    all_machines _all_machines ;
} ;

template < typename fsm_contents_types >
shy_logic_application_fsm_contents < fsm_contents_types > :: shy_logic_application_fsm_contents ( )
{
    platform_pointer :: bind ( _all_machines . machine_main , _all_states . machine_main_state_initial ) ;
    platform_pointer :: bind ( _all_machines . machine_slave , _all_states . machine_slave_state_initial ) ;
}

template < typename fsm_contents_types >
void shy_logic_application_fsm_contents < fsm_contents_types > :: tick ( typename platform_pointer :: template pointer < executor > arg_executor )
{
    arg_executor . get ( ) . tick ( _all_machines . machine_main ) ;
    arg_executor . get ( ) . tick ( _all_machines . machine_slave ) ;
}



template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_application_inputs_type
    {
    public :
        num_whole application_render ;
        num_whole application_update ;
        num_whole main_menu_created ;
        num_whole main_menu_finished ;
        num_whole text_prepared ;
        num_whole title_created ;
        num_whole title_finished ;
    } ;

    class _logic_application_actions_type
    {
    public :
        void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;

        void amusement_creation_permit ( ) ;
        void amusement_launch_permit ( ) ;
        void amusement_render ( ) ;
        void amusement_update ( ) ;
        void game_launch_permit ( ) ;
        void game_render ( ) ;
        void game_update ( ) ;
        void main_menu_creation_permit ( ) ;
        void main_menu_launch_permit ( ) ;
        void main_menu_render ( ) ;
        void main_menu_update ( ) ;
        void text_prepare_permit ( ) ;
        void text_update ( ) ;
        void title_launch_permit ( ) ;
        void title_render ( ) ;
        void title_update ( ) ;
    private :
        typename platform_pointer :: template pointer < mediator > _mediator ;
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
    void _update_inputs ( ) ;
    void _tick_fsm ( ) ;
    void _stabilize_fsm ( ) ;
    void _reset_input_events ( ) ;
    void _determine_inputs_change ( ) ;
    void _update_fixed_inputs ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    num_whole _fsm_running ;
    num_whole _inputs_changed ;
    _logic_application_inputs_type _fixed_inputs ;
    _logic_application_inputs_type _mutable_inputs ;
    _logic_application_actions_type _actions ;
} ;

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: amusement_creation_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: amusement_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: amusement_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: amusement_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_amusement_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: game_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: game_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: game_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_game_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: main_menu_creation_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_creation_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: main_menu_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: main_menu_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: main_menu_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: text_prepare_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_text_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: text_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_text_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: title_launch_permit ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: title_render ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_render ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _logic_application_actions_type :: title_update ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_title_update ( ) ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
    _actions . set_mediator ( arg_mediator ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _fsm_running = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_amusement_finished )
{
    _mutable_inputs . logic_amusement_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_render )
{
    _mutable_inputs . logic_application_render = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_application_update )
{
    _mutable_inputs . logic_application_update = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_text_prepared )
{
    _mutable_inputs . logic_text_prepared = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_created )
{
    _mutable_inputs . logic_title_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_title_finished )
{
    _mutable_inputs . logic_title_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_created )
{
    _mutable_inputs . logic_main_menu_created = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: receive ( typename messages :: logic_main_menu_finished )
{
    _mutable_inputs . logic_main_menu_finished = _platform_math_consts . get ( ) . whole_true ;
    _run_fsm ( ) ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _reset_input_events ( )
{
    _mutable_inputs . application_render = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . application_update = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . main_menu_created = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . main_menu_finished = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . text_prepared = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . title_created = _platform_math_consts . get ( ) . whole_false ;
    _mutable_inputs . title_finished = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_application_fsm < mediator > :: _determine_inputs_change ( )
{
    if ( platform_conditions :: wholes_are_equal ( _mutable_inputs . application_render , _fixed_inputs . application_render )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . application_update , _fixed_inputs . application_update )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . main_menu_created , _fixed_inputs . main_menu_created )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . main_menu_finished , _fixed_inputs . main_menu_finished )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . text_prepared , _fixed_inputs . text_prepared )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . title_created , _fixed_inputs . title_created )
      && platform_conditions :: wholes_are_equal ( _mutable_inputs . title_finished , _fixed_inputs . title_finished )
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
    _fixed_inputs = _mutable_inputs ;
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
            _tick_fsm ( ) ;
        }
        else
            break ;
    }
}

