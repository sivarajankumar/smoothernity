template < typename mediator >
class shy_logic
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
public :
    shy_logic ( mediator * arg_mediator ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void use_perspective_projection ( ) ;
    void use_ortho_projection ( ) ;
    void video_mode_changed ( ) ;
    void camera_prepared ( ) ;
    void entities_prepared ( ) ;
    void fidget_prepared ( ) ;
    void image_prepared ( ) ;
    void land_prepared ( ) ;
    void sound_prepared ( ) ;
    void text_prepared ( ) ;
    void touch_prepared ( ) ;
    void title_finished ( ) ;
    float_32 get_near_plane_distance ( ) ;
private :
    void _render_scene ( ) ;
    void _render_hud ( ) ;
    void _use_perspective_projection ( ) ;
    void _use_ortho_projection ( ) ;
    void _init_render ( ) ;
    void _clear_screen ( ) ;
    float_32 _get_near_plane_distance ( ) ;
    void _update_color ( ) ;
private :
    mediator * _mediator ;
    float_32 _color_r ;
    float_32 _color_g ;
    float_32 _color_b ;
    int_32 _color_frames ;
} ;

template < typename mediator >
shy_logic < mediator > :: shy_logic ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _color_r ( 0 )
, _color_g ( 0 )
, _color_b ( 0 )
, _color_frames ( 0 )
{
}

template < typename mediator >
void shy_logic < mediator > :: init ( )
{
    _init_render ( ) ;
    _mediator -> fidget_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: done ( )
{
}

template < typename mediator >
void shy_logic < mediator > :: render ( )
{
    _clear_screen ( ) ;
    _render_scene ( ) ;
    _render_hud ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: update ( )
{
    _update_color ( ) ;
    _mediator -> camera_update ( ) ;
    _mediator -> entities_update ( ) ;
    _mediator -> fidget_update ( ) ;
    _mediator -> image_update ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: use_perspective_projection ( )
{
    _use_perspective_projection ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: use_ortho_projection ( )
{
    _use_ortho_projection ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: fidget_prepared ( )
{
    _mediator -> camera_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: camera_prepared ( )
{
    _mediator -> prepare_land ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: land_prepared ( )
{
    _mediator -> entities_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: entities_prepared ( )
{
    _mediator -> prepare_text ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: text_prepared ( )
{
    _mediator -> image_prepare_permit ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: image_prepared ( )
{
    _mediator -> prepare_touch ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: touch_prepared ( )
{
    _mediator -> prepare_sound ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: sound_prepared ( )
{
}

template < typename mediator >
void shy_logic < mediator > :: title_finished ( )
{
}

template < typename mediator >
void shy_logic < mediator > :: video_mode_changed ( )
{
    _init_render ( ) ;
}

template < typename mediator >
typename shy_logic < mediator > :: float_32
shy_logic < mediator > :: get_near_plane_distance ( )
{
    return _get_near_plane_distance ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _render_scene ( )
{
    platform :: render_enable_depth_test ( ) ;
    _use_perspective_projection ( ) ;
    _mediator -> camera_matrix_use ( ) ;
    _mediator -> render_land ( ) ;
    _mediator -> entities_render ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _render_hud ( )
{
    platform :: render_disable_depth_test ( ) ;
    platform :: render_fog_disable ( ) ;
    _use_ortho_projection ( ) ;
    _mediator -> fidget_render ( ) ;
    _mediator -> render_text ( ) ;
    _mediator -> image_render ( ) ;
    _mediator -> render_touch ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _use_perspective_projection ( )
{
    float_32 width = platform :: render_get_aspect_width ( ) ;
    float_32 height = platform :: render_get_aspect_height ( ) ;
    platform :: render_projection_frustum ( - width , width , - height , height , _get_near_plane_distance ( ) , 50.0f ) ;
    platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _use_ortho_projection ( )
{
    float_32 width = platform :: render_get_aspect_width ( ) ;
    float_32 height = platform :: render_get_aspect_height ( ) ;
    platform :: render_projection_ortho ( - width , width , - height , height , 1.0f , 50.0f ) ;
    platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _init_render ( )
{
    platform :: render_enable_face_culling ( ) ;
    platform :: render_set_modulate_texture_mode ( ) ;
    platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _clear_screen ( )
{
    platform :: render_fog_linear 
        ( 10 + _get_near_plane_distance ( ) 
        , 20 + _get_near_plane_distance ( ) 
        , _color_r 
        , _color_g 
        , _color_b 
        , 0 
        ) ;
    platform :: render_clear_screen ( _color_r , _color_g , _color_b ) ;
}

template < typename mediator >
typename shy_logic < mediator > :: float_32
shy_logic < mediator > :: _get_near_plane_distance ( )
{
    return platform :: render_get_aspect_width ( ) + platform :: render_get_aspect_height ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _update_color ( )
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
