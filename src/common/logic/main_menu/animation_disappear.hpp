template < typename mediator >
class shy_logic_main_menu_letters_animation_disappear
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_animation_disappear_consts_type
    {
    public :
        _logic_main_menu_letters_animation_disappear_consts_type ( ) ;
    public :
        num_fract animation_time_in_seconds ; 
        num_fract time_from_begin_to_end_in_seconds ;
        num_fract delay_per_row_in_seconds ;
        num_fract delay_per_col_in_seconds ;
        num_fract scale_begin ;
        num_fract scale_end ;
    } ;
    
    class _logic_main_menu_letters_animation_disappear_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row ;
        num_whole col ;
        num_fract scale ;
        num_fract delay ;
        num_fract time_begin ;
        num_fract time_end ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole started ;
        num_fract time ;
    } ;
    
public :
    shy_logic_main_menu_letters_animation_disappear ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_disappear_start ) ;
    void receive ( typename messages :: logic_main_menu_letters_animation_disappear_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    shy_logic_main_menu_letters_animation_disappear < mediator > operator= ( const shy_logic_main_menu_letters_animation_disappear < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _transform_request_received ( ) ;
    void _compute_delay ( ) ;
    void _compute_time ( ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
    void _update_request_received ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_letters_animation_disappear_consts_type _logic_main_menu_letters_animation_disappear_consts ;
    
    _logic_main_menu_letters_animation_disappear_transform_state_type _logic_main_menu_letters_animation_disappear_transform_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_letters_animation_disappear < mediator > :: _logic_main_menu_letters_animation_disappear_consts_type :: _logic_main_menu_letters_animation_disappear_consts_type ( )
{
    platform_math :: make_num_fract ( animation_time_in_seconds , 8 , 10 ) ;
    platform_math :: make_num_fract ( time_from_begin_to_end_in_seconds , 3 , 10 ) ;
    platform_math :: make_num_fract ( delay_per_col_in_seconds , 2 , 100 ) ;
    platform_math :: make_num_fract ( delay_per_row_in_seconds , 5 , 100 ) ;
    platform_math :: make_num_fract ( scale_begin , 1 , 1 ) ;
    platform_math :: make_num_fract ( scale_end , 1 , 10 ) ;
}

template < typename mediator >
shy_logic_main_menu_letters_animation_disappear < mediator > :: shy_logic_main_menu_letters_animation_disappear ( )
{
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_disappear_start )
{
    _logic_main_menu_update_state . started = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . started ) )
        _update_request_received ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: receive ( typename messages :: logic_main_menu_letters_animation_disappear_transform_request msg )
{
    _logic_main_menu_letters_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_animation_disappear_transform_state . row = msg . row ;
    _logic_main_menu_letters_animation_disappear_transform_state . col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_animation_disappear_transform_state . requested ) )
    {
        _logic_main_menu_letters_animation_disappear_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _transform_request_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _transform_request_received ( )
{
    _compute_delay ( ) ;
    _compute_time ( ) ;
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _compute_delay ( )
{
    num_fract delay_for_row ;
    num_fract delay_for_col ;
    num_fract delay_per_row ;
    num_fract delay_per_col ;
    num_fract delay ;
    num_fract row ;
    num_fract col ;
    
    platform_math :: make_fract_from_whole ( row , _logic_main_menu_letters_animation_disappear_transform_state . row ) ;
    platform_math :: make_fract_from_whole ( col , _logic_main_menu_letters_animation_disappear_transform_state . col ) ;
    delay_per_row = _logic_main_menu_letters_animation_disappear_consts . delay_per_row_in_seconds ;
    delay_per_col = _logic_main_menu_letters_animation_disappear_consts . delay_per_col_in_seconds ;
    platform_math :: mul_fracts ( delay_for_row , delay_per_row , row ) ;
    platform_math :: mul_fracts ( delay_for_col , delay_per_col , col ) ;
    platform_math :: add_fracts ( delay , delay_for_row , delay_for_col ) ;
    
    _logic_main_menu_letters_animation_disappear_transform_state . delay = delay ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _compute_time ( )
{
    num_fract time_begin ;
    num_fract time_end ;
    num_fract delay ;
    num_fract time_from_begin_to_end_in_seconds ;
    
    delay = _logic_main_menu_letters_animation_disappear_transform_state . delay ;
    time_from_begin_to_end_in_seconds = _logic_main_menu_letters_animation_disappear_consts . time_from_begin_to_end_in_seconds ;
    time_begin = delay ;
    platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end_in_seconds ) ;
    
    _logic_main_menu_letters_animation_disappear_transform_state . time_begin = time_begin ;
    _logic_main_menu_letters_animation_disappear_transform_state . time_end = time_end ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _compute_transform ( )
{
    num_fract time_begin ;
    num_fract time_end ;
    num_fract time ;
    num_fract scale_begin ;
    num_fract scale_end ;
    num_fract scale ;
    
    time_begin = _logic_main_menu_letters_animation_disappear_transform_state . time_begin ;
    time_end = _logic_main_menu_letters_animation_disappear_transform_state . time_end ;
    time = _logic_main_menu_update_state . time ;
    scale_begin = _logic_main_menu_letters_animation_disappear_consts . scale_begin ;
    scale_end = _logic_main_menu_letters_animation_disappear_consts . scale_end ;
    
    if ( platform_conditions :: fract_less_than_fract ( time , time_begin ) )
        scale = scale_begin ;
    else if ( platform_conditions :: fract_less_than_fract ( time , time_end ) )
        engine_math :: hard_in_ease_out ( scale , time , scale_begin , time_begin , scale_end , time_end ) ;
    else
        scale = _platform_math_consts . get ( ) . fract_0 ;

    _logic_main_menu_letters_animation_disappear_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_letters_animation_disappear_transform_reply msg ;
    msg . row = _logic_main_menu_letters_animation_disappear_transform_state . row ;
    msg . col = _logic_main_menu_letters_animation_disappear_transform_state . col ;
    msg . scale = _logic_main_menu_letters_animation_disappear_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_animation_disappear < mediator > :: _update_request_received ( )
{
    num_fract time_step ;
    num_fract animation_time ;
    animation_time = _logic_main_menu_letters_animation_disappear_consts . animation_time_in_seconds ;
    platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
    platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    if ( platform_conditions :: fract_greater_than_fract ( _logic_main_menu_update_state . time , animation_time ) )
    {
        _logic_main_menu_update_state . started = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_animation_disappear_finished ( ) ) ;
    }
}
