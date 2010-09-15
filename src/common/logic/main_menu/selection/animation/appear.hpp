template < typename mediator >
class shy_logic_main_menu_selection_animation_appear
{
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
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_appear_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_animation_appear_consts_type _logic_main_menu_selection_animation_appear_consts ;
    
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_appear < mediator > :: _logic_main_menu_selection_animation_appear_consts_type :: _logic_main_menu_selection_animation_appear_consts_type ( )
{
    platform_math :: make_num_fract ( horizontal_scale_time_to_begin , 0 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_begin , 0 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_to_begin , 1 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_from_begin_to_middle , 1 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_from_middle_to_end , 5 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_begin , 1 , 5 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_middle , 3 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_end , 1 , 1 ) ;
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
    typename messages :: logic_main_menu_selection_animation_appear_transform_reply msg ;
    platform_math :: make_num_fract ( msg . scale_x , 1 , 1 ) ;
    platform_math :: make_num_fract ( msg . scale_y , 1 , 1 ) ;
    _mediator . get ( ) . send ( msg ) ;
}
