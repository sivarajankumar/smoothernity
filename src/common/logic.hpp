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
    shy_logic ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _color_r ( 0 )
    , _color_g ( 0 )
    , _color_b ( 0 )
    , _color_frames ( 0 )
    {
    }
    void init ( )
    {
        _init_render ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        _clear_screen ( ) ;
        _render_scene ( ) ;
        _render_hud ( ) ;
    }
    void update ( )
    {
        _update_color ( ) ;
    }
    float_32 get_near_plane_distance ( )
    {
        return _get_near_plane_distance ( ) ;
    }
private :
    void _render_scene ( )
    {
        platform :: render_enable_depth_test ( ) ;
        _use_perspective_projection ( ) ;
        _mediator -> use_camera_matrix ( ) ;
        _mediator -> render_land ( ) ;
        _mediator -> render_entities ( ) ;
    }
    void _render_hud ( )
    {
        platform :: render_disable_depth_test ( ) ;
        platform :: render_fog_disable ( ) ;
        _use_ortho_projection ( ) ;
        _mediator -> render_text ( ) ;
        _mediator -> render_touch ( ) ;
        _mediator -> render_fidget ( ) ;
    }
    void _use_perspective_projection ( )
    {
		float_32 width = platform :: render_get_aspect_width ( ) ;
		float_32 height = platform :: render_get_aspect_height ( ) ;
        platform :: render_projection_frustum ( - width , width , - height , height , _get_near_plane_distance ( ) , 50.0f ) ;
        platform :: render_matrix_identity ( ) ;
    }
    void _use_ortho_projection ( )
    {
		float_32 width = platform :: render_get_aspect_width ( ) ;
		float_32 height = platform :: render_get_aspect_height ( ) ;
        platform :: render_projection_ortho ( - width , width , - height , height , 1.0f , 50.0f ) ;
        platform :: render_matrix_identity ( ) ;
    }
    void _init_render ( )
    {
        platform :: render_enable_face_culling ( ) ;
		platform :: render_set_modulate_texture_mode ( ) ;
        platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    }
    void _clear_screen ( )
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
    float_32 _get_near_plane_distance ( )
    {
        return platform :: render_get_aspect_width ( ) + platform :: render_get_aspect_height ( ) ;
    }
    void _update_color ( )
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
private :
    mediator * _mediator ;
    float_32 _color_r ;
    float_32 _color_g ;
    float_32 _color_b ;
    int_32 _color_frames ;
} ;
