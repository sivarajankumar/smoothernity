template < typename mediator >
class shy_engine_mesh
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: render_index_buffer_id render_index_buffer_id ;
    typedef typename mediator :: platform :: render_vertex_buffer_id render_vertex_buffer_id ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 _max_meshes = 100 ;
    
public :
    class mesh_id
    {
        friend class shy_engine_mesh ;
    private :
        int_32 _mesh_id ;
    } ;
private :
    class _mesh_data
    {
    public :
        render_vertex_buffer_id vertex_buffer_id ;
        render_index_buffer_id triangle_strip_index_buffer_id ;
        render_index_buffer_id triangle_fan_index_buffer_id ;
        int_32 triangle_strip_indices_count ;
        int_32 triangle_fan_indices_count ;
        matrix_data transform ;
    } ;
public :
    shy_engine_mesh ( ) ;
    void mesh_create 
        ( mesh_id & result
        , vertex_data * vertices 
        , index_data * triangle_strip_indices 
        , index_data * triangle_fan_indices
        , int_32 vertices_count
        , int_32 triangle_strip_indices_count 
        , int_32 triangle_fan_indices_count
        ) ;
    void mesh_render ( mesh_id arg_mesh_id ) ;
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform ) ;
private :
    int_32 _next_mesh_id ;
    _mesh_data _meshes_data [ _max_meshes ] ;
} ;

template < typename mediator >
shy_engine_mesh < mediator > :: shy_engine_mesh ( )
: _next_mesh_id ( 0 )
{
}

template < typename mediator >
void shy_engine_mesh < mediator > :: mesh_create 
    ( mesh_id & result
    , vertex_data * vertices 
    , index_data * triangle_strip_indices 
    , index_data * triangle_fan_indices
    , int_32 vertices_count_int_32
    , int_32 triangle_strip_indices_count_int_32
    , int_32 triangle_fan_indices_count_int_32
    )
{
    num_whole vertices_count ;
    num_whole triangle_fan_indices_count ;
    num_whole triangle_strip_indices_count ;
    _mesh_data & mesh = _meshes_data [ _next_mesh_id ] ;
    mesh . triangle_strip_indices_count = triangle_strip_indices_count_int_32 ;
    mesh . triangle_fan_indices_count = triangle_fan_indices_count_int_32 ;
    platform :: matrix_identity ( mesh . transform ) ;
    platform :: math_make_num_whole ( vertices_count , vertices_count_int_32 ) ;
    platform :: math_make_num_whole ( triangle_fan_indices_count , triangle_fan_indices_count_int_32 ) ;
    platform :: math_make_num_whole ( triangle_strip_indices_count , triangle_strip_indices_count_int_32 ) ;
    platform :: render_create_vertex_buffer ( mesh . vertex_buffer_id , vertices_count , vertices ) ;
    if ( triangle_strip_indices_count_int_32 > 0 )
    {
        platform :: render_create_index_buffer 
            ( mesh . triangle_strip_index_buffer_id 
            , triangle_strip_indices_count 
            , triangle_strip_indices 
            ) ;
    }
    if ( triangle_fan_indices_count_int_32 > 0 )
    {
        platform :: render_create_index_buffer 
            ( mesh . triangle_fan_index_buffer_id 
            , triangle_fan_indices_count 
            , triangle_fan_indices 
            ) ;
    }
    result . _mesh_id = _next_mesh_id ;
    ++ _next_mesh_id ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: mesh_render ( mesh_id arg_mesh_id )
{
    _mesh_data & mesh = _meshes_data [ arg_mesh_id . _mesh_id ] ;
    platform :: render_matrix_push ( ) ;
    platform :: render_matrix_mult ( mesh . transform ) ;
    if ( mesh . triangle_strip_indices_count > 0 )
    {
        num_whole indices_count ;
        platform :: math_make_num_whole ( indices_count , mesh . triangle_strip_indices_count ) ;
        platform :: render_draw_triangle_strip 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_strip_index_buffer_id 
            , indices_count
            ) ;
    }
    if ( mesh . triangle_fan_indices_count > 0 )
    {
        num_whole indices_count ;
        platform :: math_make_num_whole ( indices_count , mesh . triangle_fan_indices_count ) ;
        platform :: render_draw_triangle_fan 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_fan_index_buffer_id 
            , indices_count
            ) ;
    }
    platform :: render_matrix_pop ( ) ;
}

template < typename mediator >
void shy_engine_mesh < mediator > :: mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform )
{
    _meshes_data [ arg_mesh_id . _mesh_id ] . transform = transform ;
}
