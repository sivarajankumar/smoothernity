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
        _mediator -> render_land ( ) ;
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
private :
    matrix_data _camera_matrix ;
    int_32 _frames_to_change_camera_target ;
    int_32 _frames_to_change_camera_origin ;
    int_32 _random_seed ;
    vector_data _desired_camera_origin ;
    vector_data _desired_camera_target ;
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    mediator * _mediator ;
} ;
