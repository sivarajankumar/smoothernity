template < typename mediator >
class shy_logic
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    
public :
    shy_logic ( mediator * arg_mediator ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void use_perspective_projection ( ) ;
    void use_ortho_projection ( ) ;
    void video_mode_changed ( ) ;
    void fidget_prepared ( ) ;
    void title_finished ( ) ;
    float_32 get_near_plane_distance ( ) ;
private :
    void _use_perspective_projection ( ) ;
    void _use_ortho_projection ( ) ;
    void _init_render ( ) ;
    float_32 _get_near_plane_distance ( ) ;
private :
    mediator * _mediator ;
} ;

template < typename mediator >
shy_logic < mediator > :: shy_logic ( mediator * arg_mediator )
: _mediator ( arg_mediator )
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
    _mediator -> application_render ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: update ( )
{
    _mediator -> application_update ( ) ;
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
    platform :: render_blend_disable ( ) ;
    platform :: render_enable_face_culling ( ) ;
    platform :: render_set_modulate_texture_mode ( ) ;
}

template < typename mediator >
typename shy_logic < mediator > :: float_32
shy_logic < mediator > :: _get_near_plane_distance ( )
{
    return platform :: render_get_aspect_width ( ) + platform :: render_get_aspect_height ( ) ;
}
