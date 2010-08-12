template < typename mediator >
class shy_logic_main_menu_meshes_storage
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator :: logic_text_stateless logic_text_stateless ;
    typedef typename mediator :: logic_text_stateless :: logic_text_alphabet_english_type logic_text_alphabet_english_type ;
    typedef typename mediator :: logic_text_stateless :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: logic_text_stateless :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    class _logic_main_menu_meshes_storage_consts_type
    {
    public :
        static const_int_32 max_meshes 
            = logic_main_menu_stateless_consts_type :: max_rows 
            * logic_main_menu_stateless_consts_type :: max_cols
            ;
    } ;

    class _mesh_state
    {
    public :
        engine_render_mesh_id mesh ;
        num_whole row ;
        num_whole col ;
    } ;
    
public :
	shy_logic_main_menu_meshes_storage ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_main_menu_mesh_has_been_created ) ;
    void receive ( typename messages :: logic_main_menu_meshes_render ) ;
private :
	shy_logic_main_menu_meshes_storage < mediator > & operator= ( const shy_logic_main_menu_meshes_storage < mediator > & ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;    
    typename platform_static_array :: template static_array < _mesh_state , _logic_main_menu_meshes_storage_consts_type :: max_meshes > _meshes ;
    num_whole _meshes_count ;
} ;

template < typename mediator >
shy_logic_main_menu_meshes_storage < mediator > :: shy_logic_main_menu_meshes_storage ( )
{
}

template < typename mediator >
shy_logic_main_menu_meshes_storage < mediator > & 
shy_logic_main_menu_meshes_storage < mediator > :: operator= ( const shy_logic_main_menu_meshes_storage < mediator > & )
{
	return * this ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_storage < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_storage < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;

    _meshes_count = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_main_menu_meshes_storage < mediator > :: receive ( typename messages :: logic_main_menu_meshes_render )
{
    for ( num_whole i = _platform_math_consts . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _meshes_count )
        ; platform_math :: inc_whole ( i )
        )
    {
        typename platform_pointer :: template pointer < engine_render_mesh_id > mesh ;
        platform_static_array :: element_ptr ( mesh , _meshes , i ) ;
        
        typename messages :: engine_render_mesh_render render_msg ;
        render_msg . mesh = mesh ;
        _mediator . get ( ) . send ( render_msg ) ;
    }
}

template < typename mediator >
void shy_logic_main_menu_meshes_storage < mediator > :: receive ( typename messages :: logic_main_menu_mesh_has_been_created msg )
{
    typename platform_pointer :: template pointer < _mesh_state > mesh_state ;
    platform_static_array :: element_ptr ( mesh_state , _meshes , _meshes_count ) ;
    mesh_state . get ( ) . mesh = msg . mesh ;
    mesh_state . get ( ) . row = msg . row ;
    mesh_state . get ( ) . col = msg . col ;
    platform_math :: inc_whole ( _meshes_count ) ;
}
