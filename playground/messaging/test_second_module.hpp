template < typename mediator >
class test_second_module
{
public :
    typedef typename mediator :: messages messages ;
public :
    test_second_module ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _awake ( false )
    {
    }
    void receive ( typename messages :: activate_second_module msg )
    {
        _awake = true ;
    }
    void receive ( typename messages :: on_some_event msg )
    {
        if ( _awake )
        {
            printf ( "second module received event (arg=%i)\n" , msg . arg ) ;
            _awake = false ;
            _mediator -> send ( typename messages :: activate_first_module ( ) ) ;
        }
    }
private :
    mediator * _mediator ;
    bool _awake ;
} ;
