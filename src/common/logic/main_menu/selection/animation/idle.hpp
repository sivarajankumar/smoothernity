template < typename mediator >
class shy_logic_main_menu_selection_animation_idle
{
    typedef typename mediator :: logic_main_menu_selection_stateless :: logic_main_menu_selection_stateless_consts_type logic_main_menu_selection_stateless_consts_type ;
    typedef typename mediator :: engine_math :: rect rect ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_main_menu_selection_animation_idle_consts_type
    {
    public :
        _logic_main_menu_selection_animation_idle_consts_type ( ) ;
    public :
        num_fract position_z ;
        num_fract horizontal_scale_min ;
        num_fract horizontal_scale_max ;
        num_fract horizontal_scale_period_in_seconds ;
        num_fract vertical_scale_min ;
        num_fract vertical_scale_max ;
        num_fract vertical_scale_period_in_seconds ;
    } ;

    class _logic_main_menu_selection_animation_idle_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row_is_selected ;
        num_whole selected_row_index ;
        num_fract horizontal_animation_scale ;
        num_fract vertical_animation_scale ;
        vector_data position ;
        num_fract scale_x ;
        num_fract scale_y ;
    } ;

    class _logic_main_menu_letters_layout_row_rect_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole replied ;
        rect row_rect ;
    } ;

    class _logic_main_menu_update_state_type
    {
    public :
        num_whole launch_permitted ;
        num_fract time ;
    } ;

public :
    shy_logic_main_menu_selection_animation_idle ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_idle_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_idle_row_selected ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_idle_void_selected ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_launch_permit ) ;
private :
    shy_logic_main_menu_selection_animation_idle < mediator > & operator= ( const shy_logic_main_menu_selection_animation_idle < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _obtain_row_rect ( ) ;
    void _received_row_rect ( ) ;
    void _reply_transform ( ) ;
    void _compute_horizontal_animation_scale ( ) ;
    void _compute_vertical_animation_scale ( ) ;
    void _compute_animation_scale
        ( num_fract & scale
        , num_fract scale_min
        , num_fract scale_max
        , num_fract period_in_seconds
        ) ;
    void _compute_row_rect_mesh_transform ( ) ;
    void _compute_empty_mesh_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_selection_stateless_consts_type > _logic_main_menu_selection_stateless_consts ;
    const _logic_main_menu_selection_animation_idle_consts_type _logic_main_menu_selection_animation_idle_consts ;
    
    _logic_main_menu_selection_animation_idle_transform_state_type _logic_main_menu_selection_animation_idle_transform_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation_idle < mediator > :: _logic_main_menu_selection_animation_idle_consts_type :: _logic_main_menu_selection_animation_idle_consts_type ( )
{
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
    platform_math :: make_num_fract ( horizontal_scale_min , 19 , 20 ) ;
    platform_math :: make_num_fract ( horizontal_scale_max , 20 , 20 ) ;
    platform_math :: make_num_fract ( horizontal_scale_period_in_seconds , 2 , 1 ) ;
    platform_math :: make_num_fract ( vertical_scale_min , 20 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_max , 23 , 10 ) ;
    platform_math :: make_num_fract ( vertical_scale_period_in_seconds , 1 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_animation_idle < mediator > :: shy_logic_main_menu_selection_animation_idle ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . logic_main_menu_selection_stateless_consts ( _logic_main_menu_selection_stateless_consts ) ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;    
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_launch_permit )
{
    _logic_main_menu_update_state . launch_permitted = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_update_state . time = _platform_math_consts . get ( ) . fract_0 ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . launch_permitted ) )
    {
        num_fract time_step ;
        platform_math :: make_num_fract ( time_step , 1 , platform :: frames_per_second ) ;
        platform_math :: add_to_fract ( _logic_main_menu_update_state . time , time_step ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_idle_transform_request )
{
    _logic_main_menu_selection_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_idle_row_selected msg )
{
    _logic_main_menu_selection_animation_idle_transform_state . row_is_selected = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_selection_animation_idle_transform_state . selected_row_index = msg . row ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_idle_void_selected )
{
    _logic_main_menu_selection_animation_idle_transform_state . row_is_selected = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letters_layout_row_rect_state . requested_row , msg . row )
       )
    {
        _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_layout_row_rect_state . row_rect = msg . row_rect ;
        _proceed_with_transform ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_idle_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_idle_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_row_rect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . replied ) )
    {
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _received_row_rect ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _obtain_row_rect ( )
{
    _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_row_rect_state . requested_row = _logic_main_menu_selection_animation_idle_transform_state . selected_row_index ;
    typename messages :: logic_main_menu_letters_layout_row_rect_request msg ;
    msg . row = _logic_main_menu_letters_layout_row_rect_state . requested_row ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _received_row_rect ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_idle_transform_state . row_is_selected ) )
    {
        _compute_horizontal_animation_scale ( ) ;
        _compute_vertical_animation_scale ( ) ;
        _compute_row_rect_mesh_transform ( ) ;
    }
    else
        _compute_empty_mesh_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_idle_transform_reply reply_msg ;
    reply_msg . position = _logic_main_menu_selection_animation_idle_transform_state . position ;
    reply_msg . scale_x = _logic_main_menu_selection_animation_idle_transform_state . scale_x ;
    reply_msg . scale_y = _logic_main_menu_selection_animation_idle_transform_state . scale_y ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _compute_empty_mesh_transform ( )
{
    num_fract zero ;
    vector_data position ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_vector :: xyz ( position , zero , zero , zero ) ;
    
    _logic_main_menu_selection_animation_idle_transform_state . position = position ;
    _logic_main_menu_selection_animation_idle_transform_state . scale_x = zero ;
    _logic_main_menu_selection_animation_idle_transform_state . scale_y = zero ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _compute_row_rect_mesh_transform ( )
{
    num_fract horizontal_animation_scale ;
    num_fract vertical_animation_scale ;
    num_fract zero ;
    num_fract half ;
    num_fract scale_x ;
    num_fract scale_y ;
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    num_fract width ;
    num_fract height ;
    num_fract mesh_size ;
    rect row_rect ;
    vector_data position ;
    
    horizontal_animation_scale = _logic_main_menu_selection_animation_idle_transform_state . horizontal_animation_scale ;
    vertical_animation_scale = _logic_main_menu_selection_animation_idle_transform_state . vertical_animation_scale ;
    row_rect = _logic_main_menu_letters_layout_row_rect_state . row_rect ;
    mesh_size = _logic_main_menu_selection_stateless_consts . get ( ) . mesh_size ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_math :: sub_fracts ( width , row_rect . right , row_rect . left ) ;
    platform_math :: sub_fracts ( height , row_rect . top , row_rect . bottom ) ;
    
    platform_math :: div_fracts ( scale_x , width , mesh_size ) ;
    platform_math :: div_fracts ( scale_y , height , mesh_size ) ;

    platform_math :: mul_fract_by ( scale_x , horizontal_animation_scale ) ;
    platform_math :: mul_fract_by ( scale_y , vertical_animation_scale ) ;

    platform_math :: add_fracts ( pos_x , row_rect . right , row_rect . left ) ;
    platform_math :: add_fracts ( pos_y , row_rect . top , row_rect . bottom ) ;
    platform_math :: div_fract_by ( pos_x , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: div_fract_by ( pos_y , _platform_math_consts . get ( ) . fract_2 ) ;
    pos_z = _logic_main_menu_selection_animation_idle_consts . position_z ;
    
    platform_vector :: xyz ( position , pos_x , pos_y , pos_z ) ;
    
    _logic_main_menu_selection_animation_idle_transform_state . position = position ;
    _logic_main_menu_selection_animation_idle_transform_state . scale_x = scale_x ;
    _logic_main_menu_selection_animation_idle_transform_state . scale_y = scale_y ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _compute_horizontal_animation_scale ( )
{
    _compute_animation_scale
        ( _logic_main_menu_selection_animation_idle_transform_state . horizontal_animation_scale
        , _logic_main_menu_selection_animation_idle_consts . horizontal_scale_min
        , _logic_main_menu_selection_animation_idle_consts . horizontal_scale_max
        , _logic_main_menu_selection_animation_idle_consts . horizontal_scale_period_in_seconds
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _compute_vertical_animation_scale ( )
{
    _compute_animation_scale
        ( _logic_main_menu_selection_animation_idle_transform_state . vertical_animation_scale
        , _logic_main_menu_selection_animation_idle_consts . vertical_scale_min
        , _logic_main_menu_selection_animation_idle_consts . vertical_scale_max
        , _logic_main_menu_selection_animation_idle_consts . vertical_scale_period_in_seconds
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_idle < mediator > :: _compute_animation_scale 
    ( num_fract & scale
    , num_fract scale_min
    , num_fract scale_max
    , num_fract period_in_seconds
    )
{
    num_fract time ;
    num_fract phase ;
    num_fract amplitude ;
    num_fract offset ;
    
    time = _logic_main_menu_update_state . time ;
    
    platform_math :: div_fracts ( phase , time , period_in_seconds ) ;
    platform_math :: mul_fract_by ( phase , _platform_math_consts . get ( ) . fract_2pi ) ;
    
    platform_math :: sub_fracts ( amplitude , scale_max , scale_min ) ;
    platform_math :: div_fract_by ( amplitude , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: add_fracts ( offset , scale_max , scale_min ) ;
    platform_math :: div_fract_by ( offset , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: sin ( scale , phase ) ;
    platform_math :: mul_fract_by ( scale , amplitude ) ;
    platform_math :: add_to_fract ( scale , offset ) ;        
}
