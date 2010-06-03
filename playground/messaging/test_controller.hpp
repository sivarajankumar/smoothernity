template < typename mediator >
class test_controller
{
public :
    typedef typename mediator :: messages messages ;
public :
    test_controller ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    {
    }
    void receive ( typename messages :: start msg )
    {
        _mediator -> send ( typename messages :: activate_first_module ( ) ) ;
    }
private :
    mediator * _mediator ;
} ;
