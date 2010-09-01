template < typename mediator >
class shy_logic_main_menu_meshes_renderer
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
 
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_meshes_render_request ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_iteration ) ;
    void receive ( typename messages :: logic_main_menu_letters_meshes_iterate_finished ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;

    num_whole _iteration_in_progress ;
} ;

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_meshes_render_request )
{
    _iteration_in_progress = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_letters_meshes_iterate_start ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_iteration msg )
{
    if ( platform_conditions :: whole_is_true ( _iteration_in_progress ) )
    {
        typename messages :: engine_render_mesh_render render_msg ;
        render_msg . mesh = msg . mesh ;
        _mediator . get ( ) . send ( render_msg ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_letters_meshes_iterate_finished )
{
    if ( platform_conditions :: whole_is_true ( _iteration_in_progress ) )
    {
        _iteration_in_progress = _platform_math_consts . get ( ) . whole_false ;
        _mediator . get ( ) . send ( typename messages :: logic_main_menu_meshes_render_reply ( ) ) ;
    }
}
