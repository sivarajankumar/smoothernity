template < typename mediator >
class shy_logic_core
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
    
    class _logic_consts_type
    {
    public :
        _logic_consts_type ( ) ;
        num_fract z_far ;
        num_fract z_near ;
    } ;
    
public :
    shy_logic_core ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: render ) ;
    void receive ( typename messages :: update ) ;
    void receive ( typename messages :: use_perspective_projection_request ) ;
    void receive ( typename messages :: use_ortho_projection_request ) ;
    void receive ( typename messages :: video_mode_changed ) ;
    void receive ( typename messages :: fidget_prepared ) ;
    void receive ( typename messages :: near_plane_distance_request ) ;
    void receive ( typename messages :: render_aspect_reply ) ;
private :
    shy_logic_core < mediator > & operator= ( const shy_logic_core < mediator > & ) ;
    void _init_render ( ) ;
    void _get_near_plane_distance ( num_fract & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_consts_type _logic_consts ;
    num_whole _fidget_prepared ;
    
    num_whole _render_aspect_requested ;
    num_fract _render_aspect_width ;
    num_fract _render_aspect_height ;
    
    num_whole _handling_near_plane_distance_request ;
    num_whole _handling_use_ortho_projection_request ;
    num_whole _handling_use_perspective_projection_request ;
} ;

template < typename mediator >
shy_logic_core < mediator > :: shy_logic_core ( )
{
}

template < typename mediator >
shy_logic_core < mediator > & shy_logic_core < mediator > :: operator= ( const shy_logic_core < mediator > & )
{
    return * this ;
}

template < typename mediator >
shy_logic_core < mediator > :: _logic_consts_type :: _logic_consts_type ( )
{
    platform_math :: make_num_fract ( z_near , 1 , 1 ) ;
    platform_math :: make_num_fract ( z_far , 50 , 1 ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_false ;
    _handling_near_plane_distance_request = _platform_math_consts . get ( ) . whole_false ;
    _handling_use_ortho_projection_request = _platform_math_consts . get ( ) . whole_false ;
    _handling_use_perspective_projection_request = _platform_math_consts . get ( ) . whole_false ;
    _fidget_prepared = _platform_math_consts . get ( ) . whole_false ;
    _init_render ( ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: render )
{
    _mediator . get ( ) . send ( typename messages :: application_render ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: update )
{
    if ( platform_conditions :: whole_is_true ( _fidget_prepared ) )
        _mediator . get ( ) . send ( typename messages :: application_update ( ) ) ;
    else
        _mediator . get ( ) . send ( typename messages :: fidget_prepare_permit ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: fidget_update ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: use_perspective_projection_request )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_use_perspective_projection_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: use_ortho_projection_request )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_use_ortho_projection_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: fidget_prepared )
{
    _fidget_prepared = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: video_mode_changed )
{
    _init_render ( ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: near_plane_distance_request )
{
    _render_aspect_requested = _platform_math_consts . get ( ) . whole_true ;
    _handling_near_plane_distance_request = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: receive ( typename messages :: render_aspect_reply msg )
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
            platform_math :: neg_fract ( neg_width , width ) ;
            platform_math :: neg_fract ( neg_height , height ) ;
            
            typename messages :: render_projection_ortho proj_msg ;
            proj_msg . left = neg_width ;
            proj_msg . right = width ;
            proj_msg . bottom = neg_height ;
            proj_msg . top = height ;
            proj_msg . znear = _logic_consts . z_near ;
            proj_msg . zfar = _logic_consts . z_far ;
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
            num_fract z_near ;
            _get_near_plane_distance ( z_near ) ;
            platform_math :: neg_fract ( neg_width , width ) ;
            platform_math :: neg_fract ( neg_height , height ) ;
            
            typename messages :: render_projection_frustum proj_msg ;
            proj_msg . left = neg_width ;
            proj_msg . right = width ;
            proj_msg . bottom = neg_height ;
            proj_msg . top = height ;
            proj_msg . znear = z_near ;
            proj_msg . zfar = _logic_consts . z_far ;
            _mediator . get ( ) . send ( proj_msg ) ;
            
            _mediator . get ( ) . send ( typename messages :: render_matrix_identity ( ) ) ;
            _mediator . get ( ) . send ( typename messages :: use_perspective_projection_reply ( ) ) ;
        }
    }
}

template < typename mediator >
void shy_logic_core < mediator > :: _init_render ( )
{
    _mediator . get ( ) . send ( typename messages :: render_blend_disable ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: render_enable_face_culling ( ) ) ;
    _mediator . get ( ) . send ( typename messages :: render_texture_mode_modulate ( ) ) ;
}

template < typename mediator >
void shy_logic_core < mediator > :: _get_near_plane_distance ( num_fract & result )
{
    platform_math :: add_fracts ( result , _render_aspect_width , _render_aspect_height ) ;
}
