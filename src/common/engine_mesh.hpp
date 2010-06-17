template < typename mediator >
class shy_engine_mesh
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
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
        num_whole triangle_strip_indices_count ;
        num_whole triangle_fan_indices_count ;
        matrix_data transform ;
    } ;
public :
    shy_engine_mesh ( ) ;
    template 
        < typename vertex_array 
        , typename strip_index_array
        , typename fan_index_array
        > 
    void mesh_create 
        ( mesh_id & result
        , const vertex_array & vertices 
        , const strip_index_array & triangle_strip_indices 
        , const fan_index_array & triangle_fan_indices
        , num_whole vertices_count
        , num_whole triangle_strip_indices_count 
        , num_whole triangle_fan_indices_count
        ) ;
    void receive ( typename messages :: mesh_delete msg ) ;
    void receive ( typename messages :: mesh_render msg ) ;
    void receive ( typename messages :: mesh_set_transform msg ) ;
private :
    num_whole _next_mesh_id ;
    typename platform_static_array :: template static_array < _mesh_data , _max_meshes > _meshes_data ;
} ;

template < typename mediator >
shy_engine_mesh < mediator > :: shy_engine_mesh ( )
{
    platform_math :: math_make_num_whole ( _next_mesh_id , 0 ) ;
}

template < typename mediator >
template 
    < typename vertex_array 
    , typename strip_index_array 
    , typename fan_index_array
    >
void shy_engine_mesh < mediator > :: mesh_create 
    ( mesh_id & result
    , const vertex_array & vertices 
    , const strip_index_array & triangle_strip_indices 
    , const fan_index_array & triangle_fan_indices
    , num_whole vertices_count
    , num_whole triangle_strip_indices_count
    , num_whole triangle_fan_indices_count
    )
{
    _mesh_data & mesh = platform_static_array :: array_element ( _meshes_data , _next_mesh_id ) ;
    mesh . triangle_strip_indices_count = triangle_strip_indices_count ;
    mesh . triangle_fan_indices_count = triangle_fan_indices_count ;
    platform_matrix :: matrix_identity ( mesh . transform ) ;
    platform_render :: render_create_vertex_buffer ( mesh . vertex_buffer_id , vertices_count , vertices ) ;
    if ( platform_conditions :: condition_whole_greater_than_zero ( triangle_strip_indices_count ) )
    {
        platform_render :: render_create_index_buffer 
            ( mesh . triangle_strip_index_buffer_id 
            , triangle_strip_indices_count 
            , triangle_strip_indices 
            ) ;
    }
    if ( platform_conditions :: condition_whole_greater_than_zero ( triangle_fan_indices_count ) )
    {
        platform_render :: render_create_index_buffer 
            ( mesh . triangle_fan_index_buffer_id 
            , triangle_fan_indices_count 
            , triangle_fan_indices 
            ) ;
    }
    result . _mesh_id = _next_mesh_id ;
    platform_math :: math_inc_whole ( _next_mesh_id ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_delete msg )
{
    _mesh_data & mesh = platform_static_array :: array_element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: render_delete_vertex_buffer ( mesh . vertex_buffer_id ) ;
    if ( platform_conditions :: condition_whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
        platform_render :: render_delete_index_buffer ( mesh . triangle_strip_index_buffer_id ) ;
    if ( platform_conditions :: condition_whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
        platform_render :: render_delete_index_buffer ( mesh . triangle_fan_index_buffer_id ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_render msg )
{
    _mesh_data & mesh = platform_static_array :: array_element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: render_matrix_push ( ) ;
    platform_render :: render_matrix_mult ( mesh . transform ) ;
    if ( platform_conditions :: condition_whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
    {
        platform_render :: render_draw_triangle_strip 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_strip_index_buffer_id 
            , mesh . triangle_strip_indices_count
            ) ;
    }
    if ( platform_conditions :: condition_whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
    {
        platform_render :: render_draw_triangle_fan 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_fan_index_buffer_id 
            , mesh . triangle_fan_indices_count
            ) ;
    }
    platform_render :: render_matrix_pop ( ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: receive ( typename messages :: mesh_set_transform msg )
{
    _mesh_data & mesh = platform_static_array :: array_element ( _meshes_data , msg . mesh . _mesh_id ) ;
    mesh . transform = msg . transform ;
}
