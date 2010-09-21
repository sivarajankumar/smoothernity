template < typename mediator >
class shy_logic_main_menu_selection_animation_unselect
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
    
    class _logic_main_menu_selection_animation_unselect_consts_type
    {
    public :
        _logic_main_menu_selection_animation_unselect_consts_type ( ) ;
    public :
        num_fract horizontal_scale_time_to_begin ;
        num_fract horizontal_scale_time_from_begin_to_end ;
        num_fract horizontal_scale_value_begin ;
        num_fract horizontal_scale_value_end ;
        num_fract vertical_scale_time_to_begin ;
        num_fract vertical_scale_time_from_begin_to_end ;
        num_fract vertical_scale_value_begin ;
        num_fract vertical_scale_value_end ;
        num_fract total_animation_time ;
    } ;

    class _logic_main_menu_selection_animation_unselect_transform_state_type
    {
    public :
        num_fract horizontal_scale ;
        num_fract vertical_scale ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole select_started ;
        num_fract time ;
    } ;

public :
    shy_logic_main_menu_selection_animation_unselect ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_unselect_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_unselect_start ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    shy_logic_main_menu_selection_animation_unselect < mediator > & operator= ( const shy_logic_main_menu_selection_animation_unselect < mediator > & ) ;
    void _compute_horizontal_scale ( ) ;
    void _compute_vertical_scale ( ) ;
    void _compute_identity_scale ( ) ;
    void _reply_computed_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_animation_unselect_consts_type _logic_main_menu_selection_animation_unselect_consts ;
    
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_selection_animation_unselect_transform_state_type _logic_main_menu_selection_animation_unselect_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_unselect < mediator > :: _logic_main_menu_selection_animation_unselect_consts_type :: _logic_main_menu_selection_animation_unselect_consts_type ( )
{
    platform_math :: make_num_fract ( horizontal_scale_time_to_begin , 0 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_time_from_begin_to_end , 1 , 10 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_scale_value_end , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_to_begin , 0 , 100 ) ;
    platform_math :: make_num_fract ( vertical_scale_time_from_begin_to_end , 10 , 100 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_value_end , 0 , 1 ) ;
    platform_math :: make_num_fract ( total_animation_time , 10 , 100 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_animation_unselect < mediator > :: shy_logic_main_menu_selection_animation_unselect ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_unselect_start )
{
    _logic_main_menu_update_state . select_started = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . select_started ) )
    {
        num_fract time_step ;
        num_fract time ;
        num_fract total_animation_time ;
        
        time = _logic_main_menu_update_state . time ;
        total_animation_time = _logic_main_menu_selection_animation_unselect_consts . total_animation_time ;
        
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( time , time_step ) ;
        
        if ( platform_conditions :: fract_greater_than_fract ( time , total_animation_time ) )
        {
            _logic_main_menu_update_state . select_started = _platform_math_consts . get ( ) . whole_false ;
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_unselect_finished ( ) ) ;
        }

        _logic_main_menu_update_state . time = time ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_unselect_transform_request )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . select_started ) )
    {
        _compute_horizontal_scale ( ) ;
        _compute_vertical_scale ( ) ;
    }
    else
        _compute_identity_scale ( ) ;
    _reply_computed_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: _compute_horizontal_scale ( )
{
    num_fract horizontal_scale_time_to_begin ;
    num_fract horizontal_scale_time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    
    horizontal_scale_time_to_begin = _logic_main_menu_selection_animation_unselect_consts . horizontal_scale_time_to_begin ;
    horizontal_scale_time_from_begin_to_end = _logic_main_menu_selection_animation_unselect_consts . horizontal_scale_time_from_begin_to_end ;
    
    time_begin = horizontal_scale_time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , horizontal_scale_time_from_begin_to_end ) ;
    
    engine_math :: easy_in_hard_out
        ( _logic_main_menu_selection_animation_unselect_transform_state . horizontal_scale
        , _logic_main_menu_update_state . time
        , _logic_main_menu_selection_animation_unselect_consts . horizontal_scale_value_begin
        , time_begin
        , _logic_main_menu_selection_animation_unselect_consts . horizontal_scale_value_end
        , time_end
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: _compute_vertical_scale ( )
{
    num_fract vertical_scale_time_to_begin ;
    num_fract vertical_scale_time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    
    vertical_scale_time_to_begin = _logic_main_menu_selection_animation_unselect_consts . vertical_scale_time_to_begin ;
    vertical_scale_time_from_begin_to_end = _logic_main_menu_selection_animation_unselect_consts . vertical_scale_time_from_begin_to_end ;
    
    time_begin = vertical_scale_time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , vertical_scale_time_from_begin_to_end ) ;
    
    engine_math :: easy_in_hard_out
        ( _logic_main_menu_selection_animation_unselect_transform_state . vertical_scale
        , _logic_main_menu_update_state . time
        , _logic_main_menu_selection_animation_unselect_consts . vertical_scale_value_begin
        , time_begin
        , _logic_main_menu_selection_animation_unselect_consts . vertical_scale_value_end
        , time_end
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: _compute_identity_scale ( )
{
    _logic_main_menu_selection_animation_unselect_transform_state . vertical_scale = _platform_math_consts . get ( ) . fract_1 ;
    _logic_main_menu_selection_animation_unselect_transform_state . horizontal_scale = _platform_math_consts . get ( ) . fract_1 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_unselect < mediator > :: _reply_computed_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_unselect_transform_reply msg ;
    msg . scale_x = _logic_main_menu_selection_animation_unselect_transform_state . horizontal_scale ;
    msg . scale_y = _logic_main_menu_selection_animation_unselect_transform_state . vertical_scale ;
    _mediator . get ( ) . send ( msg ) ;
}
