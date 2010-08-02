template < typename mediator >
class shy_logic_main_menu_mesh_creator
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: main_menu_mesh_create ) ;
    void receive ( typename messages :: main_menu_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
} ;

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: init )
{
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_mesh_create )
{
    _mediator . get ( ) . send ( typename messages :: main_menu_mesh_create_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_update )
{
}
