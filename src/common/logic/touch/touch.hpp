template < typename mediator >
class shy_logic_touch
{
    typedef typename mediator :: engine_render_stateless :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_touch platform_touch ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;

    class _logic_touch_consts_type
    {
    public :
        _logic_touch_consts_type ( ) ;
        num_fract spot_r ;
        num_fract spot_g ;
        num_fract spot_b ;
        num_fract spot_pos_z ;
        num_fract spot_size ;
        num_whole spot_edges ;
        num_whole spot_lifetime_in_frames ;
   } ;

public :
    shy_logic_touch ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_touch_prepare_permit ) ;
    void receive ( typename messages :: logic_touch_render ) ;
    void receive ( typename messages :: logic_touch_update ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
private :
    shy_logic_touch < mediator > & operator= ( const shy_logic_touch < mediator > & ) ;
    void _update_spot ( ) ;
	void _decrease_spot_lifetime ( ) ;
	void _poll_touchscreen ( ) ;
	void _poll_mouse ( ) ;
	void _place_new_spot ( ) ;
    void _render_spot_mesh ( ) ;
    void _create_spot_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < platform_touch > _platform_touch ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_touch_consts_type _logic_touch_consts ;
    num_whole _spot_frames_left ;
    num_whole _spot_mesh_created ;
    num_whole _spot_prepare_permitted ;
	num_whole _should_place_new_spot ;
    num_whole _mesh_create_requested ;
	num_fract _spot_x ;
	num_fract _spot_y ;
    engine_render_mesh_id _spot_mesh_id ;
    vector_data _spot_position ;
} ;

template < typename mediator >
shy_logic_touch < mediator > :: shy_logic_touch ( )
{
}

template < typename mediator >
shy_logic_touch < mediator > & shy_logic_touch < mediator > :: operator= ( const shy_logic_touch < mediator > & )
{
    return * this ;
}

template < typename mediator >
shy_logic_touch < mediator > :: _logic_touch_consts_type :: _logic_touch_consts_type ( )
{
    platform_math :: make_num_fract ( spot_r , 255 , 255 ) ;
    platform_math :: make_num_fract ( spot_g , 255 , 255 ) ;
    platform_math :: make_num_fract ( spot_b , 255 , 255 ) ;
    platform_math :: make_num_fract ( spot_size , 3 , 10 ) ;
    platform_math :: make_num_fract ( spot_pos_z , - 3 , 1 ) ;
    platform_math :: make_num_whole ( spot_edges , 32 ) ;
    platform_math :: make_num_whole ( spot_lifetime_in_frames , 60 ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_touch = platform_obj . get ( ) . touch ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _spot_frames_left = _platform_math_consts . get ( ) . whole_0 ;
    _spot_mesh_created = _platform_math_consts . get ( ) . whole_false ;
    _spot_prepare_permitted = _platform_math_consts . get ( ) . whole_false ;
    _should_place_new_spot = _platform_math_consts . get ( ) . whole_false ;
    _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: logic_touch_prepare_permit )
{
    _spot_prepare_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: logic_touch_render )
{
    if ( platform_conditions :: whole_is_true ( _spot_mesh_created ) && platform_conditions :: whole_greater_than_zero ( _spot_frames_left ) )
        _render_spot_mesh ( ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: logic_touch_update )
{
    if ( platform_conditions :: whole_is_true ( _spot_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _spot_mesh_created ) )
        {
            _mesh_create_requested = _platform_math_consts . get ( ) . whole_true ;
            
            typename messages :: engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = _logic_touch_consts . spot_edges ;
            mesh_create_msg . triangle_fan_indices = _logic_touch_consts . spot_edges ;
            mesh_create_msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_0 ;
            _mediator . get ( ) . send ( mesh_create_msg ) ;
        }
        else
            _update_spot ( ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
        _spot_mesh_id = msg . mesh ;
        _create_spot_mesh ( ) ;
        _spot_mesh_created = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_touch_prepared ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _update_spot ( )
{
    _decrease_spot_lifetime ( ) ;
    _poll_touchscreen ( ) ;
    _poll_mouse ( ) ;
    _place_new_spot ( ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: _decrease_spot_lifetime ( )
{
    if ( platform_conditions :: whole_greater_than_zero ( _spot_frames_left ) )
        platform_math :: dec_whole ( _spot_frames_left ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: _poll_touchscreen ( )
{
    num_whole touch ;
    _platform_touch . get ( ) . occured ( touch ) ;
    if ( platform_conditions :: whole_is_true ( touch ) )
    {
        _platform_touch . get ( ) . x ( _spot_x ) ;
        _platform_touch . get ( ) . y ( _spot_y ) ;
        _should_place_new_spot = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _poll_mouse ( )
{
    num_whole mouse_button ;
    _platform_mouse . get ( ) . left_button_down ( mouse_button ) ;
    if ( platform_conditions :: whole_is_true ( mouse_button ) )
    {
        _platform_mouse . get ( ) . x ( _spot_x ) ;
        _platform_mouse . get ( ) . y ( _spot_y ) ;
        _should_place_new_spot = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _place_new_spot ( )
{
    if ( platform_conditions :: whole_is_true ( _should_place_new_spot ) )
    {
        platform_vector :: xyz ( _spot_position , _spot_x , _spot_y , _logic_touch_consts . spot_pos_z ) ;
        _spot_frames_left = _logic_touch_consts . spot_lifetime_in_frames ;
        _should_place_new_spot = _platform_math_consts . get ( ) . whole_false ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _render_spot_mesh ( )
{
    matrix_data matrix ;
    num_fract fract_spot_frames_left ;
    num_fract fract_spot_lifetime_in_frames ;
    num_fract scale ;
    platform_math :: make_fract_from_whole ( fract_spot_frames_left , _spot_frames_left ) ;
    platform_math :: make_fract_from_whole ( fract_spot_lifetime_in_frames , _logic_touch_consts . spot_lifetime_in_frames ) ;
    platform_math :: div_fracts ( scale , fract_spot_frames_left , fract_spot_lifetime_in_frames ) ;
    platform_matrix :: set_axis_x ( matrix , scale , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_y ( matrix , _platform_math_consts . get ( ) . fract_0 , scale , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_z ( matrix , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , scale ) ;
    platform_matrix :: set_origin ( matrix , _spot_position ) ;
    _mediator . get ( ) . send ( typename messages :: engine_render_texture_unselect ( ) ) ;
    {
        typename messages :: engine_render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _spot_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    }
    {
        typename messages :: engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = _spot_mesh_id ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _create_spot_mesh ( )
{
    num_fract fract_spot_edges ;
    platform_math :: make_fract_from_whole ( fract_spot_edges , _logic_touch_consts . spot_edges ) ;
            
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , _logic_touch_consts . spot_edges ) 
        ; platform_math :: inc_whole ( i )
        )
    {
        num_fract angle ;
        num_fract fract_i ;
        num_fract angle_cos ;
        num_fract angle_sin ;
        num_fract vertex_x ;
        num_fract vertex_y ;
        num_fract vertex_z ;
        num_fract vertex_r ;
        num_fract vertex_g ;
        num_fract vertex_b ;
        num_fract vertex_a ;
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( angle , _platform_math_consts . get ( ) . fract_2pi , fract_i ) ;
        platform_math :: div_fract_by ( angle , fract_spot_edges ) ;
        platform_math :: cos ( angle_cos , angle ) ;
        platform_math :: sin ( angle_sin , angle ) ;
        platform_math :: mul_fracts ( vertex_x , _logic_touch_consts . spot_size , angle_cos ) ;
        platform_math :: mul_fracts ( vertex_y , _logic_touch_consts . spot_size , angle_sin ) ;
        vertex_z = _platform_math_consts . get ( ) . fract_0 ;
        vertex_r = _logic_touch_consts . spot_r ;
        vertex_g = _logic_touch_consts . spot_g ;
        vertex_b = _logic_touch_consts . spot_b ;
        vertex_a = _platform_math_consts . get ( ) . fract_1 ;

        typename messages :: engine_render_mesh_set_vertex_position set_pos_msg ;
        set_pos_msg . mesh = _spot_mesh_id ;
        set_pos_msg . offset = i ;
        set_pos_msg . x = vertex_x ;
        set_pos_msg . y = vertex_y ;
        set_pos_msg . z = vertex_z ;
        _mediator . get ( ) . send ( set_pos_msg ) ;

        typename messages :: engine_render_mesh_set_vertex_color set_col_msg ;
        set_col_msg . mesh = _spot_mesh_id ;
        set_col_msg . offset = i ;
        set_col_msg . r = vertex_r ;
        set_col_msg . g = vertex_g ;
        set_col_msg . b = vertex_b ;
        set_col_msg . a = vertex_a ;
        _mediator . get ( ) . send ( set_col_msg ) ;
        
        typename messages :: engine_render_mesh_set_triangle_fan_index_value set_index_msg ;
        set_index_msg . mesh = _spot_mesh_id ;
        set_index_msg . offset = i ;
        set_index_msg . index = i ;
        _mediator . get ( ) . send ( set_index_msg ) ;
    }
    
    typename messages :: engine_render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _spot_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}
