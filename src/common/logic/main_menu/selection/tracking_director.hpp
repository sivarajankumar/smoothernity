template < typename mediator >
class shy_logic_main_menu_selection_tracking_director
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_selection_tracking_director_update_state_type
    {
    public :
        num_whole requested ;
        num_whole row_selected ;
        num_whole selected_row_index ;
        num_whole selection_animation_in_progress ;
        num_whole unselection_animation_in_progress ;
    } ;
    
    class _logic_main_menu_selection_track_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_tracking_director_update ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_reply ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_row_selected ) ;
    void receive ( typename messages :: logic_main_menu_selection_track_void_selected ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_select_finished ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_unselect_finished ) ;
private :
    void _proceed_with_tracking ( ) ;
    void _update_received ( ) ;
    void _request_track ( ) ;
    void _place_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_selection_tracking_director_update_state_type _logic_main_menu_selection_tracking_director_update_state ;
    _logic_main_menu_selection_track_state_type _logic_main_menu_selection_track_state ;
} ;

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _logic_main_menu_selection_tracking_director_update_state . selection_animation_in_progress = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_selection_tracking_director_update_state . unselection_animation_in_progress = _platform_math_consts . get ( ) . whole_false ;
    _logic_main_menu_selection_tracking_director_update_state . row_selected = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_tracking_director_update )
{
    _logic_main_menu_selection_tracking_director_update_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_tracking ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_reply )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . requested ) )
    {
        _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_selection_track_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_tracking ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_row_selected msg )
{
    num_whole prev_row_selected ;
    
    prev_row_selected = _logic_main_menu_selection_tracking_director_update_state . row_selected ;
    _logic_main_menu_selection_tracking_director_update_state . row_selected = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_selection_tracking_director_update_state . selected_row_index = msg . row ;
    
    if ( platform_conditions :: whole_is_true ( prev_row_selected ) )
    {
        _logic_main_menu_selection_tracking_director_update_state . unselection_animation_in_progress = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_unselect_start ( ) ) ;
    }
    else
    {        
        _logic_main_menu_selection_tracking_director_update_state . selection_animation_in_progress = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_select_start ( ) ) ;
        
        typename messages :: logic_main_menu_selection_animation_idle_row_selected idle_row_selected_msg ;
        idle_row_selected_msg . row = _logic_main_menu_selection_tracking_director_update_state . selected_row_index ;
        _mediator . get ( ) . send ( idle_row_selected_msg ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_track_void_selected )
{
    num_whole prev_row_selected ;
    
    prev_row_selected = _logic_main_menu_selection_tracking_director_update_state . row_selected ;
    _logic_main_menu_selection_tracking_director_update_state . row_selected = _platform_math_consts . get ( ) . whole_false ;
    
    if ( platform_conditions :: whole_is_true ( prev_row_selected ) )
    {
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_unselect_start ( ) ) ;
        _logic_main_menu_selection_tracking_director_update_state . unselection_animation_in_progress = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_select_finished )
{
    _logic_main_menu_selection_tracking_director_update_state . selection_animation_in_progress = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_unselect_finished )
{
    _logic_main_menu_selection_tracking_director_update_state . unselection_animation_in_progress = _platform_math_consts . get ( ) . whole_false ;
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_tracking_director_update_state . row_selected ) )
    {        
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_select_start ( ) ) ;
        _logic_main_menu_selection_tracking_director_update_state . selection_animation_in_progress = _platform_math_consts . get ( ) . whole_true ;
        typename messages :: logic_main_menu_selection_animation_idle_row_selected idle_row_selected_msg ;
        idle_row_selected_msg . row = _logic_main_menu_selection_tracking_director_update_state . selected_row_index ;
        _mediator . get ( ) . send ( idle_row_selected_msg ) ;
    }
    else
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_animation_idle_void_selected ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: _proceed_with_tracking ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_tracking_director_update_state . requested ) )
    {
        _logic_main_menu_selection_tracking_director_update_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _update_received ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . replied ) )
    {
        _logic_main_menu_selection_track_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _place_mesh ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: _update_received ( )
{
    if ( platform_conditions :: whole_is_false ( _logic_main_menu_selection_tracking_director_update_state . selection_animation_in_progress ) 
      && platform_conditions :: whole_is_false ( _logic_main_menu_selection_tracking_director_update_state . unselection_animation_in_progress )
       )
    {
        _request_track ( ) ;
    }
    else
        _place_mesh ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: _request_track ( )
{
    _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_track_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracking_director < mediator > :: _place_mesh ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_place ( ) ) ;
}
