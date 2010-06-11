template < typename mediator >
class shy_logic_game
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    
    static const_int_32 _fade_in_frames = 90 ;
    static const num_fract _final_r ( ) { num_fract n ; platform :: math_make_num_fract ( n , 0 , 1 ) ; return n ; }
    static const num_fract _final_g ( ) { num_fract n ; platform :: math_make_num_fract ( n , 1 , 10 ) ; return n ; }
    static const num_fract _final_b ( ) { num_fract n ; platform :: math_make_num_fract ( n , 4 , 10 ) ; return n ; }
public :
    shy_logic_game ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: game_launch_permit msg ) ;
    void receive ( typename messages :: game_render msg ) ;
    void receive ( typename messages :: game_update msg ) ;
    void receive ( typename messages :: camera_prepared msg ) ;
    void receive ( typename messages :: entities_prepared msg ) ;
    void receive ( typename messages :: image_prepared msg ) ;
    void receive ( typename messages :: land_prepared msg ) ;
    void sound_prepared ( ) ;
    void touch_prepared ( ) ;
private :
    void _render_scene ( ) ;
    void _render_hud ( ) ;
    void _clear_screen ( ) ;
    void _update_color ( ) ;
private :
    mediator * _mediator ;
    num_fract _color_r ;
    num_fract _color_g ;
    num_fract _color_b ;
    num_whole _color_frames ;
    num_whole _game_launched ;
    num_whole _game_launch_permitted ;
} ;

template < typename mediator >
shy_logic_game < mediator > :: shy_logic_game ( )
: _mediator ( 0 )
{
    platform :: math_make_num_fract ( _color_r , 0 , 1 ) ;
    platform :: math_make_num_fract ( _color_g , 0 , 1 ) ;
    platform :: math_make_num_fract ( _color_b , 0 , 1 ) ;
    platform :: math_make_num_whole ( _color_frames , 0 ) ;
    platform :: math_make_num_whole ( _game_launched , false ) ;
    platform :: math_make_num_whole ( _game_launch_permitted , false ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_launch_permit msg )
{
    platform :: math_make_num_whole ( _game_launch_permitted , true ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_render msg )
{
    if ( platform :: condition_true ( _game_launched ) )
    {
        _clear_screen ( ) ;
        _render_scene ( ) ;
        _render_hud ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_update msg )
{
    if ( platform :: condition_true ( _game_launch_permitted ) )
    {
        if ( platform :: condition_false ( _game_launched ) )
        {
            _mediator -> send ( typename messages :: camera_prepare_permit ( ) ) ;
            platform :: math_make_num_whole ( _game_launched , true ) ;
        }
    }
    if ( platform :: condition_true ( _game_launched ) )
    {
        _update_color ( ) ;
        _mediator -> send ( typename messages :: camera_update ( ) ) ;
        _mediator -> send ( typename messages :: entities_update ( ) ) ;
        _mediator -> land_update ( ) ;
        _mediator -> send ( typename messages :: image_update ( ) ) ;
        _mediator -> sound_update ( ) ;
        _mediator -> text_update ( ) ;
        _mediator -> touch_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: camera_prepared msg )
{
    _mediator -> send ( typename messages :: land_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: land_prepared msg )
{
    _mediator -> send ( typename messages :: entities_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: entities_prepared msg )
{
    _mediator -> send ( typename messages :: image_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: image_prepared msg )
{
    _mediator -> touch_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: touch_prepared ( )
{
    _mediator -> send ( typename messages :: sound_prepare_permit ( ) ) ;
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
    _mediator -> send ( typename messages :: camera_matrix_use ( ) ) ;
    _mediator -> send ( typename messages :: land_render ( ) ) ;
    _mediator -> send ( typename messages :: entities_render ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _render_hud ( )
{
    platform :: render_disable_depth_test ( ) ;
    platform :: render_fog_disable ( ) ;
    _mediator -> use_ortho_projection ( ) ;
    _mediator -> send ( typename messages :: fidget_render ( ) ) ;
    _mediator -> text_render ( ) ;
    _mediator -> send ( typename messages :: image_render ( ) ) ;
    _mediator -> touch_render ( ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _clear_screen ( )
{
    num_fract fog_a ;
    num_fract fog_far ;
    num_fract fog_near ;
    num_fract near_plane ;
    num_fract fog_far_shift ;
    num_fract fog_near_shift ;
    _mediator -> get_near_plane_distance ( near_plane ) ;
    platform :: math_make_num_fract ( fog_a , 0 , 1 ) ;
    platform :: math_make_num_fract ( fog_far_shift , 20 , 1 ) ;
    platform :: math_make_num_fract ( fog_near_shift , 10 , 1 ) ;
    platform :: math_add_fracts ( fog_far , fog_far_shift , near_plane ) ;
    platform :: math_add_fracts ( fog_near , fog_near_shift , near_plane ) ;
    platform :: render_fog_linear ( fog_near , fog_far , _color_r , _color_g , _color_b , fog_a ) ;
    platform :: render_clear_screen ( _color_r , _color_g , _color_b ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _update_color ( )
{
    num_fract scale ;
    num_fract fract_color_frames ;
    num_fract fract_fade_in_frames ;
    num_whole whole_fade_in_frames ;
    platform :: math_make_num_whole ( whole_fade_in_frames , _fade_in_frames ) ;
    platform :: math_make_num_fract ( fract_fade_in_frames , _fade_in_frames , 1 ) ;
    platform :: math_make_fract_from_whole ( fract_color_frames , _color_frames ) ;
    platform :: math_div_fracts ( scale , fract_color_frames , fract_fade_in_frames ) ;
    platform :: math_mul_fracts ( _color_r , scale , _final_r ( ) ) ;
    platform :: math_mul_fracts ( _color_g , scale , _final_g ( ) ) ;
    platform :: math_mul_fracts ( _color_b , scale , _final_b ( ) ) ;
    if ( platform :: condition_whole_less_than_whole ( _color_frames , whole_fade_in_frames ) )
        platform :: math_inc_whole ( _color_frames ) ;
}
