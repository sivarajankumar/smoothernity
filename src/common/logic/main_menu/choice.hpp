template < typename mediator >
class shy_logic_main_menu_choice
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_touch platform_touch ;    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
    void receive ( typename messages :: logic_main_menu_choice_row_selected ) ;
    void receive ( typename messages :: logic_main_menu_choice_void_selected ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < platform_touch > _platform_touch ;
    
    num_whole _prev_touch_occured ;
    num_whole _prev_mouse_button ;
    num_whole _row_selected ;
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
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_touch = platform_obj . get ( ) . touch ;
    
    _prev_touch_occured = _platform_math_consts . get ( ) . whole_false ;
    _prev_mouse_button = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_choice_row_selected )
{
    _row_selected = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_choice_void_selected )
{
    _row_selected = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_choice < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    num_whole touch_occured ;
    num_whole mouse_button ;
    _platform_touch . get ( ) . occured ( touch_occured ) ;
    _platform_mouse . get ( ) . left_button_down ( mouse_button ) ;
    if ( ( platform_conditions :: whole_is_false ( touch_occured ) && platform_conditions :: whole_is_true ( _prev_touch_occured ) )
      || ( platform_conditions :: whole_is_false ( mouse_button ) && platform_conditions :: whole_is_true ( _prev_mouse_button ) )
       )
    {
        if ( platform_conditions :: whole_is_true ( _row_selected ) )
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_row_chosen ( ) ) ;
        else
            _mediator . get ( ) . send ( typename messages :: logic_main_menu_void_chosen ( ) ) ;
    }
    _prev_touch_occured = touch_occured ;
    _prev_mouse_button = mouse_button ;
}
