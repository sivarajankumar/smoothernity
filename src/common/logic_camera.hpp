template < typename mediator >
class shy_logic_camera
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

    static const int_32 ENTITY_MESH_SPANS = 50 ;
    static const int_32 ENTITY_MESH_GRID = 5 ;

public :
    shy_logic_camera ( mediator * arg_mediator ) ;
    void camera_update ( ) ;
    void camera_prepare_permit ( ) ;
    void camera_matrix_use ( ) ;
private :
    void _reset_camera_rubber ( ) ;
    void _fill_camera_schedules ( ) ;
    void _update_camera ( ) ;
    void _update_desired_camera_origin ( ) ;
    void _update_desired_camera_target ( ) ;
    void _update_current_camera_origin ( ) ;
    void _update_current_camera_target ( ) ;
    void _update_camera_matrix ( ) ;
    int_32 _random_camera_origin_index ( ) ;
    int_32 _random_camera_target_index ( ) ;
    int_32 _get_random_index ( int_32 index_min , int_32 index_max ) ;
    int_32 _camera_origin_index_is_duplicate ( int_32 index ) ;
    int_32 _camera_target_index_is_duplicate ( int_32 index ) ;
private :
    mediator * _mediator ;
    matrix_data _camera_matrix ;
    int_32 _camera_prepare_permitted ;
    int_32 _frames_to_change_camera_target ;
    int_32 _frames_to_change_camera_origin ;
    int_32 _random_seed ;
    vector_data _desired_camera_origin ;
    vector_data _desired_camera_target ;
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    int_32 _scheduled_camera_origin_indices [ 4 ] ;
    int_32 _scheduled_camera_target_indices [ 4 ] ;
    vector_data _scheduled_camera_origins [ 4 ] ;
    vector_data _scheduled_camera_targets [ 4 ] ;
    int_32 _camera_created ;
} ;

template < typename mediator >
shy_logic_camera < mediator > :: shy_logic_camera ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _camera_prepare_permitted ( false )
, _frames_to_change_camera_target ( 0 )
, _frames_to_change_camera_origin ( 0 )
, _random_seed ( 0 )
, _camera_created ( false )
{
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        _scheduled_camera_origin_indices [ i ] = 0 ;
        _scheduled_camera_target_indices [ i ] = 0 ;
        _scheduled_camera_origins [ i ] = platform :: vector_xyz ( 0 , 0 , 0 ) ;
        _scheduled_camera_targets [ i ] = platform :: vector_xyz ( 0 , 0 , 0 ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_matrix_use ( )
{
    if ( _camera_created )
        platform :: render_matrix_load ( _camera_matrix ) ;
    else
        platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_prepare_permit ( )
{
    _camera_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_update ( )
{
    if ( _camera_prepare_permitted )
    {
        if ( ! _camera_created )
        {
            _fill_camera_schedules ( ) ;
            _reset_camera_rubber ( ) ;
            _update_camera ( ) ;
            _camera_created = true ;
            _mediator -> camera_prepared ( ) ;
        }
        else
            _update_camera ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _reset_camera_rubber ( )
{
    _current_camera_origin = _scheduled_camera_origins [ 2 ] ;
    _current_camera_target = _scheduled_camera_targets [ 2 ] ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _fill_camera_schedules ( )
{
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        int_32 origin_index = _random_camera_origin_index ( ) ;
        int_32 target_index = _random_camera_target_index ( ) ;
        _scheduled_camera_origin_indices [ i ] = origin_index ;
        _scheduled_camera_target_indices [ i ] = target_index ;
        _scheduled_camera_origins [ i ] = _mediator -> get_entity_origin ( origin_index ) ;
        _scheduled_camera_targets [ i ] = _mediator -> get_entity_origin ( target_index ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_camera ( )
{
    _update_desired_camera_origin ( ) ;
    _update_desired_camera_target ( ) ;
    _update_current_camera_origin ( ) ;
    _update_current_camera_target ( ) ;
    _update_camera_matrix ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_origin ( )
{
    static const int_32 CHANGE_ORIGIN_IN_FRAMES = 139 ;
    if ( -- _frames_to_change_camera_origin <= 0 )
    {
        _frames_to_change_camera_origin = CHANGE_ORIGIN_IN_FRAMES ;
        int_32 new_origin_index = _random_camera_origin_index ( ) ;
        _scheduled_camera_origin_indices [ 0 ] = _scheduled_camera_origin_indices [ 1 ] ;
        _scheduled_camera_origin_indices [ 1 ] = _scheduled_camera_origin_indices [ 2 ] ;
        _scheduled_camera_origin_indices [ 2 ] = _scheduled_camera_origin_indices [ 3 ] ;
        _scheduled_camera_origin_indices [ 3 ] = new_origin_index ;
        _scheduled_camera_origins [ 0 ] = _scheduled_camera_origins [ 1 ] ;
        _scheduled_camera_origins [ 1 ] = _scheduled_camera_origins [ 2 ] ;
        _scheduled_camera_origins [ 2 ] = _scheduled_camera_origins [ 3 ] ;
        _scheduled_camera_origins [ 3 ] = _mediator -> get_entity_origin ( new_origin_index ) ;
    }
    _desired_camera_origin = _mediator -> math_catmull_rom_spline
        ( 1.0f - float_32 ( _frames_to_change_camera_origin ) / float_32 ( CHANGE_ORIGIN_IN_FRAMES )
        , _scheduled_camera_origins [ 0 ]
        , _scheduled_camera_origins [ 1 ]
        , _scheduled_camera_origins [ 2 ]
        , _scheduled_camera_origins [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_target ( )
{
    static const int_32 CHANGE_TARGET_IN_FRAMES = 181 ;
    if ( -- _frames_to_change_camera_target <= 0 )
    {
        _frames_to_change_camera_target = CHANGE_TARGET_IN_FRAMES ;
        int_32 new_target_index = _random_camera_target_index ( ) ;
        _scheduled_camera_target_indices [ 0 ] = _scheduled_camera_target_indices [ 1 ] ;
        _scheduled_camera_target_indices [ 1 ] = _scheduled_camera_target_indices [ 2 ] ;
        _scheduled_camera_target_indices [ 2 ] = _scheduled_camera_target_indices [ 3 ] ;
        _scheduled_camera_target_indices [ 3 ] = new_target_index ;
        _scheduled_camera_targets [ 0 ] = _scheduled_camera_targets [ 1 ] ;
        _scheduled_camera_targets [ 1 ] = _scheduled_camera_targets [ 2 ] ;
        _scheduled_camera_targets [ 2 ] = _scheduled_camera_targets [ 3 ] ;
        _scheduled_camera_targets [ 3 ] = _mediator -> get_entity_origin ( new_target_index ) ;
    }
    _desired_camera_target = _mediator -> math_catmull_rom_spline
        ( 1.0f - float_32 ( _frames_to_change_camera_target ) / float_32 ( CHANGE_TARGET_IN_FRAMES )
        , _scheduled_camera_targets [ 0 ]
        , _scheduled_camera_targets [ 1 ]
        , _scheduled_camera_targets [ 2 ]
        , _scheduled_camera_targets [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_origin ( )
{
    const float_32 origin_rubber = 0 ; // 0.99f ;
    _current_camera_origin = platform :: vector_add
        ( platform :: vector_mul ( _current_camera_origin , origin_rubber )
        , platform :: vector_mul ( _desired_camera_origin , 1.0f - origin_rubber )
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_target ( )
{
    const float_32 target_rubber = 0 ; // 0.9f ;
    _current_camera_target = platform :: vector_add
        ( platform :: vector_mul ( _current_camera_target , target_rubber )
        , platform :: vector_mul ( _desired_camera_target , 1.0f - target_rubber )
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_camera_matrix ( )
{
    float_32 height = _mediator -> get_entity_height ( ) 
                    + platform :: render_get_aspect_height ( ) 
                    + _mediator -> get_near_plane_distance ( ) ;
    _mediator -> camera_matrix_look_at 
        ( _camera_matrix 
        , platform :: vector_add ( _current_camera_origin , platform :: vector_xyz ( 0.0f , height , 0.0f ) )
        , _current_camera_target
        , platform :: vector_xyz ( 0 , 1 , 0 )
        ) ;
}

template < typename mediator >
typename shy_logic_camera < mediator > :: int_32
shy_logic_camera < mediator > :: _random_camera_origin_index ( )
{
    int_32 index = 0 ;
    do
    {
        index = _get_random_index ( 0 , ENTITY_MESH_GRID * ( ENTITY_MESH_GRID / 2 ) ) ;
    } while ( _camera_origin_index_is_duplicate ( index ) ) ;
    return index ;
}

template < typename mediator >
typename shy_logic_camera < mediator > :: int_32
shy_logic_camera < mediator > :: _random_camera_target_index ( )
{
    int_32 index = 0 ;
    do
    {
        index = _get_random_index
            ( ENTITY_MESH_GRID * ( ENTITY_MESH_GRID / 2 )
            , ENTITY_MESH_GRID * ENTITY_MESH_GRID
            ) ;
    } while ( _camera_target_index_is_duplicate ( index ) ) ;
    return index ;
}

template < typename mediator >
typename shy_logic_camera < mediator > :: int_32
shy_logic_camera < mediator > :: _get_random_index ( int_32 index_min , int_32 index_max )
{
    _random_seed = ( _random_seed + 181 ) % 139 ;
    return index_min + ( _random_seed % ( index_max - index_min ) ) ;
}

template < typename mediator >
typename shy_logic_camera < mediator > :: int_32
shy_logic_camera < mediator > :: _camera_origin_index_is_duplicate ( int_32 index )
{
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        if ( _scheduled_camera_origin_indices [ i ] == index )
            return true ;
    }
    return false ;
}

template < typename mediator >
typename shy_logic_camera < mediator > :: int_32
shy_logic_camera < mediator > :: _camera_target_index_is_duplicate ( int_32 index )
{
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        if ( _scheduled_camera_target_indices [ i ] == index )
            return true ;
    }
    return false ;
}
