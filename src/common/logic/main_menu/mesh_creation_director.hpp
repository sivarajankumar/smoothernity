template < typename mediator >
class shy_logic_main_menu_mesh_creation_director
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
} ;

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: receive ( typename messages :: init )
{
}
