template < typename mediator >
class shy_logic
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: done msg ) ;
    void receive ( typename messages :: render msg ) ;
    void receive ( typename messages :: update msg ) ;
    void receive ( typename messages :: use_perspective_projection_request msg ) ;
    void receive ( typename messages :: use_ortho_projection_request msg ) ;
    void receive ( typename messages :: video_mode_changed msg ) ;
    void receive ( typename messages :: fidget_prepared msg ) ;
    void receive ( typename messages :: near_plane_distance_request msg ) ;
    void receive ( typename messages :: render_aspect_reply msg ) ;
private :
    void _init_render ( ) ;
    void _get_near_plane_distance ( num_fract & result ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    num_whole _fidget_prepared ;
    
    num_whole _render_aspect_requested ;
    num_fract _render_aspect_width ;
    num_fract _render_aspect_height ;
    
    num_whole _handling_near_plane_distance_request ;
    num_whole _handling_use_ortho_projection_request ;
    num_whole _handling_use_perspective_projection_request ;
} ;

template < typename mediator >
void shy_logic < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: init msg )
{
    _platform_math_consts = _mediator . get ( ) . platform_obj ( ) . math_consts_ptr ;
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
    _handling_near_plane_distance_request = _platform_math_consts . get ( ) . whole_false ;
    _handling_use_ortho_projection_request = _platform_math_consts . get ( ) . whole_false ;
    _handling_use_perspective_projection_request = _platform_math_consts . get ( ) . whole_false ;
    _fidget_prepared = _platform_math_consts . get ( ) . whole_false ;
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
    if ( platform_conditions :: whole_is_true ( _fidget_prepared ) )
        _mediator . get ( ) . send ( typename messages :: application_update ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_update ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: use_perspective_projection_request msg )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_use_perspective_projection_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: use_ortho_projection_request msg )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_use_ortho_projection_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: fidget_prepared msg )
{
    _fidget_prepared = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: video_mode_changed msg )
{
    _init_render ( ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: near_plane_distance_request msg )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_near_plane_distance_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: receive ( typename messages :: render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _render_aspect_requested ) )
    {
        _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
        _render_aspect_width = msg . width ;
        _render_aspect_height = msg . height ;
        if ( platform_conditions :: whole_is_true ( _handling_near_plane_distance_request ) )
        {
            _handling_near_plane_distance_request = _platform_math_consts . get ( ) . whole_false ;
            typename messages :: near_plane_distance_reply near_plane_distance_reply_msg ;
            _get_near_plane_distance ( near_plane_distance_reply_msg . distance ) ;
            _mediator . get ( ) . send ( near_plane_distance_reply_msg ) ;
        }
        if ( platform_conditions :: whole_is_true ( _handling_use_ortho_projection_request ) )
        {
            _handling_use_ortho_projection_request = _platform_math_consts . get ( ) . whole_false ;
            
            num_fract width = _render_aspect_width ;
            num_fract height = _render_aspect_height ;
            num_fract neg_width ;
            num_fract neg_height ;
            num_fract z_far ;
            num_fract z_near ;
            platform_math :: neg_fract ( neg_width , width ) ;
            platform_math :: neg_fract ( neg_height , height ) ;
            platform_math :: make_num_fract ( z_near , 1 , 1 ) ;
            platform_math :: make_num_fract ( z_far , 50 , 1 ) ;
            
            typename messages :: render_projection_ortho proj_msg ;
            proj_msg . left = neg_width ;
            proj_msg . right = width ;
            proj_msg . bottom = neg_height ;
            proj_msg . top = height ;
            proj_msg . znear = z_near ;
            proj_msg . zfar = z_far ;
            _mediator . get ( ) . send ( proj_msg ) ;
            
            _mediator . get ( ) . send ( typename messages :: render_matrix_identity ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: use_ortho_projection_reply ( ) ) ;
        }
        if ( platform_conditions :: whole_is_true ( _handling_use_perspective_projection_request ) )
        {
            _handling_use_perspective_projection_request = _platform_math_consts . get ( ) . whole_false ;
        
            num_fract width = _render_aspect_width ;
            num_fract height = _render_aspect_height ;
            num_fract neg_width ;
            num_fract neg_height ;
            num_fract z_far ;
            num_fract z_near ;
            _get_near_plane_distance ( z_near ) ;
            platform_math :: make_num_fract ( z_far , 50 , 1 ) ;
            platform_math :: neg_fract ( neg_width , width ) ;
            platform_math :: neg_fract ( neg_height , height ) ;
            
            typename messages :: render_projection_frustum proj_msg ;
            proj_msg . left = neg_width ;
            proj_msg . right = width ;
            proj_msg . bottom = neg_height ;
            proj_msg . top = height ;
            proj_msg . znear = z_near ;
            proj_msg . zfar = z_far ;
            _mediator . get ( ) . send ( proj_msg ) ;
            
            _mediator . get ( ) . send ( typename messages :: render_matrix_identity ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: use_perspective_projection_reply ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic < mediator > :: _init_render ( )
{
    _mediator . get ( ) . send ( typename messages :: render_blend_disable ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: render_enable_face_culling ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: render_texture_mode_modulate ( ) ) ;
}

template < typename mediator >
void shy_logic < mediator > :: _get_near_plane_distance ( num_fract & result )
{
    platform_math :: add_fracts ( result , _render_aspect_width , _render_aspect_height ) ;
}
