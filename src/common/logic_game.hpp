template < typename mediator >
class shy_logic_game
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
public :
    shy_logic_game ( mediator * arg_mediator ) ;
    void game_launch_permit ( ) ;
    void game_render ( ) ;
    void game_update ( ) ;
    void camera_prepared ( ) ;
    void entities_prepared ( ) ;
    void image_prepared ( ) ;
    void land_prepared ( ) ;
    void sound_prepared ( ) ;
    void text_prepared ( ) ;
    void touch_prepared ( ) ;
private :
    void _render_scene ( ) ;
    void _render_hud ( ) ;
    void _clear_screen ( ) ;
    void _update_color ( ) ;
private :
    mediator * _mediator ;
    float_32 _color_r ;
    float_32 _color_g ;
    float_32 _color_b ;
    int_32 _color_frames ;
    int_32 _game_launched ;
    int_32 _game_launch_permitted ;
} ;

template < typename mediator >
shy_logic_game < mediator > :: shy_logic_game ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _color_r ( 0 )
, _color_g ( 0 )
, _color_b ( 0 )
, _color_frames ( 0 )
, _game_launched ( false )
, _game_launch_permitted ( false )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: game_launch_permit ( )
{
    _game_launch_permitted = true ;
}

template < typename mediator >
void shy_logic_game < mediator > :: game_render ( )
{
    if ( _game_launched )
    {
        _clear_screen ( ) ;
        _render_scene ( ) ;
        _render_hud ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: game_update ( )
{
    if ( _game_launch_permitted )
    {
        if ( ! _game_launched )
        {
            _mediator -> camera_prepare_permit ( ) ;
            _game_launched = true ;
        }
    }
    if ( _game_launched )
    {
        _update_color ( ) ;
        _mediator -> camera_update ( ) ;
        _mediator -> entities_update ( ) ;
        _mediator -> fidget_update ( ) ;
        _mediator -> image_update ( ) ;
        _mediator -> land_update ( ) ;
        _mediator -> sound_update ( ) ;
        _mediator -> text_update ( ) ;
        _mediator -> touch_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: camera_prepared ( )
{
    _mediator -> land_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: land_prepared ( )
{
    _mediator -> entities_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: entities_prepared ( )
{
    _mediator -> text_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: text_prepared ( )
{
    _mediator -> image_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: image_prepared ( )
{
    _mediator -> touch_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: touch_prepared ( )
{
    _mediator -> sound_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: sound_prepared ( )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: _render_scene ( )
{
    platform :: render_enable_depth_test ( ) ;
    _mediator -> use_perspective_projection ( ) ;
    _mediator -> camera_matrix_use ( ) ;
    _mediator -> land_render ( ) ;
    _mediator -> entities_render ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _render_hud ( )
{
    platform :: render_disable_depth_test ( ) ;
    platform :: render_fog_disable ( ) ;
    _mediator -> use_ortho_projection ( ) ;
    _mediator -> fidget_render ( ) ;
    _mediator -> text_render ( ) ;
    _mediator -> image_render ( ) ;
    _mediator -> touch_render ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _clear_screen ( )
{
    platform :: render_fog_linear 
        ( 10 + _mediator -> get_near_plane_distance ( ) 
        , 20 + _mediator -> get_near_plane_distance ( ) 
        , _color_r 
        , _color_g 
        , _color_b 
        , 0 
        ) ;
    platform :: render_clear_screen ( _color_r , _color_g , _color_b ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _update_color ( )
{
    static const float_32 FINAL_R = 0.0f ;
    static const float_32 FINAL_G = 0.1f ;
    static const float_32 FINAL_B = 0.4f ;
    static const int_32 FADE_IN_FRAMES = 90 ;
    if ( _color_frames < FADE_IN_FRAMES )
        _color_frames ++ ;
    float_32 scale = float_32 ( _color_frames ) / float_32 ( FADE_IN_FRAMES ) ;
    _color_r = scale * FINAL_R ;
    _color_g = scale * FINAL_G ;
    _color_b = scale * FINAL_B ;
}
