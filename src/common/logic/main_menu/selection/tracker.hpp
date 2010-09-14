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
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_main_menu_selection_track_state_type
    {
    public :
        num_whole requested ;
        num_whole current_row ;
        num_whole under_mouse_cursor ;
        num_whole prev_row_is_selected ;
        num_whole prev_selected_row_index ;
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
    void _send_row_selected ( ) ;
    void _send_void_selected ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_selection_track_state_type _logic_main_menu_selection_track_state ;
    _logic_main_menu_letters_rows_state_type _logic_main_menu_letters_rows_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
} ;

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
        _send_row_selected ( ) ;
    else
    {
        platform_math :: inc_whole ( current_row ) ;
        if ( platform_conditions :: whole_less_than_whole ( current_row , rows_count ) )
        {
            _logic_main_menu_selection_track_state . current_row = current_row ;
            _obtain_current_row_rect ( ) ;
        }
        else
            _send_void_selected ( ) ;
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
void shy_logic_main_menu_selection_tracker < mediator > :: _send_row_selected ( )
{
    num_whole prev_row_is_selected ;
    num_whole prev_selected_row_index ;
    num_whole current_row ;
    
    prev_row_is_selected = _logic_main_menu_selection_track_state . prev_row_is_selected ;
    prev_selected_row_index = _logic_main_menu_selection_track_state . prev_selected_row_index ;
    current_row = _logic_main_menu_selection_track_state . current_row ;
    
    if ( ! platform_conditions :: whole_is_true ( prev_row_is_selected ) 
    ||   ! platform_conditions :: wholes_are_equal ( prev_selected_row_index , current_row )
       )
    {
        prev_row_is_selected = _platform_math_consts . get ( ) . whole_true ;
        prev_selected_row_index = current_row ;
        
        _logic_main_menu_selection_track_state . prev_row_is_selected = prev_row_is_selected ;
        _logic_main_menu_selection_track_state . prev_selected_row_index = prev_selected_row_index ;

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
