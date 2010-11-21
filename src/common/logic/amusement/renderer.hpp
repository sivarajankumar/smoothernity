template < typename mediator >
class shy_logic_amusement_renderer
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_amusement_renderer_consts_type
    {
    public :
        _logic_amusement_renderer_consts_type ( ) ;
    public :
        num_fract clear_color_r ;
        num_fract clear_color_g ;
        num_fract clear_color_b ;
    } ;

    class _logic_amusement_render_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _logic_core_use_ortho_projection_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

    class _logic_observer_animation_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        matrix_data transform ;
    } ;

    class _logic_perspective_planes_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract x_left ;
        num_fract x_right ;
        num_fract y_bottom ;
        num_fract y_top ;
        num_fract z_near ;
        num_fract z_far ;
        num_fract scene_scale ;
    } ;

    class _logic_blanket_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

    class _logic_door_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

    class _logic_room_render_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

public :
    shy_logic_amusement_renderer ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_amusement_render ) ;
    void receive ( typename messages :: logic_core_use_ortho_projection_reply ) ;
    void receive ( typename messages :: logic_observer_animation_transform_reply ) ;
    void receive ( typename messages :: logic_perspective_planes_reply ) ;
    void receive ( typename messages :: logic_blanket_render_reply ) ;
    void receive ( typename messages :: logic_door_render_reply ) ;
    void receive ( typename messages :: logic_room_render_reply ) ;
private :
    shy_logic_amusement_renderer < mediator > & operator= ( const shy_logic_amusement_renderer < mediator > & ) ;
    void _proceed_with_render ( ) ;
    void _prepare_ortho_render ( ) ;
    void _prepare_perspective_render ( ) ;
    void _request_ortho_projection ( ) ;
    void _request_observer_size ( ) ;
    void _request_observer_transform ( ) ;
    void _request_perspective_planes ( ) ;
    void _request_blanket_render ( ) ;
    void _request_door_render ( ) ;
    void _request_room_render ( ) ;
    void _observer_transform_received ( ) ;
    void _clear_screen ( ) ;
    void _disable_depth_test ( ) ;
    void _enable_depth_test ( ) ;
    void _use_perspective_projection ( ) ;
    void _use_observer_transform ( ) ;
    void _use_observer_size ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_amusement_renderer_consts_type _logic_amusement_renderer_consts ;

    _logic_amusement_render_state_type _logic_amusement_render_state ;
    _logic_core_use_ortho_projection_state_type _logic_core_use_ortho_projection_state ;
    _logic_observer_animation_transform_state_type _logic_observer_animation_transform_state ;
    _logic_perspective_planes_state_type _logic_perspective_planes_state ;
    _logic_blanket_render_state_type _logic_blanket_render_state ; 
    _logic_door_render_state_type _logic_door_render_state ;
    _logic_room_render_state_type _logic_room_render_state ;
} ;

template < typename mediator >
shy_logic_amusement_renderer < mediator > :: _logic_amusement_renderer_consts_type :: _logic_amusement_renderer_consts_type ( )
{
    platform_math :: make_num_fract ( clear_color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( clear_color_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( clear_color_b , 1 , 3 ) ;
}

template < typename mediator >
shy_logic_amusement_renderer < mediator > :: shy_logic_amusement_renderer ( )
{
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_amusement_render )
{
    _logic_amusement_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_render ( ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_core_use_ortho_projection_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_core_use_ortho_projection_state . requested ) )
    {
        _logic_core_use_ortho_projection_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_core_use_ortho_projection_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_observer_animation_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_observer_animation_transform_state . requested ) )
    {
        _logic_observer_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_observer_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_observer_animation_transform_state . transform = msg . transform ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_perspective_planes_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_perspective_planes_state . requested ) )
    {
        _logic_perspective_planes_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_perspective_planes_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_perspective_planes_state . x_left = msg . x_left ;
        _logic_perspective_planes_state . x_right = msg . x_right ;
        _logic_perspective_planes_state . y_bottom = msg . y_bottom ;
        _logic_perspective_planes_state . y_top = msg . y_top ;
        _logic_perspective_planes_state . z_near = msg . z_near ;
        _logic_perspective_planes_state . z_far = msg . z_far ;
        _logic_perspective_planes_state . scene_scale = msg . scene_scale ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_blanket_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_blanket_render_state . requested ) )
    {
        _logic_blanket_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_blanket_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_door_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_render_state . requested ) )
    {
        _logic_door_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_door_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: receive ( typename messages :: logic_room_render_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_render_state . requested ) )
    {
        _logic_room_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_room_render_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_amusement_render_state . requested ) )
    {
        _logic_amusement_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_perspective_planes ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_perspective_planes_state . replied ) )
    {
        _logic_perspective_planes_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_observer_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_observer_animation_transform_state . replied ) )
    {
        _logic_observer_animation_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _prepare_perspective_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_room_render_state . replied ) )
    {
        _logic_room_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_door_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_door_render_state . replied ) )
    {
        _logic_door_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _prepare_ortho_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_core_use_ortho_projection_state . replied ) )
    {
        _logic_core_use_ortho_projection_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_blanket_render ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_blanket_render_state . replied ) )
    {
        _logic_blanket_render_state . replied = _platform_math_consts . get ( ) . whole_false ;
    }
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _prepare_perspective_render ( )
{
    _clear_screen ( ) ;
    _enable_depth_test ( ) ;
    _use_perspective_projection ( ) ;
    _use_observer_size ( ) ;
    _use_observer_transform ( ) ;
    _request_room_render ( ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _prepare_ortho_render ( )
{
    _disable_depth_test ( ) ;
    _request_ortho_projection ( ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_perspective_planes ( )
{
    _logic_perspective_planes_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_perspective_planes_request ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_observer_transform ( )
{
    _logic_observer_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_observer_animation_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_ortho_projection ( )
{
    _logic_core_use_ortho_projection_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_core_use_ortho_projection_request ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _enable_depth_test ( )
{
    _mediator . get ( ) . send ( typename messages :: engine_render_enable_depth_test ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _disable_depth_test ( ) 
{
    _mediator . get ( ) . send ( typename messages :: engine_render_disable_depth_test ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _clear_screen ( )
{
    typename messages :: engine_render_clear_screen msg ;
    msg . r = _logic_amusement_renderer_consts . clear_color_r ; 
    msg . g = _logic_amusement_renderer_consts . clear_color_g ; 
    msg . b = _logic_amusement_renderer_consts . clear_color_b ; 
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _use_perspective_projection ( )
{
    typename messages :: engine_render_projection_frustum msg ;
    msg . left = _logic_perspective_planes_state . x_left ;
    msg . right = _logic_perspective_planes_state . x_right ;
    msg . bottom = _logic_perspective_planes_state . y_bottom ;
    msg . top = _logic_perspective_planes_state . y_top ;
    msg . znear = _logic_perspective_planes_state . z_near ;
    msg . zfar = _logic_perspective_planes_state . z_far ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _use_observer_transform ( )
{
    typename messages :: engine_render_matrix_mult msg ;
    msg . matrix = _logic_observer_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _use_observer_size ( )
{
    num_fract scene_scale ;
    matrix_data transform ;

    scene_scale = _logic_perspective_planes_state . scene_scale ;
    engine_math :: scale ( transform , scene_scale ) ;

    typename messages :: engine_render_matrix_load msg ;
    msg . matrix = transform ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_blanket_render ( )
{
    _logic_blanket_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_blanket_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_door_render ( )
{
    _logic_door_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_door_render_request ( ) ) ;
}

template < typename mediator >
void shy_logic_amusement_renderer < mediator > :: _request_room_render ( )
{
    _logic_room_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_room_render_request ( ) ) ;
}

