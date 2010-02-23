#pragma once

#define PROFILE_FRAME_LOSSES 1
#define PROFILE_COMPUTATION_DELAY 0

#if ( PROFILE_FRAME_LOSSES && ! PROFILE_COMPUTATION_DELAY )
	#define topR 192
	#define topG 255
	#define topB 192
	#define currentR 64
	#define currentG 255
	#define currentB 64
#elif ( PROFILE_COMPUTATION_DELAY && ! PROFILE_FRAME_LOSSES )
	#define topR 192
	#define topG 192
	#define topB 255
	#define currentR 64
	#define currentG 64
	#define currentB 255
#else
	#define topR 32
	#define topG 192
	#define topB 192
	#define currentR 64
	#define currentG 255
	#define currentB 255
#endif

template < typename platform >
class shy_measurer_logic
{
public :
    void init ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_projection_frustum ( -1.0f , 1.0f , -1.515f , 1.515f , 1.0f , 10.0f ) ;
        _create_top_mesh ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
    }
    void update ( typename platform :: int_32 current_step , typename platform :: int_32 max_steps )
    {
    }
private :
    void _create_top_mesh ( )
    {
        typename platform :: vertex_data top_vertices [ 4 ] ;
        typename platform :: index_data top_indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( top_vertices [ 0 ] , -1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 1 ] ,  1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 2 ] , -1.0f ,  1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 3 ] ,  1.0f ,  1.0f , 0.0f ) ;
        
        platform :: render_set_vertex_color    ( top_vertices [ 0 ] , topR , topG , topB , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 1 ] , topR , topG , topB , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 2 ] , topR , topG , topB , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 3 ] , topR , topG , topB , 255 ) ;
        
        platform :: render_set_index_value ( top_indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( top_indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( top_indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( top_indices [ 3 ] , 3 ) ;
        
        platform :: render_create_buffer_id ( _top_vertex_buffer_id ) ;
        platform :: render_create_buffer_id ( _top_index_buffer_id ) ;
        platform :: render_bind_vertex_buffer ( _top_vertex_buffer_id , 4 , top_vertices ) ;
        platform :: render_bind_index_buffer ( _top_index_buffer_id , 4 , top_indices ) ;
    }
private :
    typename platform :: buffer_id _top_vertex_buffer_id ;
    typename platform :: buffer_id _top_index_buffer_id ;
} ;
