template 
    < typename _actions
    , typename _executor
    , typename _inputs 
    , typename _platform
    , typename _state
    >
class shy_fsm_contents_types
{
public :
    typedef _actions actions ;
    typedef _executor executor ;
    typedef _inputs inputs ;
    typedef _platform platform ;
    typedef _state state ;
} ;

template < typename fsm_contents_types >
class shy_logic_application_fsm_contents
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
public :
    shy_logic_application_fsm_contents ( ) ;
    void tick ( ) ;
private :
    all_states _all_states ;
    typename platform_pointer :: template pointer < state > _machine_main ;
    typename platform_pointer :: template pointer < state > _machine_slave ;
} ;

template < typename fsm_contents_types >
shy_logic_application_fsm_contents < fsm_contents_types > :: shy_logic_application_fsm_contents ( )
{
    platform_pointer :: bind ( _machine_main , _all_states . machine_main_state_initial ) ;
    platform_pointer :: bind ( _machine_slave , _all_states . machine_slave_state_initial ) ;
}

template < typename fsm_contents_types >
void shy_logic_application_fsm_contents < fsm_contents_types > :: tick ( )
{
    executor :: tick ( _machine_main ) ;
    executor :: tick ( _machine_slave ) ;
}



template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_application_inputs_type
    {
    public :
        num_whole logic_application_render ;
        num_whole logic_application_update ;
        num_whole text_generated ;
        num_whole title_generated ;
    } ;

    class _logic_application_actions_type
    {
    public :
        void logic_text_creation_permit ( ) ;
        void logic_text_update ( ) ;
        void logic_title_creation_permit ( ) ;
        void logic_title_render ( ) ;
        void logic_title_update ( ) ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_application_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_application_inputs_type _logic_application_inputs ;
} ;

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
}

