template < typename mediator >
class shy_logic_controls
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_touch platform_touch ;

    class _logic_controls_state_type
    {
    public :
        num_whole primary_button_down ;
        num_fract cursor_x ;
        num_fract cursor_y ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_controls_state_request ) ;
private :
    void _compute_identity_state ( ) ;
    void _compute_mouse_state ( ) ;
    void _compute_touch_state ( ) ;
    void _reply_controls_state ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < platform_touch > _platform_touch ;

    _logic_controls_state_type _logic_controls_state ;
} ;

template < typename mediator >
void shy_logic_controls < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_controls < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_touch = platform_obj . get ( ) . touch ;
}

template < typename mediator >
void shy_logic_controls < mediator > :: receive ( typename messages :: logic_controls_state_request )
{
    _compute_identity_state ( ) ;
    _compute_mouse_state ( ) ;
    _compute_touch_state ( ) ;
    _reply_controls_state ( ) ;
}

template < typename mediator >
void shy_logic_controls < mediator > :: _compute_identity_state ( )
{
    num_fract cursor_x ;
    num_fract cursor_y ;
    num_whole primary_button_down ;

    cursor_x = _platform_math_consts . get ( ) . fract_0 ;
    cursor_y = _platform_math_consts . get ( ) . fract_0 ;
    primary_button_down = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_controls < mediator > :: _compute_mouse_state ( )
{
    num_fract cursor_x ;
    num_fract cursor_y ;
    num_whole mouse_enabled ;
    num_whole primary_button_down ;

    _platform_mouse . get ( ) . enabled ( mouse_enabled ) ;
    if ( platform_conditions :: whole_is_true ( mouse_enabled ) )
    {
        _platform_mouse . get ( ) . left_button_down ( primary_button_down ) ;
        _platform_mouse . get ( ) . x ( cursor_x ) ;
        _platform_mouse . get ( ) . y ( cursor_y ) ;

        _logic_controls_state . cursor_x = cursor_x ;
        _logic_controls_state . cursor_y = cursor_y ;
        _logic_controls_state . primary_button_down = primary_button_down ;
    }
}

template < typename mediator >
void shy_logic_controls < mediator > :: _compute_touch_state ( )
{
    num_fract cursor_x ;
    num_fract cursor_y ;
    num_whole touch_enabled ;
    num_whole primary_button_down ;

    _platform_touch . get ( ) . enabled ( touch_enabled ) ;
    if ( platform_conditions :: whole_is_true ( touch_enabled ) )
    {
        _platform_touch . get ( ) . occured ( primary_button_down ) ;
        _platform_touch . get ( ) . x ( cursor_x ) ;
        _platform_touch . get ( ) . y ( cursor_y ) ;

        _logic_controls_state . cursor_x = cursor_x ;
        _logic_controls_state . cursor_y = cursor_y ;
        _logic_controls_state . primary_button_down = primary_button_down ;
    }
}

template < typename mediator >
void shy_logic_controls < mediator > :: _reply_controls_state ( )
{
    typename messages :: logic_controls_state_reply msg ;
    msg . primary_button_down = _logic_controls_state . primary_button_down ;
    msg . cursor_x = _logic_controls_state . cursor_x ;
    msg . cursor_y = _logic_controls_state . cursor_y ;
    _mediator . get ( ) . send ( msg ) ;
}

