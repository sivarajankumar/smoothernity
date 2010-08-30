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
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
     
    class _logic_game_consts_type
    {
    public :
        _logic_game_consts_type ( ) ;
        num_fract final_r ;
        num_fract final_g ;
        num_fract final_b ;
        num_fract fog_far_shift ;
        num_fract fog_near_shift ;
        num_whole fade_in_frames ;
    } ;
    
public :
    shy_logic_game ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_game_launch_permit ) ;
    void receive ( typename messages :: logic_game_render ) ;
    void receive ( typename messages :: logic_game_update ) ;
    void receive ( typename messages :: logic_camera_prepared ) ;
    void receive ( typename messages :: logic_entities_prepared ) ;
    void receive ( typename messages :: logic_image_prepared ) ;
    void receive ( typename messages :: logic_land_prepared ) ;
    void receive ( typename messages :: logic_sound_prepared ) ;
    void receive ( typename messages :: logic_touch_prepared ) ;
    void receive ( typename messages :: logic_core_near_plane_distance_reply ) ;
    void receive ( typename messages :: logic_camera_matrix_reply ) ;
    void receive ( typename messages :: logic_core_use_perspective_projection_reply ) ;
    void receive ( typename messages :: logic_core_use_ortho_projection_reply ) ;
    void receive ( typename messages :: logic_land_render_reply ) ;
    void receive ( typename messages :: logic_entities_render_reply ) ;
    void receive ( typename messages :: logic_fidget_render_reply ) ;
    void receive ( typename messages :: logic_text_render_reply ) ;
    void receive ( typename messages :: logic_image_render_reply ) ;
private :
    shy_logic_game < mediator > & operator= ( const shy_logic_game < mediator > & ) ;
    void _clear_screen ( ) ;
    void _update_color ( ) ;
    void _proceed_with_render ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_game_consts_type _logic_game_consts ;
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
    num_whole _use_perspective_projection_replied ;

    num_whole _use_ortho_projection_requested ;
    num_whole _use_ortho_projection_replied ;
    
    num_whole _land_render_requested ;
    num_whole _land_render_replied ;
    
    num_whole _entities_render_requested ;
    num_whole _entities_render_replied ;
    
    num_whole _fidget_render_requested ;
    num_whole _fidget_render_replied ;
    
    num_whole _text_render_requested ;
    num_whole _text_render_replied ;

    num_whole _image_render_requested ;
    num_whole _image_render_replied ;
} ;

template < typename mediator >
shy_logic_game < mediator > :: shy_logic_game ( )
{
}

template < typename mediator >
shy_logic_game < mediator > :: _logic_game_consts_type :: _logic_game_consts_type ( )
{
    platform_math :: make_num_fract ( final_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( final_g , 1 , 10 ) ;
    platform_math :: make_num_fract ( final_b , 4 , 10 ) ;
    platform_math :: make_num_fract ( fog_far_shift , 20 , 1 ) ;
    platform_math :: make_num_fract ( fog_near_shift , 10 , 1 ) ;
    platform_math :: make_num_whole ( fade_in_frames , 90 ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _color_r = _platform_math_consts . get ( ) . fract_0 ;
    _color_g = _platform_math_consts . get ( ) . fract_0 ;
    _color_b = _platform_math_consts . get ( ) . fract_0 ;
    _color_frames = _platform_math_consts . get ( ) . whole_0 ;
    _game_launched = _platform_math_consts . get ( ) . whole_false ;
    _game_launch_permitted = _platform_math_consts . get ( ) . whole_false ;
    _near_plane_distance_requested = _platform_math_consts . get ( ) . whole_false ;
    _near_plane_distance_replied = _platform_math_consts . get ( ) . whole_false ;
    _camera_matrix_requested = _platform_math_consts . get ( ) . whole_false ;
    _camera_matrix_replied = _platform_math_consts . get ( ) . whole_false ;
    _use_perspective_projection_requested = _platform_math_consts . get ( ) . whole_false ;
    _use_perspective_projection_replied = _platform_math_consts . get ( ) . whole_false ;
    _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_false ;
    _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_false ;
    _land_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _land_render_replied = _platform_math_consts . get ( ) . whole_false ;
    _entities_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _entities_render_replied = _platform_math_consts . get ( ) . whole_false ;
    _fidget_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _fidget_render_replied = _platform_math_consts . get ( ) . whole_false ;
    _text_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _text_render_replied = _platform_math_consts . get ( ) . whole_false ;
    _image_render_requested = _platform_math_consts . get ( ) . whole_false ;
    _image_render_replied = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_game_launch_permit )
{
    _game_launch_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_game_render )
{
    if ( platform_conditions :: whole_is_true ( _game_launched ) )
    {
        _near_plane_distance_requested = _platform_math_consts . get ( ) . whole_true ;
        _camera_matrix_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_core_near_plane_distance_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_camera_matrix_request ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_core_near_plane_distance_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _near_plane_distance_requested ) )
    {
        _near_plane_distance_requested = _platform_math_consts . get ( ) . whole_false ;
        _near_plane_distance_replied = _platform_math_consts . get ( ) . whole_true ;
        _near_plane_distance = msg . distance ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_camera_matrix_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _camera_matrix_requested ) )
    {
        _camera_matrix_requested = _platform_math_consts . get ( ) . whole_false ;
        _camera_matrix_replied = _platform_math_consts . get ( ) . whole_true ;
        _camera_matrix = msg . matrix ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_game_update )
{
    if ( platform_conditions :: whole_is_true ( _game_launch_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _game_launched ) )
        {
            _mediator . get ( ) . send ( typename messages :: logic_camera_prepare_permit ( ) ) ;
            _game_launched = _platform_math_consts . get ( ) . whole_true ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _game_launched ) )
    {
        _update_color ( ) ;
        _mediator . get ( ) . send ( typename messages :: logic_camera_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_entities_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_land_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_image_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_sound_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_text_update ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_touch_update ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_camera_prepared )
{
    _mediator . get ( ) . send ( typename messages :: logic_land_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_land_prepared )
{
    _mediator . get ( ) . send ( typename messages :: logic_entities_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_entities_prepared )
{
    _mediator . get ( ) . send ( typename messages :: logic_image_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_image_prepared )
{
    _mediator . get ( ) . send ( typename messages :: logic_touch_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_touch_prepared )
{
    _mediator . get ( ) . send ( typename messages :: logic_sound_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_sound_prepared )
{
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_core_use_perspective_projection_reply )
{
    if ( platform_conditions :: whole_is_true ( _use_perspective_projection_requested ) )
    {
        _use_perspective_projection_requested = _platform_math_consts . get ( ) . whole_false ;
        _use_perspective_projection_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;        
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_land_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _land_render_requested ) )
    {
        _land_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _land_render_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_entities_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _entities_render_requested ) )
    {
        _entities_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _entities_render_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_core_use_ortho_projection_reply )
{
    if ( platform_conditions :: whole_is_true ( _use_ortho_projection_requested ) )
    {
        _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_false ;
        _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_fidget_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _fidget_render_requested ) )
    {
        _fidget_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _fidget_render_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_text_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _text_render_requested ) )
    {
        _text_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _text_render_replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: receive ( typename messages :: logic_image_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _image_render_requested ) )
    {
        _image_render_requested = _platform_math_consts . get ( ) . whole_false ;
        _image_render_replied = _platform_math_consts . get ( ) . whole_true ;
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
        _camera_matrix_replied = _platform_math_consts . get ( ) . whole_false ;
        _near_plane_distance_replied = _platform_math_consts . get ( ) . whole_false ;
        _clear_screen ( ) ;
        
        _use_perspective_projection_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_core_use_perspective_projection_request ( ) ) ;    
    }
    if ( platform_conditions :: whole_is_true ( _use_perspective_projection_replied ) )
    {
        _use_perspective_projection_replied = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: engine_render_enable_depth_test ( ) ) ;
        
        typename messages :: engine_render_matrix_load matrix_load_msg ;
        matrix_load_msg . matrix = _camera_matrix ;
        _mediator . get ( ) . send ( matrix_load_msg ) ;
        
        _land_render_requested = _platform_math_consts . get ( ) . whole_true ;
        _entities_render_requested = _platform_math_consts . get ( ) . whole_true ;
        
        _mediator . get ( ) . send ( typename messages :: logic_land_render_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_entities_render_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _land_render_replied )
      && platform_conditions :: whole_is_true ( _entities_render_replied )
       )
    {
        _land_render_replied = _platform_math_consts . get ( ) . whole_false ;
        _entities_render_replied = _platform_math_consts . get ( ) . whole_false ;
        
        _use_ortho_projection_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_core_use_ortho_projection_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _use_ortho_projection_replied ) )
    {
        _use_ortho_projection_replied = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: engine_render_disable_depth_test ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: engine_render_fog_disable ( ) ) ;
        
        _fidget_render_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_fidget_render_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _fidget_render_replied ) )
    {
        _fidget_render_replied = _platform_math_consts . get ( ) . whole_false ;
        _text_render_requested = _platform_math_consts . get ( ) . whole_true ;
        _image_render_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_text_render_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: logic_image_render_request ( ) ) ;
    }
    if ( platform_conditions :: whole_is_true ( _text_render_replied )
      && platform_conditions :: whole_is_true ( _image_render_replied )
       )
    {
        _text_render_replied = _platform_math_consts . get ( ) . whole_false ;
        _image_render_replied = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: logic_touch_render ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_game < mediator > :: _clear_screen ( )
{
    num_fract fog_a ;
    num_fract fog_far ;
    num_fract fog_near ;
    fog_a = _platform_math_consts . get ( ) . fract_0 ;
    platform_math :: add_fracts ( fog_far , _logic_game_consts . fog_far_shift , _near_plane_distance ) ;
    platform_math :: add_fracts ( fog_near , _logic_game_consts . fog_near_shift , _near_plane_distance ) ;
    
    typename messages :: engine_render_fog_linear fog_msg ;
    fog_msg . znear = fog_near ;
    fog_msg . zfar = fog_far ;
    fog_msg . r = _color_r ;
    fog_msg . g = _color_g ;
    fog_msg . b = _color_b ;
    fog_msg . a = fog_a ;
    _mediator . get ( ) . send ( fog_msg ) ;

    typename messages :: engine_render_clear_screen clear_screen_msg ;
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
    platform_math :: make_fract_from_whole ( fract_fade_in_frames , _logic_game_consts . fade_in_frames ) ;
    platform_math :: make_fract_from_whole ( fract_color_frames , _color_frames ) ;
    platform_math :: div_fracts ( scale , fract_color_frames , fract_fade_in_frames ) ;
    platform_math :: mul_fracts ( _color_r , scale , _logic_game_consts . final_r ) ;
    platform_math :: mul_fracts ( _color_g , scale , _logic_game_consts . final_g ) ;
    platform_math :: mul_fracts ( _color_b , scale , _logic_game_consts . final_b ) ;
    if ( platform_conditions :: whole_less_than_whole ( _color_frames , _logic_game_consts . fade_in_frames ) )
        platform_math :: inc_whole ( _color_frames ) ;
}
