template < typename mediator >
class shy_logic_main_menu_animation
{
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
    
    class _logic_main_menu_animation_transform_state_type
    {
    public :
        num_whole requested ;
        matrix_data view ;
    } ;
    
    class _logic_main_menu_animation_shake_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract shift_x ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_animation_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_animation_shake_transform_reply ) ;
private :
    void _proceed_with_transform ( ) ;
    void _obtain_shake_transform ( ) ;
    void _compute_and_reply_transform ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_animation_transform_state_type _logic_main_menu_animation_transform_state ;
    _logic_main_menu_animation_shake_transform_state_type _logic_main_menu_animation_shake_transform_state ;
} ;

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_animation_transform_request )
{
    _logic_main_menu_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_animation_shake_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_shake_transform_state . requested ) )
    {
        _logic_main_menu_animation_shake_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_animation_shake_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_animation_shake_transform_state . shift_x = msg . shift_x ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_transform_state . requested ) )
    {
        _logic_main_menu_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_shake_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_shake_transform_state . replied ) )
    {
        _logic_main_menu_animation_shake_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _compute_and_reply_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _obtain_shake_transform ( )
{
    _logic_main_menu_animation_shake_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_animation_shake_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _compute_and_reply_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _compute_transform ( )
{
    matrix_data view ;
    num_fract shake_shift_x ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;

    shake_shift_x = _logic_main_menu_animation_shake_transform_state . shift_x ;

    origin_x = _platform_math_consts . get ( ) . fract_0 ;
    origin_y = _platform_math_consts . get ( ) . fract_0 ;
    origin_z = _platform_math_consts . get ( ) . fract_0 ;

    platform_math :: add_to_fract ( origin_x , shake_shift_x ) ;

    platform_matrix :: identity ( view ) ;
    platform_matrix :: set_origin ( view , origin_x , origin_y , origin_z ) ;

    _logic_main_menu_animation_transform_state . view = view ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_animation_transform_reply msg ;
    msg . view = _logic_main_menu_animation_transform_state . view ;
    _mediator . get ( ) . send ( msg ) ;
}
