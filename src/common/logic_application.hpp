template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
public :
    shy_logic_application ( ) ;
    void set_mediator ( typename platform :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: application_render msg ) ;
    void receive ( typename messages :: application_update msg ) ;
    void receive ( typename messages :: title_finished msg ) ;
    void receive ( typename messages :: text_prepared msg ) ;
private :
    typename platform :: template pointer < mediator > _mediator ;
    num_whole _application_launched ;
    num_whole _title_active ;
    num_whole _text_active ;
    num_whole _game_active ;
} ;

template < typename mediator >
shy_logic_application < mediator > :: shy_logic_application ( )
{
    platform :: math_make_num_whole ( _application_launched , false ) ;
    platform :: math_make_num_whole ( _title_active , false ) ;
    platform :: math_make_num_whole ( _game_active , false ) ;
    platform :: math_make_num_whole ( _text_active , false ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: set_mediator ( typename platform :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: text_prepared msg )
{
    platform :: math_make_num_whole ( _text_active , false ) ;
    platform :: math_make_num_whole ( _title_active , true ) ;
    _mediator . get ( ) . send ( typename messages :: title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: title_finished msg )
{
    platform :: math_make_num_whole ( _title_active , false ) ;
    platform :: math_make_num_whole ( _game_active , true ) ;
    _mediator . get ( ) . send ( typename messages :: game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: application_render msg )
{
    if ( platform :: condition_true ( _game_active ) )
        _mediator . get ( ) . send ( typename messages :: game_render ( ) ) ;
    if ( platform :: condition_true ( _title_active ) )
        _mediator . get ( ) . send ( typename messages :: title_render ( ) ) ;
    if ( platform :: condition_false ( _application_launched ) )
    {
        num_fract black ;
        platform :: math_make_num_fract ( black , 0 , 1 ) ;
        platform :: render_clear_screen ( black , black , black ) ;
    }
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: application_update msg )
{
    if ( platform :: condition_false ( _application_launched ) )
    {
        platform :: math_make_num_whole ( _application_launched , true ) ;
        platform :: math_make_num_whole ( _text_active , true ) ;
        _mediator . get ( ) . send ( typename messages :: text_prepare_permit ( ) ) ;
    }
    if ( platform :: condition_true ( _text_active ) )
        _mediator . get ( ) . send ( typename messages :: text_update ( ) ) ;
    if ( platform :: condition_true ( _game_active ) )
        _mediator . get ( ) . send ( typename messages :: game_update ( ) ) ;
    if ( platform :: condition_true ( _title_active ) )
        _mediator . get ( ) . send ( typename messages :: title_update ( ) ) ;
}
