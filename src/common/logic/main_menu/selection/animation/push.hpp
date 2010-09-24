template < typename mediator >
class shy_logic_main_menu_selection_animation_push
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_animation_push_transform_request ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_animation_push < mediator > :: receive ( typename messages :: logic_main_menu_selection_animation_push_transform_request )
{
    typename messages :: logic_main_menu_selection_animation_push_transform_reply msg ;
    msg . scale_x = _platform_math_consts . get ( ) . fract_1 ;
    msg . scale_y = _platform_math_consts . get ( ) . fract_1 ;
    _mediator . get ( ) . send ( msg ) ;
}
