template < typename mediator >
class shy_logic_main_menu_animation
{
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
    
    class _logic_main_menu_animation_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row ;
        num_whole col ;
        matrix_data transform ;
    } ;

    class _logic_main_menu_animation_appear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        num_fract scale ;
    } ;
    
    class _logic_main_menu_animation_disappear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        num_fract scale ;
    } ;
    
    class _logic_main_menu_animation_idle_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        vector_data position ;
        num_fract scale ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_animation_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_appear_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_disappear_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_idle_transform_reply ) ;
private :
    void _proceed_with_transform ( ) ;
    void _obtain_appear_transform ( ) ;
    void _obtain_disappear_transform ( ) ;
    void _obtain_idle_transform ( ) ;
    void _all_transforms_received ( ) ;
    void _compute_transform ( ) ;
    void _reply_animated_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > _logic_main_menu_stateless_consts ;
    
    _logic_main_menu_animation_transform_state_type _logic_main_menu_animation_transform_state ;
    _logic_main_menu_animation_appear_transform_state_type _logic_main_menu_animation_appear_transform_state ;
    _logic_main_menu_animation_disappear_transform_state_type _logic_main_menu_animation_disappear_transform_state ;
    _logic_main_menu_animation_idle_transform_state_type _logic_main_menu_animation_idle_transform_state ;
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
    _mediator . get ( ) . logic_main_menu_stateless_consts ( _logic_main_menu_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_animation_transform_request msg )
{
    _logic_main_menu_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_transform_state . row = msg . row ;
    _logic_main_menu_animation_transform_state . col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_idle_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_idle_transform_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_idle_transform_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_idle_transform_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_animation_idle_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_animation_idle_transform_state . position = msg . position ;
        _logic_main_menu_animation_idle_transform_state . scale = msg . scale ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_appear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_appear_transform_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_appear_transform_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_appear_transform_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_animation_appear_transform_state . scale = msg . scale ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_disappear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_disappear_transform_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_disappear_transform_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_animation_disappear_transform_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_animation_disappear_transform_state . scale = msg . scale ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_transform_state . requested ) )
    {
        _logic_main_menu_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_appear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_appear_transform_state . replied ) )
    {
        _logic_main_menu_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_disappear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_disappear_transform_state . replied ) )
    {
        _logic_main_menu_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_idle_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_idle_transform_state . replied ) )
    {
        _logic_main_menu_animation_idle_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _all_transforms_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _obtain_appear_transform ( )
{
    _logic_main_menu_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_appear_transform_state . requested_row = _logic_main_menu_animation_transform_state . row ;
    _logic_main_menu_animation_appear_transform_state . requested_col = _logic_main_menu_animation_transform_state . col ;
    typename messages :: logic_main_menu_letters_animation_appear_transform_request msg ;
    msg . row = _logic_main_menu_animation_transform_state . row ;
    msg . col = _logic_main_menu_animation_transform_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _obtain_disappear_transform ( )
{
    _logic_main_menu_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_disappear_transform_state . requested_row = _logic_main_menu_animation_transform_state . row ;
    _logic_main_menu_animation_disappear_transform_state . requested_col = _logic_main_menu_animation_transform_state . col ;
    typename messages :: logic_main_menu_letters_animation_disappear_transform_request msg ;
    msg . row = _logic_main_menu_animation_transform_state . row ;
    msg . col = _logic_main_menu_animation_transform_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _obtain_idle_transform ( )
{
    _logic_main_menu_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_idle_transform_state . requested_row = _logic_main_menu_animation_transform_state . row ;
    _logic_main_menu_animation_idle_transform_state . requested_col = _logic_main_menu_animation_transform_state . col ;
    typename messages :: logic_main_menu_letters_animation_idle_transform_request msg ;
    msg . row = _logic_main_menu_animation_transform_state . row ;
    msg . col = _logic_main_menu_animation_transform_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _all_transforms_received ( )
{
    _compute_transform ( ) ;
    _reply_animated_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _compute_transform ( )
{
    matrix_data transform ;
    vector_data position ;
    num_fract scale_appear ;
    num_fract scale_disappear ;
    num_fract scale_idle ;
    num_fract scale ;
    num_fract zero ;
    
    position = _logic_main_menu_animation_idle_transform_state . position ;
    scale_appear = _logic_main_menu_animation_appear_transform_state . scale ;
    scale_disappear = _logic_main_menu_animation_disappear_transform_state . scale ;
    scale_idle = _logic_main_menu_animation_idle_transform_state . scale ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_math :: mul_fracts ( scale , scale_idle , scale_appear ) ;
    platform_math :: mul_fract_by ( scale , scale_disappear ) ;
    
    platform_matrix :: set_origin ( transform , position ) ;
    platform_matrix :: set_axis_x ( transform , scale , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale ) ;
    
    _logic_main_menu_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_main_menu_animation < mediator > :: _reply_animated_transform ( )
{
    typename messages :: logic_main_menu_animation_transform_reply msg ;
    msg . row = _logic_main_menu_animation_transform_state . row ;
    msg . col = _logic_main_menu_animation_transform_state . col ;
    msg . transform = _logic_main_menu_animation_transform_state . transform ;
    _mediator . get ( ) . send ( msg ) ;
}
