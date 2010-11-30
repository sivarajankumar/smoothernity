template < typename mediator >
class shy_logic_application_fsm
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _inputs_type
    {
    public :
        num_whole logic_application_render ;
        num_whole logic_application_update ;
    } ;

    class _state_type
    {
    public :
        virtual void entry_actions ( ) ;
        virtual void exit_actions ( ) ;
        virtual void input_actions ( ) ;
        virtual void transition ( ) ;
    } ;

    class _machine_main_state_initial_type
    : public _state_type
    {
    public :
        virtual void transition ( ) ;
    } ;

    class _machine_main_state_application_launched_type
    : public _state_type
    {
    public :
        virtual void entry_actions ( ) ;
        virtual void input_actions ( ) ;
        virtual void transition ( ) ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_application_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _inputs_type _inputs ;

    _machine_main_state_initial_type _machine_main_state_initial ;
    _machine_main_state_application_launched_type _machine_main_state_application_launched ;
    typename platform_pointer :: template pointer < _state_type > _machine_main_state ;
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

