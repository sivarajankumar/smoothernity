template < typename mediator >
class shy_logic_main_menu_selection_animation
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
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_selection_animation_consts_type
    {
    public :
        _logic_main_menu_selection_animation_consts_type ( ) ;
    public :
        num_fract position_z ;
    } ;

    class _logic_main_menu_selection_animation_transform_state_type
    {
    public :
        num_whole requested ;
        num_whole row_is_selected ;
        num_whole selected_row_index ;
        matrix_data transform ;
    } ;

    class _logic_main_menu_letters_layout_row_rect_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
        num_whole replied ;
        rect row_rect ;
    } ;

public :
    shy_logic_main_menu_selection_animation ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_transform_request ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_row_selected ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_void_selected ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply ) ;
private :
    shy_logic_main_menu_selection_animation < mediator > & operator= ( const shy_logic_main_menu_selection_animation < mediator > & ) ;
    void _proceed_with_transform ( ) ;
    void _obtain_row_rect ( ) ;
    void _received_row_rect ( ) ;
    void _reply_transform ( ) ;
    void _compute_row_rect_mesh_transform ( ) ;
    void _compute_empty_mesh_transform ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_selection_stateless_consts_type > _logic_main_menu_selection_stateless_consts ;
    const _logic_main_menu_selection_animation_consts_type _logic_main_menu_selection_animation_consts ;
    
    _logic_main_menu_selection_animation_transform_state_type _logic_main_menu_selection_animation_transform_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_animation < mediator > :: _logic_main_menu_selection_animation_consts_type :: _logic_main_menu_selection_animation_consts_type ( )
{
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_animation < mediator > :: shy_logic_main_menu_selection_animation ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . logic_main_menu_selection_stateless_consts ( _logic_main_menu_selection_stateless_consts ) ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_transform_request )
{
    _logic_main_menu_selection_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_row_selected msg )
{
    _logic_main_menu_selection_animation_transform_state . row_is_selected = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_selection_animation_transform_state . selected_row_index = msg . row ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_void_selected )
{
    _logic_main_menu_selection_animation_transform_state . row_is_selected = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply msg )
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
void shy_logic_main_menu_selection_animation < mediator > :: _proceed_with_transform ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_transform_state . requested ) )
    {
        _logic_main_menu_selection_animation_transform_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_row_rect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . replied ) )
    {
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _received_row_rect ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _obtain_row_rect ( )
{
    _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_row_rect_state . requested_row = _logic_main_menu_selection_animation_transform_state . selected_row_index ;
    typename messages :: logic_main_menu_letters_layout_row_rect_request msg ;
    msg . row = _logic_main_menu_letters_layout_row_rect_state . requested_row ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _received_row_rect ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_animation_transform_state . row_is_selected ) )
        _compute_row_rect_mesh_transform ( ) ;
    else
        _compute_empty_mesh_transform ( ) ;
    _reply_transform ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _reply_transform ( )
{
    typename messages :: logic_main_menu_selection_animation_transform_reply reply_msg ;
    reply_msg . transform = _logic_main_menu_selection_animation_transform_state . transform ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _compute_empty_mesh_transform ( )
{
    matrix_data transform ;
    num_fract zero ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , zero , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , zero , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , zero ) ;
    
    _logic_main_menu_selection_animation_transform_state . transform = transform ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation < mediator > :: _compute_row_rect_mesh_transform ( )
{
    matrix_data transform ;
    num_fract zero ;
    num_fract half ;
    num_fract scale_x ;
    num_fract scale_y ;
    num_fract scale_z ;
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    num_fract width ;
    num_fract height ;
    num_fract mesh_size ;
    rect row_rect ;

    row_rect = _logic_main_menu_letters_layout_row_rect_state . row_rect ;
    mesh_size = _logic_main_menu_selection_stateless_consts . get ( ) . mesh_size ;
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_math :: sub_fracts ( width , row_rect . right , row_rect . left ) ;
    platform_math :: sub_fracts ( height , row_rect . top , row_rect . bottom ) ;
    
    platform_math :: div_fracts ( scale_x , width , mesh_size ) ;
    platform_math :: div_fracts ( scale_y , height , mesh_size ) ;
    scale_z = _platform_math_consts . get ( ) . fract_1 ;

    platform_math :: add_fracts ( pos_x , row_rect . right , row_rect . left ) ;
    platform_math :: add_fracts ( pos_y , row_rect . top , row_rect . bottom ) ;
    platform_math :: div_fract_by ( pos_x , _platform_math_consts . get ( ) . fract_2 ) ;
    platform_math :: div_fract_by ( pos_y , _platform_math_consts . get ( ) . fract_2 ) ;
    pos_z = _logic_main_menu_selection_animation_consts . position_z ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , scale_x , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale_y , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale_z ) ;
    platform_matrix :: set_origin ( transform , pos_x , pos_y , pos_z ) ;
    
    _logic_main_menu_selection_animation_transform_state . transform = transform ;
}
