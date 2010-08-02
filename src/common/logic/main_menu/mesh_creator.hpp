template < typename mediator >
class shy_logic_main_menu_mesh_creator
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: main_menu_letter_added msg ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
} ;

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: init msg )
{
}

template < typename mediator >
void shy_logic_main_menu_mesh_creator < mediator > :: receive ( typename messages :: main_menu_letter_added msg )
{
}
