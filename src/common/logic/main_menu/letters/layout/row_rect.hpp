template < typename mediator >
class shy_logic_main_menu_letters_layout_row_rect
{
    typedef typename mediator :: logic_main_menu_letters_layout_stateless :: logic_main_menu_letters_layout_stateless_consts_type logic_main_menu_letters_layout_stateless_consts_type ;
    typedef typename mediator :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    
    class _logic_main_menu_letters_layout_row_rect_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_row ;
    } ;
    
    class _logic_main_menu_letters_boundaries_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole rows ;
        num_whole cols ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_boundaries_reply ) ;
private :
    void _proceed_with_row_rect ( ) ;
    void _obtain_boundaries ( ) ;
    void _reply_row_rect ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_meshes_stateless_consts_type > _logic_main_menu_letters_meshes_stateless_consts ;
    typename platform_pointer :: template pointer < const logic_main_menu_letters_layout_stateless_consts_type > _logic_main_menu_letters_layout_stateless_consts ;
    
    _logic_main_menu_letters_layout_row_rect_state_type _logic_main_menu_letters_layout_row_rect_state ;
    _logic_main_menu_letters_boundaries_state_type _logic_main_menu_letters_boundaries_state ;
} ;

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . logic_main_menu_letters_meshes_stateless_consts ( _logic_main_menu_letters_meshes_stateless_consts ) ;
    _mediator . get ( ) . logic_main_menu_letters_layout_stateless_consts ( _logic_main_menu_letters_layout_stateless_consts ) ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_row_rect_request msg )
{
    _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_letters_layout_row_rect_state . requested_row = msg . row ;
    _proceed_with_row_rect ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: receive ( typename messages :: logic_main_menu_letters_boundaries_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_boundaries_state . requested ) )
    {
        _logic_main_menu_letters_boundaries_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_letters_boundaries_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_letters_boundaries_state . rows = msg . rows ;
        _logic_main_menu_letters_boundaries_state . cols = msg . cols ;
        _proceed_with_row_rect ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: _proceed_with_row_rect ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_layout_row_rect_state . requested ) )
    {
        _logic_main_menu_letters_layout_row_rect_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_boundaries ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_letters_boundaries_state . replied ) )
    {
        _logic_main_menu_letters_boundaries_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _reply_row_rect ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: _obtain_boundaries ( )
{
    _logic_main_menu_letters_boundaries_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_boundaries_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: _reply_row_rect ( )
{
    typename messages :: logic_main_menu_letters_layout_row_rect_reply reply_msg ;
    reply_msg . row = _logic_main_menu_letters_layout_row_rect_state . requested_row ;
    reply_msg . row_rect . left = _platform_math_consts . get ( ) . fract_minus_1 ;
    reply_msg . row_rect . right = _platform_math_consts . get ( ) . fract_1 ;
    reply_msg . row_rect . bottom = _platform_math_consts . get ( ) . fract_minus_1 ;
    reply_msg . row_rect . top = _platform_math_consts . get ( ) . fract_1 ;
    _mediator . get ( ) . send ( reply_msg ) ;
}
