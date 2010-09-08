template < typename mediator >
class shy_logic_main_menu_letters_layout_row_rect
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_letters_layout_row_rect_request ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
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
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_letters_layout_row_rect < mediator > :: receive ( typename messages :: logic_main_menu_letters_layout_row_rect_request msg )
{
    typename messages :: logic_main_menu_letters_layout_row_rect_reply reply_msg ;
    reply_msg . row = msg . row ;
    reply_msg . row_rect . left = _platform_math_consts . get ( ) . fract_minus_1 ;
    reply_msg . row_rect . right = _platform_math_consts . get ( ) . fract_1 ;
    reply_msg . row_rect . bottom = _platform_math_consts . get ( ) . fract_minus_1 ;
    reply_msg . row_rect . top = _platform_math_consts . get ( ) . fract_1 ;
    _mediator . get ( ) . send ( reply_msg ) ;
}
