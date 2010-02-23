#pragma once

#define MESH_SPANS 5000
#define COMPUTATION_STEP_DELAY_IN_MICROSECONDS 2000
#define COMPUTATION_STEP_DELAY_CHECK_ACCURACY_PERCENTS 1
#define MAX_FRAMES_WITHOUT_LOSSES 200
#define PROFILE_FRAME_LOSSES 1
#define PROFILE_COMPUTATION_DELAY 0

#define PI 3.141592f
#define MAX_TIME_FOR_UPDATES_IN_MICROSECONDS \
    ( ( 100 + COMPUTATION_STEP_DELAY_CHECK_ACCURACY_PERCENTS ) \
    * COMPUTATION_STEP_DELAY_IN_MICROSECONDS * COMPUTATION_STEPS \
    / 100 \
    )

#if ( PROFILE_FRAME_LOSSES && ! PROFILE_COMPUTATION_DELAY )
	#define TOP_R 192
	#define TOP_G 255
	#define TOP_B 192
	#define CURRENT_R 64
	#define CURRENT_G 255
	#define CURRENT_B 64
#elif ( PROFILE_COMPUTATION_DELAY && ! PROFILE_FRAME_LOSSES )
	#define TOP_R 192
	#define TOP_G 192
	#define TOP_B 255
	#define CURRENT_R 64
	#define CURRENT_G 64
	#define CURRENT_B 255
#else
	#define TOP_R 32
	#define TOP_G 192
	#define TOP_B 192
	#define CURRENT_R 64
	#define CURRENT_G 255
	#define CURRENT_B 255
#endif

static const GLubyte COLORS_R [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ;
static const GLubyte COLORS_G [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ;
static const GLubyte COLORS_B [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ;
static const GLubyte COLORS_A [ ] = { 255 , 255 , 255 , 255 , 255 , 255 , 255 } ;

template < typename platform >
class shy_measurer_logic
{
public :
    shy_measurer_logic ( )
    : _top_pos ( 0.5f )
    , _current_pos ( 0.25f )
    , _benchmark_indices_count ( 0 )
    , _time_consumed_for_updates ( 0 )
    {
    }
    void init ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_projection_frustum ( -1.0f , 1.0f , -1.515f , 1.515f , 1.0f , 10.0f ) ;
        _create_top_mesh ( ) ;
        _create_current_mesh ( ) ;
        _create_benchmark_mesh ( ) ;
        platform :: time_get_current ( _previous_frame_time_begin ) ;
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
        _render_benchmark_mesh ( ) ;
        _update_measures ( ) ;
    }
    void update ( typename platform :: int_32 step )
    {
        typename platform :: time_data time_begin ;
        typename platform :: time_data time_current ;
        platform :: time_get_current ( time_begin ) ;
		while ( true )
		{
            platform :: time_get_current ( time_current ) ;
            if ( platform :: time_diff_in_microseconds ( time_begin , time_current ) >= COMPUTATION_STEP_DELAY_IN_MICROSECONDS )
                break ;
		}
        platform :: time_get_current ( time_current ) ;
        _time_consumed_for_updates += platform :: time_diff_in_microseconds ( time_begin , time_current ) ;
    }
private :
    void _update_measures ( )
    {
        static typename platform :: int_32 max_frames_without_losses = 0 ;
        static typename platform :: int_32 frames_without_losses = 0 ;
        static typename platform :: int_32 best_result_expiration_frames = 0 ;
        
        frames_without_losses ++ ;
#if PROFILE_FRAME_LOSSES
        typename platform :: time_data current_time ;
        platform :: time_get_current ( current_time ) ;
        if ( platform :: time_diff_in_microseconds ( _previous_frame_time_begin , current_time ) 
           > 1000000 / platform :: frames_per_second ( )
           )
        {
            frames_without_losses = 0 ;
        }
        _previous_frame_time_begin = current_time ;
#endif
        if ( frames_without_losses > max_frames_without_losses )
        {
            max_frames_without_losses = frames_without_losses ;
            best_result_expiration_frames = 0 ;
        }
        else
            best_result_expiration_frames ++ ;
        if ( best_result_expiration_frames > MAX_FRAMES_WITHOUT_LOSSES )
            max_frames_without_losses = 0 ;
        
        _current_pos = ( ( typename platform :: float_32 ) frames_without_losses )
                       / ( typename platform :: float_32 ) MAX_FRAMES_WITHOUT_LOSSES ;
        _top_pos = ( ( typename platform :: float_32 ) max_frames_without_losses ) 
                   / ( typename platform :: float_32 ) MAX_FRAMES_WITHOUT_LOSSES ;
        if ( _current_pos > 1.0f )
            _current_pos = 1.0f ;
        if ( _top_pos > 1.0f )
            _top_pos = 1.0f ;
            
#if PROFILE_COMPUTATION_DELAY
        if ( _time_consumed_for_updates > MAX_TIME_FOR_UPDATES_IN_MICROSECONDS )
            frames_without_losses = 0 ;
#endif
        _time_consumed_for_updates = 0 ;
    }
    void _create_top_mesh ( )
    {
        typename platform :: vertex_data top_vertices [ 4 ] ;
        typename platform :: index_data top_indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( top_vertices [ 0 ] , -1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 1 ] ,  1.0f , -1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 2 ] , -1.0f ,  1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 3 ] ,  1.0f ,  1.0f , 0.0f ) ;
        
        platform :: render_set_vertex_color    ( top_vertices [ 0 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 1 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 2 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 3 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        
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
        
        platform :: render_set_vertex_color    ( current_vertices [ 0 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 1 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 2 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 3 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        
        platform :: render_set_index_value ( current_indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( current_indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( current_indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( current_indices [ 3 ] , 3 ) ;
        
        platform :: render_create_buffer_id ( _current_vertex_buffer_id ) ;
        platform :: render_create_buffer_id ( _current_index_buffer_id ) ;
        platform :: render_load_vertex_buffer ( _current_vertex_buffer_id , 4 , current_vertices ) ;
        platform :: render_load_index_buffer ( _current_index_buffer_id , 4 , current_indices ) ;
    }
    void _create_benchmark_mesh ( )
    {
        typename platform :: vertex_data vertices [ ( MESH_SPANS + 1 ) * 2 ] ;
        typename platform :: index_data indices [ ( MESH_SPANS + 1 ) * 2 ] ;
        typename platform :: int_32 indices_count = 0 ;
		for ( typename platform :: int_32 i = 0; i < MESH_SPANS + 1 ; i ++ )
		{
			typename platform :: float_32 angle 
                = ( ( typename platform :: float_32 ) i ) 
                * PI 
                * 2.0f 
                / ( typename platform :: float_32 ) MESH_SPANS
                ;
			typename platform :: float_32 x = platform :: math_sin ( angle ) ;
			typename platform :: float_32 z = platform :: math_cos ( angle ) ;
			typename platform :: int_32 color = ( i * 21 / ( MESH_SPANS + 1 ) ) % 7;
			typename platform :: int_32 color1 = color;
			typename platform :: int_32 color2 = ( color + 1 ) % 7;
            platform :: render_set_vertex_position 
                ( vertices [ indices_count ] 
                , x 
                , 1.0f 
                , z 
                ) ;
            platform :: render_set_vertex_color 
                ( vertices [ indices_count ] 
                , COLORS_R [ color1 ]
                , COLORS_G [ color1 ]
                , COLORS_B [ color1 ]
                , COLORS_A [ color1 ]
                ) ;
            platform :: render_set_index_value ( indices [ indices_count ] , indices_count ) ;
			indices_count++;
            platform :: render_set_vertex_position 
                ( vertices [ indices_count ] 
                , x 
                , -1.0f 
                , z 
                ) ;
            platform :: render_set_vertex_color 
                ( vertices [ indices_count ] 
                , COLORS_R [ color2 ]
                , COLORS_G [ color2 ]
                , COLORS_B [ color2 ]
                , COLORS_A [ color2 ]
                ) ;
            platform :: render_set_index_value ( indices [ indices_count ] , indices_count ) ;
			indices_count++;
		}
		// NSLog(@"faces in mesh: %i", indices_count-2);
        platform :: render_create_buffer_id ( _benchmark_vertex_buffer_id ) ;
        platform :: render_create_buffer_id ( _benchmark_index_buffer_id ) ;
        platform :: render_load_vertex_buffer ( _benchmark_vertex_buffer_id , indices_count , vertices ) ;
        platform :: render_load_index_buffer ( _benchmark_index_buffer_id , indices_count , indices ) ;
        _benchmark_indices_count = indices_count ;
    }
    void _render_top_mesh ( )
    {
        platform :: render_matrix_identity ( ) ;
        platform :: render_matrix_translate ( 0.0f , -7.0f + ( 6.0f * _top_pos ) , -2.0f ) ;
        platform :: render_matrix_scale ( 4.0f , 4.0f , 4.0f ) ;
        platform :: render_draw_triangle_strip 
            ( _top_vertex_buffer_id 
            , _top_index_buffer_id 
            , 4 
            ) ;
    }
    void _render_current_mesh ( )
    {
        platform :: render_matrix_identity ( ) ;
        platform :: render_matrix_translate ( 0.0f , -7.0f + ( 6.0f * _current_pos ) , -2.0f ) ;
        platform :: render_matrix_scale ( 4.0f , 4.0f , 4.0f ) ;
        platform :: render_draw_triangle_strip 
            ( _current_vertex_buffer_id 
            , _current_index_buffer_id 
            , 4 
            ) ;
    }
    void _render_benchmark_mesh ( )
    {
        static typename platform :: float_32 angle = 0.0f ;
        angle += 2.0f ;
        platform :: render_matrix_identity ( ) ;
        platform :: render_matrix_translate ( 0.0f , 0.0f , -2.0f ) ;
        platform :: render_matrix_rotate ( angle , 0.0f , 1.0f , 0.0f ) ;
        platform :: render_draw_triangle_strip 
            ( _benchmark_vertex_buffer_id 
            , _benchmark_index_buffer_id 
            , _benchmark_indices_count 
            ) ;    
    }
private :
    typename platform :: buffer_id _top_vertex_buffer_id ;
    typename platform :: buffer_id _top_index_buffer_id ;
    typename platform :: float_32 _top_pos ;

    typename platform :: buffer_id _current_vertex_buffer_id ;
    typename platform :: buffer_id _current_index_buffer_id ;
    typename platform :: float_32 _current_pos ;
    
    typename platform :: buffer_id _benchmark_vertex_buffer_id ;
    typename platform :: buffer_id _benchmark_index_buffer_id ;
    typename platform :: int_32 _benchmark_indices_count ;
    
    typename platform :: int_32 _time_consumed_for_updates ;
    typename platform :: time_data _previous_frame_time_begin ;
} ;
