template < typename mediator >
class shy_logic_perspective
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_perspective_consts_type
    {
    public :
        _logic_perspective_consts_type ( ) ;
    public :
        num_fract z_far_unscaled ;
    } ;

    class _logic_perspective_planes_state_type
    {
    public :
        num_whole requested ;
        num_fract x_left ;
        num_fract x_right ;
        num_fract y_top ;
        num_fract y_bottom ;
        num_fract z_near ;
        num_fract z_far ;
        num_fract scene_scale ;
    } ;

    class _engine_render_aspect_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract width ;
        num_fract height ;
    } ;

public :
    shy_logic_perspective ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_perspective_planes_request ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    shy_logic_perspective < mediator > & operator= ( const shy_logic_perspective < mediator > & ) ;
    void _proceed_with_planes ( ) ;
    void _request_aspect ( ) ;
    void _compute_x_left ( ) ;
    void _compute_x_right ( ) ;
    void _compute_y_top ( ) ;
    void _compute_y_bottom ( ) ;
    void _compute_z_near ( ) ;
    void _compute_z_far ( ) ;
    void _compute_scene_scale ( ) ;
    void _reply_computed_planes ( ) ;
    void _reply_planes ( ) ;
    void _scene_scale ( num_fract & ) ;
    void _z_near ( num_fract & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_perspective_consts_type _logic_perspective_consts ; 

    _logic_perspective_planes_state_type _logic_perspective_planes_state ;
    _engine_render_aspect_state_type _engine_render_aspect_state ;
} ;

template < typename mediator >
shy_logic_perspective < mediator > :: _logic_perspective_consts_type :: _logic_perspective_consts_type ( )
{
    platform_math :: make_num_fract ( z_far_unscaled , 50 , 1 ) ;
}

template < typename mediator >
shy_logic_perspective < mediator > :: shy_logic_perspective ( )
{
}

template < typename mediator >
void shy_logic_perspective < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: receive ( typename messages :: logic_perspective_planes_request )
{
    _logic_perspective_planes_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_planes ( ) ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . requested ) )
    {
        _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_aspect_state . width = msg . width ;
        _engine_render_aspect_state . height = msg . height ;
        _proceed_with_planes ( ) ;
    }
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _proceed_with_planes ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_perspective_planes_state . requested ) )
    {
        _logic_perspective_planes_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_aspect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . replied ) )
    {
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_computed_planes ( ) ;
    }
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _request_aspect ( )
{
    _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _reply_computed_planes ( )
{
    _compute_x_left ( ) ;
    _compute_x_right ( ) ;
    _compute_y_top ( ) ;
    _compute_y_bottom ( ) ;
    _compute_z_near ( ) ;
    _compute_z_far ( ) ;
    _compute_scene_scale ( ) ;
    _reply_planes ( ) ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_x_left ( )
{
    num_fract x_left ;
    num_fract aspect_width ;

    aspect_width = _engine_render_aspect_state . width ;
    platform_math :: mul_fracts ( x_left , aspect_width , _platform_math_consts . get ( ) . fract_minus_1 ) ;

    _logic_perspective_planes_state . x_left = x_left ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_x_right ( )
{
    num_fract x_right ;
    num_fract aspect_width ;

    aspect_width = _engine_render_aspect_state . width ;
    x_right = aspect_width ;

    _logic_perspective_planes_state . x_right = x_right ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_y_bottom ( )
{
    num_fract y_bottom ;
    num_fract aspect_height ;

    aspect_height = _engine_render_aspect_state . height ;
    platform_math :: mul_fracts ( y_bottom , aspect_height , _platform_math_consts . get ( ) . fract_minus_1 ) ;

    _logic_perspective_planes_state . y_bottom = y_bottom ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_y_top ( )
{
    num_fract y_top ;
    num_fract aspect_height ;

    aspect_height = _engine_render_aspect_state . height ;
    y_top = aspect_height ;

    _logic_perspective_planes_state . y_top = y_top ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_z_near ( )
{
    num_fract z_near ;
    _z_near ( z_near ) ;
    _logic_perspective_planes_state . z_near = z_near ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_z_far ( )
{
    num_fract scene_scale ;
    num_fract z_far_unscaled ;
    num_fract z_far ;

    z_far_unscaled = _logic_perspective_consts . z_far_unscaled ;
    _scene_scale ( scene_scale ) ;
    platform_math :: mul_fracts ( z_far , z_far_unscaled , scene_scale ) ;

    _logic_perspective_planes_state . z_far = z_far ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _compute_scene_scale ( )
{
    num_fract scene_scale ;
    _scene_scale ( scene_scale ) ;
    _logic_perspective_planes_state . scene_scale = scene_scale ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _scene_scale ( num_fract & scene_scale )
{
    num_fract aspect_width ;
    num_fract aspect_height ;
    num_fract z_near ;

    aspect_width = _engine_render_aspect_state . width ;
    aspect_height = _engine_render_aspect_state . height ;
    _z_near ( z_near ) ;

    platform_math :: add_fracts ( scene_scale , aspect_width , aspect_height ) ;
    platform_math :: add_to_fract ( scene_scale , z_near ) ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _z_near ( num_fract & z_near )
{
    num_fract aspect_width ;
    num_fract aspect_height ;

    aspect_width = _engine_render_aspect_state . width ;
    aspect_height = _engine_render_aspect_state . height ;
    platform_math :: add_fracts ( z_near , aspect_width , aspect_height ) ;
}

template < typename mediator >
void shy_logic_perspective < mediator > :: _reply_planes ( )
{
    typename messages :: logic_perspective_planes_reply msg ;
    msg . x_left = _logic_perspective_planes_state . x_left ;
    msg . x_right = _logic_perspective_planes_state . x_right ;
    msg . y_top = _logic_perspective_planes_state . y_top ;
    msg . y_bottom = _logic_perspective_planes_state . y_bottom ;
    msg . z_near = _logic_perspective_planes_state . z_near ;
    msg . z_far = _logic_perspective_planes_state . z_far ;
    msg . scene_scale = _logic_perspective_planes_state . scene_scale ;
    _mediator . get ( ) . send ( msg ) ;
}
