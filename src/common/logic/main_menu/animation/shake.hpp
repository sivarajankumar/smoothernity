template < typename mediator >
class shy_logic_main_menu_animation_shake
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: logic_main_menu_animation_stateless :: logic_main_menu_animation_stateless_consts_type logic_main_menu_animation_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_animation_shake_transform_state_type
    {
    public :
        num_fract shift_x ;
    } ;

    class _logic_main_menu_update_state_type
    {
    public :
        num_whole started ;
        num_fract time ;
    } ;

public :
    shy_logic_main_menu_animation_shake ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_void_chosen ) ;
    void receive ( typename messages :: logic_main_menu_animation_shake_transform_request ) ;
private :
    shy_logic_main_menu_animation_shake < mediator > & operator= ( const shy_logic_main_menu_animation_shake < mediator > & ) ;
    void _compute_transform ( ) ;
    void _reply_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_animation_stateless_consts_type > _logic_main_menu_animation_stateless_consts ;

    _logic_main_menu_animation_shake_transform_state_type _logic_main_menu_animation_shake_transform_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_animation_shake < mediator > :: shy_logic_main_menu_animation_shake ( )
{
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_animation_stateless_consts ( _logic_main_menu_animation_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _logic_main_menu_update_state . started = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . started ) )
    {
        num_fract time ;
        num_fract time_step ;
        num_fract time_total ;
        num_fract time_to_begin ;
        num_fract time_from_begin_to_end ;

        time = _logic_main_menu_update_state . time ;
        time_to_begin = _logic_main_menu_animation_stateless_consts . get ( ) . shake_time_to_begin ;
        time_from_begin_to_end = _logic_main_menu_animation_stateless_consts . get ( ) . shake_time_from_begin_to_end ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;

        platform_math :: add_fracts ( time_total , time_to_begin , time_from_begin_to_end ) ;
        platform_math :: add_to_fract ( time , time_step ) ;
        if ( platform_conditions :: fract_greater_than_fract ( time , time_total ) )
            _logic_main_menu_update_state . started = _platform_math_consts . get ( ) . whole_false ;

        _logic_main_menu_update_state . time = time ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: receive ( typename messages :: logic_main_menu_void_chosen )
{
    if ( platform_conditions :: whole_is_false ( _logic_main_menu_update_state . started ) )
    {
        _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
        _logic_main_menu_update_state . started = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: receive ( typename messages :: logic_main_menu_animation_shake_transform_request )
{
    _compute_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: _compute_transform ( )
{
    num_fract time ;
    num_fract time_to_begin ;
    num_fract time_from_begin_to_end ;
    num_fract time_begin ;
    num_fract time_end ;
    num_fract shift_x_amplitude_begin ;
    num_fract shift_x_amplitude_end ;
    num_fract shift_x_amplitude ;
    num_fract shift_x_period_in_seconds ;
    num_fract shift_x_phase ;
    num_fract shift_x ;

    time = _logic_main_menu_update_state . time ;
    time_to_begin = _logic_main_menu_animation_stateless_consts . get ( ) . shake_time_to_begin ;
    time_from_begin_to_end = _logic_main_menu_animation_stateless_consts . get ( ) . shake_time_from_begin_to_end ;
    shift_x_amplitude_begin = _logic_main_menu_animation_stateless_consts . get ( ) . shake_shift_x_amplitude_begin ;
    shift_x_amplitude_end = _logic_main_menu_animation_stateless_consts . get ( ) . shake_shift_x_amplitude_end ;
    shift_x_period_in_seconds = _logic_main_menu_animation_stateless_consts . get ( ) . shake_shift_x_period_in_seconds ;

    time_begin = time_to_begin ;
    platform_math :: add_fracts ( time_end , time_begin , time_from_begin_to_end ) ;

    engine_math :: easy_in_easy_out
        ( shift_x_amplitude
        , time
        , shift_x_amplitude_begin
        , time_begin
        , shift_x_amplitude_end
        , time_end
        ) ;

    platform_math :: mul_fracts ( shift_x_phase , time , _platform_math_consts . get ( ) . fract_2pi ) ;
    platform_math :: div_fract_by ( shift_x_phase , shift_x_period_in_seconds ) ;

    platform_math :: sin ( shift_x , shift_x_phase ) ;
    platform_math :: mul_fract_by ( shift_x , shift_x_amplitude ) ;

    _logic_main_menu_animation_shake_transform_state . shift_x = shift_x ;
}

template < typename mediator >
void shy_logic_main_menu_animation_shake < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_animation_shake_transform_reply msg ;
    msg . shift_x = _logic_main_menu_animation_shake_transform_state . shift_x ;
    _mediator . get ( ) . send ( msg ) ;
}
