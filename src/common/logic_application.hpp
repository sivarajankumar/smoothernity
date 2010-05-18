template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: int_32 int_32 ;
public :
    shy_logic_application ( mediator * arg_mediator ) ;
    void application_render ( ) ;
    void application_update ( ) ;
private :
    mediator * _mediator ;
    int_32 _application_launched ;
} ;

template < typename mediator >
shy_logic_application < mediator > :: shy_logic_application ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _application_launched ( false )
{
}

template < typename mediator >
void shy_logic_application < mediator > :: application_render ( )
{
    if ( _application_launched )
        _mediator -> game_render ( ) ;
    else
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: application_update ( )
{
    if ( ! _application_launched )
    {
        _application_launched = true ;
        _mediator -> game_launch_permit ( ) ;
    }
    else
        _mediator -> game_update ( ) ;
}
