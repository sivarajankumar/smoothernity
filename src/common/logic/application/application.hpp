template < typename mediator >
class shy_logic_application
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_application_render ) ;
    void receive ( typename messages :: logic_application_update ) ;
    void receive ( typename messages :: logic_title_created ) ;
    void receive ( typename messages :: logic_title_finished ) ;
    void receive ( typename messages :: logic_text_prepared ) ;
    void receive ( typename messages :: logic_main_menu_created ) ;
    void receive ( typename messages :: logic_main_menu_finished ) ;
    void receive ( typename messages :: logic_amusement_finished ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    num_whole _application_launched ;
    num_whole _title_active ;
    num_whole _text_active ;
    num_whole _game_active ;
    num_whole _main_menu_render_active ;
    num_whole _main_menu_update_active ;
    num_whole _amusement_render_active ;
    num_whole _amusement_update_active ;
} ;

template < typename mediator >
void shy_logic_application < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _application_launched = _platform_math_consts . get ( ) . whole_false ;
    _title_active = _platform_math_consts . get ( ) . whole_false ;
    _game_active = _platform_math_consts . get ( ) . whole_false ;
    _text_active = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_render_active = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_update_active = _platform_math_consts . get ( ) . whole_false ;
    _amusement_render_active = _platform_math_consts . get ( ) . whole_false ;
    _amusement_update_active = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_text_prepared )
{
    _text_active = _platform_math_consts . get ( ) . whole_false ;
    _title_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_title_created )
{
    _main_menu_update_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_title_finished )
{
    _title_active = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_render_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_main_menu_created )
{
    _amusement_update_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_main_menu_finished )
{
    _main_menu_update_active = _platform_math_consts . get ( ) . whole_false ;
    _main_menu_render_active = _platform_math_consts . get ( ) . whole_false ;
    _amusement_render_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_amusement_finished )
{
    _amusement_update_active = _platform_math_consts . get ( ) . whole_false ;
    _amusement_render_active = _platform_math_consts . get ( ) . whole_false ;
    _game_active = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_application_render )
{
    if ( platform_conditions :: whole_is_false ( _application_launched ) )
    {
        typename messages :: engine_render_clear_screen clear_screen_msg ;
        clear_screen_msg . r = _platform_math_consts . get ( ) . fract_0 ;
        clear_screen_msg . g = _platform_math_consts . get ( ) . fract_0 ;
        clear_screen_msg . b = _platform_math_consts . get ( ) . fract_0 ;
        _mediator . get ( ) . send ( clear_screen_msg ) ;
    }
}

template < typename mediator >
void shy_logic_application < mediator > :: receive ( typename messages :: logic_application_update )
{
    if ( platform_conditions :: whole_is_false ( _application_launched ) )
    {
        _application_launched = _platform_math_consts . get ( ) . whole_true ;
        _text_active = _platform_math_consts . get ( ) . whole_true ;
    }
}
