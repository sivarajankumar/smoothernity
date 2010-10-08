template < typename mediator >
class shy_logic_main_menu_letters_animation_selection_push
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_animation_selection_push_consts_type
    {
    public :
        _logic_main_menu_letters_animation_selection_push_consts_type ( ) ;
    public :
        num_fract time_from_begin_to_middle ;
        num_fract time_from_middle_to_end ;
        num_fract scale_begin ;
        num_fract scale_middle ;
        num_fract scale_end ;
    } ;

    class _logic_main_menu_letters_animation_selection_push_transform_state_type
    {
    public :
        num_whole requested_row ;
        num_whole requested_col ;
        num_fract scale ;
    } ;

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
    
public :
    shy_logic_main_menu_letters_animation_selection_push ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_controls_state_reply ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_void_chosen ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_selection_push_transform_request ) ;
private :
    shy_logic_main_menu_letters_animation_selection_push < mediator > & operator= ( const shy_logic_main_menu_letters_animation_selection_push < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _proceed_with_update ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
    void _obtain_controls_state ( ) ;
    void _controls_state_received ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_letters_animation_selection_push_consts_type _logic_main_menu_letters_animation_selection_push_consts ;
    
    _logic_controls_state_type _logic_controls_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_letters_animation_selection_push_transform_state_type _logic_main_menu_letters_animation_selection_push_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_selection_push < mediator >
:: _logic_main_menu_letters_animation_selection_push_consts_type
:: _logic_main_menu_letters_animation_selection_push_consts_type ( )
{
    platform_math :: make_num_fract ( time_from_begin_to_middle , 10 , 100 ) ;
    platform_math :: make_num_fract ( time_from_middle_to_end , 20 , 100 ) ;
    platform_math :: make_num_fract ( scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( scale_middle , 6 , 10 ) ;
    platform_math :: make_num_fract ( scale_end , 8 , 10 ) ;
}

template < typename mediator >
shy_logic_main_menu_letters_animation_selection_push < mediator > :: shy_logic_main_menu_letters_animation_selection_push ( )
{
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: receive ( typename messages :: logic_main_menu_void_chosen )
{
    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_update ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: receive ( typename messages :: logic_controls_state_reply msg )
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
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_selection_push_transform_request msg )
{
    _logic_main_menu_letters_animation_selection_push_transform_state . requested_row = msg . row ;
    _logic_main_menu_letters_animation_selection_push_transform_state . requested_col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _proceed_with_update ( )
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
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _proceed_with_transform ( )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _obtain_controls_state ( )
{
    _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_controls_state_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _controls_state_received ( )
{
    num_fract time ;
    num_fract time_step ;
    num_whole clicked ;
    num_whole primary_button_down ;

    time = _logic_main_menu_update_state . time ;
    platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
    clicked = _logic_main_menu_update_state . clicked ;
    primary_button_down = _logic_controls_state . primary_button_down ;

    if ( platform_conditions :: whole_is_true ( primary_button_down ) )
        clicked = _platform_math_consts . get ( ) . whole_true ;

    if ( platform_conditions :: whole_is_true ( clicked ) )
        platform_math :: add_to_fract ( time , time_step ) ;

    _logic_main_menu_update_state . time = time ;
    _logic_main_menu_update_state . clicked = clicked ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _compute_transform ( )
{
    num_fract time_from_begin_to_middle ;
    num_fract time_from_middle_to_end ;
    num_fract time_begin ;
    num_fract time_middle ;
    num_fract time_end ;
    num_fract time ;
    num_fract scale_begin ;
    num_fract scale_middle ;
    num_fract scale_end ;
    num_fract scale ;
    
    time_from_begin_to_middle = _logic_main_menu_letters_animation_selection_push_consts . time_from_begin_to_middle ;
    time_from_middle_to_end = _logic_main_menu_letters_animation_selection_push_consts . time_from_middle_to_end ;
    time = _logic_main_menu_update_state . time ;
    scale_begin = _logic_main_menu_letters_animation_selection_push_consts . scale_begin ;
    scale_middle = _logic_main_menu_letters_animation_selection_push_consts . scale_middle ;
    scale_end = _logic_main_menu_letters_animation_selection_push_consts . scale_end ;
    
    time_begin = _platform_math_consts . get ( ) . fract_0 ;
    time_middle = time_from_begin_to_middle ;
    platform_math :: add_fracts ( time_end , time_middle , time_from_middle_to_end ) ;
    
    engine_math :: hard_attack_easy_decay
        ( scale
        , time
        , scale_begin
        , time_begin
        , scale_middle
        , time_middle
        , scale_end
        , time_end
        ) ;
        
    _logic_main_menu_letters_animation_selection_push_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection_push < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_letters_animation_selection_push_transform_reply msg ;
    msg . row = _logic_main_menu_letters_animation_selection_push_transform_state . requested_row ;
    msg . col = _logic_main_menu_letters_animation_selection_push_transform_state . requested_col ;
    msg . scale = _logic_main_menu_letters_animation_selection_push_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}
