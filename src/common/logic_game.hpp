template < typename mediator >
class shy_logic_game
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    static const_int_32 _fade_in_frames = 90 ;
    static const num_fract _final_r ( ) { num_fract n ; platform_math :: make_num_fract ( n , 0 , 1 ) ; return n ; }
    static const num_fract _final_g ( ) { num_fract n ; platform_math :: make_num_fract ( n , 1 , 10 ) ; return n ; }
    static const num_fract _final_b ( ) { num_fract n ; platform_math :: make_num_fract ( n , 4 , 10 ) ; return n ; }
public :
    shy_logic_game ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: game_launch_permit msg ) ;
    void receive ( typename messages :: game_render msg ) ;
    void receive ( typename messages :: game_update msg ) ;
    void receive ( typename messages :: camera_prepared msg ) ;
    void receive ( typename messages :: entities_prepared msg ) ;
    void receive ( typename messages :: image_prepared msg ) ;
    void receive ( typename messages :: land_prepared msg ) ;
    void receive ( typename messages :: sound_prepared msg ) ;
    void receive ( typename messages :: touch_prepared msg ) ;
    void receive ( typename messages :: near_plane_distance_reply msg ) ;
    void receive ( typename messages :: camera_matrix_reply msg ) ;
    void receive ( typename messages :: use_perspective_projection_reply msg ) ;
private :
    void _render_scene ( ) ;
    void _render_hud ( ) ;
    void _clear_screen ( ) ;
    void _update_color ( ) ;
    void _proceed_with_render ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_fract _color_r ;
    num_fract _color_g ;
    num_fract _color_b ;
    num_whole _color_frames ;
    num_whole _game_launched ;
    num_whole _game_launch_permitted ;
    
    num_whole _near_plane_distance_requested ;
    num_whole _near_plane_distance_replied ;
    num_fract _near_plane_distance ;
    
    num_whole _camera_matrix_requested ;
    num_whole _camera_matrix_replied ;
    matrix_data _camera_matrix ;
    
    num_whole _use_perspective_projection_requested ;
} ;

template < typename mediator >
shy_logic_game < mediator > :: shy_logic_game ( )
{
    _color_r = platform :: math_consts . fract_0 ;
    _color_g = platform :: math_consts . fract_0 ;
    _color_b = platform :: math_consts . fract_0 ;
    _color_frames = platform :: math_consts . whole_0 ;
    _game_launched = platform :: math_consts . whole_false ;
    _game_launch_permitted = platform :: math_consts . whole_false ;
    _near_plane_distance_requested = platform :: math_consts . whole_false ;
    _near_plane_distance_replied = platform :: math_consts . whole_false ;
    _camera_matrix_requested = platform :: math_consts . whole_false ;
    _camera_matrix_replied = platform :: math_consts . whole_false ;
    _use_perspective_projection_requested = platform :: math_consts . whole_false ;
}

template < typename mediator >
void shy_logic_game < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_launch_permit msg )
{
    platform_math :: make_num_whole ( _game_launch_permitted , true ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_render msg )
{
    if ( platform_conditions :: whole_is_true ( _game_launched ) )
    {
        _near_plane_distance_requested = platform :: math_consts . whole_true ;
        _camera_matrix_requested = platform :: math_consts . whole_true ;
        _mediator . get ( ) . send ( typename messages :: near_plane_distance_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: camera_matrix_request ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: near_plane_distance_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _near_plane_distance_requested ) )
    {
        _near_plane_distance_requested = platform :: math_consts . whole_false ;
        _near_plane_distance_replied = platform :: math_consts . whole_true ;
        _near_plane_distance = msg . distance ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: camera_matrix_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _camera_matrix_requested ) )
    {
        _camera_matrix_requested = platform :: math_consts . whole_false ;
        _camera_matrix_replied = platform :: math_consts . whole_true ;
        _camera_matrix = msg . matrix ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _camera_matrix_replied )
      && platform_conditions :: whole_is_true ( _near_plane_distance_replied )
       )
    {
        _camera_matrix_replied = platform :: math_consts . whole_false ;
        _near_plane_distance_replied = platform :: math_consts . whole_false ;
        _clear_screen ( ) ;
        _render_scene ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: game_update msg )
{
    if ( platform_conditions :: whole_is_true ( _game_launch_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _game_launched ) )
        {
            _mediator . get ( ) . send ( typename messages :: camera_prepare_permit ( ) ) ;
            platform_math :: make_num_whole ( _game_launched , true ) ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _game_launched ) )
    {
        _update_color ( ) ;
        _mediator . get ( ) . send ( typename messages :: camera_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: entities_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: land_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: image_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: sound_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: text_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: touch_update ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: camera_prepared msg )
{
    _mediator . get ( ) . send ( typename messages :: land_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: land_prepared msg )
{
    _mediator . get ( ) . send ( typename messages :: entities_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: entities_prepared msg )
{
    _mediator . get ( ) . send ( typename messages :: image_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: image_prepared msg )
{
    _mediator . get ( ) . send ( typename messages :: touch_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: touch_prepared msg )
{
    _mediator . get ( ) . send ( typename messages :: sound_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: sound_prepared msg )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: use_perspective_projection_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _use_perspective_projection_requested ) )
    {
        _use_perspective_projection_requested = platform :: math_consts . whole_false ;
        
        _mediator . get ( ) . send ( typename messages :: render_enable_depth_test ( ) ) ;
        
        typename messages :: render_matrix_load matrix_load_msg ;
        matrix_load_msg . matrix = _camera_matrix ;
        _mediator . get ( ) . send ( matrix_load_msg ) ;
        
        _mediator . get ( ) . send ( typename messages :: land_render ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: entities_render ( ) ) ;
        
        _render_hud ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: _render_scene ( )
{
    _use_perspective_projection_requested = platform :: math_consts . whole_true ;
    _mediator . get ( ) . send ( typename messages :: use_perspective_projection_request ( ) ) ;    
}

template < typename mediator >
void shy_logic_game < mediator > :: _render_hud ( )
{
    _mediator . get ( ) . send ( typename messages :: render_disable_depth_test ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: render_fog_disable ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: use_ortho_projection ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_render ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: text_render ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: image_render ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: touch_render ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _clear_screen ( )
{
    num_fract fog_a ;
    num_fract fog_far ;
    num_fract fog_near ;
    num_fract fog_far_shift ;
    num_fract fog_near_shift ;
    platform_math :: make_num_fract ( fog_a , 0 , 1 ) ;
    platform_math :: make_num_fract ( fog_far_shift , 20 , 1 ) ;
    platform_math :: make_num_fract ( fog_near_shift , 10 , 1 ) ;
    platform_math :: add_fracts ( fog_far , fog_far_shift , _near_plane_distance ) ;
    platform_math :: add_fracts ( fog_near , fog_near_shift , _near_plane_distance ) ;
    
    typename messages :: render_fog_linear fog_msg ;
    fog_msg . near = fog_near ;
    fog_msg . far = fog_far ;
    fog_msg . r = _color_r ;
    fog_msg . g = _color_g ;
    fog_msg . b = _color_b ;
    fog_msg . a = fog_a ;
    _mediator . get ( ) . send ( fog_msg ) ;

    typename messages :: render_clear_screen clear_screen_msg ;
    clear_screen_msg . r = _color_r ;
    clear_screen_msg . g = _color_g ;
    clear_screen_msg . b = _color_b ;
    _mediator . get ( ) . send ( clear_screen_msg ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: _update_color ( )
{
    num_fract scale ;
    num_fract fract_color_frames ;
    num_fract fract_fade_in_frames ;
    num_whole whole_fade_in_frames ;
    platform_math :: make_num_whole ( whole_fade_in_frames , _fade_in_frames ) ;
    platform_math :: make_num_fract ( fract_fade_in_frames , _fade_in_frames , 1 ) ;
    platform_math :: make_fract_from_whole ( fract_color_frames , _color_frames ) ;
    platform_math :: div_fracts ( scale , fract_color_frames , fract_fade_in_frames ) ;
    platform_math :: mul_fracts ( _color_r , scale , _final_r ( ) ) ;
    platform_math :: mul_fracts ( _color_g , scale , _final_g ( ) ) ;
    platform_math :: mul_fracts ( _color_b , scale , _final_b ( ) ) ;
    if ( platform_conditions :: whole_less_than_whole ( _color_frames , whole_fade_in_frames ) )
        platform_math :: inc_whole ( _color_frames ) ;
}
