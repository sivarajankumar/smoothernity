template < typename mediator >
class shy_logic_main_menu_letters_animation_selection
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_main_menu_letters_animation_stateless :: logic_main_menu_letters_animation_stateless_consts_type logic_main_menu_letters_animation_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_animation_selection_transform_state_type
    {
    public :
        num_whole requested_col ;
        num_whole requested_row ;
        num_fract scale ;
        num_fract weight ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;
    
public :
    shy_logic_main_menu_letters_animation_selection ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_selection_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    shy_logic_main_menu_letters_animation_selection < mediator > operator= ( const shy_logic_main_menu_letters_animation_selection < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _compute_weight ( ) ;
    void _invert_even_weight ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_animation_stateless_consts_type > _logic_main_menu_letters_animation_stateless_consts ;
    
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
    _logic_main_menu_letters_animation_selection_transform_state_type _logic_main_menu_letters_animation_selection_transform_state ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_selection < mediator > :: shy_logic_main_menu_letters_animation_selection ( )
{
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_letters_animation_stateless_consts ( _logic_main_menu_letters_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . launch_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_selection_transform_request msg )
{
    _logic_main_menu_letters_animation_selection_transform_state . requested_row = msg . row ;
    _logic_main_menu_letters_animation_selection_transform_state . requested_col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: _proceed_with_transform ( )
{
    _compute_weight ( ) ;
    _invert_even_weight ( ) ;
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: _compute_weight ( )
{
    num_fract time ;
    num_fract time_stable ;
    num_fract time_transition ;
    num_fract time_raise_begin ;
    num_fract time_raise_end ;
    num_fract time_fall_begin ;
    num_fract time_fall_end ;
    num_fract weight_low ;
    num_fract weight_high ;
    num_fract weight ;
    
    time = _logic_main_menu_update_state . time ;
    time_stable = _logic_main_menu_letters_animation_stateless_consts . get ( ) . selection_time_stable ;
    time_transition = _logic_main_menu_letters_animation_stateless_consts . get ( ) . selection_time_transition ;
    weight_low = _platform_math_consts . get ( ) . fract_0 ;
    weight_high = _platform_math_consts . get ( ) . fract_1 ;

    time_raise_begin = time_stable ;
    platform_math :: add_fracts ( time_raise_end , time_raise_begin , time_transition ) ;
    platform_math :: add_fracts ( time_fall_begin , time_raise_end , time_stable ) ;
    platform_math :: add_fracts ( time_fall_end , time_fall_begin , time_transition ) ;
    
    while ( platform_conditions :: fract_greater_than_fract ( time , time_fall_end ) )
        platform_math :: sub_from_fract ( time , time_fall_end ) ;

    if ( platform_conditions :: fract_less_than_fract ( time , time_raise_end ) )
    {
        engine_math :: easy_in_easy_out
            ( weight
            , time
            , weight_low
            , time_raise_begin
            , weight_high
            , time_raise_end
            ) ;
    }
    else
    {
        engine_math :: easy_in_easy_out
            ( weight
            , time
            , weight_high
            , time_fall_begin
            , weight_low
            , time_fall_end
            ) ;
    }

    _logic_main_menu_update_state . time = time ;
    _logic_main_menu_letters_animation_selection_transform_state . weight = weight ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: _invert_even_weight ( )
{
    num_whole requested_row ;
    num_whole requested_col ;
    num_whole index ;
    num_fract weight ;
    
    requested_row = _logic_main_menu_letters_animation_selection_transform_state . requested_row ;
    requested_col = _logic_main_menu_letters_animation_selection_transform_state . requested_col ;
    weight = _logic_main_menu_letters_animation_selection_transform_state . weight ;
    
    platform_math :: add_wholes ( index , requested_row , requested_col ) ;
    platform_math :: mod_whole_by ( index , _platform_math_consts . get ( ) . whole_2 ) ;
    
    if ( platform_conditions :: whole_is_zero ( index ) )
    {
        platform_math :: sub_fracts ( weight , _platform_math_consts . get ( ) . fract_1 , weight ) ;
        _logic_main_menu_letters_animation_selection_transform_state . weight = weight ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: _compute_transform ( )
{
    num_fract scale_min ;
    num_fract scale_max ;
    num_fract scale ;
    num_fract weight_min ;
    num_fract weight_max ;
    num_fract weight ;
    
    scale_min = _logic_main_menu_letters_animation_stateless_consts . get ( ) . selection_scale_min ;
    scale_max = _logic_main_menu_letters_animation_stateless_consts . get ( ) . selection_scale_max ;
    weight_min = _platform_math_consts . get ( ) . fract_0 ;
    weight_max = _platform_math_consts . get ( ) . fract_1 ;
    weight = _logic_main_menu_letters_animation_selection_transform_state . weight ;
    
    engine_math :: lerp
        ( scale
        , weight
        , scale_min
        , weight_min
        , scale_max
        , weight_max
        ) ;
    
    _logic_main_menu_letters_animation_selection_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_selection < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_letters_animation_selection_transform_reply reply_msg ;
    reply_msg . row = _logic_main_menu_letters_animation_selection_transform_state . requested_row ;
    reply_msg . col = _logic_main_menu_letters_animation_selection_transform_state . requested_col ;
    reply_msg . scale = _logic_main_menu_letters_animation_selection_transform_state . scale ;
    _mediator . get ( ) . send ( reply_msg ) ;
}
