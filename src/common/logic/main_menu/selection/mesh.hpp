template < typename mediator >
class shy_logic_main_menu_selection_mesh
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_create ) ;
    void receive ( typename messages :: logic_main_menu_selection_mesh_destroy_request ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
} ;

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_create )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_create_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_selection_mesh < mediator > :: receive ( typename messages :: logic_main_menu_selection_mesh_destroy_request )
{
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_selection_mesh_destroy_reply ( ) ) ;
}
