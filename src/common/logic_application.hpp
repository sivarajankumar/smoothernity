template < typename mediator >
class shy_logic_application
{
public :
    shy_logic_application ( mediator * arg_mediator ) ;
    void application_render ( ) ;
    void application_update ( ) ;
private :
    mediator * _mediator ;
} ;

template < typename mediator >
shy_logic_application < mediator > :: shy_logic_application ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
}

template < typename mediator >
void shy_logic_application < mediator > :: application_render ( )
{
}

template < typename mediator >
void shy_logic_application < mediator > :: application_update ( )
{
}
