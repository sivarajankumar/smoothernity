template < typename mediator >
class shy_engine_mesh
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: render_index_buffer_id render_index_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: render_vertex_buffer_id render_vertex_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    static const_int_32 _max_meshes = 100 ;
    static const_int_32 _max_vertices = 1000 ;
    static const_int_32 _max_indices = 1000 ;
    
public :
    class mesh_id
    {
        friend class shy_engine_mesh ;
    private :
        num_whole _mesh_id ;
    } ;
private :
    class _mesh_data
    {
    public :
        render_vertex_buffer_id vertex_buffer_id ;
        render_index_buffer_id triangle_strip_index_buffer_id ;
        render_index_buffer_id triangle_fan_index_buffer_id ;
        num_whole vertices_count ;
        num_whole triangle_strip_indices_count ;
        num_whole triangle_fan_indices_count ;
        matrix_data transform ;
        typename platform_static_array :: template static_array < vertex_data , _max_vertices > vertices ;
        typename platform_static_array :: template static_array < index_data , _max_indices > triangle_strip_indices ;
        typename platform_static_array :: template static_array < index_data , _max_indices > triangle_fan_indices ;
    } ;
public :
    shy_engine_mesh ( ) ;
    void mesh_create ( mesh_id & mesh , num_whole vertices_count , num_whole triangle_strip_indices_count , num_whole triangle_fan_indices_count ) ;
    void receive ( typename messages :: mesh_finalize msg ) ;
    void receive ( typename messages :: mesh_set_vertex_position msg ) ;
    void receive ( typename messages :: mesh_set_vertex_tex_coord msg ) ;
    void mesh_set_vertex_color ( mesh_id mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void receive ( typename messages :: mesh_set_triangle_strip_index_value msg ) ;
    void receive ( typename messages :: mesh_set_triangle_fan_index_value msg ) ;
    void receive ( typename messages :: mesh_set_transform msg ) ;
    void receive ( typename messages :: mesh_render msg ) ;
    void receive ( typename messages :: mesh_delete msg ) ;
private :
    num_whole _next_mesh_id ;
    typename platform_static_array :: template static_array < _mesh_data , _max_meshes > _meshes_data ;
} ;

template < typename mediator >
shy_engine_mesh < mediator > :: shy_engine_mesh ( )
{
    platform_math :: make_num_whole ( _next_mesh_id , 0 ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: mesh_create ( mesh_id & result , num_whole vertices_count , num_whole triangle_strip_indices_count , num_whole triangle_fan_indices_count )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , _next_mesh_id ) ;
    mesh . vertices_count = vertices_count ;
    mesh . triangle_strip_indices_count = triangle_strip_indices_count ;
    mesh . triangle_fan_indices_count = triangle_fan_indices_count ;
    platform_matrix :: identity ( mesh . transform ) ;
    result . _mesh_id = _next_mesh_id ;
    platform_math :: inc_whole ( _next_mesh_id ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_finalize msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: create_vertex_buffer ( mesh . vertex_buffer_id , mesh . vertices_count , mesh . vertices ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
    {
        platform_render :: create_index_buffer 
            ( mesh . triangle_strip_index_buffer_id 
            , mesh . triangle_strip_indices_count 
            , mesh . triangle_strip_indices 
            ) ;
    }
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
    {
        platform_render :: create_index_buffer 
            ( mesh . triangle_fan_index_buffer_id 
            , mesh . triangle_fan_indices_count 
            , mesh . triangle_fan_indices 
            ) ;
    }
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_vertex_position msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , msg . offset ) ;
    platform_render :: set_vertex_position ( vertex , msg . x , msg . y , msg . z ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_vertex_tex_coord msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , msg . offset ) ;
    platform_render :: set_vertex_tex_coord ( vertex , msg . u , msg . v ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: mesh_set_vertex_color ( mesh_id arg_mesh , num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , arg_mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , offset ) ;
    platform_render :: set_vertex_color ( vertex , r , g , b , a ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_triangle_strip_index_value msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    index_data & index = platform_static_array :: element ( mesh . triangle_strip_indices , msg . offset ) ;
    platform_render :: set_index_value ( index , msg . index ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_triangle_fan_index_value msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    index_data & index = platform_static_array :: element ( mesh . triangle_fan_indices , msg . offset ) ;
    platform_render :: set_index_value ( index , msg . index ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_delete msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: delete_vertex_buffer ( mesh . vertex_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
        platform_render :: delete_index_buffer ( mesh . triangle_strip_index_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
        platform_render :: delete_index_buffer ( mesh . triangle_fan_index_buffer_id ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_render msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: matrix_push ( ) ;
    platform_render :: matrix_mult ( mesh . transform ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
    {
        platform_render :: draw_triangle_strip 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_strip_index_buffer_id 
            , mesh . triangle_strip_indices_count
            ) ;
    }
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
    {
        platform_render :: draw_triangle_fan 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_fan_index_buffer_id 
            , mesh . triangle_fan_indices_count
            ) ;
    }
    platform_render :: matrix_pop ( ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_transform msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    mesh . transform = msg . transform ;
}
