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
    shy_measurer_logic ( )
    : _top_pos ( 0.5f )
    , _current_pos ( 0.25f )
    {
    }
    void init ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_projection_frustum ( -1.0f , 1.0f , -1.515f , 1.515f , 1.0f , 10.0f ) ;
        _create_top_mesh ( ) ;
        _create_current_mesh ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
        platform :: render_select_modelview_matrix ( ) ;
        _render_top_mesh ( ) ;
        _render_current_mesh ( ) ;
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
        platform :: render_load_vertex_buffer ( _top_vertex_buffer_id , 4 , top_vertices ) ;
        platform :: render_load_index_buffer ( _top_index_buffer_id , 4 , top_indices ) ;
    }
    void _create_current_mesh ( )
    {
        typename platform :: vertex_data current_vertices [ 4 ] ;
        typename platform :: index_data current_indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( current_vertices [ 0 ] , -1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 1 ] ,  1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 2 ] , -1.0f ,  1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 3 ] ,  1.0f ,  1.0f , 0.0f ) ;
        
        platform :: render_set_vertex_color    ( current_vertices [ 0 ] , currentR , currentG , currentB , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 1 ] , currentR , currentG , currentB , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 2 ] , currentR , currentG , currentB , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 3 ] , currentR , currentG , currentB , 255 ) ;
        
        platform :: render_set_index_value ( current_indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( current_indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( current_indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( current_indices [ 3 ] , 3 ) ;
        
        platform :: render_create_buffer_id ( _current_vertex_buffer_id ) ;
        platform :: render_create_buffer_id ( _current_index_buffer_id ) ;
        platform :: render_load_vertex_buffer ( _current_vertex_buffer_id , 4 , current_vertices ) ;
        platform :: render_load_index_buffer ( _current_index_buffer_id , 4 , current_indices ) ;
    }
    void _render_top_mesh ( )
    {
        platform :: render_matrix_identity ( ) ;
        platform :: render_matrix_translate ( 0.0f , -7.0f + ( 6.0f * _top_pos ) , -2.0f ) ;
        platform :: render_matrix_scale ( 4.0f , 4.0f , 4.0f ) ;
        platform :: render_draw_triangle_strip ( _top_vertex_buffer_id , _top_index_buffer_id , 4 ) ;
    }
    void _render_current_mesh ( )
    {
        platform :: render_matrix_identity ( ) ;
        platform :: render_matrix_translate ( 0.0f , -7.0f + ( 6.0f * _current_pos ) , -2.0f ) ;
        platform :: render_matrix_scale ( 4.0f , 4.0f , 4.0f ) ;
        platform :: render_draw_triangle_strip ( _current_vertex_buffer_id , _current_index_buffer_id , 4 ) ;
    }
private :
    typename platform :: buffer_id _top_vertex_buffer_id ;
    typename platform :: buffer_id _top_index_buffer_id ;
    typename platform :: float_32 _top_pos ;

    typename platform :: buffer_id _current_vertex_buffer_id ;
    typename platform :: buffer_id _current_index_buffer_id ;
    typename platform :: float_32 _current_pos ;
} ;
