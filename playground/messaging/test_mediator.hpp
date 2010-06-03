template 
    < typename mediator_types
    , class _messages
    > 
class test_mediator
{
public :
    typedef _messages messages ;
public :
    test_mediator ( )
    : _first_module ( 0 )
    , _second_module ( 0 )
    , _controller ( 0 )
    {
    }
    void register_modules
        ( typename mediator_types :: template modules < test_mediator > :: first_module * first_module
        , typename mediator_types :: template modules < test_mediator > :: second_module * second_module
        , typename mediator_types :: template modules < test_mediator > :: controller * controller
        )
    {
        _first_module = first_module ;
        _second_module = second_module ;
        _controller = controller ;
    }
    void send ( typename messages :: start msg )
    {
        _controller -> receive ( msg ) ;
    }
    void send ( typename messages :: activate_first_module msg )
    {
        _first_module -> receive ( msg ) ;
    }
    void send ( typename messages :: activate_second_module msg )
    {
        _second_module -> receive ( msg ) ;
    }
    void send ( typename messages :: on_some_event msg )
    {
        _first_module -> receive ( msg ) ;
        _second_module -> receive ( msg ) ;
    }
private :
    typename mediator_types :: template modules < test_mediator > :: first_module * _first_module ;
    typename mediator_types :: template modules < test_mediator > :: second_module * _second_module ;
    typename mediator_types :: template modules < test_mediator > :: controller * _controller ;
} ;
