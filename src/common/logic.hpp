template < typename mediator >
class shy_logic
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: num_fract num_fract ;
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
    void get_near_plane_distance ( float_32 & result ) ;
private :
    void _init_render ( ) ;
    void _get_near_plane_distance ( float_32 & result ) ;
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
    float_32 width ;
    float_32 height ;
    float_32 near_plane ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract x_left ;
    num_fract x_right ;
    num_fract z_far ;
    num_fract z_near ;
    _get_near_plane_distance ( near_plane ) ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_make_num_fract ( x_left , int_32 ( - width * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( x_right , int_32 ( width * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( y_bottom , int_32 ( - height * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( y_top , int_32 ( height * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( z_near , int_32 ( near_plane * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( z_far , 50 , 1 ) ;
    platform :: render_projection_frustum ( x_left , x_right , y_bottom , y_top , z_near , z_far ) ;
    platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: use_ortho_projection ( )
{
    float_32 width ;
    float_32 height ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract x_left ;
    num_fract x_right ;
    num_fract z_far ;
    num_fract z_near ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_make_num_fract ( x_left , int_32 ( - width * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( x_right , int_32 ( width * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( y_bottom , int_32 ( - height * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( y_top , int_32 ( height * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( z_near , 1 , 1 ) ;
    platform :: math_make_num_fract ( z_far , 50 , 1 ) ;
    platform :: render_projection_ortho ( x_left , x_right , y_bottom , y_top , z_near , z_far ) ;
    platform :: render_matrix_identity ( ) ;
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
void shy_logic < mediator > :: get_near_plane_distance ( float_32 & result )
{
    _get_near_plane_distance ( result ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _init_render ( )
{
    platform :: render_blend_disable ( ) ;
    platform :: render_enable_face_culling ( ) ;
    platform :: render_set_modulate_texture_mode ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _get_near_plane_distance ( float_32 & result )
{
    float_32 width ;
    float_32 height ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    result = width + height ;
}
