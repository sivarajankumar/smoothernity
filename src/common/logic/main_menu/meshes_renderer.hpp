template < typename mediator >
class shy_logic_main_menu_meshes_renderer
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
 
    class _logic_main_menu_meshes_render_state_type
    {
    public :
        num_whole requested ;
        num_whole current_mesh_index ;
    } ;
       
    class _logic_main_menu_meshes_count_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        num_whole meshes ;
    } ;

    class _logic_main_menu_mesh_id_state_type
    {
    public :
        num_whole requested ;
        num_whole requested_index ;
        num_whole replied ;
        engine_render_mesh_id mesh ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_meshes_render ) ;
    void receive ( typename messages :: logic_main_menu_meshes_count_reply ) ;
    void receive ( typename messages :: logic_main_menu_mesh_id_reply ) ;
private :
    void _proceed_with_render ( ) ;
    void _obtain_meshes_count ( ) ;
    void _obtain_first_mesh_id ( ) ;
    void _obtain_current_mesh_id ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    
    _logic_main_menu_meshes_render_state_type _logic_main_menu_meshes_render_state ;
    _logic_main_menu_meshes_count_state_type _logic_main_menu_meshes_count_state ;
    _logic_main_menu_mesh_id_state_type _logic_main_menu_mesh_id_state ;
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
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_meshes_render )
{
    _logic_main_menu_meshes_render_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_render ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_meshes_count_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . requested ) )
    {
        _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _logic_main_menu_meshes_count_state . meshes = msg . meshes ;
        _proceed_with_render ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: receive ( typename messages :: logic_main_menu_mesh_id_reply msg )
{
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: _proceed_with_render ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_render_state . requested ) )
    {
        _logic_main_menu_meshes_render_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _obtain_meshes_count ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _logic_main_menu_meshes_count_state . replied ) )
    {
        _logic_main_menu_meshes_count_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _obtain_first_mesh_id ( ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: _obtain_meshes_count ( )
{
    _logic_main_menu_meshes_count_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: logic_main_menu_meshes_count_request ( ) ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: _obtain_first_mesh_id ( )
{
    _logic_main_menu_meshes_render_state . current_mesh_index = _platform_math_consts . get ( ) . whole_0 ;
    _obtain_current_mesh_id ( ) ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_renderer < mediator > :: _obtain_current_mesh_id ( )
{
    _logic_main_menu_mesh_id_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _logic_main_menu_mesh_id_state . requested_index = _logic_main_menu_meshes_render_state . current_mesh_index ;
    typename messages :: logic_main_menu_mesh_id_request msg ;
    msg . index = _logic_main_menu_meshes_render_state . current_mesh_index ;
    _mediator . get ( ) . send ( msg ) ;
}
