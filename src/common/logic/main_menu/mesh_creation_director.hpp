template < typename mediator >
class shy_logic_main_menu_mesh_creation_director
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_meshes_create ) ;
    void receive ( typename messages :: logic_main_menu_meshes_creation_finished ) ;
    void receive ( typename messages :: logic_main_menu_update ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    num_whole _creation_in_progress ;
} ;

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _creation_in_progress = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_meshes_create )
{
    _creation_in_progress = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_meshes_creation_finished )
{
    _creation_in_progress = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_main_menu_mesh_creation_director < mediator > :: receive ( typename messages :: logic_main_menu_update )
{
    if ( platform_conditions :: whole_is_true ( _creation_in_progress ) )
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_mesh_create_next ( ) ) ;
}
