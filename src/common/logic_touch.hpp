template < typename mediator >
class shy_logic_touch
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 _spot_lifetime_in_frames = 60 ;
    static const int_32 _spot_r = 255 ;
    static const int_32 _spot_g = 255 ;
    static const int_32 _spot_b = 255 ;
    static const int_32 _spot_edges = 32 ;    
    static const float_32 _spot_size ( ) { return 0.3f ; }

public :
    shy_logic_touch ( mediator * arg_mediator ) ;
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
    int_32 _spot_frames_left ;
    int_32 _spot_mesh_created ;
    int_32 _spot_prepare_permitted ;
	int_32 _should_place_new_spot ;
	num_fract _spot_x ;
	num_fract _spot_y ;
    mesh_id _spot_mesh_id ;
    vector_data _spot_position ;
} ;

template < typename mediator >
shy_logic_touch < mediator > :: shy_logic_touch ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _spot_frames_left ( 0 )
, _spot_mesh_created ( false )
, _spot_prepare_permitted ( false )
, _should_place_new_spot ( false )
{
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_prepare_permit ( )
{
    _spot_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_render ( )
{
    if ( _spot_mesh_created && _spot_frames_left > 0 )
        _render_spot_mesh ( ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: touch_update ( )
{
    if ( _spot_prepare_permitted )
    {
        if ( ! _spot_mesh_created )
        {
            _create_spot_mesh ( ) ;
            _spot_mesh_created = true ;
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
    if ( _spot_frames_left > 0 )
        _spot_frames_left -- ;
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
        _should_place_new_spot = true ;
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
        _should_place_new_spot = true ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _place_new_spot ( )
{
    if ( _should_place_new_spot )
    {
        num_fract pos_z ;
        platform :: math_make_num_fract ( pos_z , - 3 , 1 ) ;
        platform :: vector_xyz ( _spot_position , _spot_x , _spot_y , pos_z ) ;
        _spot_frames_left = _spot_lifetime_in_frames ;
        _should_place_new_spot = false ;
    }
}

template < typename mediator >
void shy_logic_touch < mediator > :: _render_spot_mesh ( )
{
    _mediator -> texture_unselect ( ) ;
    matrix_data matrix ;
    float_32 scale = float_32 ( _spot_frames_left ) / float_32 ( _spot_lifetime_in_frames ) ;
    num_fract num_scale ;
    num_fract num_zero ;
    platform :: math_make_num_fract ( num_scale , int_32 ( scale * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( num_zero , 0 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , num_scale , num_zero , num_zero ) ;
    platform :: matrix_set_axis_y ( matrix , num_zero , num_scale , num_zero ) ;
    platform :: matrix_set_axis_z ( matrix , num_zero , num_zero , num_scale ) ;
    platform :: matrix_set_origin ( matrix , _spot_position ) ;
    _mediator -> mesh_set_transform ( _spot_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _spot_mesh_id ) ;
}

template < typename mediator >
void shy_logic_touch < mediator > :: _create_spot_mesh ( )
{
    vertex_data vertices [ _spot_edges ] ;
    index_data indices [ _spot_edges ] ;
    
    for ( int_32 i = 0 ; i < _spot_edges ; i ++ )
    {
        float_32 pi ;
        _mediator -> math_pi ( pi ) ;
        float_32 angle = pi * 2.0f * float_32 ( i ) / float_32 ( _spot_edges ) ;
        float_32 angle_cos ;
        float_32 angle_sin ;
        num_fract num_angle ;
        num_fract vertex_x ;
        num_fract vertex_y ;
        num_fract vertex_z ;
        num_whole vertex_r ;
        num_whole vertex_g ;
        num_whole vertex_b ;
        num_whole vertex_a ;
        num_whole index ;
        platform :: math_make_num_fract ( num_angle , int_32 ( angle * 1000.0f ) , 1000 ) ;
        platform :: math_cos ( angle_cos , num_angle ) ;
        platform :: math_sin ( angle_sin , num_angle ) ;
        platform :: math_make_num_fract ( vertex_x , int_32 ( _spot_size ( ) * angle_cos * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_fract ( vertex_y , int_32 ( _spot_size ( ) * angle_sin * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform :: math_make_num_whole ( vertex_r , _spot_r ) ;
        platform :: math_make_num_whole ( vertex_g , _spot_g ) ;
        platform :: math_make_num_whole ( vertex_b , _spot_b ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: math_make_num_whole ( index , i ) ;
        platform :: render_set_vertex_position ( vertices [ i ] , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( vertices [ i ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( indices [ i ] , index ) ;
    }
    _mediator -> mesh_create ( _spot_mesh_id , vertices , 0 , indices , _spot_edges , 0 , _spot_edges ) ;
}
