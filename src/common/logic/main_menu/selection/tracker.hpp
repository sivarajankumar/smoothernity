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
        num_fract position_z ;
    } ;

    class _logic_main_menu_selection_track_state_type
    {
    public :
        num_whole requested ;
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
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_track ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_reply ) ;
private :
    void _proceed_with_track ( ) ;
    void _place_mesh ( ) ;
    void _obtain_row_rect ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_main_menu_selection_tracker_consts_type _logic_main_menu_selection_tracker_consts ;
    
    _logic_main_menu_selection_track_state_type _logic_main_menu_selection_track_state ;
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_tracker < mediator > :: _logic_main_menu_selection_tracker_consts_type :: _logic_main_menu_selection_tracker_consts_type ( )
{
    platform_math :: make_num_fract ( position_z , - 3 , 1 ) ;
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
        _place_mesh ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _proceed_with_track ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_selection_track_state . requested ) )
    {
        _logic_main_menu_selection_track_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_row_rect ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . replied ) )
    {
        _logic_main_menu_letters_layout_row_rect_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _place_mesh ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _obtain_row_rect ( )
{
    _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_row_rect_state . requested_row = _platform_math_consts . get ( ) . whole_0 ;

    typename messages :: logic_main_menu_letters_layout_row_rect_request msg ;
    msg . row = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_tracker < mediator > :: _place_mesh ( )
{
    matrix_data transform ;
    num_fract zero ;
    num_fract half ;
    num_fract shift ;
    
    platform_math :: make_num_fract ( zero , 0 , 1 ) ;
    platform_math :: make_num_fract ( half , 1 , 2 ) ;
    shift = _logic_main_menu_selection_tracker_consts . position_z ;
    
    platform_matrix :: identity ( transform ) ;
    platform_matrix :: set_axis_x ( transform , half , zero , zero ) ;
    platform_matrix :: set_axis_y ( transform , zero , half , zero ) ;
    platform_matrix :: set_axis_z ( transform , zero , zero , half ) ;
    platform_matrix :: set_origin ( transform , zero , zero , shift ) ;
    
    typename messages :: logic_main_menu_selection_mesh_set_transform transform_msg ;
    transform_msg . transform = transform ;
    _mediator . get ( ) . send ( transform_msg ) ;
}
