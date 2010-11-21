template < typename mediator >
class shy_logic_observer_size
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_observer_size_state_type
    {
    public :
        num_whole requested ;
        num_fract size ;
    } ;

    class _logic_core_near_plane_distance_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract distance ;
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
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_observer_size_request ) ;
    void receive ( typename messages :: logic_core_near_plane_distance_reply ) ;
    void receive ( typename messages :: engine_render_aspect_reply ) ;
private :
    void _proceed_with_size ( ) ;
    void _request_aspect ( ) ;
    void _request_near_plane_distance ( ) ;
    void _reply_calculated_size ( ) ;
    void _calculate_size ( ) ;
    void _reply_size ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_observer_size_state_type _logic_observer_size_state ;
    _logic_core_near_plane_distance_state_type _logic_core_near_plane_distance_state ;
    _engine_render_aspect_state_type _engine_render_aspect_state ;
} ;

template < typename mediator >
void shy_logic_observer_size < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: receive ( typename messages :: logic_observer_size_request )
{
    _logic_observer_size_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_size ( ) ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: receive ( typename messages :: logic_core_near_plane_distance_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_core_near_plane_distance_state . requested ) )
    {
        _logic_core_near_plane_distance_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_core_near_plane_distance_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_core_near_plane_distance_state . distance = msg . distance ;
        _proceed_with_size ( ) ;
    }
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: receive ( typename messages :: engine_render_aspect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . requested ) )
    {
        _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_aspect_state . width = msg . width ;
        _engine_render_aspect_state . height = msg . height ;
        _proceed_with_size ( ) ;
    }
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _proceed_with_size ( ) 
{
    if ( platform_conditions :: whole_is_true ( _logic_observer_size_state . requested ) )
    {
        _logic_observer_size_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_near_plane_distance ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_core_near_plane_distance_state . replied ) )
    {
        _logic_core_near_plane_distance_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _request_aspect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_aspect_state . replied ) )
    {
        _engine_render_aspect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_calculated_size ( ) ;
    }
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _request_near_plane_distance ( )
{
    _logic_core_near_plane_distance_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_core_near_plane_distance_request ( ) ) ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _request_aspect ( )
{
    _engine_render_aspect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_aspect_request ( ) ) ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _reply_calculated_size ( )
{
    _calculate_size ( ) ;
    _reply_size ( ) ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _calculate_size ( )
{
    _logic_observer_size_state . size = _platform_math_consts . get ( ) . fract_2 ;
}

template < typename mediator >
void shy_logic_observer_size < mediator > :: _reply_size ( )
{
    typename messages :: logic_observer_size_reply msg ;
    msg . size = _logic_observer_size_state . size ;
    _mediator . get ( ) . send ( msg ) ;
}
