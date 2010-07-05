template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: application_render msg ) ;
    void receive ( typename messages :: application_update msg ) ;
    void receive ( typename messages :: title_finished msg ) ;
    void receive ( typename messages :: text_prepared msg ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_whole _application_launched ;
    num_whole _title_active ;
    num_whole _text_active ;
    num_whole _game_active ;
} ;

template < typename mediator >
void shy_logic_application < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: init msg )
{
    platform_math :: make_num_whole ( _application_launched , false ) ;
    platform_math :: make_num_whole ( _title_active , false ) ;
    platform_math :: make_num_whole ( _game_active , false ) ;
    platform_math :: make_num_whole ( _text_active , false ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: text_prepared msg )
{
    platform_math :: make_num_whole ( _text_active , false ) ;
    platform_math :: make_num_whole ( _title_active , true ) ;
    _mediator . get ( ) . send ( typename messages :: title_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: title_finished msg )
{
    platform_math :: make_num_whole ( _title_active , false ) ;
    platform_math :: make_num_whole ( _game_active , true ) ;
    _mediator . get ( ) . send ( typename messages :: game_launch_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: application_render msg )
{
    if ( platform_conditions :: whole_is_true ( _game_active ) )
        _mediator . get ( ) . send ( typename messages :: game_render ( ) ) ;
    if ( platform_conditions :: whole_is_true ( _title_active ) )
        _mediator . get ( ) . send ( typename messages :: title_render ( ) ) ;
    if ( platform_conditions :: whole_is_false ( _application_launched ) )
    {
        typename messages :: render_clear_screen clear_screen_msg ;
        clear_screen_msg . r = platform :: math_consts . fract_0 ;
        clear_screen_msg . g = platform :: math_consts . fract_0 ;
        clear_screen_msg . b = platform :: math_consts . fract_0 ;
        _mediator . get ( ) . send ( clear_screen_msg ) ;
    }
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: application_update msg )
{
    if ( platform_conditions :: whole_is_false ( _application_launched ) )
    {
        platform_math :: make_num_whole ( _application_launched , true ) ;
        platform_math :: make_num_whole ( _text_active , true ) ;
        _mediator . get ( ) . send ( typename messages :: text_prepare_permit ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _text_active ) )
        _mediator . get ( ) . send ( typename messages :: text_update ( ) ) ;
    if ( platform_conditions :: whole_is_true ( _game_active ) )
        _mediator . get ( ) . send ( typename messages :: game_update ( ) ) ;
    if ( platform_conditions :: whole_is_true ( _title_active ) )
        _mediator . get ( ) . send ( typename messages :: title_update ( ) ) ;
}
