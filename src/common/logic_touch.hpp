template < typename mediator >
class shy_logic_touch
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const_int_32 _spot_lifetime_in_frames = 60 ;
    static const_int_32 _spot_r = 255 ;
    static const_int_32 _spot_g = 255 ;
    static const_int_32 _spot_b = 255 ;
    static const_int_32 _spot_edges = 32 ;    
    static const num_fract _spot_size ( ) { num_fract n ; platform :: math_make_num_fract ( n , 3 , 10 ) ; return n ; }

public :
    shy_logic_touch ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void touch_done ( ) ;
    void touch_prepare_permit ( ) ;
    void touch_render ( ) ;
    void touch_update ( ) ;
private :
    void _update_spot ( ) ;
	void _decrease_spot_lifetime ( ) ;
	void _poll_touchscreen ( ) ;
	void _poll_mouse ( ) ;
	void _place_new_spot ( ) ;
    void _render_spot_mesh ( ) ;
    void _create_spot_mesh ( ) ;
private :
    mediator * _mediator ;
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
: _mediator ( 0 )
{
    platform :: math_make_num_whole ( _spot_frames_left , 0 ) ;
    platform :: math_make_num_whole ( _spot_mesh_created , false ) ;
    platform :: math_make_num_whole ( _spot_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _should_place_new_spot , false ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_done ( )
{
    if ( platform :: condition_true ( _spot_mesh_created ) )
        _mediator -> mesh_delete ( _spot_mesh_id ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_prepare_permit ( )
{
    platform :: math_make_num_whole ( _spot_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_render ( )
{
    if ( platform :: condition_true ( _spot_mesh_created ) && platform :: condition_whole_greater_than_zero ( _spot_frames_left ) )
        _render_spot_mesh ( ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_update ( )
{
    if ( platform :: condition_true ( _spot_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _spot_mesh_created ) )
        {
            _create_spot_mesh ( ) ;
            platform :: math_make_num_whole ( _spot_mesh_created , true ) ;
            _mediator -> touch_prepared ( ) ;
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
        platform :: math_dec_whole ( _spot_frames_left ) ;
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
        platform :: math_make_num_whole ( _should_place_new_spot , true ) ;
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
        platform :: math_make_num_whole ( _should_place_new_spot , true ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _place_new_spot ( )
{
    if ( platform :: condition_true ( _should_place_new_spot ) )
    {
        num_fract pos_z ;
        platform :: math_make_num_fract ( pos_z , - 3 , 1 ) ;
        platform :: vector_xyz ( _spot_position , _spot_x , _spot_y , pos_z ) ;
        platform :: math_make_num_whole ( _spot_frames_left , _spot_lifetime_in_frames ) ;
        platform :: math_make_num_whole ( _should_place_new_spot , false ) ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _render_spot_mesh ( )
{
    matrix_data matrix ;
    num_fract fract_spot_frames_left ;
    num_fract fract_spot_lifetime_in_frames ;
    num_fract scale ;
    platform :: math_make_fract_from_whole ( fract_spot_frames_left , _spot_frames_left ) ;
    platform :: math_make_num_fract ( fract_spot_lifetime_in_frames , _spot_lifetime_in_frames , 1 ) ;
    platform :: math_div_fracts ( scale , fract_spot_frames_left , fract_spot_lifetime_in_frames ) ;
    platform :: matrix_set_axis_x ( matrix , scale , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , platform :: fract_0 , scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , scale ) ;
    platform :: matrix_set_origin ( matrix , _spot_position ) ;
    _mediator -> texture_unselect ( ) ;
    _mediator -> mesh_set_transform ( _spot_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _spot_mesh_id ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: _create_spot_mesh ( )
{
    typename platform :: template static_array < vertex_data , _spot_edges > vertices ;
    typename platform :: template static_array < index_data , _spot_edges > indices ;
    num_whole i ;
    num_whole whole_spot_edges ;
    num_fract fract_spot_edges ;
    
    platform :: math_make_num_whole ( whole_spot_edges , _spot_edges ) ;
    platform :: math_make_num_fract ( fract_spot_edges , _spot_edges , 1 ) ;
    
    for ( platform :: math_make_num_whole ( i , 0 )
        ; platform :: condition_whole_less_than_whole ( i , whole_spot_edges ) 
        ; platform :: math_inc_whole ( i )
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
        platform :: math_make_fract_from_whole ( fract_i , i ) ;
        platform :: math_mul_fracts ( angle , platform :: fract_2pi , fract_i ) ;
        platform :: math_div_fract_by ( angle , fract_spot_edges ) ;
        platform :: math_cos ( angle_cos , angle ) ;
        platform :: math_sin ( angle_sin , angle ) ;
        platform :: math_mul_fracts ( vertex_x , _spot_size ( ) , angle_cos ) ;
        platform :: math_mul_fracts ( vertex_y , _spot_size ( ) , angle_sin ) ;
        platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform :: math_make_num_fract ( vertex_r , _spot_r , 255 ) ;
        platform :: math_make_num_fract ( vertex_g , _spot_g , 255 ) ;
        platform :: math_make_num_fract ( vertex_b , _spot_b , 255 ) ;
        platform :: math_make_num_fract ( vertex_a , 1 , 1 ) ;
        {
            vertex_data & vertex = platform :: array_element ( vertices , i ) ;
            platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        {
            index_data & index = platform :: array_element ( indices , i ) ;
            platform :: render_set_index_value ( index , i ) ;
        }
    }
    _mediator -> mesh_create
        ( _spot_mesh_id 
        , vertices 
        , indices
        , indices 
        , whole_spot_edges 
        , platform :: whole_0 
        , whole_spot_edges 
        ) ;
}
