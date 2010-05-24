template < typename mediator >
class shy_logic_camera
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: time_data time_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;

    static const_int_32 _change_origin_in_frames = 139 ;
    static const_int_32 _change_target_in_frames = 181 ;
    static const num_fract _origin_rubber ( ) { return platform :: fract_0 ; }
    static const num_fract _target_rubber ( ) { return platform :: fract_0 ; }
public :
    shy_logic_camera ( mediator * arg_mediator ) ;
    void camera_update ( ) ;
    void camera_prepare_permit ( ) ;
    void camera_matrix_use ( ) ;
private :
    void _get_entity_mesh_grid ( num_whole & result ) ;
    void _reset_camera_rubber ( ) ;
    void _fill_camera_schedules ( ) ;
    void _update_camera ( ) ;
    void _update_desired_camera_origin ( ) ;
    void _update_desired_camera_target ( ) ;
    void _update_current_camera_origin ( ) ;
    void _update_current_camera_target ( ) ;
    void _update_camera_matrix ( ) ;
    void _random_camera_origin_index ( num_whole & result ) ;
    void _random_camera_target_index ( num_whole & result ) ;
    void _get_random_index ( num_whole & result , num_whole index_min , num_whole index_max ) ;
    void _camera_origin_index_is_duplicate ( num_whole & result , num_whole index ) ;
    void _camera_target_index_is_duplicate ( num_whole & result , num_whole index ) ;
private :
    mediator * _mediator ;
    matrix_data _camera_matrix ;
    num_whole _camera_prepare_permitted ;
    num_whole _frames_to_change_camera_target ;
    num_whole _frames_to_change_camera_origin ;
    num_whole _random_seed ;
    vector_data _desired_camera_origin ;
    vector_data _desired_camera_target ;
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    num_whole _scheduled_camera_origin_indices [ 4 ] ;
    num_whole _scheduled_camera_target_indices [ 4 ] ;
    vector_data _scheduled_camera_origins [ 4 ] ;
    vector_data _scheduled_camera_targets [ 4 ] ;
    num_whole _camera_created ;
} ;

template < typename mediator >
shy_logic_camera < mediator > :: shy_logic_camera ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    num_whole i ;
    num_whole i_max ;
    num_fract zero ;
    platform :: math_make_num_whole ( i , 0 ) ;
    platform :: math_make_num_whole ( i_max , 4 ) ;
    platform :: math_make_num_fract ( zero , 0 , 1 ) ;
    platform :: math_make_num_whole ( _camera_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _frames_to_change_camera_target , 0 ) ;
    platform :: math_make_num_whole ( _frames_to_change_camera_origin , 0 ) ;
    platform :: math_make_num_whole ( _random_seed , 0 ) ;
    platform :: math_make_num_whole ( _camera_created , false ) ;
    for ( 
        ; platform :: condition_whole_less_than_whole ( i , i_max ) 
        ; platform :: math_inc_whole ( i )
        )
    {
        num_whole * origin_index_ptr = 0 ;
        num_whole * target_index_ptr = 0 ;
        vector_data * origin_ptr = 0 ;
        vector_data * target_ptr = 0 ;
        platform :: memory_pointer_offset ( origin_index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: memory_pointer_offset ( target_index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: memory_pointer_offset ( origin_ptr , _scheduled_camera_origins , i ) ;
        platform :: memory_pointer_offset ( target_ptr , _scheduled_camera_targets , i ) ;
        platform :: math_make_num_whole ( * origin_index_ptr , 0 ) ;
        platform :: math_make_num_whole ( * target_index_ptr , 0 ) ;
        platform :: vector_xyz ( * origin_ptr , zero , zero , zero ) ;
        platform :: vector_xyz ( * target_ptr , zero , zero , zero ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_matrix_use ( )
{
    if ( platform :: condition_true ( _camera_created ) )
        platform :: render_matrix_load ( _camera_matrix ) ;
    else
        platform :: render_matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_prepare_permit ( )
{
    platform :: math_make_num_whole ( _camera_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: camera_update ( )
{
    if ( platform :: condition_true ( _camera_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _camera_created ) )
        {
            _fill_camera_schedules ( ) ;
            _reset_camera_rubber ( ) ;
            _update_camera ( ) ;
            platform :: math_make_num_whole ( _camera_created , true ) ;
            _mediator -> camera_prepared ( ) ;
        }
        else
            _update_camera ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _get_entity_mesh_grid ( num_whole & result )
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
    num_whole i ;
    num_whole i_max ;
    platform :: math_make_num_whole ( i , 0 ) ;
    platform :: math_make_num_whole ( i_max , 4 ) ;
    for (
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        num_whole * origin_index_ptr = 0 ;
        num_whole * target_index_ptr = 0 ;
        vector_data * origin_pos_ptr = 0 ;
        vector_data * target_pos_ptr = 0 ;        
        platform :: memory_pointer_offset ( origin_pos_ptr , _scheduled_camera_origins , i ) ;
        platform :: memory_pointer_offset ( target_pos_ptr , _scheduled_camera_targets , i ) ;
        platform :: memory_pointer_offset ( origin_index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: memory_pointer_offset ( target_index_ptr , _scheduled_camera_target_indices , i ) ;
        _random_camera_origin_index ( * origin_index_ptr ) ;
        _random_camera_target_index ( * target_index_ptr ) ;
        _mediator -> get_entity_origin ( * origin_pos_ptr , * origin_index_ptr ) ;
        _mediator -> get_entity_origin ( * target_pos_ptr , * target_index_ptr ) ;
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
    num_fract fract_frames_to_change_origin ;
    num_fract fract_change_origin_in_frames ;
    num_fract spline_t ;
    
    platform :: math_make_fract_from_whole ( fract_frames_to_change_origin , _frames_to_change_camera_origin ) ;
    platform :: math_make_num_fract ( fract_change_origin_in_frames , _change_origin_in_frames , 1 ) ;
    platform :: math_div_fracts ( spline_t , fract_frames_to_change_origin , fract_change_origin_in_frames ) ;
    platform :: math_neg_fract ( spline_t ) ;
    platform :: math_add_to_fract ( spline_t , platform :: fract_1 ) ;
    platform :: math_dec_whole ( _frames_to_change_camera_origin ) ;
    if ( platform :: condition_whole_less_or_equal_to_zero ( _frames_to_change_camera_origin ) )
    {
        num_whole new_origin_index ;
        vector_data new_origin_pos ;
        platform :: math_make_num_whole ( _frames_to_change_camera_origin , _change_origin_in_frames ) ;
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
        , spline_t
        , _scheduled_camera_origins [ 0 ]
        , _scheduled_camera_origins [ 1 ]
        , _scheduled_camera_origins [ 2 ]
        , _scheduled_camera_origins [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_target ( )
{
    num_fract fract_frames_to_change_target ;
    num_fract fract_change_target_in_frames ;
    num_fract spline_t ;
    
    platform :: math_make_fract_from_whole ( fract_frames_to_change_target , _frames_to_change_camera_target ) ;
    platform :: math_make_num_fract ( fract_change_target_in_frames , _change_target_in_frames , 1 ) ;
    platform :: math_div_fracts ( spline_t , fract_frames_to_change_target , fract_change_target_in_frames ) ;
    platform :: math_neg_fract ( spline_t ) ;
    platform :: math_add_to_fract ( spline_t , platform :: fract_1 ) ;
    platform :: math_dec_whole ( _frames_to_change_camera_target ) ;
    if ( platform :: condition_whole_less_or_equal_to_zero ( _frames_to_change_camera_target ) )
    {
        num_whole new_target_index ;
        vector_data new_target_pos ;
        platform :: math_make_num_whole ( _frames_to_change_camera_target , _change_target_in_frames ) ;
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
        , spline_t
        , _scheduled_camera_targets [ 0 ]
        , _scheduled_camera_targets [ 1 ]
        , _scheduled_camera_targets [ 2 ]
        , _scheduled_camera_targets [ 3 ]
        ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_origin ( )
{
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform :: math_sub_fracts ( inv_rubber , platform :: fract_1 , _origin_rubber ( ) ) ;
    platform :: vector_mul ( old_part , _current_camera_origin , _origin_rubber ( ) ) ;
    platform :: vector_mul ( new_part , _desired_camera_origin , inv_rubber ) ;
    platform :: vector_add ( _current_camera_origin , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_target ( )
{
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform :: math_sub_fracts ( inv_rubber , platform :: fract_1 , _target_rubber ( ) ) ;
    platform :: vector_mul ( old_part , _current_camera_target , _target_rubber ( ) ) ;
    platform :: vector_mul ( new_part , _desired_camera_target , inv_rubber ) ;
    platform :: vector_add ( _current_camera_target , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_camera_matrix ( )
{
    num_fract shift_y ;
    vector_data up ;
    vector_data shift ;
    vector_data shifted_origin ;
    num_fract near_plane ;
    num_fract aspect_height ;
    num_fract entity_height ;
    
    _mediator -> get_entity_height ( entity_height ) ;
    _mediator -> get_near_plane_distance ( near_plane ) ;
    platform :: render_get_aspect_height ( aspect_height ) ;
    platform :: math_add_fracts ( shift_y , entity_height , near_plane ) ;
    platform :: math_add_to_fract ( shift_y , aspect_height ) ;
    platform :: vector_xyz ( up , platform :: fract_0 , platform :: fract_1 , platform :: fract_0 ) ;
    platform :: vector_xyz ( shift , platform :: fract_0 , shift_y , platform :: fract_0 ) ;
    platform :: vector_add ( shifted_origin , _current_camera_origin , shift ) ;
    _mediator -> camera_matrix_look_at ( _camera_matrix , shifted_origin , _current_camera_target , up ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_origin_index ( num_whole & result )
{
    num_whole index = platform :: whole_0 ;
    num_whole mesh_grid ;
    num_whole is_duplicate ;
    num_whole whole_2 ;
    num_whole index_max ;
    
    _get_entity_mesh_grid ( mesh_grid ) ;
    platform :: math_make_num_whole ( whole_2 , 2 ) ;
    platform :: math_mul_wholes ( index_max , mesh_grid , mesh_grid ) ;
    platform :: math_div_whole_by ( index_max , whole_2 ) ;
    do
    {
        _get_random_index ( index , platform :: whole_0 , index_max ) ;
        _camera_origin_index_is_duplicate ( is_duplicate , index ) ;
    } while ( platform :: condition_true ( is_duplicate ) ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_target_index ( num_whole & result )
{
    num_whole index = platform :: whole_0 ;
    num_whole mesh_grid ;
    num_whole is_duplicate ;
    num_whole whole_2 ;
    num_whole index_max ;
    num_whole index_min ;
    
    _get_entity_mesh_grid ( mesh_grid ) ;
    platform :: math_make_num_whole ( whole_2 , 2 ) ;
    platform :: math_mul_wholes ( index_max , mesh_grid , mesh_grid ) ;
    platform :: math_div_wholes ( index_min , index_max , whole_2 ) ;
    do
    {
        _get_random_index ( index , index_min , index_max ) ;
        _camera_target_index_is_duplicate ( is_duplicate , index ) ;
    } while ( platform :: condition_true ( is_duplicate ) ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _get_random_index ( num_whole & result , num_whole index_min , num_whole index_max )
{
    num_whole random_const_1 ;
    num_whole random_const_2 ;
    num_whole index_diff ;
    platform :: math_make_num_whole ( random_const_1 , 181 ) ;
    platform :: math_make_num_whole ( random_const_2 , 139 ) ;
    platform :: math_add_to_whole ( _random_seed , random_const_1 ) ;
    platform :: math_mod_whole_by ( _random_seed , random_const_2 ) ;
    platform :: math_sub_wholes ( index_diff , index_max , index_min ) ;
    platform :: math_mod_wholes ( result , _random_seed , index_diff ) ;
    platform :: math_add_to_whole ( result , index_min ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_origin_index_is_duplicate ( num_whole & result , num_whole index )
{
    num_whole i ;
    num_whole i_max ;
    num_whole * origin_index_ptr = 0 ;
    
    platform :: math_make_num_whole ( result , false ) ;
    for ( platform :: math_make_num_whole ( i , 0 )
        , platform :: math_make_num_whole ( i_max , 4 )
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i )
        )
    {
        platform :: memory_pointer_offset ( origin_index_ptr , _scheduled_camera_origin_indices , i ) ;
        if ( platform :: condition_wholes_are_equal ( * origin_index_ptr , index ) )
        {
            platform :: math_make_num_whole ( result , true ) ;
            break ;
        }
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_target_index_is_duplicate ( num_whole & result , num_whole index )
{
    num_whole i ;
    num_whole i_max ;
    num_whole * target_index_ptr = 0 ;
    
    platform :: math_make_num_whole ( result , false ) ;
    for ( platform :: math_make_num_whole ( i , 0 )
        , platform :: math_make_num_whole ( i_max , 4 ) 
        ; platform :: condition_whole_less_than_whole ( i , i_max )
        ; platform :: math_inc_whole ( i ) 
        )
    {
        platform :: memory_pointer_offset ( target_index_ptr , _scheduled_camera_target_indices , i ) ;
        if ( platform :: condition_wholes_are_equal ( * target_index_ptr , index ) )
        {
            platform :: math_make_num_whole ( result , true ) ;
            break ;
        }
    }
}
