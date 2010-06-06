template < typename mediator >
class shy_logic
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_fract num_fract ;
public :
    shy_logic ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void use_perspective_projection ( ) ;
    void use_ortho_projection ( ) ;
    void video_mode_changed ( ) ;
    void fidget_prepared ( ) ;
    void get_near_plane_distance ( num_fract & result ) ;
private :
    void _init_render ( ) ;
    void _get_near_plane_distance ( num_fract & result ) ;
private :
    mediator * _mediator ;
} ;

template < typename mediator >
shy_logic < mediator > :: shy_logic ( )
: _mediator ( 0 )
{
}

template < typename mediator >
void shy_logic < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
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
    _mediator -> entities_done ( ) ;
    _mediator -> fidget_done ( ) ;
    _mediator -> image_done ( ) ;
    _mediator -> land_done ( ) ;
    _mediator -> text_done ( ) ;
    _mediator -> title_done ( ) ;
    _mediator -> touch_done ( ) ;
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
    _mediator -> fidget_update ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: use_perspective_projection ( )
{
    num_fract width ;
    num_fract height ;
    num_fract neg_width ;
    num_fract neg_height ;
    num_fract z_far ;
    num_fract z_near ;
    _get_near_plane_distance ( z_near ) ;
    platform :: math_make_num_fract ( z_far , 50 , 1 ) ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_neg_fract ( neg_width , width ) ;
    platform :: math_neg_fract ( neg_height , height ) ;
    platform :: render_projection_frustum ( neg_width , width , neg_height , height , z_near , z_far ) ;
    platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: use_ortho_projection ( )
{
    num_fract width ;
    num_fract height ;
    num_fract neg_width ;
    num_fract neg_height ;
    num_fract z_far ;
    num_fract z_near ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_neg_fract ( neg_width , width ) ;
    platform :: math_neg_fract ( neg_height , height ) ;
    platform :: math_make_num_fract ( z_near , 1 , 1 ) ;
    platform :: math_make_num_fract ( z_far , 50 , 1 ) ;
    platform :: render_projection_ortho ( neg_width , width , neg_height , height , z_near , z_far ) ;
    platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: fidget_prepared ( )
{
}

template < typename mediator >
void shy_logic < mediator > :: video_mode_changed ( )
{
    _init_render ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: get_near_plane_distance ( num_fract & result )
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
void shy_logic < mediator > :: _get_near_plane_distance ( num_fract & result )
{
    num_fract width ;
    num_fract height ;
    platform :: render_get_aspect_width ( width ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_add_fracts ( result , width , height ) ;
}
