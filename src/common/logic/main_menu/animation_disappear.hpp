template < typename mediator >
class shy_logic_main_menu_animation_disappear
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_animation_disappear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row ;
        num_whole col ;
        num_fract scale ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_animation_disappear_transform_request ) ;
private :
    void _proceed_with_transform ( ) ;
    void _transform_request_received ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_animation_disappear_transform_state_type _logic_main_menu_animation_disappear_transform_state ;
} ;

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: receive ( typename messages :: logic_main_menu_animation_disappear_transform_request msg )
{
    _logic_main_menu_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_disappear_transform_state . row = msg . row ;
    _logic_main_menu_animation_disappear_transform_state . col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_disappear_transform_state . requested ) )
    {
        _logic_main_menu_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _transform_request_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: _transform_request_received ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: _compute_transform ( )
{
    num_fract scale ;
    platform_math :: make_num_fract ( scale , 1 , 1 ) ;
    _logic_main_menu_animation_disappear_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_main_menu_animation_disappear < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_animation_disappear_transform_reply msg ;
    msg . row = _logic_main_menu_animation_disappear_transform_state . row ;
    msg . col = _logic_main_menu_animation_disappear_transform_state . col ;
    msg . scale = _logic_main_menu_animation_disappear_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}
