template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
public :
    shy_logic_application ( mediator * arg_mediator ) ;
    void application_render ( ) ;
    void application_update ( ) ;
private :
    mediator * _mediator ;
    num_whole _application_launched ;
} ;

template < typename mediator >
shy_logic_application < mediator > :: shy_logic_application ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _application_launched , false ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: application_render ( )
{
    if ( platform :: condition_true ( _application_launched ) )
        _mediator -> game_render ( ) ;
    else
    {
        num_fract black ;
        platform :: math_make_num_fract ( black , 0 , 1 ) ;
        platform :: render_clear_screen ( black , black , black ) ;
    }
}

template < typename mediator >
void shy_logic_application < mediator > :: application_update ( )
{
    if ( platform :: condition_false ( _application_launched ) )
    {
        platform :: math_make_num_whole ( _application_launched , true ) ;
        _mediator -> game_launch_permit ( ) ;
    }
    else
        _mediator -> game_update ( ) ;
}
