template < typename mediator >
class shy_logic_touch
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const_int_32 _spot_lifetime_in_frames = 60 ;
    static const_int_32 _spot_r = 255 ;
    static const_int_32 _spot_g = 255 ;
    static const_int_32 _spot_b = 255 ;
    static const_int_32 _spot_edges = 32 ;    
    static const num_fract _spot_size ( ) { num_fract n ; platform_math :: math_make_num_fract ( n , 3 , 10 ) ; return n ; }

public :
    shy_logic_touch ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: touch_done msg ) ;
    void receive ( typename messages :: touch_prepare_permit msg ) ;
    void receive ( typename messages :: touch_render msg ) ;
    void receive ( typename messages :: touch_update msg ) ;
private :
    void _update_spot ( ) ;
	void _decrease_spot_lifetime ( ) ;
	void _poll_touchscreen ( ) ;
	void _poll_mouse ( ) ;
	void _place_new_spot ( ) ;
    void _render_spot_mesh ( ) ;
    void _create_spot_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_whole _spot_frames_left ;
    num_whole _spot_mesh_created ;
    num_whole _spot_prepare_permitted ;
	num_whole _should_place_new_spot ;
	num_fract _spot_x ;
	num_fract _spot_y ;
    mesh_id _spot_mesh_id ;
    vector_data _spot_position ;
} ;

template < typename mediator >
shy_logic_touch < mediator > :: shy_logic_touch ( )
{
    platform_math :: math_make_num_whole ( _spot_frames_left , 0 ) ;
    platform_math :: math_make_num_whole ( _spot_mesh_created , false ) ;
    platform_math :: math_make_num_whole ( _spot_prepare_permitted , false ) ;
    platform_math :: math_make_num_whole ( _should_place_new_spot , false ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: touch_done msg )
{
    if ( platform :: condition_true ( _spot_mesh_created ) )
    {
        typename messages :: mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _spot_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: touch_prepare_permit msg )
{
    platform_math :: math_make_num_whole ( _spot_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: touch_render msg )
{
    if ( platform :: condition_true ( _spot_mesh_created ) && platform :: condition_whole_greater_than_zero ( _spot_frames_left ) )
        _render_spot_mesh ( ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: receive ( typename messages :: touch_update msg )
{
    if ( platform :: condition_true ( _spot_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _spot_mesh_created ) )
        {
            _create_spot_mesh ( ) ;
            platform_math :: math_make_num_whole ( _spot_mesh_created , true ) ;
            _mediator . get ( ) . send ( typename messages :: touch_prepared ( ) ) ;
        }
        else
            _update_spot ( ) ;
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
    if ( platform :: condition_whole_greater_than_zero ( _spot_frames_left ) )
        platform_math :: math_dec_whole ( _spot_frames_left ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: _poll_touchscreen ( )
{
    num_whole touch ;
    platform :: touch_occured ( touch ) ;
    if ( platform :: condition_true ( touch ) )
    {
        platform :: touch_x ( _spot_x ) ;
        platform :: touch_y ( _spot_y ) ;
        platform_math :: math_make_num_whole ( _should_place_new_spot , true ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _poll_mouse ( )
{
    num_whole mouse_button ;
    platform :: mouse_left_button_down ( mouse_button ) ;
    if ( platform :: condition_true ( mouse_button ) )
    {
        platform :: mouse_x ( _spot_x ) ;
        platform :: mouse_y ( _spot_y ) ;
        platform_math :: math_make_num_whole ( _should_place_new_spot , true ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _place_new_spot ( )
{
    if ( platform :: condition_true ( _should_place_new_spot ) )
    {
        num_fract pos_z ;
        platform_math :: math_make_num_fract ( pos_z , - 3 , 1 ) ;
        platform :: vector_xyz ( _spot_position , _spot_x , _spot_y , pos_z ) ;
        platform_math :: math_make_num_whole ( _spot_frames_left , _spot_lifetime_in_frames ) ;
        platform_math :: math_make_num_whole ( _should_place_new_spot , false ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _render_spot_mesh ( )
{
    matrix_data matrix ;
    num_fract fract_spot_frames_left ;
    num_fract fract_spot_lifetime_in_frames ;
    num_fract scale ;
    platform_math :: math_make_fract_from_whole ( fract_spot_frames_left , _spot_frames_left ) ;
    platform_math :: math_make_num_fract ( fract_spot_lifetime_in_frames , _spot_lifetime_in_frames , 1 ) ;
    platform_math :: math_div_fracts ( scale , fract_spot_frames_left , fract_spot_lifetime_in_frames ) ;
    platform :: matrix_set_axis_x ( matrix , scale , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , platform :: math_consts . fract_0 , scale , platform :: math_consts . fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , scale ) ;
    platform :: matrix_set_origin ( matrix , _spot_position ) ;
    _mediator . get ( ) . send ( typename messages :: texture_unselect ( ) ) ;
    {
        typename messages :: mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _spot_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    }
    {
        typename messages :: mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = _spot_mesh_id ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _create_spot_mesh ( )
{
    typename platform_static_array :: template static_array < vertex_data , _spot_edges > vertices ;
    typename platform_static_array :: template static_array < index_data , _spot_edges > indices ;
    num_whole i ;
    num_whole whole_spot_edges ;
    num_fract fract_spot_edges ;
    
    platform_math :: math_make_num_whole ( whole_spot_edges , _spot_edges ) ;
    platform_math :: math_make_num_fract ( fract_spot_edges , _spot_edges , 1 ) ;
    
    for ( platform_math :: math_make_num_whole ( i , 0 )
        ; platform :: condition_whole_less_than_whole ( i , whole_spot_edges ) 
        ; platform_math :: math_inc_whole ( i )
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
        platform_math :: math_make_fract_from_whole ( fract_i , i ) ;
        platform_math :: math_mul_fracts ( angle , platform :: math_consts . fract_2pi , fract_i ) ;
        platform_math :: math_div_fract_by ( angle , fract_spot_edges ) ;
        platform_math :: math_cos ( angle_cos , angle ) ;
        platform_math :: math_sin ( angle_sin , angle ) ;
        platform_math :: math_mul_fracts ( vertex_x , _spot_size ( ) , angle_cos ) ;
        platform_math :: math_mul_fracts ( vertex_y , _spot_size ( ) , angle_sin ) ;
        platform_math :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform_math :: math_make_num_fract ( vertex_r , _spot_r , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_g , _spot_g , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_b , _spot_b , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_a , 1 , 1 ) ;
        {
            vertex_data & vertex = platform_static_array :: array_element ( vertices , i ) ;
            platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        {
            index_data & index = platform_static_array :: array_element ( indices , i ) ;
            platform :: render_set_index_value ( index , i ) ;
        }
    }
    _mediator . get ( ) . mesh_create
        ( _spot_mesh_id 
        , vertices 
        , indices
        , indices 
        , whole_spot_edges 
        , platform :: math_consts . whole_0 
        , whole_spot_edges 
        ) ;
}
