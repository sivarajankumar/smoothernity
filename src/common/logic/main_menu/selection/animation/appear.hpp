template < typename mediator >
class shy_logic_main_menu_selection_animation_appear
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
    
    class _logic_main_menu_selection_animation_appear_consts_type
    {
    public :
        _logic_main_menu_selection_animation_appear_consts_type ( ) ;
    public :
        num_fract horizontal_scale_time_to_begin ;
        num_fract horizontal_scale_time_from_begin_to_end ;
        num_fract horizontal_scale_value_begin ;
        num_fract horizontal_scale_value_end ;
        num_fract vertical_scale_time_to_begin ;
        num_fract vertical_scale_time_from_begin_to_middle ;
        num_fract vertical_scale_time_from_middle_to_end ;
        num_fract vertical_scale_value_begin ;
        num_fract vertical_scale_value_middle ;
        num_fract vertical_scale_value_end ;
    } ;

    class _logic_main_menu_selection_animation_appear_transform_state_type
    {
    public :
        num_fract horizontal_scale ;
        num_fract vertical_scale ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;

public :
    shy_logic_main_menu_selection_animation_appear ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_appear_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    shy_logic_main_menu_selection_animation_appear < mediator > & operator= ( const shy_logic_main_menu_selection_animation_appear < mediator > & ) ;
    void _compute_horizontal_scale ( ) ;
    void _compute_vertical_scale ( ) ;
    void _reply_computed_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_animation_appear_consts_type _logic_main_menu_selection_animation_appear_consts ;
    
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_selection_animation_appear_transform_state_type _logic_main_menu_selection_animation_appear_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_appear < mediator > :: _logic_main_menu_selection_animation_appear_consts_type :: _logic_main_menu_selection_animation_appear_consts_type ( )
{
    platform_math :: make_num_fract ( horizontal_scale_time_to_begin , 5 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_begin , 0 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_to_begin , 10 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_from_begin_to_middle , 1 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_from_middle_to_end , 5 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_begin , 1 , 5 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_middle , 2 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_end , 1 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_animation_appear < mediator > :: shy_logic_main_menu_selection_animation_appear ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . launch_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_appear_transform_request )
{
    _compute_horizontal_scale ( ) ;
    _compute_vertical_scale ( ) ;
    _reply_computed_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: _compute_horizontal_scale ( )
{
    num_fract horizontal_scale_time_to_begin ;
    num_fract horizontal_scale_time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    
    horizontal_scale_time_to_begin = _logic_main_menu_selection_animation_appear_consts . horizontal_scale_time_to_begin ;
    horizontal_scale_time_from_begin_to_end = _logic_main_menu_selection_animation_appear_consts . horizontal_scale_time_from_begin_to_end ;
    
    time_begin = horizontal_scale_time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , horizontal_scale_time_from_begin_to_end ) ;
    
    engine_math :: hard_in_ease_out
        ( _logic_main_menu_selection_animation_appear_transform_state . horizontal_scale
        , _logic_main_menu_update_state . time
        , _logic_main_menu_selection_animation_appear_consts . horizontal_scale_value_begin
        , time_begin
        , _logic_main_menu_selection_animation_appear_consts . horizontal_scale_value_end
        , time_end
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: _compute_vertical_scale ( )
{
    num_fract vertical_scale_time_to_begin ;
    num_fract vertical_scale_time_from_begin_to_middle ;
    num_fract vertical_scale_time_from_middle_to_end ;
    num_fract time_begin ;
    num_fract time_middle ;
    num_fract time_end ;
    
    vertical_scale_time_to_begin = _logic_main_menu_selection_animation_appear_consts . vertical_scale_time_to_begin ;
    vertical_scale_time_from_begin_to_middle = _logic_main_menu_selection_animation_appear_consts . vertical_scale_time_from_begin_to_middle ;
    vertical_scale_time_from_middle_to_end = _logic_main_menu_selection_animation_appear_consts . vertical_scale_time_from_middle_to_end ;
    
    time_begin = vertical_scale_time_to_begin ;
    platform_math :: add_fracts ( time_middle , time_begin , vertical_scale_time_from_begin_to_middle ) ;
    platform_math :: add_fracts ( time_end , time_middle , vertical_scale_time_from_middle_to_end ) ;
    
    engine_math :: hard_attack_ease_decay
        ( _logic_main_menu_selection_animation_appear_transform_state . vertical_scale
        , _logic_main_menu_update_state . time
        , _logic_main_menu_selection_animation_appear_consts . vertical_scale_value_begin
        , time_begin
        , _logic_main_menu_selection_animation_appear_consts . vertical_scale_value_middle
        , time_middle
        , _logic_main_menu_selection_animation_appear_consts . vertical_scale_value_end
        , time_end
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_appear < mediator > :: _reply_computed_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_appear_transform_reply msg ;
    msg . scale_x = _logic_main_menu_selection_animation_appear_transform_state . horizontal_scale ;
    msg . scale_y = _logic_main_menu_selection_animation_appear_transform_state . vertical_scale ;
    _mediator . get ( ) . send ( msg ) ;
}
