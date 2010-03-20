#pragma once

#define MAX_MESHES 100

template < typename mediator >
class shy_measurer_mesh
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: buffer_id buffer_id ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
public :
    class mesh_id
    {
        friend class shy_measurer_mesh ;
    private :
        int_32 _mesh_id ;
    } ;
private :
    class _mesh_data
    {
    public :
        buffer_id vertex_buffer_id ;
        buffer_id index_buffer_id ;
        int_32 indices_count ;
        matrix_data transform ;
    } ;
public :
    shy_measurer_mesh ( )
    : _next_mesh_id ( 0 )
    {
    }
    mesh_id mesh_create ( vertex_data * vertices , index_data * indices , int_32 vertices_count , int_32 indices_count )
    {
        _mesh_data & mesh = _meshes_data [ _next_mesh_id ] ;
        mesh . indices_count = indices_count ;
        platform :: matrix_identity ( mesh . transform ) ;
        platform :: render_create_buffer_id ( mesh . vertex_buffer_id ) ;
        platform :: render_create_buffer_id ( mesh . index_buffer_id ) ;
        platform :: render_load_vertex_buffer ( mesh . vertex_buffer_id , vertices_count , vertices ) ;
        platform :: render_load_index_buffer ( mesh . index_buffer_id , indices_count , indices ) ;
        mesh_id new_id ;
        new_id . _mesh_id = _next_mesh_id ;
        ++ _next_mesh_id ;
        return new_id ;
    }
    void mesh_render ( mesh_id arg_mesh_id )
    {
        _mesh_data & mesh = _meshes_data [ arg_mesh_id . _mesh_id ] ;
        platform :: render_matrix_push ( ) ;
        platform :: render_matrix_mult ( mesh . transform ) ;
        platform :: render_draw_triangle_strip 
            ( mesh . vertex_buffer_id 
            , mesh . index_buffer_id 
            , mesh . indices_count 
            ) ;
        platform :: render_matrix_pop ( ) ;
    }
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform )
    {
        _meshes_data [ arg_mesh_id . _mesh_id ] . transform = transform ;
    }
private :
    int_32 _next_mesh_id ;
    _mesh_data _meshes_data [ MAX_MESHES ] ;
} ;
