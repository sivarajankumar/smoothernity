#pragma once

template 
    < typename _platform
    , template < typename mediator > class measurer_camera
    , template < typename mediator > class measurer_logic 
    , template < typename mediator > class measurer_mesh
    >
class shy_measurer_mediator
{
public :
    typedef _platform platform ;
    typedef typename measurer_mesh < shy_measurer_mediator > :: mesh_id mesh_id ;
    typedef typename platform :: int_32 int_32 ;
    typedef typename platform :: index_data index_data ;
    typedef typename platform :: matrix_data matrix_data ;
    typedef typename platform :: vector_data vector_data ;
    typedef typename platform :: vertex_data vertex_data ;
public :
    shy_measurer_mediator ( )
    : _logic ( this )
    {
    }
public :
    void camera_matrix_look_at ( matrix_data & matrix , vector_data from , vector_data to , vector_data norm_up )
    {
        _camera . camera_matrix_look_at ( matrix , from , to , norm_up ) ;
    }
    void done ( )
    {
        _logic . done ( ) ;
    }
    void init ( )
    {
        _logic . init ( ) ;
    }
    mesh_id mesh_create ( vertex_data * vertices , index_data * indices , int_32 vertices_count )
    {
        return _mesh . mesh_create ( vertices , indices , vertices_count ) ;
    }
    void mesh_render ( mesh_id arg_mesh_id )
    {
        _mesh . mesh_render ( arg_mesh_id ) ;
    }
    void mesh_set_transform ( mesh_id arg_mesh_id , const matrix_data & transform )
    {
        _mesh . mesh_set_transform ( arg_mesh_id , transform ) ;
    }
    void render ( )
    {
        _logic . render ( ) ;
    }
    void render_finished ( )
    {
        _logic . render_finished ( ) ;
    }
    void update ( int_32 step )
    {
        _logic . update ( step ) ;
    }
private :
    measurer_camera < shy_measurer_mediator > _camera ;
    measurer_logic < shy_measurer_mediator > _logic ;
    measurer_mesh < shy_measurer_mediator > _mesh ;
} ;
