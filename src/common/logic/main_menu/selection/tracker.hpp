template < typename mediator >
class shy_logic_main_menu_selection_tracker
{
    typedef typename mediator :: engine_math :: rect rect ;
    typedef typename mediator :: logic_main_menu_selection_stateless :: logic_main_menu_selection_stateless_consts_type logic_main_menu_selection_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_selection_tracker_consts_type
    {
    public :
        _logic_main_menu_selection_tracker_consts_type ( ) ;
    public :
        num_fract position_z ;
    } ;

    class _logic_main_menu_selection_track_state_type
    {
    public :
        num_whole requested ;
        num_whole current_row ;
        num_whole under_mouse_cursor ;
        matrix_data transform ;
    } ;

    class _logic_main_menu_letters_rows_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole rows ;
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
    shy_logic_main_menu_selection_tracker ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_track ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_rows_reply ) ;
private :
    shy_logic_main_menu_selection_tracker < mediator > & operator= ( const shy_logic_main_menu_selection_tracker & ) ;
    void _proceed_with_track ( ) ;
    void _obtain_rows_count ( ) ;
    void _obtain_first_row_rect ( ) ;
    void _obtain_current_row_rect ( ) ;
    void _received_row_rect ( ) ;
    void _determine_mouse_selection ( ) ;
    void _compute_row_rect_mesh_transform ( ) ;
    void _compute_empty_mesh_transform ( ) ;
    void _place_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_selection_stateless_consts_type > _logic_main_menu_selection_stateless_consts ;
    const _logic_main_menu_selection_tracker_consts_type _logic_main_menu_selection_tracker_consts ;
    
    _logic_main_menu_selection_track_state_type _logic_main_menu_selection_track_state ;
    _logic_main_menu_letters_rows_state_type _logic_main_menu_letters_rows_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_tracker < mediator > :: _logic_main_menu_selection_tracker_consts_type :: _logic_main_menu_selection_tracker_consts_type ( )
{
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_tracker < mediator > :: shy_logic_main_menu_selection_tracker ( )
{
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . logic_main_menu_selection_stateless_consts ( _logic_main_menu_selection_stateless_consts ) ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_main_menu_selection_track )
{
    _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_track ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . requested )
      && platform_conditions :: wholes_are_equal ( _logic_main_menu_letters_layout_row_rect_state . requested_row , msg . row )
       )
    {
        _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_layout_row_rect_state . row_rect = msg . row_rect ;
        _proceed_with_track ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_main_menu_letters_rows_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . requested ) )
    {
        _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_rows_state . rows = msg . rows ;
        _proceed_with_track ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _proceed_with_track ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . requested ) )
    {
        _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_rows_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_rows_state . replied ) )
    {
        _logic_main_menu_letters_rows_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_first_row_rect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . replied ) )
    {
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _received_row_rect ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _obtain_rows_count ( )
{
    _logic_main_menu_letters_rows_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_rows_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _obtain_first_row_rect ( )
{
    _logic_main_menu_selection_track_state . current_row = _platform_math_consts . get ( ) . whole_0 ;
    _obtain_current_row_rect ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _obtain_current_row_rect ( )
{
    _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_row_rect_state . requested_row = _logic_main_menu_selection_track_state . current_row ;

    typename messages :: logic_main_menu_letters_layout_row_rect_request msg ;
    msg . row = _logic_main_menu_letters_layout_row_rect_state . requested_row ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _received_row_rect ( )
{
    num_whole under_mouse_cursor ;
    num_whole current_row ;
    num_whole rows_count ;
    
    _determine_mouse_selection ( ) ;
    
    under_mouse_cursor = _logic_main_menu_selection_track_state . under_mouse_cursor ;
    current_row = _logic_main_menu_selection_track_state . current_row ;
    rows_count = _logic_main_menu_letters_rows_state . rows ;
    
    if ( platform_conditions :: whole_is_true ( under_mouse_cursor ) )
    {
        _compute_row_rect_mesh_transform ( ) ;
        _place_mesh ( ) ;
    }
    else
    {
        platform_math :: inc_whole ( current_row ) ;
        if ( platform_conditions :: whole_less_than_whole ( current_row , rows_count ) )
        {
            _logic_main_menu_selection_track_state . current_row = current_row ;
            _obtain_current_row_rect ( ) ;
        }
        else
        {
            _compute_empty_mesh_transform ( ) ;
            _place_mesh ( ) ;
        }
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _determine_mouse_selection ( )
{
    num_whole under_mouse_cursor ;
    num_fract mouse_x ;
    num_fract mouse_y ;
    rect row_rect ;
        
    row_rect = _logic_main_menu_letters_layout_row_rect_state . row_rect ;

    _platform_mouse . get ( ) . x ( mouse_x ) ;
    _platform_mouse . get ( ) . y ( mouse_y ) ;
    
    if ( platform_conditions :: fract_less_than_fract ( mouse_x , row_rect . left ) 
      || platform_conditions :: fract_less_than_fract ( mouse_y , row_rect . bottom ) 
      || platform_conditions :: fract_greater_than_fract ( mouse_x , row_rect . right ) 
      || platform_conditions :: fract_greater_than_fract ( mouse_y , row_rect . top ) 
       )
    {
        under_mouse_cursor = _platform_math_consts . get ( ) . whole_false ;
    }
    else
        under_mouse_cursor = _platform_math_consts . get ( ) . whole_true ;
    
    _logic_main_menu_selection_track_state . under_mouse_cursor = under_mouse_cursor ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _compute_empty_mesh_transform ( )
{
    matrix_data transform ;
    num_fract zero ;
    
    zero = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , zero , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , zero , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , zero ) ;
    
    _logic_main_menu_selection_track_state . transform = transform ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _compute_row_rect_mesh_transform ( )
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
    pos_z = _logic_main_menu_selection_tracker_consts . position_z ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , scale_x , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , scale_y , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , scale_z ) ;
    platform_matrix :: set_origin ( transform , pos_x , pos_y , pos_z ) ;
    
    _logic_main_menu_selection_track_state . transform = transform ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _place_mesh ( )
{
    typename messages :: logic_main_menu_selection_mesh_set_transform transform_msg ;
    transform_msg . transform = _logic_main_menu_selection_track_state . transform ;
    _mediator . get ( ) . send ( transform_msg ) ;
}
