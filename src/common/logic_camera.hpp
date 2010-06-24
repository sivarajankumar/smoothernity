template < typename mediator >
class shy_logic_camera
{
    typedef typename mediator :: engine_camera engine_camera ;
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    static const_int_32 _change_origin_in_frames = 139 ;
    static const_int_32 _change_target_in_frames = 181 ;
    static const num_fract _origin_rubber ( ) { return platform :: math_consts . fract_0 ; } // 0.99f ;
    static const num_fract _target_rubber ( ) { return platform :: math_consts . fract_0 ; } // 0.9f ;
public :
    shy_logic_camera ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: camera_update msg ) ;
    void receive ( typename messages :: camera_prepare_permit msg ) ;
    void receive ( typename messages :: camera_matrix_use msg ) ;
    void receive ( typename messages :: entities_height_reply msg ) ;
    void receive ( typename messages :: entities_mesh_grid_reply msg ) ;
    void receive ( typename messages :: entities_origin_reply msg ) ;
    void receive ( typename messages :: near_plane_distance_reply msg ) ;
private :
    void _proceed_with_update ( ) ;
    void _proceed_with_fill_camera_schedules ( ) ;
    void _proceed_with_camera_update ( ) ;
    void _proceed_with_update_desired_camera_target ( ) ;
    void _proceed_with_update_desired_camera_origin ( ) ;
    void _fill_next_camera_schedule ( ) ;
    void _reset_camera_rubber ( ) ;
    void _update_camera ( ) ;
    void _update_desired_camera_origin ( ) ;
    void _update_desired_camera_target ( ) ;
    void _update_current_camera_origin ( ) ;
    void _update_current_camera_target ( ) ;
    void _update_camera_matrix ( ) ;
    void _calc_desired_camera_target_pos ( ) ;
    void _calc_desired_camera_origin_pos ( ) ;
    void _random_camera_origin_index ( num_whole & result ) ;
    void _random_camera_target_index ( num_whole & result ) ;
    void _get_random_index ( num_whole & result , num_whole index_min , num_whole index_max ) ;
    void _camera_origin_index_is_duplicate ( num_whole & result , num_whole index ) ;
    void _camera_target_index_is_duplicate ( num_whole & result , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    matrix_data _camera_matrix ;
    num_whole _camera_prepare_permitted ;
    num_whole _frames_to_change_camera_target ;
    num_whole _frames_to_change_camera_origin ;
    num_whole _random_seed ;
    num_whole _camera_created ;
    
    num_whole _entities_height_requested ;
    num_whole _entities_height_replied ;
    num_fract _entities_height ;
    
    num_whole _entities_mesh_grid_requested ;
    num_whole _entities_mesh_grid_replied ;
    num_whole _entities_mesh_grid ;
    
    num_whole _near_plane_distance_requested ;
    num_whole _near_plane_distance_replied ;
    num_fract _near_plane_distance ;
    
    num_whole _filling_camera_schedules ;
    num_whole _fill_camera_schedules_index ;
    
    num_whole _fill_schedules_origin_requested ;
    num_whole _fill_schedules_origin_replied ;
    num_whole _fill_schedules_origin_index ;
    vector_data _fill_schedules_origin ;
    
    num_whole _fill_schedules_target_requested ;
    num_whole _fill_schedules_target_replied ;
    num_whole _fill_schedules_target_index ;
    vector_data _fill_schedules_target ;
    
    num_whole _desired_camera_origin_is_ready ;
    vector_data _desired_camera_origin ;
    num_whole _desired_camera_origin_new_requested ;
    num_whole _desired_camera_origin_new_index ;
    vector_data _desired_camera_origin_new_position ;
    
    num_whole _desired_camera_target_is_ready ;
    vector_data _desired_camera_target ;
    num_whole _desired_camera_target_new_requested ;
    num_whole _desired_camera_target_new_index ;
    vector_data _desired_camera_target_new_position ;
    
    vector_data _current_camera_origin ;
    vector_data _current_camera_target ;
    
    typename platform_static_array :: template static_array < num_whole , 4 > _scheduled_camera_origin_indices ;
    typename platform_static_array :: template static_array < num_whole , 4 > _scheduled_camera_target_indices ;
    typename platform_static_array :: template static_array < vector_data , 4 > _scheduled_camera_origins ;
    typename platform_static_array :: template static_array < vector_data , 4 > _scheduled_camera_targets ;
} ;

template < typename mediator >
shy_logic_camera < mediator > :: shy_logic_camera ( )
{
    _camera_prepare_permitted = platform :: math_consts . whole_false ;
    _camera_created = platform :: math_consts . whole_false ;
    _entities_height_requested = platform :: math_consts . whole_false ;
    _entities_height_replied = platform :: math_consts . whole_false ;
    _entities_mesh_grid_requested = platform :: math_consts . whole_false ;
    _entities_mesh_grid_replied = platform :: math_consts . whole_false ;
    _near_plane_distance_requested = platform :: math_consts . whole_false ;
    _near_plane_distance_replied = platform :: math_consts . whole_false ;
    _random_seed = platform :: math_consts . whole_0 ;
    _frames_to_change_camera_target = platform :: math_consts . whole_0 ;
    _frames_to_change_camera_origin = platform :: math_consts . whole_0 ;
    _filling_camera_schedules = platform :: math_consts . whole_false ;
    _fill_camera_schedules_index = platform :: math_consts . whole_0 ;
    _fill_schedules_origin_requested = platform :: math_consts . whole_false ;
    _fill_schedules_origin_replied = platform :: math_consts . whole_false ;
    _fill_schedules_target_requested = platform :: math_consts . whole_false ;
    _fill_schedules_target_replied = platform :: math_consts . whole_false ;
    _desired_camera_origin_new_requested = platform :: math_consts . whole_false ;
    _desired_camera_target_new_requested = platform :: math_consts . whole_false ;
    for ( num_whole i = platform :: math_consts . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , platform :: math_consts . whole_4 )
        ; platform_math :: inc_whole ( i )
        )
    {
        num_whole & origin_index = platform_static_array :: element ( _scheduled_camera_origin_indices , i ) ;
        num_whole & target_index = platform_static_array :: element ( _scheduled_camera_target_indices , i ) ;
        vector_data & origin_pos = platform_static_array :: element ( _scheduled_camera_origins , i ) ;
        vector_data & target_pos = platform_static_array :: element ( _scheduled_camera_targets , i ) ;
        origin_index = platform :: math_consts . whole_0 ;
        target_index = platform :: math_consts . whole_0 ;
        platform_vector :: xyz ( origin_pos , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
        platform_vector :: xyz ( target_pos , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: camera_matrix_use msg )
{
    if ( platform_conditions :: whole_is_true ( _camera_created ) )
        platform_render :: matrix_load ( _camera_matrix ) ;
    else
        platform_render :: matrix_identity ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: camera_prepare_permit msg )
{
    platform_math :: make_num_whole ( _camera_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: camera_update msg )
{
    if ( platform_conditions :: whole_is_true ( _camera_prepare_permitted ) )
    {
        _entities_height_requested = platform :: math_consts . whole_true ;
        _entities_mesh_grid_requested = platform :: math_consts . whole_true ;
        _near_plane_distance_requested = platform :: math_consts . whole_true ;
        _mediator . get ( ) . send ( typename messages :: entities_height_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: entities_mesh_grid_request ( ) ) ;
        _mediator . get ( ) . send ( typename messages :: near_plane_distance_request ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: entities_height_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _entities_height_requested ) )
    {
        _entities_height_requested = platform :: math_consts . whole_false ;
        _entities_height_replied = platform :: math_consts . whole_true ;
        _entities_height = msg . height ;
        _proceed_with_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: entities_mesh_grid_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _entities_mesh_grid_requested ) )
    {
        _entities_mesh_grid_requested = platform :: math_consts . whole_false ;
        _entities_mesh_grid_replied = platform :: math_consts . whole_true ;
        _entities_mesh_grid = msg . grid ;
        _proceed_with_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: near_plane_distance_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _near_plane_distance_requested ) )
    {
        _near_plane_distance_requested = platform :: math_consts . whole_false ;
        _near_plane_distance_replied = platform :: math_consts . whole_true ;
        _near_plane_distance = msg . distance ;
        _proceed_with_update ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: receive ( typename messages :: entities_origin_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _fill_schedules_origin_requested )
      && platform_conditions :: wholes_are_equal ( _fill_schedules_origin_index , msg . index )
       )
    {
        _fill_schedules_origin_requested = platform :: math_consts . whole_false ;
        _fill_schedules_origin_replied = platform :: math_consts . whole_true ;
        _fill_schedules_origin = msg . origin ;
        _proceed_with_fill_camera_schedules ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _fill_schedules_target_requested )
      && platform_conditions :: wholes_are_equal ( _fill_schedules_target_index , msg . index )
       )
    {
        _fill_schedules_target_requested = platform :: math_consts . whole_false ;
        _fill_schedules_target_replied = platform :: math_consts . whole_true ;
        _fill_schedules_target = msg . origin ;
        _proceed_with_fill_camera_schedules ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _desired_camera_origin_new_requested )
      && platform_conditions :: wholes_are_equal ( _desired_camera_origin_new_index , msg . index )
       )
    {
        _desired_camera_origin_new_requested = platform :: math_consts . whole_false ;
        _desired_camera_origin_new_position = msg . origin ;
        _proceed_with_update_desired_camera_origin ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _desired_camera_target_new_requested )
      && platform_conditions :: wholes_are_equal ( _desired_camera_target_new_index , msg . index )
       )
    {
        _desired_camera_target_new_requested = platform :: math_consts . whole_false ;
        _desired_camera_target_new_position = msg . origin ;
        _proceed_with_update_desired_camera_target ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _proceed_with_update ( )
{
    if ( platform_conditions :: whole_is_true ( _entities_height_replied ) 
      && platform_conditions :: whole_is_true ( _entities_mesh_grid_replied )
      && platform_conditions :: whole_is_true ( _near_plane_distance_replied )
       )
    {
        _entities_height_replied = platform :: math_consts . whole_false ;
        _entities_mesh_grid_replied = platform :: math_consts . whole_false ;
        if ( platform_conditions :: whole_is_false ( _camera_created ) )
        {
            if ( platform_conditions :: whole_is_false ( _filling_camera_schedules ) )
            {
                _filling_camera_schedules = platform :: math_consts . whole_true ;
                _fill_next_camera_schedule ( ) ;
            }
        }
        else
            _update_camera ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _reset_camera_rubber ( )
{
    _current_camera_origin = platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_2 ) ;
    _current_camera_target = platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_2 ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _proceed_with_fill_camera_schedules ( )
{
    if ( platform_conditions :: whole_is_true ( _fill_schedules_origin_replied )
      && platform_conditions :: whole_is_true ( _fill_schedules_target_replied )
       )
    {
        _fill_schedules_origin_replied = platform :: math_consts . whole_false ;
        _fill_schedules_target_replied = platform :: math_consts . whole_false ;
        platform_static_array :: element ( _scheduled_camera_origin_indices , _fill_camera_schedules_index ) = _fill_schedules_origin_index ;
        platform_static_array :: element ( _scheduled_camera_target_indices , _fill_camera_schedules_index ) = _fill_schedules_target_index ;
        platform_static_array :: element ( _scheduled_camera_origins , _fill_camera_schedules_index ) = _fill_schedules_origin ;
        platform_static_array :: element ( _scheduled_camera_targets , _fill_camera_schedules_index ) = _fill_schedules_target ;
        platform_math :: inc_whole ( _fill_camera_schedules_index ) ;
        _fill_next_camera_schedule ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _fill_next_camera_schedule ( )
{
    if ( platform_conditions :: whole_less_than_whole ( _fill_camera_schedules_index , platform :: math_consts . whole_4 ) )
    {
        _random_camera_origin_index ( _fill_schedules_origin_index ) ;
        _random_camera_target_index ( _fill_schedules_target_index ) ;
        _fill_schedules_origin_requested = platform :: math_consts . whole_true ;
        _fill_schedules_target_requested = platform :: math_consts . whole_true ;
        typename messages :: entities_origin_request origin_request_msg ;
        typename messages :: entities_origin_request target_request_msg ;
        origin_request_msg . index = _fill_schedules_origin_index ;
        target_request_msg . index = _fill_schedules_target_index ;
        _mediator . get ( ) . send ( origin_request_msg ) ;
        _mediator . get ( ) . send ( target_request_msg ) ;
    }
    else
    {
        _reset_camera_rubber ( ) ;
        _update_camera ( ) ;
        platform_math :: make_num_whole ( _camera_created , true ) ;
        _mediator . get ( ) . send ( typename messages :: camera_prepared ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_camera ( )
{
    _update_desired_camera_origin ( ) ;
    _update_desired_camera_target ( ) ;
    _proceed_with_camera_update ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _proceed_with_camera_update ( )
{
    if ( platform_conditions :: whole_is_true ( _desired_camera_origin_is_ready ) 
      && platform_conditions :: whole_is_true ( _desired_camera_target_is_ready )
       )
    {
        _update_current_camera_origin ( ) ;
        _update_current_camera_target ( ) ;
        _update_camera_matrix ( ) ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _proceed_with_update_desired_camera_origin ( )
{
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_0 ) =
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_1 ) ;
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_1 ) = 
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_2 ) ;
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_2 ) =
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_3 ) ;
    platform_static_array :: element ( _scheduled_camera_origin_indices , platform :: math_consts . whole_3 ) = _desired_camera_origin_new_index ;

    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_0 ) = 
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_1 ) ;
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_1 ) = 
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_2 ) ;
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_2 ) = 
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_3 ) ;
    platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_3 ) = _desired_camera_origin_new_position ;
    
    _calc_desired_camera_origin_pos ( ) ;
    _desired_camera_origin_is_ready = platform :: math_consts . whole_true ;
    
    _proceed_with_camera_update ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_origin ( )
{
    _desired_camera_origin_is_ready = platform :: math_consts . whole_false ;
    platform_math :: dec_whole ( _frames_to_change_camera_origin ) ;
    if ( platform_conditions :: whole_less_or_equal_to_zero ( _frames_to_change_camera_origin ) )
    {
        platform_math :: make_num_whole ( _frames_to_change_camera_origin , _change_origin_in_frames ) ;
        _random_camera_origin_index ( _desired_camera_origin_new_index ) ;
        _desired_camera_origin_new_requested = platform :: math_consts . whole_true ;
        typename messages :: entities_origin_request entities_origin_request_msg ;
        entities_origin_request_msg . index = _desired_camera_origin_new_index ;
        _mediator . get ( ) . send ( entities_origin_request_msg ) ;
    }
    else
    {
        _calc_desired_camera_origin_pos ( ) ;
        _desired_camera_origin_is_ready = platform :: math_consts . whole_true ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _calc_desired_camera_origin_pos ( )
{
    num_fract fract_frames_to_change_camera_origin ;
    num_fract fract_change_origin_in_frames ;
    num_fract spline_pos ;
    platform_math :: make_fract_from_whole ( fract_frames_to_change_camera_origin , _frames_to_change_camera_origin ) ;
    platform_math :: make_num_fract ( fract_change_origin_in_frames , _change_origin_in_frames , 1 ) ;
    platform_math :: div_fracts ( spline_pos , fract_frames_to_change_camera_origin , fract_change_origin_in_frames ) ;
    platform_math :: neg_fract ( spline_pos ) ;
    platform_math :: add_to_fract ( spline_pos , platform :: math_consts . fract_1 ) ;
    
    engine_math :: math_catmull_rom_spline
        ( _desired_camera_origin
        , spline_pos
        , platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_0 )
        , platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_1 )
        , platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_2 )
        , platform_static_array :: element ( _scheduled_camera_origins , platform :: math_consts . whole_3 )
        ) ;        
}

template < typename mediator >
void shy_logic_camera < mediator > :: _proceed_with_update_desired_camera_target ( )
{        
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_0 ) = 
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_1 ) ;
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_1 ) = 
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_2 ) ;
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_2 ) = 
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_3 ) ;
    platform_static_array :: element ( _scheduled_camera_target_indices , platform :: math_consts . whole_3 ) = _desired_camera_target_new_index ;
    
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_0 ) = 
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_1 ) ;
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_1 ) = 
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_2 ) ;
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_2 ) = 
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_3 ) ;
    platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_3 ) = _desired_camera_target_new_position ;
    
    _calc_desired_camera_target_pos ( ) ;
    _desired_camera_target_is_ready = platform :: math_consts . whole_true ;
    
    _proceed_with_camera_update ( ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_desired_camera_target ( )
{
    _desired_camera_target_is_ready = platform :: math_consts . whole_false ;
    platform_math :: dec_whole ( _frames_to_change_camera_target ) ;
    if ( platform_conditions :: whole_less_or_equal_to_zero ( _frames_to_change_camera_target ) )
    {
        platform_math :: make_num_whole ( _frames_to_change_camera_target , _change_target_in_frames ) ;
        _random_camera_target_index ( _desired_camera_target_new_index ) ;
        _desired_camera_target_new_requested = platform :: math_consts . whole_true ;
        typename messages :: entities_origin_request entities_origin_request_msg ;
        entities_origin_request_msg . index = _desired_camera_target_new_index ;
        _mediator . get ( ) . send ( entities_origin_request_msg ) ;
    }
    else
    {
        _calc_desired_camera_target_pos ( ) ;
        _desired_camera_target_is_ready = platform :: math_consts . whole_true ;
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _calc_desired_camera_target_pos ( )
{
    num_fract fract_frames_to_change_camera_target ;
    num_fract fract_change_target_in_frames ;
    num_fract spline_pos ;
    platform_math :: make_fract_from_whole ( fract_frames_to_change_camera_target , _frames_to_change_camera_target ) ;
    platform_math :: make_num_fract ( fract_change_target_in_frames , _change_target_in_frames , 1 ) ;
    platform_math :: div_fracts ( spline_pos , fract_frames_to_change_camera_target , fract_change_target_in_frames ) ;
    platform_math :: neg_fract ( spline_pos ) ;
    platform_math :: add_to_fract ( spline_pos , platform :: math_consts . fract_1 ) ;
    
    engine_math :: math_catmull_rom_spline
        ( _desired_camera_target
        , spline_pos
        , platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_0 )
        , platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_1 )
        , platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_2 )
        , platform_static_array :: element ( _scheduled_camera_targets , platform :: math_consts . whole_3 )
        ) ;        
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_origin ( )
{
    num_fract rubber ;
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform_math :: sub_fracts ( inv_rubber , platform :: math_consts . fract_1 , _origin_rubber ( ) ) ;
    platform_vector :: mul ( old_part , _current_camera_origin , _origin_rubber ( ) ) ;
    platform_vector :: mul ( new_part , _desired_camera_origin , inv_rubber ) ;
    platform_vector :: add ( _current_camera_origin , old_part , new_part ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _update_current_camera_target ( )
{
    num_fract rubber ;
    num_fract inv_rubber ;
    vector_data old_part ;
    vector_data new_part ;
    platform_math :: sub_fracts ( inv_rubber , platform :: math_consts . fract_1 , _target_rubber ( ) ) ;
    platform_vector :: mul ( old_part , _current_camera_target , _target_rubber ( ) ) ;
    platform_vector :: mul ( new_part , _desired_camera_target , inv_rubber ) ;
    platform_vector :: add ( _current_camera_target , old_part , new_part ) ;
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
    num_fract aspect_height ;
    num_fract entity_height ;
    
    platform_render :: get_aspect_height ( aspect_height ) ;
    platform_math :: make_num_fract ( up_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( up_y , 1 , 1 ) ;
    platform_math :: make_num_fract ( up_z , 0 , 1 ) ;
    platform_math :: make_num_fract ( shift_x , 0 , 1 ) ;
    shift_y = _entities_height ;
    platform_math :: add_to_fract ( shift_y , aspect_height ) ;
    platform_math :: add_to_fract ( shift_y , _near_plane_distance ) ;
    platform_math :: make_num_fract ( shift_z , 0 , 1 ) ;
    platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    platform_vector :: xyz ( shift , shift_x , shift_y , shift_z ) ;
    platform_vector :: add ( shifted_origin , _current_camera_origin , shift ) ;
    engine_camera :: camera_matrix_look_at ( _camera_matrix , shifted_origin , _current_camera_target , up ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_origin_index ( num_whole & result )
{
    num_whole index ;
    num_whole index_max ;
    num_whole is_duplicate ;
    platform_math :: make_num_whole ( index , 0 ) ;
    platform_math :: div_wholes ( index_max , _entities_mesh_grid , platform :: math_consts . whole_2 ) ;
    platform_math :: mul_whole_by ( index_max , _entities_mesh_grid ) ;
    do
    {
        _get_random_index ( index , platform :: math_consts . whole_0 , index_max ) ;
        _camera_origin_index_is_duplicate ( is_duplicate , index ) ;
    } while ( platform_conditions :: whole_is_true ( is_duplicate ) ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _random_camera_target_index ( num_whole & result )
{
    num_whole index ;
    num_whole index_min ;
    num_whole index_max ;
    num_whole is_duplicate ;
    platform_math :: make_num_whole ( index , 0 ) ;
    platform_math :: div_wholes ( index_min , _entities_mesh_grid , platform :: math_consts . whole_2 ) ;
    platform_math :: mul_whole_by ( index_min , _entities_mesh_grid ) ;
    platform_math :: mul_wholes ( index_max , _entities_mesh_grid , _entities_mesh_grid ) ;
    do
    {
        _get_random_index ( index , index_min , index_max ) ;
        _camera_target_index_is_duplicate ( is_duplicate , index ) ;
    } while ( platform_conditions :: whole_is_true ( is_duplicate ) ) ;
    result = index ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _get_random_index ( num_whole & result , num_whole index_min , num_whole index_max )
{
    num_whole random_const_1 ;
    num_whole random_const_2 ;
    num_whole index_diff ;
    platform_math :: make_num_whole ( random_const_1 , 181 ) ;
    platform_math :: make_num_whole ( random_const_2 , 139 ) ;
    platform_math :: add_to_whole ( _random_seed , random_const_1 ) ;
    platform_math :: mod_whole_by ( _random_seed , random_const_2 ) ;
    platform_math :: sub_wholes ( index_diff , index_max , index_min ) ;
    platform_math :: mod_wholes ( result , _random_seed , index_diff ) ;
    platform_math :: add_to_whole ( result , index_min ) ;
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_origin_index_is_duplicate ( num_whole & result , num_whole index )
{
    platform_math :: make_num_whole ( result , false ) ;
    for ( num_whole i = platform :: math_consts . whole_0 
        ; platform_conditions :: whole_less_than_whole ( i , platform :: math_consts . whole_4 ) 
        ; platform_math :: inc_whole ( i )
        )
    {
        num_whole & index_ptr = platform_static_array :: element ( _scheduled_camera_origin_indices , i ) ;
        if ( platform_conditions :: wholes_are_equal ( index_ptr , index ) )
        {
            platform_math :: make_num_whole ( result , true ) ;
            break ;
        }
    }
}

template < typename mediator >
void shy_logic_camera < mediator > :: _camera_target_index_is_duplicate ( num_whole & result , num_whole index )
{
    platform_math :: make_num_whole ( result , false ) ;
    for ( num_whole i = platform :: math_consts . whole_0 
        ; platform_conditions :: whole_less_than_whole ( i , platform :: math_consts . whole_4 ) 
        ; platform_math :: inc_whole ( i )
        )
    {
        num_whole & index_ptr = platform_static_array :: element ( _scheduled_camera_target_indices , i ) ;
        if ( platform_conditions :: wholes_are_equal ( index_ptr , index ) )
        {
            platform_math :: make_num_whole ( result , true ) ;
            break ;
        }
    }
}
