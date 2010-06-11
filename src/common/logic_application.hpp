template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
public :
    shy_logic_application ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: application_render msg ) ;
    void application_update ( ) ;
    void title_finished ( ) ;
    void text_prepared ( ) ;
private :
    mediator * _mediator ;
    num_whole _application_launched ;
    num_whole _title_active ;
    num_whole _text_active ;
    num_whole _game_active ;
} ;

template < typename mediator >
shy_logic_application < mediator > :: shy_logic_application ( )
: _mediator ( 0 )
{
    platform :: math_make_num_whole ( _application_launched , false ) ;
    platform :: math_make_num_whole ( _title_active , false ) ;
    platform :: math_make_num_whole ( _game_active , false ) ;
    platform :: math_make_num_whole ( _text_active , false ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application < mediator > :: text_prepared ( )
{
    platform :: math_make_num_whole ( _text_active , false ) ;
    platform :: math_make_num_whole ( _title_active , true ) ;
    _mediator -> title_launch_permit ( ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: title_finished ( )
{
    platform :: math_make_num_whole ( _title_active , false ) ;
    platform :: math_make_num_whole ( _game_active , true ) ;
    _mediator -> game_launch_permit ( ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: application_render msg )
{
    if ( platform :: condition_true ( _game_active ) )
        _mediator -> game_render ( ) ;
    if ( platform :: condition_true ( _title_active ) )
        _mediator -> title_render ( ) ;
    if ( platform :: condition_false ( _application_launched ) )
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
        platform :: math_make_num_whole ( _text_active , true ) ;
        _mediator -> text_prepare_permit ( ) ;
    }
    if ( platform :: condition_true ( _text_active ) )
        _mediator -> text_update ( ) ;
    if ( platform :: condition_true ( _game_active ) )
        _mediator -> game_update ( ) ;
    if ( platform :: condition_true ( _title_active ) )
        _mediator -> title_update ( ) ;
}
