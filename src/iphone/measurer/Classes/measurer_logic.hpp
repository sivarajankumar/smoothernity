#pragma once

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
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
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
        _create_entity_mesh ( ) ;
        _create_entity_grid ( ) ;
        _create_land_mesh ( ) ;
        _reset_camera_rubber ( ) ;
        _update_camera ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        _clear_screen ( ) ;
        _use_camera_matrix ( ) ;
        _render_land ( ) ;
        _render_entities ( ) ;
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
    void _init_sound ( )
    {
        platform :: sound_set_listener_position ( platform :: vector_xyz ( 0 , 0 , 4 ) ) ;
        platform :: sound_set_listener_velocity ( platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
        platform :: sound_set_listener_orientation
            ( platform :: vector_xyz ( 0 , 0 , 1 )
            , platform :: vector_xyz ( 0 , 1 , 0 )
            ) ;
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
    void _render_entities ( )
    {
        for ( int_32 i = 0 ; i < ENTITY_MESH_GRID * ENTITY_MESH_GRID ; i ++ )
        {
            _mediator -> mesh_set_transform ( _entity_mesh_id , _entities_grid_matrices [ i ] ) ;
            _mediator -> mesh_render ( _entity_mesh_id ) ;
        }
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
        return platform :: matrix_get_origin 
            ( _entities_grid_matrices [ index_min + ( _random_seed % ( index_max - index_min ) ) ]
            ) ;
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
    void _create_entity_mesh ( )
    {
        static const int_32 COLORS_R [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ;
        static const int_32 COLORS_G [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ;
        static const int_32 COLORS_B [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ;
        
        static const int_32 COLOR_ROOF_R = 255 ;
        static const int_32 COLOR_ROOF_G = 255 ;
        static const int_32 COLOR_ROOF_B = 255 ;

        vertex_data vertices [ ( ENTITY_MESH_SPANS + 1 ) * 2 + 1 ] ;
        index_data strip_indices [ ( ENTITY_MESH_SPANS + 1 ) * 2 ] ;
        index_data fan_indices [ ENTITY_MESH_SPANS + 2 ] ;
        int_32 strip_indices_count = 0 ;
        int_32 fan_indices_count = 0 ;
        int_32 vertices_count = 0 ;
		for ( int_32 i = 0; i < ENTITY_MESH_SPANS + 1 ; i ++ )
		{
			float_32 angle 
                = ( ( float_32 ) i ) 
                * PI 
                * 2.0f 
                / ( float_32 ) ENTITY_MESH_SPANS
                ;
			float_32 x = platform :: math_sin ( angle ) ;
			float_32 z = platform :: math_cos ( angle ) ;
			int_32 color = ( i * 21 / ( ENTITY_MESH_SPANS + 1 ) ) % 7;
			int_32 color1 = color;
			int_32 color2 = ( color + 1 ) % 7;
            platform :: render_set_vertex_position 
                ( vertices [ vertices_count ] 
                , x 
                , 1.0f 
                , z 
                ) ;
            platform :: render_set_vertex_color 
                ( vertices [ vertices_count ] 
                , COLORS_R [ color1 ]
                , COLORS_G [ color1 ]
                , COLORS_B [ color1 ]
                , 255
                ) ;
            platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
            ++ strip_indices_count ;
            ++ vertices_count ;
            platform :: render_set_vertex_position 
                ( vertices [ vertices_count ] 
                , x 
                , - 1.0f 
                , z 
                ) ;
            platform :: render_set_vertex_color 
                ( vertices [ vertices_count ] 
                , COLORS_R [ color2 ]
                , COLORS_G [ color2 ]
                , COLORS_B [ color2 ]
                , 255
                ) ;
            platform :: render_set_index_value ( strip_indices [ strip_indices_count ] , vertices_count ) ;
            ++ strip_indices_count ;
            ++ vertices_count ;
		}
        platform :: render_set_vertex_position 
            ( vertices [ vertices_count ] 
            , 0.0f
            , 1.0f 
            , 0.0f 
            ) ;
        platform :: render_set_vertex_color 
            ( vertices [ vertices_count ] 
            , COLOR_ROOF_R
            , COLOR_ROOF_G
            , COLOR_ROOF_B
            , 255
            ) ;
        platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , vertices_count ) ;
        ++ fan_indices_count ;
        ++ vertices_count ;
        for ( int_32 i = 0 ; i < ENTITY_MESH_SPANS + 1 ; ++ i )
        {
            platform :: render_set_index_value ( fan_indices [ fan_indices_count ] , i * 2 ) ;
            ++ fan_indices_count ;
        }
        _entity_mesh_id = _mediator -> mesh_create 
            ( vertices 
            , strip_indices 
            , fan_indices 
            , vertices_count 
            , strip_indices_count 
            , fan_indices_count
            ) ;
    }
    void _create_entity_grid ( )
    {
        const float_32 grid_step = 5.0f ;
        for ( int_32 x = 0 ; x < ENTITY_MESH_GRID ; x ++ )
            for ( int_32 z = 0 ; z < ENTITY_MESH_GRID ; z ++ )
            {
                matrix_data & matrix = _entities_grid_matrices [ x + ENTITY_MESH_GRID * z ] ;
                platform :: matrix_identity ( matrix ) ;
                platform :: matrix_set_origin 
                    ( matrix
                    , grid_step * ( float_32 ) ( x - ( ENTITY_MESH_GRID / 2 ) )
                    , 1.0f
                    , grid_step * ( float_32 ) ( z - ( ENTITY_MESH_GRID / 2 ) )
                    ) ;
            }
    }
private :
    mesh_id _entity_mesh_id ;
    mesh_id _land_mesh_id ;
    matrix_data _camera_matrix ;
    matrix_data _entities_grid_matrices [ ENTITY_MESH_GRID * ENTITY_MESH_GRID ] ;
    int_32 _frames_to_change_camera_target ;
    int_32 _frames_to_change_camera_origin ;
    int_32 _random_seed ;
    vector_data _desired_camera_origin ;
    vector_data _desired_camera_target ;
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    mediator * _mediator ;
} ;
