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
    typedef typename mediator :: platform :: num_whole num_whole ;
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
    for ( num_whole i = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( i , platform :: whole_4 )
        ; platform :: math_inc_whole ( i )
        )
    {
        int_32 * origin_index_ptr = 0 ;
        int_32 * target_index_ptr = 0 ;
        vector_data * origin_pos_ptr = 0 ;
        vector_data * target_pos_ptr = 0 ;
        platform :: memory_pointer_offset ( origin_index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: memory_pointer_offset ( target_index_ptr , _scheduled_camera_target_indices , i ) ;
        platform :: memory_pointer_offset ( origin_pos_ptr , _scheduled_camera_origins , i ) ;
        platform :: memory_pointer_offset ( target_pos_ptr , _scheduled_camera_targets , i ) ;
        * origin_index_ptr = 0 ;
        * target_index_ptr = 0 ;
        platform :: vector_xyz ( * origin_pos_ptr , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
        platform :: vector_xyz ( * target_pos_ptr , platform :: fract_0 , platform :: fract_0 , platform :: fract_0 ) ;
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
    for ( num_whole i = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( i , platform :: whole_4 ) 
        ; platform :: math_inc_whole ( i )
        )
    {
        int_32 origin_index ;
        int_32 target_index ;
        vector_data origin_pos ;
        vector_data target_pos ;
        int_32 * origin_index_ptr = 0 ;
        int_32 * target_index_ptr = 0 ;
        vector_data * origin_pos_ptr = 0 ;
        vector_data * target_pos_ptr = 0 ;
        
        _random_camera_origin_index ( origin_index ) ;
        _random_camera_target_index ( target_index ) ;
        _mediator -> get_entity_origin ( origin_pos , origin_index ) ;
        _mediator -> get_entity_origin ( target_pos , target_index ) ;
        
        platform :: memory_pointer_offset ( origin_index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: memory_pointer_offset ( target_index_ptr , _scheduled_camera_target_indices , i ) ;
        platform :: memory_pointer_offset ( origin_pos_ptr , _scheduled_camera_origins , i ) ;
        platform :: memory_pointer_offset ( target_pos_ptr , _scheduled_camera_targets , i ) ;
        
        * origin_index_ptr = origin_index ;
        * target_index_ptr = target_index ;
        * origin_pos_ptr = origin_pos ;
        * target_pos_ptr = target_pos ;
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
    num_whole whole_frames_to_change_camera_origin ;
    platform :: math_make_num_whole ( whole_frames_to_change_camera_origin , _frames_to_change_camera_origin ) ;
    platform :: math_dec_whole ( whole_frames_to_change_camera_origin ) ;
    if ( platform :: condition_whole_less_or_equal_to_zero ( whole_frames_to_change_camera_origin ) )
    {
        int_32 new_origin_index ;
        vector_data new_origin_pos ;
        
        platform :: math_make_num_whole ( whole_frames_to_change_camera_origin , _change_origin_in_frames ) ;
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
    
    num_fract fract_frames_to_change_camera_origin ;
    num_fract fract_change_origin_in_frames ;
    num_fract spline_pos ;
    platform :: math_make_fract_from_whole ( fract_frames_to_change_camera_origin , whole_frames_to_change_camera_origin ) ;
    platform :: math_make_num_fract ( fract_change_origin_in_frames , _change_origin_in_frames , 1 ) ;
    platform :: math_div_fracts ( spline_pos , fract_frames_to_change_camera_origin , fract_change_origin_in_frames ) ;
    platform :: math_neg_fract ( spline_pos ) ;
    platform :: math_add_to_fract ( spline_pos , platform :: fract_1 ) ;
    
    _mediator -> math_catmull_rom_spline
        ( _desired_camera_origin
        , spline_pos . debug_to_float_32 ( )
        , _scheduled_camera_origins [ 0 ]
        , _scheduled_camera_origins [ 1 ]
        , _scheduled_camera_origins [ 2 ]
        , _scheduled_camera_origins [ 3 ]
        ) ;
        
    _frames_to_change_camera_origin = whole_frames_to_change_camera_origin . debug_to_int_32 ( ) ;    
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_target ( )
{
    num_whole whole_frames_to_change_camera_target ;
    platform :: math_make_num_whole ( whole_frames_to_change_camera_target , _frames_to_change_camera_target ) ;
    platform :: math_dec_whole ( whole_frames_to_change_camera_target ) ;
    if ( platform :: condition_whole_less_or_equal_to_zero ( whole_frames_to_change_camera_target ) )
    {
        int_32 new_target_index ;
        vector_data new_target_pos ;
        
        platform :: math_make_num_whole ( whole_frames_to_change_camera_target , _change_target_in_frames ) ;
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
    
    num_fract fract_frames_to_change_camera_target ;
    num_fract fract_change_target_in_frames ;
    num_fract spline_pos ;
    platform :: math_make_fract_from_whole ( fract_frames_to_change_camera_target , whole_frames_to_change_camera_target ) ;
    platform :: math_make_num_fract ( fract_change_target_in_frames , _change_target_in_frames , 1 ) ;
    platform :: math_div_fracts ( spline_pos , fract_frames_to_change_camera_target , fract_change_target_in_frames ) ;
    platform :: math_neg_fract ( spline_pos ) ;
    platform :: math_add_to_fract ( spline_pos , platform :: fract_1 ) ;
    
    _mediator -> math_catmull_rom_spline
        ( _desired_camera_target
        , spline_pos . debug_to_float_32 ( )
        , _scheduled_camera_targets [ 0 ]
        , _scheduled_camera_targets [ 1 ]
        , _scheduled_camera_targets [ 2 ]
        , _scheduled_camera_targets [ 3 ]
        ) ;
        
    _frames_to_change_camera_target = whole_frames_to_change_camera_target . debug_to_int_32 ( ) ;    
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_origin ( )
{
    num_fract rubber ;
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform :: math_make_num_fract ( rubber , int_32 ( _origin_rubber ( ) * 1000.0f ) , 1000 ) ;
    platform :: math_sub_fracts ( inv_rubber , platform :: fract_1 , rubber ) ;
    platform :: vector_mul ( old_part , _current_camera_origin , rubber ) ;
    platform :: vector_mul ( new_part , _desired_camera_origin , inv_rubber ) ;
    platform :: vector_add ( _current_camera_origin , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_target ( )
{
    num_fract rubber ;
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform :: math_make_num_fract ( rubber , int_32 ( _target_rubber ( ) * 1000.0f ) , 1000 ) ;
    platform :: math_sub_fracts ( inv_rubber , platform :: fract_1 , rubber ) ;
    platform :: vector_mul ( old_part , _current_camera_target , rubber ) ;
    platform :: vector_mul ( new_part , _desired_camera_target , inv_rubber ) ;
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
    num_fract near_plane ;
    num_fract aspect_height ;
    num_fract entity_height ;
    
    float_32 entity_height_float_32 ;
    _mediator -> get_entity_height ( entity_height_float_32 ) ;
    platform :: math_make_num_fract ( entity_height , int_32 ( entity_height_float_32 * 1000.0f ) , 1000 ) ;
    
    _mediator -> get_near_plane_distance ( near_plane ) ;
    platform :: render_get_aspect_height ( aspect_height ) ;
    platform :: math_make_num_fract ( up_x , 0 , 1 ) ;
    platform :: math_make_num_fract ( up_y , 1 , 1 ) ;
    platform :: math_make_num_fract ( up_z , 0 , 1 ) ;
    platform :: math_make_num_fract ( shift_x , 0 , 1 ) ;
    shift_y = entity_height ;
    platform :: math_add_to_fract ( shift_y , aspect_height ) ;
    platform :: math_add_to_fract ( shift_y , near_plane ) ;
    platform :: math_make_num_fract ( shift_z , 0 , 1 ) ;
    platform :: vector_xyz ( up , up_x , up_y , up_z ) ;
    platform :: vector_xyz ( shift , shift_x , shift_y , shift_z ) ;
    platform :: vector_add ( shifted_origin , _current_camera_origin , shift ) ;
    _mediator -> camera_matrix_look_at ( _camera_matrix , shifted_origin , _current_camera_target , up ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_origin_index ( int_32 & result )
{
    num_whole index ;
    num_whole index_max ;
    num_whole mesh_grid ;
    num_whole is_duplicate ;
    int_32 mesh_grid_int_32 ;
    platform :: math_make_num_whole ( index , 0 ) ;
    _get_entity_mesh_grid ( mesh_grid_int_32 ) ;
    platform :: math_make_num_whole ( mesh_grid , mesh_grid_int_32 ) ;
    platform :: math_div_wholes ( index_max , mesh_grid , platform :: whole_2 ) ;
    platform :: math_mul_whole_by ( index_max , mesh_grid ) ;
    do
    {
        int_32 index_int_32 ;
        int_32 is_duplicate_int_32 ;
        _get_random_index ( index_int_32 , platform :: whole_0 . debug_to_int_32 ( ) , index_max . debug_to_int_32 ( ) ) ;
        platform :: math_make_num_whole ( index , index_int_32 ) ;
        _camera_origin_index_is_duplicate ( is_duplicate_int_32 , index . debug_to_int_32 ( ) ) ;
        platform :: math_make_num_whole ( is_duplicate , is_duplicate_int_32 ) ;
    } while ( platform :: condition_true ( is_duplicate ) ) ;
    result = index . debug_to_int_32 ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_target_index ( int_32 & result )
{
    num_whole index ;
    num_whole index_min ;
    num_whole index_max ;
    num_whole mesh_grid ;
    num_whole is_duplicate ;
    int_32 mesh_grid_int_32 ;
    platform :: math_make_num_whole ( index , 0 ) ;
    _get_entity_mesh_grid ( mesh_grid_int_32 ) ;
    platform :: math_make_num_whole ( mesh_grid , mesh_grid_int_32 ) ;
    platform :: math_div_wholes ( index_min , mesh_grid , platform :: whole_2 ) ;
    platform :: math_mul_whole_by ( index_min , mesh_grid ) ;
    platform :: math_mul_wholes ( index_max , mesh_grid , mesh_grid ) ;
    do
    {
        int_32 index_int_32 ;
        int_32 is_duplicate_int_32 ;
        _get_random_index ( index_int_32 , index_min . debug_to_int_32 ( ) , index_max . debug_to_int_32 ( ) ) ;
        platform :: math_make_num_whole ( index , index_int_32 ) ;
        _camera_target_index_is_duplicate ( is_duplicate_int_32 , index . debug_to_int_32 ( ) ) ;
        platform :: math_make_num_whole ( is_duplicate , is_duplicate_int_32 ) ;
    } while ( platform :: condition_true ( is_duplicate ) ) ;
    result = index . debug_to_int_32 ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _get_random_index ( int_32 & result_int_32 , int_32 index_min_int_32 , int_32 index_max_int_32 )
{
    num_whole num_random_seed ;
    num_whole random_const_1 ;
    num_whole random_const_2 ;
    num_whole result ;
    num_whole index_min ;
    num_whole index_max ;
    num_whole index_diff ;
    platform :: math_make_num_whole ( num_random_seed , _random_seed ) ;
    platform :: math_make_num_whole ( random_const_1 , 181 ) ;
    platform :: math_make_num_whole ( random_const_2 , 139 ) ;
    platform :: math_make_num_whole ( index_min , index_min_int_32 ) ;
    platform :: math_make_num_whole ( index_max , index_max_int_32 ) ;
    platform :: math_add_to_whole ( num_random_seed , random_const_1 ) ;
    platform :: math_mod_whole_by ( num_random_seed , random_const_2 ) ;
    platform :: math_sub_wholes ( index_diff , index_max , index_min ) ;
    platform :: math_mod_wholes ( result , num_random_seed , index_diff ) ;
    platform :: math_add_to_whole ( result , index_min ) ;
    _random_seed = num_random_seed . debug_to_int_32 ( ) ;
    result_int_32 = result . debug_to_int_32 ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_origin_index_is_duplicate ( int_32 & result_int_32 , int_32 index_int_32 )
{
    num_whole index ;
    num_whole result ;
    platform :: math_make_num_whole ( index , index_int_32 ) ;
    platform :: math_make_num_whole ( result , false ) ;
    for ( num_whole i = platform :: whole_0 
        ; platform :: condition_whole_less_than_whole ( i , platform :: whole_4 ) 
        ; platform :: math_inc_whole ( i )
        )
    {
        num_whole num_index ;
        int_32 * index_ptr = 0 ;
        platform :: memory_pointer_offset ( index_ptr , _scheduled_camera_origin_indices , i ) ;
        platform :: math_make_num_whole ( num_index , * index_ptr ) ;
        if ( platform :: condition_wholes_are_equal ( num_index , index ) )
        {
            platform :: math_make_num_whole ( result , true ) ;
            break ;
        }
    }
    result_int_32 = result . debug_to_int_32 ( ) ;
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
