template 
    < template < typename mediator > class _first_module
    , template < typename mediator > class _second_module
    , template < typename mediator > class _controller
    >
class test_mediator_types
{
public :
    template < typename mediator >
    class modules
    {
    public :
        typedef _first_module < mediator > first_module ;
        typedef _second_module < mediator > second_module ;
        typedef _controller < mediator > controller ;
    } ;
} ;

template 
    < template < typename > class first_module
    , template < typename > class second_module
    , template < typename > class controller
    , template < typename , typename > class mediator
    , typename messages
    >
class test_aggregator
{
public :
    test_aggregator ( )
    : _first_module ( & _mediator )
    , _second_module ( & _mediator )
    , _controller ( & _mediator )
    {
        _mediator . register_modules 
            ( & _first_module 
            , & _second_module 
            , & _controller 
            ) ;
    }
    void start ( )
    {
        _mediator . send ( typename messages :: start ( ) ) ;
    }
    void on_some_event ( int arg )
    {
        typename messages :: on_some_event msg ;
        msg . arg = arg ;
        _mediator . send ( msg ) ;
    }
private :
    typedef mediator 
        < test_mediator_types
            < first_module 
            , second_module 
            , controller
            >
        , messages
        > mediator_type ;
    mediator_type _mediator ;
    first_module < mediator_type > _first_module ;
    second_module < mediator_type > _second_module ;
    controller < mediator_type > _controller ;
} ;
