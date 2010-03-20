#pragma once

#define MEMORY_POOL_SIZE 48*1024*1024
#define MESH_SPANS 5000
#define COMPUTATION_STEP_DELAY_IN_MICROSECONDS 2000
#define COMPUTATION_STEP_DELAY_CHECK_ACCURACY_PERCENTS 20
#define MAX_FRAMES_WITHOUT_LOSSES 200
#define PROFILE_FRAME_LOSSES 0
#define PROFILE_COMPUTATION_DELAY 1

#define PI 3.141592f
#define MAX_TIME_FOR_UPDATES_IN_MICROSECONDS \
    ( ( 100 + COMPUTATION_STEP_DELAY_CHECK_ACCURACY_PERCENTS ) \
    * COMPUTATION_STEP_DELAY_IN_MICROSECONDS * platform :: max_update_steps ( ) \
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

template < typename mediator >
class shy_measurer_logic
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
public :
    shy_measurer_logic ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _time_consumed_for_updates ( 0 )
    , _max_frames_without_losses ( 0 )
    , _frames_without_losses ( 0 )
    , _best_result_expiration_frames ( 0 )
    , _benchmark_mesh_rotation_angle ( 0 )
    {
    }
    void init ( )
    {
        _init_render ( ) ;
        _create_top_mesh ( ) ;
        _create_current_mesh ( ) ;
        _create_benchmark_mesh ( ) ;
        _make_fake_memory_useable ( ) ;
        _save_frame_time ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        _update_measures ( ) ;
        _rotate_benchmark_mesh ( ) ;
        _clear_screen ( ) ;
        _render_top_mesh ( ) ;
        _render_current_mesh ( ) ;
        _render_benchmark_mesh ( ) ;
    }
    void render_finished ( )
    {
        _profile_computation_delay ( ) ;
        _profile_frame_losses ( ) ;
    }
    void update ( typename platform :: int_32 step )
    {
        typename platform :: time_data time_begin ;
        platform :: time_get_current ( time_begin ) ;
        _wait_for_time ( COMPUTATION_STEP_DELAY_IN_MICROSECONDS ) ;
        typename platform :: time_data time_end ;
        platform :: time_get_current ( time_end ) ;
        _time_consumed_for_updates += platform :: time_diff_in_microseconds ( time_begin , time_end ) ;
    }
private :
    void _update_measures ( )
    {
        _advance_frame_counter ( ) ;
        _advance_max_frames_counter ( ) ;
        _crop_max_frames_counter ( ) ;
        _calc_current_pos ( ) ;
        _calc_top_pos ( ) ;
    }
    void _init_render ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_projection_frustum ( - 1.0f , 1.0f , - 1.515f , 1.515f , 1.0f , 10.0f ) ;
        platform :: render_select_modelview_matrix ( ) ;
    }
    void _clear_screen ( )
    {
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
    }
    void _wait_for_time ( typename platform :: int_32 delay )
    {
        typename platform :: time_data time_begin ;
        platform :: time_get_current ( time_begin ) ;
		while ( true )
		{
            typename platform :: time_data time_current ;
            platform :: time_get_current ( time_current ) ;
            if ( platform :: time_diff_in_microseconds ( time_begin , time_current ) >= delay )
                break ;
		}
    }
    void _rotate_benchmark_mesh ( )
    {
        _benchmark_mesh_rotation_angle += 2.0f * PI / 360.0f ;
        typename platform :: float_32 cos_a = platform :: math_cos ( _benchmark_mesh_rotation_angle ) ;
        typename platform :: float_32 sin_a = platform :: math_sin ( _benchmark_mesh_rotation_angle ) ;
        typename platform :: matrix_data matrix ;
        platform :: matrix_set_axis_x ( matrix , cos_a , 0.0f , - sin_a ) ;
        platform :: matrix_set_axis_y ( matrix ,  0.0f , 1.0f ,    0.0f ) ;
        platform :: matrix_set_axis_z ( matrix , sin_a , 0.0f ,   cos_a ) ;
        platform :: matrix_set_origin ( matrix ,  0.0f , 0.0f ,  - 2.0f ) ;
        _mediator -> mesh_set_transform ( _benchmark_mesh_id , matrix ) ;
    }
    void _save_frame_time ( )
    {
        platform :: time_get_current ( _frame_time_begin ) ;
    }
    void _make_fake_memory_useable ( )
    {
        _fake_memory_pool [ 0 ] = MEMORY_POOL_SIZE ;
    }
    void _profile_frame_losses ( )
    {
#if PROFILE_FRAME_LOSSES
        typename platform :: time_data time_prev = _frame_time_begin ;
        _save_frame_time ( ) ;
        typename platform :: int_32 whole_frame_time 
            = platform :: time_diff_in_microseconds ( _frame_time_begin , time_prev )
            * platform :: frames_per_second ( ) ;
        if ( whole_frame_time > 1500000 )
        {
            _frames_without_losses = 0 ;
            if ( whole_frame_time > 3000000 )
                _max_frames_without_losses = 0 ;
        }
#endif
    }
    void _profile_computation_delay ( )
    {
#if PROFILE_COMPUTATION_DELAY
        if ( _time_consumed_for_updates * 100 > MAX_TIME_FOR_UPDATES_IN_MICROSECONDS )
            _frames_without_losses = 0 ;
        _time_consumed_for_updates = 0 ;
#endif
    }
    void _calc_current_pos ( )
    {
        typename platform :: float_32 current_pos = 0 ;
        typename platform :: matrix_data matrix ;
        current_pos = ( ( typename platform :: float_32 ) _frames_without_losses )
                      / ( typename platform :: float_32 ) MAX_FRAMES_WITHOUT_LOSSES ;
        if ( current_pos > 1.0f )
            current_pos = 1.0f ;
        platform :: matrix_set_axis_x ( matrix , 4.0f , 0.0f , 0.0f ) ;
        platform :: matrix_set_axis_y ( matrix , 0.0f , 4.0f , 0.0f ) ;
        platform :: matrix_set_axis_z ( matrix , 0.0f , 0.0f , 4.0f ) ;
        platform :: matrix_set_origin ( matrix , 0.0f , - 7.0f + ( 6.0f * current_pos ) , - 2.0f ) ;
        _mediator -> mesh_set_transform ( _current_mesh_id , matrix ) ;
    }
    void _calc_top_pos ( )
    {
        typename platform :: float_32 top_pos = 0 ;
        typename platform :: matrix_data matrix ;
        top_pos = ( ( typename platform :: float_32 ) _max_frames_without_losses ) 
                  / ( typename platform :: float_32 ) MAX_FRAMES_WITHOUT_LOSSES ;
        if ( top_pos > 1.0f )
            top_pos = 1.0f ;
        platform :: matrix_set_axis_x ( matrix , 4.0f , 0.0f , 0.0f ) ;
        platform :: matrix_set_axis_y ( matrix , 0.0f , 4.0f , 0.0f ) ;
        platform :: matrix_set_axis_z ( matrix , 0.0f , 0.0f , 4.0f ) ;
        platform :: matrix_set_origin ( matrix , 0.0f , - 7.0f + ( 6.0f * top_pos ) , - 2.0f ) ;
        _mediator -> mesh_set_transform ( _top_mesh_id , matrix ) ;
    }
    void _advance_frame_counter ( )
    {
        _frames_without_losses ++ ;
    }
    void _advance_max_frames_counter ( )
    {
        if ( _frames_without_losses > _max_frames_without_losses )
        {
            _max_frames_without_losses = _frames_without_losses ;
            _best_result_expiration_frames = 0 ;
        }
        else
            _best_result_expiration_frames ++ ;
    }
    void _crop_max_frames_counter ( )
    {
        if ( _best_result_expiration_frames > MAX_FRAMES_WITHOUT_LOSSES )
            _max_frames_without_losses = 0 ;
    }
    void _create_top_mesh ( )
    {
        typename platform :: vertex_data top_vertices [ 4 ] ;
        typename platform :: index_data top_indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( top_vertices [ 0 ] , - 1.0f , - 1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 1 ] ,   1.0f , - 1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 2 ] , - 1.0f ,   1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( top_vertices [ 3 ] ,   1.0f ,   1.0f , 0.0f ) ;
        
        platform :: render_set_vertex_color    ( top_vertices [ 0 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 1 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 2 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        platform :: render_set_vertex_color    ( top_vertices [ 3 ] , TOP_R , TOP_G , TOP_B , 255 ) ;
        
        platform :: render_set_index_value ( top_indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( top_indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( top_indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( top_indices [ 3 ] , 3 ) ;
        
        _top_mesh_id = _mediator -> mesh_create ( top_vertices , top_indices , 4 ) ;
    }
    void _create_current_mesh ( )
    {
        typename platform :: vertex_data current_vertices [ 4 ] ;
        typename platform :: index_data current_indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( current_vertices [ 0 ] , - 1.0f , - 1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 1 ] ,   1.0f , - 1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 2 ] , - 1.0f ,   1.0f , 0.0f ) ;
        platform :: render_set_vertex_position ( current_vertices [ 3 ] ,   1.0f ,   1.0f , 0.0f ) ;
        
        platform :: render_set_vertex_color    ( current_vertices [ 0 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 1 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 2 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        platform :: render_set_vertex_color    ( current_vertices [ 3 ] , CURRENT_R , CURRENT_G , CURRENT_B , 255 ) ;
        
        platform :: render_set_index_value ( current_indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( current_indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( current_indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( current_indices [ 3 ] , 3 ) ;
        
        _current_mesh_id = _mediator -> mesh_create ( current_vertices , current_indices , 4 ) ;
    }
    void _create_benchmark_mesh ( )
    {
        static const typename platform :: int_32 COLORS_R [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ;
        static const typename platform :: int_32 COLORS_G [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ;
        static const typename platform :: int_32 COLORS_B [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ;
        static const typename platform :: int_32 COLORS_A [ ] = { 255 , 255 , 255 , 255 , 255 , 255 , 255 } ;

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
                , - 1.0f 
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
        _benchmark_mesh_id = _mediator -> mesh_create ( vertices , indices , indices_count ) ;
    }
    void _render_top_mesh ( )
    {
        _mediator -> mesh_render ( _top_mesh_id ) ;
    }
    void _render_current_mesh ( )
    {
        _mediator -> mesh_render ( _current_mesh_id ) ;
    }
    void _render_benchmark_mesh ( )
    {
        _mediator -> mesh_render ( _benchmark_mesh_id ) ;
    }
private :
    mesh_id _top_mesh_id ;
    mesh_id _current_mesh_id ;
    mesh_id _benchmark_mesh_id ;
    
    matrix_data _camera_matrix ;
    
    typename platform :: float_32 _benchmark_mesh_rotation_angle ;    
    
    typename platform :: int_32 _time_consumed_for_updates ;
    typename platform :: time_data _frame_time_begin ;
    typename platform :: int_32 _max_frames_without_losses ;
    typename platform :: int_32 _frames_without_losses ;
    typename platform :: int_32 _best_result_expiration_frames ;
    
	typename platform :: int_32 _fake_memory_pool [ MEMORY_POOL_SIZE / sizeof ( typename platform :: int_32 ) ] ;
    
    mediator * _mediator ;
} ;
