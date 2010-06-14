template < typename mediator >
class shy_logic
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: num_fract num_fract ;
public :
    shy_logic ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: done msg ) ;
    void receive ( typename messages :: render msg ) ;
    void receive ( typename messages :: update msg ) ;
    void use_perspective_projection ( ) ;
    void receive ( typename messages :: use_ortho_projection msg ) ;
    void receive ( typename messages :: video_mode_changed msg ) ;
    void receive ( typename messages :: fidget_prepared msg ) ;
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
void shy_logic < mediator > :: receive ( typename messages :: init msg )
{
    _init_render ( ) ;
    _mediator -> send ( typename messages :: fidget_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: done msg )
{
    _mediator -> send ( typename messages :: entities_done ( ) ) ;
    _mediator -> send ( typename messages :: fidget_done ( ) ) ;
    _mediator -> send ( typename messages :: image_done ( ) ) ;
    _mediator -> send ( typename messages :: land_done ( ) ) ;
    _mediator -> send ( typename messages :: text_done ( ) ) ;
    _mediator -> send ( typename messages :: title_done ( ) ) ;
    _mediator -> send ( typename messages :: touch_done ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: render msg )
{
    _mediator -> send ( typename messages :: application_render ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: update msg )
{
    _mediator -> send ( typename messages :: application_update ( ) ) ;
    _mediator -> send ( typename messages :: fidget_update ( ) ) ;
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
void shy_logic < mediator > :: receive ( typename messages :: use_ortho_projection msg )
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
void shy_logic < mediator > :: receive ( typename messages :: fidget_prepared msg )
{
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: video_mode_changed msg )
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
