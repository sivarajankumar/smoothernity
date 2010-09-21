template < typename mediator >
class shy_logic_main_menu_selection_animation
{
    typedef typename mediator :: logic_main_menu_selection_stateless :: logic_main_menu_selection_stateless_consts_type logic_main_menu_selection_stateless_consts_type ;
    typedef typename mediator :: engine_math :: rect rect ;
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
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_main_menu_selection_animation_transform_state_type
    {
    public :
        num_whole requested ;
        matrix_data transform ;
    } ;

    class _logic_main_menu_selection_animation_idle_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        vector_data position ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

    class _logic_main_menu_selection_animation_appear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

    class _logic_main_menu_selection_animation_disappear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

    class _logic_main_menu_selection_animation_select_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

    class _logic_main_menu_selection_animation_unselect_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

public :
    shy_logic_main_menu_selection_animation ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_idle_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_appear_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_disappear_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_select_transform_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_unselect_transform_reply ) ;
private :
    shy_logic_main_menu_selection_animation < mediator > & operator= ( const shy_logic_main_menu_selection_animation < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _obtain_idle_transform ( ) ;
    void _obtain_appear_transform ( ) ;
    void _obtain_disappear_transform ( ) ;
    void _obtain_select_transform ( ) ;
    void _obtain_unselect_transform ( ) ;
    void _reply_transform ( ) ;
    void _reply_computed_transform ( ) ;
    void _compute_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_selection_animation_transform_state_type _logic_main_menu_selection_animation_transform_state ;
    _logic_main_menu_selection_animation_idle_transform_state_type _logic_main_menu_selection_animation_idle_transform_state ;
    _logic_main_menu_selection_animation_appear_transform_state_type _logic_main_menu_selection_animation_appear_transform_state ;
    _logic_main_menu_selection_animation_disappear_transform_state_type _logic_main_menu_selection_animation_disappear_transform_state ;
    _logic_main_menu_selection_animation_select_transform_state_type _logic_main_menu_selection_animation_select_transform_state ;
    _logic_main_menu_selection_animation_unselect_transform_state_type _logic_main_menu_selection_animation_unselect_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation < mediator > :: shy_logic_main_menu_selection_animation ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;    
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_transform_request )
{
    _logic_main_menu_selection_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_idle_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_idle_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_animation_idle_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_selection_animation_idle_transform_state . position = msg . position ;
        _logic_main_menu_selection_animation_idle_transform_state . scale_x = msg . scale_x ;
        _logic_main_menu_selection_animation_idle_transform_state . scale_y = msg . scale_y ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_appear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_appear_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_selection_animation_appear_transform_state . scale_x = msg . scale_x ;
        _logic_main_menu_selection_animation_appear_transform_state . scale_y = msg . scale_y ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_disappear_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_disappear_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_selection_animation_disappear_transform_state . scale_x = msg . scale_x ;
        _logic_main_menu_selection_animation_disappear_transform_state . scale_y = msg . scale_y ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_select_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_select_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_select_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_animation_select_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_selection_animation_select_transform_state . scale_x = msg . scale_x ;
        _logic_main_menu_selection_animation_select_transform_state . scale_y = msg . scale_y ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_unselect_transform_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_unselect_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_unselect_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_animation_unselect_transform_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_selection_animation_unselect_transform_state . scale_x = msg . scale_x ;
        _logic_main_menu_selection_animation_unselect_transform_state . scale_y = msg . scale_y ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_idle_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_idle_transform_state . replied ) )
    {
        _logic_main_menu_selection_animation_idle_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_appear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_appear_transform_state . replied ) )
    {
        _logic_main_menu_selection_animation_appear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_disappear_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_disappear_transform_state . replied ) )
    {
        _logic_main_menu_selection_animation_disappear_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_select_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_select_transform_state . replied ) )
    {
        _logic_main_menu_selection_animation_select_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_unselect_transform ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_unselect_transform_state . replied ) )
    {
        _logic_main_menu_selection_animation_unselect_transform_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_idle_transform ( )
{
    _logic_main_menu_selection_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_idle_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_appear_transform ( )
{
    _logic_main_menu_selection_animation_appear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_appear_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_disappear_transform ( )
{
    _logic_main_menu_selection_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_disappear_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_select_transform ( )
{
    _logic_main_menu_selection_animation_select_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_select_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_unselect_transform ( )
{
    _logic_main_menu_selection_animation_unselect_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_unselect_transform_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _reply_transform ( )
{
    _compute_transform ( ) ;
    _reply_computed_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _compute_transform ( )
{
    num_fract zero ;
    vector_data idle_position ;
    num_fract idle_scale_x ;
    num_fract idle_scale_y ;
    num_fract appear_scale_x ;
    num_fract appear_scale_y ;
    num_fract disappear_scale_x ;
    num_fract disappear_scale_y ;
    num_fract select_scale_x ;
    num_fract select_scale_y ;
    num_fract unselect_scale_x ;
    num_fract unselect_scale_y ;
    num_fract scale_x ;
    num_fract scale_y ;
    num_fract scale_z ;
    vector_data position ;
    matrix_data transform ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    idle_position = _logic_main_menu_selection_animation_idle_transform_state . position ;
    idle_scale_x = _logic_main_menu_selection_animation_idle_transform_state . scale_x ;
    idle_scale_y = _logic_main_menu_selection_animation_idle_transform_state . scale_y ;
    appear_scale_x = _logic_main_menu_selection_animation_appear_transform_state . scale_x ;
    appear_scale_y = _logic_main_menu_selection_animation_appear_transform_state . scale_y ;
    disappear_scale_x = _logic_main_menu_selection_animation_disappear_transform_state . scale_x ;
    disappear_scale_y = _logic_main_menu_selection_animation_disappear_transform_state . scale_y ;
    select_scale_x = _logic_main_menu_selection_animation_select_transform_state . scale_x ;
    select_scale_y = _logic_main_menu_selection_animation_select_transform_state . scale_y ;
    unselect_scale_x = _logic_main_menu_selection_animation_unselect_transform_state . scale_x ;
    unselect_scale_y = _logic_main_menu_selection_animation_unselect_transform_state . scale_y ;
    
    position = idle_position ;
    platform_math :: mul_fracts ( scale_x , idle_scale_x , appear_scale_x ) ;
    platform_math :: mul_fracts ( scale_y , idle_scale_y , appear_scale_y ) ;
    platform_math :: mul_fract_by ( scale_x , disappear_scale_x ) ;
    platform_math :: mul_fract_by ( scale_y , disappear_scale_y ) ;
    platform_math :: mul_fract_by ( scale_x , select_scale_x ) ;
    platform_math :: mul_fract_by ( scale_y , select_scale_y ) ;
    platform_math :: mul_fract_by ( scale_x , unselect_scale_x ) ;
    platform_math :: mul_fract_by ( scale_y , unselect_scale_y ) ;
    scale_z = _platform_math_consts . get ( ) . fract_1 ;
    
    platform_matrix :: set_origin ( transform , position ) ;
    platform_matrix :: set_axis_x ( transform , scale_x , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale_y , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale_z ) ;
    
    _logic_main_menu_selection_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _reply_computed_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_transform_reply reply_msg ;
    reply_msg . transform = _logic_main_menu_selection_animation_transform_state . transform ;
    _mediator . get ( ) . send ( reply_msg ) ;
}
