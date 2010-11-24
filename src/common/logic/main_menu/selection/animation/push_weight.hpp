template < typename mediator >
class shy_logic_main_menu_selection_animation_push_weight
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
    
    class _logic_main_menu_selection_animation_push_weight_state_type
    {
    public :
        num_fract weight ;
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
    shy_logic_main_menu_selection_animation_push_weight ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_controls_state_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_push_weight_request ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_void_chosen ) ;
    void receive ( typename messages :: logic_main_menu_row_chosen ) ;
private :
    void _proceed_with_update ( ) ;
    void _obtain_controls_state ( ) ;
    void _controls_state_received ( ) ;
    void _compute_weight ( ) ;
    void _reply_weight ( ) ;
    shy_logic_main_menu_selection_animation_push_weight < mediator > & operator= ( const shy_logic_main_menu_selection_animation_push_weight < mediator > & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_selection_animation_stateless_consts_type > _logic_main_menu_selection_animation_stateless_consts ;
    
    _logic_main_menu_selection_animation_push_weight_state_type _logic_main_menu_selection_animation_push_weight_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_controls_state_type _logic_controls_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_push_weight < mediator > :: shy_logic_main_menu_selection_animation_push_weight ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_selection_animation_stateless_consts ( _logic_main_menu_selection_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_push_weight_request )
{
    _compute_weight ( ) ;
    _reply_weight ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_main_menu_void_chosen )
{
    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_main_menu_row_chosen )
{
    _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_update ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_controls_state_reply msg )
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
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: _proceed_with_update ( )
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
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: _obtain_controls_state ( )
{
    _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_controls_state_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: _controls_state_received ( )
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
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: _reply_weight ( )
{
    typename messages :: logic_main_menu_selection_animation_push_weight_reply msg ;
    msg . weight = _logic_main_menu_selection_animation_push_weight_state . weight ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: _compute_weight ( )
{
    num_fract time_to_begin ;
    num_fract time_from_begin_to_end ;
    num_fract time_end ;
    num_fract time_begin ;
    num_fract time ;
    num_fract weight ;
    num_fract weight_min ;
    num_fract weight_max ;
    
    time = _logic_main_menu_update_state . time ;
    time_to_begin = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_weight_time_to_begin ;
    time_from_begin_to_end = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_weight_time_from_begin_to_end ;
    weight_min = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_weight_min ;
    weight_max = _logic_main_menu_selection_animation_stateless_consts . get ( ) . push_weight_max ;
    
    time_begin = time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;

    engine_math :: easy_in_easy_out
        ( weight
        , time
        , weight_min
        , time_begin
        , weight_max
        , time_end
        ) ;
    
    _logic_main_menu_selection_animation_push_weight_state . weight = weight ;
}
