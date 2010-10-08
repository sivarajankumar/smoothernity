template < typename mediator >
class shy_logic_main_menu_selection_tracker
{
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

    class _logic_main_menu_selection_tracker_consts_type
    {
    public :
        _logic_main_menu_selection_tracker_consts_type ( ) ;
    public :
        num_fract selected_rect_vertical_scale ;
    } ;

    class _logic_main_menu_selection_track_state_type
    {
    public :
        num_whole requested ;
        num_whole current_row ;
        num_whole cursor_in_selection_rect ;
        num_whole cursor_in_prev_selection_rect ;
        num_whole prev_row_is_selected ;
        num_whole prev_selected_row_index ;
        rect prev_selection_rect ;
        rect scaled_prev_selection_rect ;
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

    class _logic_controls_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_fract cursor_x ;
        num_fract cursor_y ;
    } ;

public :
    shy_logic_main_menu_selection_tracker ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply ) ;
    void receive ( typename messages :: logic_main_menu_letters_rows_reply ) ;
    void receive ( typename messages :: logic_controls_state_reply ) ;
private :
    shy_logic_main_menu_selection_tracker < mediator > & operator= ( const shy_logic_main_menu_selection_tracker & ) ;
    void _proceed_with_track ( ) ;
    void _obtain_controls_state ( ) ;
    void _controls_state_received ( ) ;
    void _obtain_rows_count ( ) ;
    void _obtain_first_row_rect ( ) ;
    void _obtain_current_row_rect ( ) ;
    void _received_row_rect ( ) ;
    void _determine_cursor_in_selection_rect ( ) ;
    void _determine_cursor_in_prev_selection_rect ( ) ;
    void _determine_cursor_in_rect ( num_whole & result , rect row_rect ) ;
    void _scale_prev_selection_rect ( ) ;
    void _send_row_selected ( ) ;
    void _send_void_selected ( ) ;
    void _send_reply ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_tracker_consts_type _logic_main_menu_selection_tracker_consts ;
    
    _logic_controls_state_type _logic_controls_state ;
    _logic_main_menu_selection_track_state_type _logic_main_menu_selection_track_state ;
    _logic_main_menu_letters_rows_state_type _logic_main_menu_letters_rows_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_tracker < mediator > :: _logic_main_menu_selection_tracker_consts_type :: _logic_main_menu_selection_tracker_consts_type ( )
{
    platform_math :: make_num_fract ( selected_rect_vertical_scale , 20 , 10 ) ;
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
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_request )
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
void shy_logic_main_menu_selection_tracker < mediator > :: receive ( typename messages :: logic_controls_state_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . requested ) )
    {
        _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_controls_state . cursor_x = msg . cursor_x ;
        _logic_controls_state . cursor_y = msg . cursor_y ;
        _proceed_with_track ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _proceed_with_track ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . requested ) )
    {
        _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_controls_state ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . replied ) )
    {
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _controls_state_received ( ) ;
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
void shy_logic_main_menu_selection_tracker < mediator > :: _obtain_controls_state ( )
{
    _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_controls_state_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _controls_state_received ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . prev_row_is_selected ) )
    {
        _determine_cursor_in_prev_selection_rect ( ) ;
        if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . cursor_in_prev_selection_rect ) )
            _send_reply ( ) ;
        else
            _obtain_rows_count ( ) ;
    }
    else
        _obtain_rows_count ( ) ;
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
    num_whole cursor_in_selection_rect ;
    num_whole current_row ;
    num_whole rows_count ;
    
    _determine_cursor_in_selection_rect ( ) ;
    
    cursor_in_selection_rect = _logic_main_menu_selection_track_state . cursor_in_selection_rect ;
    current_row = _logic_main_menu_selection_track_state . current_row ;
    rows_count = _logic_main_menu_letters_rows_state . rows ;
    
    if ( platform_conditions :: whole_is_true ( cursor_in_selection_rect ) )
    {
        _send_row_selected ( ) ;
        _send_reply ( ) ;
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
            _send_void_selected ( ) ;
            _send_reply ( ) ;
        }
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _determine_cursor_in_selection_rect ( )
{
    _determine_cursor_in_rect
        ( _logic_main_menu_selection_track_state . cursor_in_selection_rect
        , _logic_main_menu_letters_layout_row_rect_state . row_rect
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _determine_cursor_in_prev_selection_rect ( )
{
    _scale_prev_selection_rect ( ) ;
    _determine_cursor_in_rect
        ( _logic_main_menu_selection_track_state . cursor_in_prev_selection_rect
        , _logic_main_menu_selection_track_state . scaled_prev_selection_rect
        ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _determine_cursor_in_rect ( num_whole & result , rect row_rect )
{
    num_fract cursor_x ;
    num_fract cursor_y ;
    
    cursor_x = _logic_controls_state . cursor_x ;
    cursor_y = _logic_controls_state . cursor_y ;
    
    if ( platform_conditions :: fract_less_than_fract ( cursor_x , row_rect . left ) 
      || platform_conditions :: fract_less_than_fract ( cursor_y , row_rect . bottom ) 
      || platform_conditions :: fract_greater_than_fract ( cursor_x , row_rect . right ) 
      || platform_conditions :: fract_greater_than_fract ( cursor_y , row_rect . top ) 
       )
    {
        result = _platform_math_consts . get ( ) . whole_false ;
    }
    else
        result = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _scale_prev_selection_rect ( )
{
    num_fract selected_rect_vertical_scale ;
    num_fract rect_height ;
    num_fract scaled_rect_height ;
    num_fract half_scaled_rect_height ;
    num_fract y_center ;
    rect prev_selection_rect ;
    rect scaled_prev_selection_rect ;
    
    selected_rect_vertical_scale = _logic_main_menu_selection_tracker_consts . selected_rect_vertical_scale ;
    prev_selection_rect = _logic_main_menu_selection_track_state . prev_selection_rect ;
    
    platform_math :: add_fracts ( y_center , prev_selection_rect . top , prev_selection_rect . bottom ) ;
    platform_math :: div_fract_by ( y_center , _platform_math_consts . get ( ) . fract_2 ) ;
    
    platform_math :: sub_fracts ( rect_height , prev_selection_rect . top , prev_selection_rect . bottom ) ;
    platform_math :: mul_fracts ( scaled_rect_height , rect_height , selected_rect_vertical_scale ) ;
    platform_math :: div_fracts ( half_scaled_rect_height , scaled_rect_height , _platform_math_consts . get ( ) . fract_2 ) ;
    
    scaled_prev_selection_rect = prev_selection_rect ;
    platform_math :: add_fracts ( scaled_prev_selection_rect . top , y_center , half_scaled_rect_height ) ;
    platform_math :: sub_fracts ( scaled_prev_selection_rect . bottom , y_center , half_scaled_rect_height ) ;
    
    _logic_main_menu_selection_track_state . scaled_prev_selection_rect = scaled_prev_selection_rect ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _send_row_selected ( )
{
    num_whole prev_row_is_selected ;
    num_whole prev_selected_row_index ;
    num_whole current_row ;
    rect row_rect ;
    
    prev_row_is_selected = _logic_main_menu_selection_track_state . prev_row_is_selected ;
    prev_selected_row_index = _logic_main_menu_selection_track_state . prev_selected_row_index ;
    current_row = _logic_main_menu_selection_track_state . current_row ;
    row_rect = _logic_main_menu_letters_layout_row_rect_state . row_rect ;
    
    if ( ! platform_conditions :: whole_is_true ( prev_row_is_selected ) 
      || ! platform_conditions :: wholes_are_equal ( prev_selected_row_index , current_row )
       )
    {
        prev_row_is_selected = _platform_math_consts . get ( ) . whole_true ;
        prev_selected_row_index = current_row ;
        
        _logic_main_menu_selection_track_state . prev_row_is_selected = prev_row_is_selected ;
        _logic_main_menu_selection_track_state . prev_selected_row_index = prev_selected_row_index ;
        _logic_main_menu_selection_track_state . prev_selection_rect = row_rect ;

        typename messages :: logic_main_menu_selection_track_row_selected msg ;
        msg . row = _logic_main_menu_selection_track_state . current_row ;
        _mediator . get ( ) . send ( msg ) ;        
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _send_void_selected ( )
{
    if ( ! platform_conditions :: whole_is_false ( _logic_main_menu_selection_track_state . prev_row_is_selected ) )
    {
        _logic_main_menu_selection_track_state . prev_row_is_selected = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_track_void_selected ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _send_reply ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_track_reply ( ) ) ;
}
