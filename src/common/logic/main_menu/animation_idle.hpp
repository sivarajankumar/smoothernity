template < typename mediator >
class shy_logic_main_menu_animation_idle
{
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
    
    class _logic_main_menu_animation_idle_consts_type
    {
    public :
        _logic_main_menu_animation_idle_consts_type ( ) ;
    public :
        num_fract vertical_shift_period_in_seconds ;
        num_fract vertical_shift_phase_per_col ;
        num_fract vertical_shift_phase_per_row ;
        num_fract vertical_shift_amplitude ;
        num_fract horizontal_shift_period_in_seconds ;
        num_fract horizontal_shift_phase_per_row ;
        num_fract horizontal_shift_amplitude ;
    } ;
    
    class _logic_main_menu_animation_idle_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row ;
        num_whole col ;
        vector_data vertical_position_delta ;
        vector_data horizontal_position_delta ;
        vector_data position ;
        num_fract scale ;
    } ;
    
    class _logic_main_menu_layout_position_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole requested_col ;
        num_whole replied ;
        vector_data position ;
        num_fract scale ;
    } ;
    
    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;
    
public :
    shy_logic_main_menu_animation_idle ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_animation_idle_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_layout_position_reply ) ;
private :
    shy_logic_main_menu_animation_idle < mediator > operator= ( const shy_logic_main_menu_animation_idle < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _obtain_layout_position ( ) ;
    void _layout_position_received ( ) ;
    void _compute_horizontal_position_delta ( ) ;
    void _compute_vertical_position_delta ( ) ;
    void _compute_transform ( ) ;
    void _reply_animated_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > _logic_main_menu_stateless_consts ;
    const _logic_main_menu_animation_idle_consts_type _logic_main_menu_animation_idle_consts ;
    
    _logic_main_menu_animation_idle_transform_state_type _logic_main_menu_animation_idle_transform_state ;
    _logic_main_menu_layout_position_state_type _logic_main_menu_layout_position_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_animation_idle < mediator > :: _logic_main_menu_animation_idle_consts_type :: _logic_main_menu_animation_idle_consts_type ( )
{
    platform_math :: make_num_fract ( vertical_shift_period_in_seconds , 1 , 1 ) ;
    platform_math :: make_num_fract ( vertical_shift_phase_per_col , 1 , 3 ) ;
    platform_math :: make_num_fract ( vertical_shift_phase_per_row , 1 , 5 ) ;
    platform_math :: make_num_fract ( vertical_shift_amplitude , 1 , 30 ) ;
    platform_math :: make_num_fract ( horizontal_shift_period_in_seconds , 2 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_shift_phase_per_row , 1 , 2 ) ;
    platform_math :: make_num_fract ( horizontal_shift_amplitude , 1 , 20 ) ;
}

template < typename mediator >
shy_logic_main_menu_animation_idle < mediator > :: shy_logic_main_menu_animation_idle ( )
{
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . logic_main_menu_stateless_consts ( _logic_main_menu_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . launch_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_animation_idle_transform_request msg )
{
    _logic_main_menu_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_animation_idle_transform_state . row = msg . row ;
    _logic_main_menu_animation_idle_transform_state . col = msg . col ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_layout_position_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_layout_position_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_layout_position_state . requested_row , msg . row )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_layout_position_state . requested_col , msg . col )
       )
    {
        _logic_main_menu_layout_position_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_layout_position_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_layout_position_state . position = msg . position ;
        _logic_main_menu_layout_position_state . scale = msg . scale ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_animation_idle_transform_state . requested ) )
    {
        _logic_main_menu_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_layout_position ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_layout_position_state . replied ) )
    {
        _logic_main_menu_layout_position_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _layout_position_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _obtain_layout_position ( )
{
    _logic_main_menu_layout_position_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_layout_position_state . requested_row = _logic_main_menu_animation_idle_transform_state . row ;
    _logic_main_menu_layout_position_state . requested_col = _logic_main_menu_animation_idle_transform_state . col ;
    typename messages :: logic_main_menu_layout_position_request msg ;
    msg . row = _logic_main_menu_animation_idle_transform_state . row ;
    msg . col = _logic_main_menu_animation_idle_transform_state . col ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _layout_position_received ( )
{
    _compute_horizontal_position_delta ( ) ;
    _compute_vertical_position_delta ( ) ;
    _compute_transform ( ) ;
    _reply_animated_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _compute_horizontal_position_delta ( )
{
    vector_data horizontal_position_delta ;
    num_fract zero ;
    num_fract row ;
    num_fract phase_shift ;
    num_fract phase ;
    num_fract delta ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    platform_math :: make_fract_from_whole ( row , _logic_main_menu_animation_idle_transform_state . row ) ;
    platform_math :: mul_fracts ( phase_shift , row , _logic_main_menu_animation_idle_consts . horizontal_shift_phase_per_row ) ;
    
    platform_math :: div_fracts ( phase , _logic_main_menu_update_state . time , _logic_main_menu_animation_idle_consts . horizontal_shift_period_in_seconds ) ;
    platform_math :: add_to_fract ( phase , phase_shift ) ;
    platform_math :: mul_fract_by ( phase , _platform_math_consts . get ( ) . fract_2pi ) ;
    
    platform_math :: sin ( delta , phase ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_animation_idle_consts . horizontal_shift_amplitude ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_layout_position_state . scale ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size ) ;
    
    platform_vector :: xyz ( horizontal_position_delta , delta , zero , zero ) ;
    
    _logic_main_menu_animation_idle_transform_state . horizontal_position_delta = horizontal_position_delta ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _compute_vertical_position_delta ( )
{
    vector_data vertical_position_delta ;
    num_fract zero ;
    num_fract col ;
    num_fract row ;
    num_fract phase_shift_col ;
    num_fract phase_shift_row ;
    num_fract phase ;
    num_fract delta ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    platform_math :: make_fract_from_whole ( col , _logic_main_menu_animation_idle_transform_state . col ) ;
    platform_math :: make_fract_from_whole ( row , _logic_main_menu_animation_idle_transform_state . row ) ;
    
    platform_math :: mul_fracts ( phase_shift_col , col , _logic_main_menu_animation_idle_consts . vertical_shift_phase_per_col ) ;
    platform_math :: mul_fracts ( phase_shift_row , row , _logic_main_menu_animation_idle_consts . vertical_shift_phase_per_row ) ;
    
    platform_math :: div_fracts ( phase , _logic_main_menu_update_state . time , _logic_main_menu_animation_idle_consts . vertical_shift_period_in_seconds ) ;
    platform_math :: add_to_fract ( phase , phase_shift_col ) ;
    platform_math :: add_to_fract ( phase , phase_shift_row ) ;
    platform_math :: mul_fract_by ( phase , _platform_math_consts . get ( ) . fract_2pi ) ;
    
    platform_math :: sin ( delta , phase ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_animation_idle_consts . vertical_shift_amplitude ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_layout_position_state . scale ) ;
    platform_math :: mul_fract_by ( delta , _logic_main_menu_stateless_consts . get ( ) . letter_mesh_size ) ;
    
    platform_vector :: xyz ( vertical_position_delta , zero , delta , zero ) ;
    
    _logic_main_menu_animation_idle_transform_state . vertical_position_delta = vertical_position_delta ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _compute_transform ( )
{
    vector_data vertical_position_delta ;
    vector_data horizontal_position_delta ;
    vector_data layout_position ;
    vector_data position ;
    num_fract scale ;
    
    vertical_position_delta = _logic_main_menu_animation_idle_transform_state . vertical_position_delta ;
    horizontal_position_delta = _logic_main_menu_animation_idle_transform_state . horizontal_position_delta ;
    layout_position = _logic_main_menu_layout_position_state . position ;
    scale = _logic_main_menu_layout_position_state . scale ;
    
    platform_vector :: add ( position , vertical_position_delta , horizontal_position_delta ) ;
    platform_vector :: add_to ( position , layout_position ) ;
        
    _logic_main_menu_animation_idle_transform_state . position = position ;
    _logic_main_menu_animation_idle_transform_state . scale = scale ;
}

template < typename mediator >
void shy_logic_main_menu_animation_idle < mediator > :: _reply_animated_transform ( )
{
    typename messages :: logic_main_menu_animation_idle_transform_reply msg ;
    msg . row = _logic_main_menu_animation_idle_transform_state . row ;
    msg . col = _logic_main_menu_animation_idle_transform_state . col ;
    msg . position = _logic_main_menu_animation_idle_transform_state . position ;
    msg . scale = _logic_main_menu_animation_idle_transform_state . scale ;
    _mediator . get ( ) . send ( msg ) ;
}
