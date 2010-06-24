template < typename mediator >
class shy_logic
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
public :
    shy_logic ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: done msg ) ;
    void receive ( typename messages :: render msg ) ;
    void receive ( typename messages :: update msg ) ;
    void receive ( typename messages :: use_perspective_projection msg ) ;
    void receive ( typename messages :: use_ortho_projection msg ) ;
    void receive ( typename messages :: video_mode_changed msg ) ;
    void receive ( typename messages :: fidget_prepared msg ) ;
    void receive ( typename messages :: near_plane_distance_request msg ) ;
private :
    void _init_render ( ) ;
    void _get_near_plane_distance ( num_fract & result ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
} ;

template < typename mediator >
shy_logic < mediator > :: shy_logic ( )
{
}

template < typename mediator >
void shy_logic < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: init msg )
{
    _init_render ( ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_prepare_permit ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: done msg )
{
    _mediator . get ( ) . send ( typename messages :: entities_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: image_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: land_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: text_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: title_done ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: touch_done ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: render msg )
{
    _mediator . get ( ) . send ( typename messages :: application_render ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: update msg )
{
    _mediator . get ( ) . send ( typename messages :: application_update ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_update ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: use_perspective_projection msg )
{
    num_fract width ;
    num_fract height ;
    num_fract neg_width ;
    num_fract neg_height ;
    num_fract z_far ;
    num_fract z_near ;
    _get_near_plane_distance ( z_near ) ;
    platform_math :: make_num_fract ( z_far , 50 , 1 ) ;
    platform_render :: get_aspect_width ( width ) ;
    platform_render :: get_aspect_height ( height ) ;
    platform_math :: neg_fract ( neg_width , width ) ;
    platform_math :: neg_fract ( neg_height , height ) ;
    
    typename messages :: render_projection_frustum proj_msg ;
    proj_msg . left = neg_width ;
    proj_msg . right = width ;
    proj_msg . bottom = neg_height ;
    proj_msg . top = height ;
    proj_msg . near = z_near ;
    proj_msg . far = z_far ;
    _mediator . get ( ) . send ( proj_msg ) ;
    
    _mediator . get ( ) . send ( typename messages :: render_matrix_identity ( ) ) ;
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
    platform_render :: get_aspect_width ( width ) ;
    platform_render :: get_aspect_height ( height ) ;
    platform_math :: neg_fract ( neg_width , width ) ;
    platform_math :: neg_fract ( neg_height , height ) ;
    platform_math :: make_num_fract ( z_near , 1 , 1 ) ;
    platform_math :: make_num_fract ( z_far , 50 , 1 ) ;
    
    typename messages :: render_projection_ortho proj_msg ;
    proj_msg . left = neg_width ;
    proj_msg . right = width ;
    proj_msg . bottom = neg_height ;
    proj_msg . top = height ;
    proj_msg . near = z_near ;
    proj_msg . far = z_far ;
    _mediator . get ( ) . send ( proj_msg ) ;
    
    _mediator . get ( ) . send ( typename messages :: render_matrix_identity ( ) ) ;
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
void shy_logic < mediator > :: receive ( typename messages :: near_plane_distance_request msg )
{
    typename messages :: near_plane_distance_reply near_plane_distance_reply_msg ;
    _get_near_plane_distance ( near_plane_distance_reply_msg . distance ) ;
    _mediator . get ( ) . send ( near_plane_distance_reply_msg ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _init_render ( )
{
    _mediator . get ( ) . send ( typename messages :: render_blend_disable ( ) ) ;
    platform_render :: enable_face_culling ( ) ;
    platform_render :: set_modulate_texture_mode ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _get_near_plane_distance ( num_fract & result )
{
    num_fract width ;
    num_fract height ;
    platform_render :: get_aspect_width ( width ) ;
    platform_render :: get_aspect_height ( height ) ;
    platform_math :: add_fracts ( result , width , height ) ;
}
