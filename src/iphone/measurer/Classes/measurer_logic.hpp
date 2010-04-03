#define ENTITY_MESH_SPANS 50
#define ENTITY_MESH_GRID 5
#define PI 3.141592f

template < typename mediator >
class shy_measurer_logic
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: mono_sound_sample mono_sound_sample ;
    typedef typename mediator :: platform :: sound_buffer_id sound_buffer_id ;
    typedef typename mediator :: platform :: sound_source_id sound_source_id ;
    typedef typename mediator :: platform :: stereo_sound_resource_id stereo_sound_resource_id ;
    typedef typename mediator :: platform :: stereo_sound_sample stereo_sound_sample ;
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 music_rough_and_heavy_resource_index = 1 ;
    
public :
    shy_measurer_logic ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _frames_to_change_camera_target ( 0 )
    , _frames_to_change_camera_origin ( 0 )
    , _random_seed ( 0 )
    {
    }
    void init ( )
    {
        _init_render ( ) ;
        _init_sound ( ) ;
        _create_land_mesh ( ) ;
        _reset_camera_rubber ( ) ;
        _update_camera ( ) ;
    }
    void done ( )
    {
        _done_sound ( ) ;
    }
    void render ( )
    {
        _clear_screen ( ) ;
        _use_camera_matrix ( ) ;
        _render_land ( ) ;
        _mediator -> render_entities ( ) ;
        _mediator -> render_fidget ( ) ;
    }
    void render_finished ( )
    {
    }
    void update ( )
    {
        _update_camera ( ) ;
    }
private :
    void _init_render ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_enable_depth_test ( ) ;
        platform :: render_fog_linear ( 10 , 20 , 0.0f , 0.1f , 0.4f , 0 ) ;
        platform :: render_projection_frustum ( - 1.0f , 1.0f , - 1.515f , 1.515f , 1.0f , 50.0f ) ;
        platform :: render_select_modelview_matrix ( ) ;
        platform :: render_matrix_identity ( ) ;
    }
    float_32 _int_to_sample ( int_32 i )
    {
        return float_32 ( ( i % 256 ) - 128 ) / 128.0f ;
    }
    void _init_sound ( )
    {
        platform :: sound_set_listener_position ( platform :: vector_xyz ( 0 , 0 , 4 ) ) ;
        platform :: sound_set_listener_velocity ( platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
        platform :: sound_set_listener_orientation
            ( platform :: vector_xyz ( 0 , 0 , 1 )
            , platform :: vector_xyz ( 0 , 1 , 0 )
            ) ;
            
        static mono_sound_sample mono_sound_data [ platform :: mono_sound_samples_per_second ] ;
        int_32 next_sample = 0 ;
        for ( int_32 i = 0 ; i < platform :: mono_sound_samples_per_second ; ++ i )
        {
            next_sample += int_32 ( 128.0f * ( 1.0f + platform :: math_sin ( float_32 ( i ) * 2.0f * PI / float_32 ( platform :: mono_sound_samples_per_second ) ) ) ) ;
            platform :: sound_set_sample_value ( mono_sound_data [ i ] , _int_to_sample ( next_sample ) ) ;
        }
        
        const int_32 max_stereo_sound_samples = platform :: stereo_sound_samples_per_second * 60 ;
        static stereo_sound_sample stereo_sound_data [ max_stereo_sound_samples ] ;
        int_32 loaded_stereo_sound_samples = 0 ;
        stereo_sound_resource_id music_resource_id = platform :: sound_create_stereo_resource_id 
            ( music_rough_and_heavy_resource_index 
            ) ;
        platform :: sound_load_stereo_sample_data
            ( stereo_sound_data
            , max_stereo_sound_samples
            , loaded_stereo_sound_samples
            , music_resource_id
            ) ;
        
        sound_buffer_id stereo_sound_buffer = platform :: sound_create_stereo_buffer 
            ( stereo_sound_data 
            , loaded_stereo_sound_samples - 2293 
            ) ;
        sound_buffer_id mono_sound_buffer = platform :: sound_create_mono_buffer 
            ( mono_sound_data 
            , platform :: mono_sound_samples_per_second 
            ) ;
        _sound_source = platform :: sound_create_source ( ) ;
        platform :: sound_set_source_pitch ( _sound_source , 1 ) ;
        platform :: sound_set_source_gain ( _sound_source , 1 ) ;
        platform :: sound_set_source_position ( _sound_source , platform :: vector_xyz ( 0 , 0 , - 2 ) ) ;
        platform :: sound_set_source_velocity ( _sound_source , platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
        platform :: sound_set_source_buffer ( _sound_source , stereo_sound_buffer ) ;
        platform :: sound_set_source_playback_looping ( _sound_source ) ;
        platform :: sound_source_play ( _sound_source ) ;
    }
    void _done_sound ( )
    {
        platform :: sound_source_stop ( _sound_source ) ;
    }
    void _reset_camera_rubber ( )
    {
        _current_camera_origin = _random_camera_origin ( ) ;
        _current_camera_target = _random_camera_target ( ) ;
    }
    void _clear_screen ( )
    {
        platform :: render_clear_screen ( 0 , 0.1f , 0.4f ) ;
    }
    void _use_camera_matrix ( )
    {
        platform :: render_matrix_load ( _camera_matrix ) ;
    }
    void _render_land ( )
    {
        _mediator -> mesh_render ( _land_mesh_id ) ;
    }
    void _update_camera ( )
    {
        const float_32 origin_rubber = 0.99f ;
        const float_32 target_rubber = 0.9f ;
        if ( -- _frames_to_change_camera_origin < 0 )
        {
            _frames_to_change_camera_origin = 139 ;
            _desired_camera_origin = _random_camera_origin ( ) ;
        }
        if ( -- _frames_to_change_camera_target < 0 )
        {
            _frames_to_change_camera_target = 181 ;
            _desired_camera_target = _random_camera_target ( ) ;
        }
        _current_camera_origin = platform :: vector_add
            ( platform :: vector_mul ( _current_camera_origin , origin_rubber )
            , platform :: vector_mul ( _desired_camera_origin , 1.0f - origin_rubber )
            ) ;
        _current_camera_target = platform :: vector_add
            ( platform :: vector_mul ( _current_camera_target , target_rubber )
            , platform :: vector_mul ( _desired_camera_target , 1.0f - target_rubber )
            ) ;
        _mediator -> camera_matrix_look_at 
            ( _camera_matrix 
            , _current_camera_origin
            , _current_camera_target
            , platform :: vector_xyz ( 0.0f , 1.0f , 0.0f )
            ) ;
    }
    vector_data _random_entity_origin ( int_32 index_min , int_32 index_max )
    {
        _random_seed = ( _random_seed + 181 ) % 139 ;
        return _mediator -> get_entity_origin ( index_min + ( _random_seed % ( index_max - index_min ) ) ) ;
    }
    vector_data _random_camera_origin ( )
    {
        return platform :: vector_add 
            ( _random_entity_origin ( 0 , ENTITY_MESH_GRID * ( ENTITY_MESH_GRID / 2 ) )
            , platform :: vector_xyz ( 0.0f , 3.0f , 0.0f )
            ) ;
    }
    vector_data _random_camera_target ( )
    {
        return _random_entity_origin 
            ( ENTITY_MESH_GRID * ( ENTITY_MESH_GRID / 2 )
            , ENTITY_MESH_GRID * ENTITY_MESH_GRID
            ) ;
    }
    void _create_land_mesh ( )
    {
        static const int_32 LAND_R = 0 ;
        static const int_32 LAND_G = 255 ;
        static const int_32 LAND_B = 0 ;
        static const int_32 LAND_GRID = 10 ;
        static const float_32 LAND_RADIUS = 10 ;
        
        vertex_data vertices [ ( LAND_GRID + 1 ) * ( LAND_GRID + 1 ) ] ;
        index_data indices [ ( LAND_GRID + 1 ) * 2 * LAND_GRID ] ;
        int_32 vertices_count = 0 ;
        int_32 indices_count = 0 ;
        
        const float_32 grid_step = LAND_RADIUS * 2.0f / ( float_32 ) LAND_GRID ;
        const float_32 grid_origin_x = - LAND_RADIUS ;
        const float_32 grid_origin_z = - LAND_RADIUS ;
        
        for ( int_32 iz = 0 ; iz < LAND_GRID + 1 ; iz ++ )
        {
            for ( int_32 ix = 0 ; ix < LAND_GRID + 1 ; ix ++ )
            {
                float_32 x = grid_origin_x + grid_step * ( float_32 ) ix ;
                float_32 z = grid_origin_z + grid_step * ( float_32 ) iz ;
                platform :: render_set_vertex_position 
                    ( vertices [ vertices_count ]
                    , x
                    , 0.0f
                    , z
                    ) ;
                platform :: render_set_vertex_color
                    ( vertices [ vertices_count ]
                    , LAND_R
                    , LAND_G
                    , LAND_B
                    , 255
                    ) ;
                ++ vertices_count ;
            }
        }
        
        for ( int_32 iz = 0 ; iz < LAND_GRID ; iz ++ )
        {
            for ( int_32 ix = 0 ; ix < LAND_GRID + 1 ; ix ++ )
            {
                int_32 index = 0 ;
                if ( iz % 2 == 0 )
                {
                    index = ix + ( LAND_GRID + 1 ) * iz ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                    ++ indices_count ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index + LAND_GRID + 1 ) ;
                    ++ indices_count ;
                }
                else
                {
                    index = LAND_GRID - ix + ( LAND_GRID + 1 ) * iz ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index + LAND_GRID + 1 ) ;
                    ++ indices_count ;
                    platform :: render_set_index_value ( indices [ indices_count ] , index ) ;
                    ++ indices_count ;
                }
            }
        }
        _land_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , vertices_count , indices_count , 0 ) ;
    }
private :
    mesh_id _land_mesh_id ;
    matrix_data _camera_matrix ;
    int_32 _frames_to_change_camera_target ;
    int_32 _frames_to_change_camera_origin ;
    int_32 _random_seed ;
    vector_data _desired_camera_origin ;
    vector_data _desired_camera_target ;
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    sound_source_id _sound_source ;
    mediator * _mediator ;
} ;
