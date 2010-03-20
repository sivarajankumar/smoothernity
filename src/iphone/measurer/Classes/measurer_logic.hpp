#pragma once

#define ENTITY_MESH_SPANS 50
#define ENTITY_MESH_GRID 5
#define PI 3.141592f

#define LAND_R 0
#define LAND_G 255
#define LAND_B 0

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
    , _camera_angle ( 0 )
    {
    }
    void init ( )
    {
        _init_render ( ) ;
        _create_entity_mesh ( ) ;
        _create_entity_grid ( ) ;
        _create_land_mesh ( ) ;
    }
    void done ( )
    {
    }
    void render ( )
    {
        _clear_screen ( ) ;
        _render_land ( ) ;
        _render_entities ( ) ;
    }
    void render_finished ( )
    {
    }
    void update ( int_32 step )
    {
        if ( step == 0 )
            _update_camera ( ) ;
    }
private :
    void _init_render ( )
    {
        platform :: render_enable_face_culling ( ) ;
        platform :: render_projection_frustum ( - 1.0f , 1.0f , - 1.515f , 1.515f , 1.0f , 50.0f ) ;
        platform :: render_select_modelview_matrix ( ) ;
        platform :: render_matrix_identity ( ) ;
    }
    void _clear_screen ( )
    {
        platform :: render_clear_screen ( 0 , 0 , 0 ) ;
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
        matrix_data matrix ;
        vector_data from = platform :: vector_xyz 
            ( 0.0f 
            , 1.5f + 0.3f * platform :: math_sin ( _camera_angle ) 
            , 17.0f + platform :: math_sin ( _camera_angle * 0.3f )
            ) ;
        vector_data to   = platform :: vector_xyz ( 0.0 , 0.0f , -2.0f ) ;
        vector_data norm_up = platform :: vector_xyz ( 0.0f , 1.0f , 0.0f ) ;
        _mediator -> camera_matrix_look_at ( matrix , from , to , norm_up ) ;
        _camera_angle += 0.05f ;
        platform :: render_matrix_load ( matrix ) ;
    }
    void _create_land_mesh ( )
    {
        vertex_data vertices [ 4 ] ;
        index_data indices [ 4 ] ;
        
        platform :: render_set_vertex_position ( vertices [ 0 ] , - 1.0f , 0.0f ,   1.0f ) ;
        platform :: render_set_vertex_position ( vertices [ 1 ] ,   1.0f , 0.0f ,   1.0f ) ;
        platform :: render_set_vertex_position ( vertices [ 2 ] , - 1.0f , 0.0f , - 1.0f ) ;
        platform :: render_set_vertex_position ( vertices [ 3 ] ,   1.0f , 0.0f , - 1.0f ) ;
        
        platform :: render_set_vertex_color    ( vertices [ 0 ] , LAND_R , LAND_G , LAND_B , 255 ) ;
        platform :: render_set_vertex_color    ( vertices [ 1 ] , LAND_R , LAND_G , LAND_B , 255 ) ;
        platform :: render_set_vertex_color    ( vertices [ 2 ] , LAND_R , LAND_G , LAND_B , 255 ) ;
        platform :: render_set_vertex_color    ( vertices [ 3 ] , LAND_R , LAND_G , LAND_B , 255 ) ;
        
        platform :: render_set_index_value ( indices [ 0 ] , 0 ) ;
        platform :: render_set_index_value ( indices [ 1 ] , 1 ) ;
        platform :: render_set_index_value ( indices [ 2 ] , 2 ) ;
        platform :: render_set_index_value ( indices [ 3 ] , 3 ) ;
        
        _land_mesh_id = _mediator -> mesh_create ( vertices , indices , 4 ) ;
        matrix_data matrix ;
        platform :: matrix_identity ( matrix ) ;
        platform :: matrix_set_axis_x ( matrix , 10.0f ,  0.0f ,  0.0f ) ;
        platform :: matrix_set_axis_y ( matrix ,  0.0f , 10.0f ,  0.0f ) ;
        platform :: matrix_set_axis_z ( matrix ,  0.0f ,  0.0f , 10.0f ) ;
        _mediator -> mesh_set_transform ( _land_mesh_id , matrix ) ;
    }
    void _create_entity_mesh ( )
    {
        static const int_32 COLORS_R [ ] = { 255 , 255 , 255 ,   0 ,   0 ,   0 , 255 } ;
        static const int_32 COLORS_G [ ] = {   0 , 128 , 255 , 255 , 255 ,   0 ,   0 } ;
        static const int_32 COLORS_B [ ] = {   0 ,   0 ,   0 ,   0 , 255 , 255 , 255 } ;
        static const int_32 COLORS_A [ ] = { 255 , 255 , 255 , 255 , 255 , 255 , 255 } ;

        vertex_data vertices [ ( ENTITY_MESH_SPANS + 1 ) * 2 ] ;
        index_data indices [ ( ENTITY_MESH_SPANS + 1 ) * 2 ] ;
        int_32 indices_count = 0 ;
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
			++ indices_count ;
		}
        _entity_mesh_id = _mediator -> mesh_create ( vertices , indices , indices_count ) ;
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
    matrix_data _entities_grid_matrices [ ENTITY_MESH_GRID * ENTITY_MESH_GRID ] ;
    float_32 _camera_angle ;    
    mediator * _mediator ;
} ;
