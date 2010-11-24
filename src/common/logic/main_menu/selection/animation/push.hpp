template < typename mediator >
class shy_logic_main_menu_selection_animation_push
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_main_menu_selection_animation_stateless :: logic_main_menu_selection_animation_stateless_consts_type logic_main_menu_selection_animation_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_controls_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole primary_button_down ;
    } ;

    class _logic_main_menu_update_state_type
    {
    public :
        num_whole requested ;
        num_whole clicked ;
        num_fract time ;
    } ;

    class _logic_main_menu_selection_animation_push_transform_state_type
    {
    public :
        num_fract time_begin ;
        num_fract time_middle ;
        num_fract time_end ;
        num_fract vertical_scale ;
        num_fract horizontal_scale ;
    } ;
    
public :
    shy_logic_main_menu_selection_animation_push ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_controls_state_reply ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_void_chosen ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_push_transform_request ) ;
private :
    shy_logic_main_menu_selection_animation_push < mediator > & operator= ( const shy_logic_main_menu_selection_animation_push < mediator > & ) ;
    void _proceed_with_update ( ) ;
    void _obtain_controls_state ( ) ;
    void _controls_state_received ( ) ;
    void _calculate_time ( ) ;
    void _calculate_horizontal_scale ( ) ;
    void _calculate_vertical_scale ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_selection_animation_stateless_consts_type > _logic_main_menu_selection_animation_stateless_consts ;

    _logic_controls_state_type _logic_controls_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_selection_animation_push_transform_state_type _logic_main_menu_selection_animation_push_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_push < mediator > :: shy_logic_main_menu_selection_animation_push ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_selection_animation_stateless_consts ( _logic_main_menu_selection_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: logic_main_menu_void_chosen )
{
    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_update ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: logic_controls_state_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . requested ) )
    {
        _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_controls_state . primary_button_down = msg . primary_button_down ;
        _proceed_with_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_push_transform_request )
{
    _calculate_time ( ) ;
    _calculate_vertical_scale ( ) ;
    _calculate_horizontal_scale ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _proceed_with_update ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . requested ) )
    {
        _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_controls_state ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . replied ) )
    {
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _controls_state_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _obtain_controls_state ( )
{
    _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_controls_state_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _controls_state_received ( )
{
    num_fract time ;
    num_fract time_step ;
    num_whole clicked ;
    num_whole primary_button_down ;

    time = _logic_main_menu_update_state . time ;
    clicked = _logic_main_menu_update_state . clicked ;
    primary_button_down = _logic_controls_state . primary_button_down ;
    platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;

    if ( platform_conditions :: whole_is_true ( primary_button_down ) )
        clicked = _platform_math_consts . get ( ) . whole_true ;

    if ( platform_conditions :: whole_is_true ( clicked ) )
        platform_math :: add_to_fract ( time , time_step ) ;

    _logic_main_menu_update_state . time = time ;
    _logic_main_menu_update_state . clicked = clicked ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _calculate_time ( )
{
    num_fract time_from_begin_to_middle ;
    num_fract time_from_middle_to_end ;
    num_fract time_begin ;
    num_fract time_middle ;
    num_fract time_end ;
    
    time_from_begin_to_middle = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_time_from_begin_to_middle ;
    time_from_middle_to_end = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_time_from_middle_to_end ;

    time_begin = _platform_math_consts . get ( ) . fract_0 ;
    time_middle = time_from_begin_to_middle ;
    platform_math :: add_fracts ( time_end , time_middle , time_from_middle_to_end ) ;
    
    _logic_main_menu_selection_animation_push_transform_state . time_begin = time_begin ;
    _logic_main_menu_selection_animation_push_transform_state . time_middle = time_middle ;
    _logic_main_menu_selection_animation_push_transform_state . time_end = time_end ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _calculate_horizontal_scale ( )
{
    num_fract time_begin ;
    num_fract time_middle ;
    num_fract time_end ;
    num_fract time ;
    num_fract horizontal_scale_begin ;
    num_fract horizontal_scale_middle ;
    num_fract horizontal_scale_end ;
    num_fract horizontal_scale ;

    time_begin = _logic_main_menu_selection_animation_push_transform_state . time_begin ;
    time_middle = _logic_main_menu_selection_animation_push_transform_state . time_middle ;
    time_end = _logic_main_menu_selection_animation_push_transform_state . time_end ;
    time = _logic_main_menu_update_state . time ;
    horizontal_scale_begin = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_horizontal_scale_begin ;
    horizontal_scale_middle = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_horizontal_scale_middle ;
    horizontal_scale_end = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_horizontal_scale_end ;

    engine_math :: hard_attack_easy_decay
        ( horizontal_scale
        , time
        , horizontal_scale_begin
        , time_begin
        , horizontal_scale_middle
        , time_middle
        , horizontal_scale_end
        , time_end
        ) ;

    _logic_main_menu_selection_animation_push_transform_state . horizontal_scale = horizontal_scale ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _calculate_vertical_scale ( )
{
    num_fract time_begin ;
    num_fract time_middle ;
    num_fract time_end ;
    num_fract time ;
    num_fract vertical_scale_begin ;
    num_fract vertical_scale_middle ;
    num_fract vertical_scale_end ;
    num_fract vertical_scale ;

    time_begin = _logic_main_menu_selection_animation_push_transform_state . time_begin ;
    time_middle = _logic_main_menu_selection_animation_push_transform_state . time_middle ;
    time_end = _logic_main_menu_selection_animation_push_transform_state . time_end ;
    time = _logic_main_menu_update_state . time ;
    vertical_scale_begin = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_vertical_scale_begin ;
    vertical_scale_middle = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_vertical_scale_middle ;
    vertical_scale_end = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_vertical_scale_end ;

    engine_math :: hard_attack_easy_decay
        ( vertical_scale
        , time
        , vertical_scale_begin
        , time_begin
        , vertical_scale_middle
        , time_middle
        , vertical_scale_end
        , time_end
        ) ;

    _logic_main_menu_selection_animation_push_transform_state . vertical_scale = vertical_scale ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_push_transform_reply msg ;
    msg . scale_x = _logic_main_menu_selection_animation_push_transform_state . horizontal_scale ;
    msg . scale_y = _logic_main_menu_selection_animation_push_transform_state . vertical_scale ;
    _mediator . get ( ) . send ( msg ) ;
}
