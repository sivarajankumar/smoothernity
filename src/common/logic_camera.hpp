template < typename mediator >
class shy_logic_camera
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;

    static const int_32 _change_origin_in_frames = 139 ;
    static const int_32 _change_target_in_frames = 181 ;
    static const float_32 _origin_rubber ( ) { return 0 ; } // 0.99f ;
    static const float_32 _target_rubber ( ) { return 0 ; } // 0.9f ;
public :
    shy_logic_camera ( mediator * arg_mediator ) ;
    void camera_update ( ) ;
    void camera_prepare_permit ( ) ;
    void camera_matrix_use ( ) ;
private :
    void _get_entity_mesh_grid ( int_32 & result ) ;
    void _reset_camera_rubber ( ) ;
    void _fill_camera_schedules ( ) ;
    void _update_camera ( ) ;
    void _update_desired_camera_origin ( ) ;
    void _update_desired_camera_target ( ) ;
    void _update_current_camera_origin ( ) ;
    void _update_current_camera_target ( ) ;
    void _update_camera_matrix ( ) ;
    void _random_camera_origin_index ( int_32 & result ) ;
    void _random_camera_target_index ( int_32 & result ) ;
    void _get_random_index ( int_32 & result , int_32 index_min , int_32 index_max ) ;
    void _camera_origin_index_is_duplicate ( int_32 & result , int_32 index ) ;
    void _camera_target_index_is_duplicate ( int_32 & result , int_32 index ) ;
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
        num_fract zero ;
        platform :: math_make_num_fract ( zero , 0 , 1 ) ;
        platform :: vector_xyz ( _scheduled_camera_origins [ i ] , zero , zero , zero ) ;
        platform :: vector_xyz ( _scheduled_camera_targets [ i ] , zero , zero , zero ) ;
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
void shy_logic_camera < mediator > :: _get_entity_mesh_grid ( int_32 & result )
{
    _mediator -> get_entity_mesh_grid ( result ) ;
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
        int_32 origin_index ;
        int_32 target_index ;
        vector_data origin_pos ;
        vector_data target_pos ;
        _random_camera_origin_index ( origin_index ) ;
        _random_camera_target_index ( target_index ) ;
        _mediator -> get_entity_origin ( origin_pos , origin_index ) ;
        _mediator -> get_entity_origin ( target_pos , target_index ) ;
        _scheduled_camera_origin_indices [ i ] = origin_index ;
        _scheduled_camera_target_indices [ i ] = target_index ;
        _scheduled_camera_origins [ i ] = origin_pos ;
        _scheduled_camera_targets [ i ] = target_pos ;
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
    if ( -- _frames_to_change_camera_origin <= 0 )
    {
        _frames_to_change_camera_origin = _change_origin_in_frames ;
        int_32 new_origin_index ;
        vector_data new_origin_pos ;
        _random_camera_origin_index ( new_origin_index ) ;
        _mediator -> get_entity_origin ( new_origin_pos , new_origin_index ) ;
        _scheduled_camera_origin_indices [ 0 ] = _scheduled_camera_origin_indices [ 1 ] ;
        _scheduled_camera_origin_indices [ 1 ] = _scheduled_camera_origin_indices [ 2 ] ;
        _scheduled_camera_origin_indices [ 2 ] = _scheduled_camera_origin_indices [ 3 ] ;
        _scheduled_camera_origin_indices [ 3 ] = new_origin_index ;
        _scheduled_camera_origins [ 0 ] = _scheduled_camera_origins [ 1 ] ;
        _scheduled_camera_origins [ 1 ] = _scheduled_camera_origins [ 2 ] ;
        _scheduled_camera_origins [ 2 ] = _scheduled_camera_origins [ 3 ] ;
        _scheduled_camera_origins [ 3 ] = new_origin_pos ;
    }
    _mediator -> math_catmull_rom_spline
        ( _desired_camera_origin
        , 1.0f - float_32 ( _frames_to_change_camera_origin ) / float_32 ( _change_origin_in_frames )
        , _scheduled_camera_origins [ 0 ]
        , _scheduled_camera_origins [ 1 ]
        , _scheduled_camera_origins [ 2 ]
        , _scheduled_camera_origins [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_target ( )
{
    if ( -- _frames_to_change_camera_target <= 0 )
    {
        _frames_to_change_camera_target = _change_target_in_frames ;
        int_32 new_target_index ;
        vector_data new_target_pos ;
        _random_camera_target_index ( new_target_index ) ;
        _mediator -> get_entity_origin ( new_target_pos , new_target_index ) ;
        _scheduled_camera_target_indices [ 0 ] = _scheduled_camera_target_indices [ 1 ] ;
        _scheduled_camera_target_indices [ 1 ] = _scheduled_camera_target_indices [ 2 ] ;
        _scheduled_camera_target_indices [ 2 ] = _scheduled_camera_target_indices [ 3 ] ;
        _scheduled_camera_target_indices [ 3 ] = new_target_index ;
        _scheduled_camera_targets [ 0 ] = _scheduled_camera_targets [ 1 ] ;
        _scheduled_camera_targets [ 1 ] = _scheduled_camera_targets [ 2 ] ;
        _scheduled_camera_targets [ 2 ] = _scheduled_camera_targets [ 3 ] ;
        _scheduled_camera_targets [ 3 ] = new_target_pos ;
    }
    _mediator -> math_catmull_rom_spline
        ( _desired_camera_target
        , 1.0f - float_32 ( _frames_to_change_camera_target ) / float_32 ( _change_target_in_frames )
        , _scheduled_camera_targets [ 0 ]
        , _scheduled_camera_targets [ 1 ]
        , _scheduled_camera_targets [ 2 ]
        , _scheduled_camera_targets [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_origin ( )
{
    vector_data old_part ;
    vector_data new_part ;
    platform :: vector_mul ( old_part , _current_camera_origin , _origin_rubber ( ) ) ;
    platform :: vector_mul ( new_part , _desired_camera_origin , 1.0f - _origin_rubber ( ) ) ;
    platform :: vector_add ( _current_camera_origin , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_target ( )
{
    vector_data old_part ;
    vector_data new_part ;
    platform :: vector_mul ( old_part , _current_camera_target , _target_rubber ( ) ) ;
    platform :: vector_mul ( new_part , _desired_camera_target , 1.0f - _target_rubber ( ) ) ;
    platform :: vector_add ( _current_camera_target , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_camera_matrix ( )
{
    num_fract up_x ;
    num_fract up_y ;
    num_fract up_z ;
    num_fract shift_x ;
    num_fract shift_y ;
    num_fract shift_z ;
    vector_data up ;
    vector_data shift ;
    vector_data shifted_origin ;
    float_32 near_plane ;
    float_32 aspect_height ;
    float_32 entity_height ;
    
    _mediator -> get_entity_height ( entity_height ) ;
    _mediator -> get_near_plane_distance ( near_plane ) ;
    platform :: render_get_aspect_height ( aspect_height ) ;
    platform :: math_make_num_fract ( up_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( up_y , 1 , 1 ) ;
    platform :: math_make_num_fract ( up_z , 0 , 1 ) ;
    platform :: math_make_num_fract ( shift_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( shift_y , int_32 ( 1000.0f * ( entity_height + aspect_height + near_plane ) ) , 1000 ) ;
    platform :: math_make_num_fract ( shift_z , 0 , 1 ) ;
    platform :: vector_xyz ( up , up_x , up_y , up_z ) ;
    platform :: vector_xyz ( shift , shift_x , shift_y , shift_z ) ;
    platform :: vector_add ( shifted_origin , _current_camera_origin , shift ) ;
    _mediator -> camera_matrix_look_at ( _camera_matrix , shifted_origin , _current_camera_target , up ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_origin_index ( int_32 & result )
{
    int_32 index = 0 ;
    int_32 mesh_grid ;
    int_32 is_duplicate ;
    _get_entity_mesh_grid ( mesh_grid ) ;
    do
    {
        _get_random_index ( index , 0 , mesh_grid * ( mesh_grid / 2 ) ) ;
        _camera_origin_index_is_duplicate ( is_duplicate , index ) ;
    } while ( is_duplicate ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_target_index ( int_32 & result )
{
    int_32 index = 0 ;
    int_32 mesh_grid ;
    int_32 is_duplicate ;
    _get_entity_mesh_grid ( mesh_grid ) ;
    do
    {
        _get_random_index ( index , mesh_grid * ( mesh_grid / 2 ) , mesh_grid * mesh_grid ) ;
        _camera_target_index_is_duplicate ( is_duplicate , index ) ;
    } while ( is_duplicate ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _get_random_index ( int_32 & result , int_32 index_min , int_32 index_max )
{
    _random_seed = ( _random_seed + 181 ) % 139 ;
    result = index_min + ( _random_seed % ( index_max - index_min ) ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_origin_index_is_duplicate ( int_32 & result , int_32 index )
{
    result = false ;
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        if ( _scheduled_camera_origin_indices [ i ] == index )
        {
            result = true ;
            break ;
        }
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_target_index_is_duplicate ( int_32 & result , int_32 index )
{
    result = false ;
    for ( int_32 i = 0 ; i < 4 ; i ++ )
    {
        if ( _scheduled_camera_target_indices [ i ] == index )
        {
            result = true ;
            break ;
        }
    }
}
