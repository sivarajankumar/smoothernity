template < typename mediator >
class shy_logic_main_menu_choice
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

    class _logic_controls_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole primary_button_down ;
    } ;

    class _logic_main_menu_update_state_type
    {
    public :
        num_whole requested ;
        num_whole prev_primary_button_down ;
        num_whole row_selected ;
    } ;

public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_controls_state_reply ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_choice_row_selected ) ;
    void receive ( typename messages :: logic_main_menu_choice_void_selected ) ;
private :
    void _proceed_with_update ( ) ;
    void _obtain_controls_state ( ) ;
    void _controls_state_received ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    _logic_controls_state_type _logic_controls_state ;
    _logic_main_menu_update_state_type _logic_main_menu_update_state ;    
} ;

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _logic_main_menu_update_state . prev_primary_button_down = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_choice_row_selected )
{
    _logic_main_menu_update_state . row_selected = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_choice_void_selected )
{
    _logic_main_menu_update_state . row_selected = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_update ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_controls_state_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . requested ) )
    {
        _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_controls_state . primary_button_down = msg . primary_button_down ;
        _proceed_with_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: _proceed_with_update ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_update_state . requested ) )
    {
        _logic_main_menu_update_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_controls_state ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_controls_state . replied ) )
    {
        _logic_controls_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _controls_state_received ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: _obtain_controls_state ( )
{
    _logic_controls_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_controls_state_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: _controls_state_received ( )
{
    num_whole row_selected ;
    num_whole primary_button_down ;
    num_whole prev_primary_button_down ;

    row_selected = _logic_main_menu_update_state . row_selected ;
    primary_button_down = _logic_controls_state . primary_button_down ;
    prev_primary_button_down = _logic_main_menu_update_state . prev_primary_button_down ;    

    if ( platform_conditions :: whole_is_false ( primary_button_down ) 
      && platform_conditions :: whole_is_true ( prev_primary_button_down )
       )
    {
        if ( platform_conditions :: whole_is_true ( row_selected ) )
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_row_chosen ( ) ) ;
        else
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_void_chosen ( ) ) ;
    }

    prev_primary_button_down = primary_button_down ;
    _logic_main_menu_update_state . prev_primary_button_down = prev_primary_button_down ;
}
