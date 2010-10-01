template < typename mediator >
class shy_logic_main_menu_selection_animation_push_weight
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_selection_animation_push_weight_consts_type
    {
    public :
        _logic_main_menu_selection_animation_push_weight_consts_type ( ) ;
    public :
        num_fract time_to_begin ;
        num_fract time_from_begin_to_end ;
        num_fract weight_min ;
        num_fract weight_max ;
    } ;
    
    class _logic_main_menu_selection_animation_push_weight_state_type
    {
    public :
        num_fract weight ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole clicked ;
        num_fract time ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_push_weight_request ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_void_chosen ) ;
private :
    void _compute_weight ( ) ;
    void _reply_weight ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_animation_push_weight_consts_type _logic_main_menu_selection_animation_push_weight_consts ;
    
    _logic_main_menu_selection_animation_push_weight_state_type _logic_main_menu_selection_animation_push_weight_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_push_weight < mediator >
:: _logic_main_menu_selection_animation_push_weight_consts_type
:: _logic_main_menu_selection_animation_push_weight_consts_type ( )
{
    platform_math :: make_num_fract ( time_to_begin , 10 , 100 ) ;
    platform_math :: make_num_fract ( time_from_begin_to_end , 20 , 100 ) ;
    platform_math :: make_num_fract ( weight_min , 0 , 1 ) ;
    platform_math :: make_num_fract ( weight_max , 1 , 1 ) ;
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
    _platform_mouse = platform_obj . get ( ) . mouse ;
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
void shy_logic_main_menu_selection_animation_push_weight < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    num_whole mouse_button ;
    _platform_mouse . get ( ) . left_button_down ( mouse_button ) ;
    if ( platform_conditions :: whole_is_true ( mouse_button ) )
        _logic_main_menu_update_state . clicked = _platform_math_consts . get ( ) . whole_true ;
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . clicked ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
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
    time_to_begin = _logic_main_menu_selection_animation_push_weight_consts . time_to_begin ;
    time_from_begin_to_end = _logic_main_menu_selection_animation_push_weight_consts . time_from_begin_to_end ;
    weight_min = _logic_main_menu_selection_animation_push_weight_consts . weight_min ;
    weight_max = _logic_main_menu_selection_animation_push_weight_consts . weight_max ;
    
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
