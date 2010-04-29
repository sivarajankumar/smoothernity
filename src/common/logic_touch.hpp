template < typename mediator >
class shy_logic_touch
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 _spot_lifetime_in_frames = 60 ;
    
public :
    shy_logic_touch ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _spot_frames_left ( 0 )
    , _spot_mesh_created ( false )
	, _should_place_new_spot ( false )
	, _spot_x ( 0 )
	, _spot_y ( 0 )
    {
    }
    void render_touch ( )
    {
        if ( _spot_mesh_created && _spot_frames_left > 0 )
            _render_spot_mesh ( ) ;
    }
    void update ( )
    {
        if ( ! _spot_mesh_created )
        {
            _create_spot_mesh ( ) ;
            _spot_mesh_created = true ;
        }
        else
            _update_spot ( ) ;
    }
private :
    void _update_spot ( )
    {
		_decrease_spot_lifetime ( ) ;
		_poll_touchscreen ( ) ;
		_poll_mouse ( ) ;
		_place_new_spot ( ) ;
    }
	void _decrease_spot_lifetime ( )
	{
        if ( _spot_frames_left > 0 )
            _spot_frames_left -- ;
	}
	void _poll_touchscreen ( )
	{
        if ( platform :: touch_occured ( ) )
        {
			_should_place_new_spot = true ;
			_spot_x = platform :: touch_x ( ) ;
			_spot_y = platform :: touch_y ( ) ;
        }
	}
	void _poll_mouse ( )
	{
		if ( platform :: mouse_left_button_down ( ) )
		{
			_should_place_new_spot = true ;
			_spot_x = platform :: mouse_x ( ) ;
			_spot_y = platform :: mouse_y ( ) ;
		}
	}
	void _place_new_spot ( )
	{
		if ( _should_place_new_spot )
		{
			_should_place_new_spot = false ;
            _spot_position = platform :: vector_xyz ( _spot_x , _spot_y , - 3.0f ) ;
            _spot_frames_left = _spot_lifetime_in_frames ;
		}
	}
    void _render_spot_mesh ( )
    {
        platform :: render_disable_texturing ( ) ;
        matrix_data matrix ;
        float_32 scale = float_32 ( _spot_frames_left ) / float_32 ( _spot_lifetime_in_frames ) ;
        platform :: matrix_set_axis_x ( matrix , scale , 0 , 0 ) ;
        platform :: matrix_set_axis_y ( matrix , 0 , scale , 0 ) ;
        platform :: matrix_set_axis_z ( matrix , 0 , 0 , scale ) ;
        platform :: matrix_set_origin ( matrix , _spot_position ) ;
        _mediator -> mesh_set_transform ( _spot_mesh_id , matrix ) ;
        _mediator -> mesh_render ( _spot_mesh_id ) ;
    }
    void _create_spot_mesh ( )
    {
        static const int_32 SPOT_R = 255 ;
        static const int_32 SPOT_G = 255 ;
        static const int_32 SPOT_B = 255 ;
        
        static const float_32 spot_size = 0.3f ;
        static const int_32 spot_edges = 32 ;
        
        vertex_data vertices [ spot_edges ] ;
        index_data indices [ spot_edges ] ;
        
        for ( int_32 i = 0 ; i < spot_edges ; i ++ )
        {
            float_32 angle = _mediator -> math_pi ( ) * 2.0f * float_32 ( i ) / float_32 ( spot_edges ) ;
            platform :: render_set_vertex_position
                ( vertices [ i ]
                , spot_size * platform :: math_cos ( angle )
                , spot_size * platform :: math_sin ( angle )
                , 0.0f
                ) ;
            platform :: render_set_vertex_color
                ( vertices [ i ]
                , SPOT_R
                , SPOT_G
                , SPOT_B
                , 255
                ) ;
            platform :: render_set_index_value
                ( indices [ i ]
                , i
                ) ;
        }
        _spot_mesh_id = _mediator -> mesh_create ( vertices , 0 , indices , spot_edges , 0 , spot_edges ) ;
    }
private :
    mediator * _mediator ;
    int_32 _spot_frames_left ;
    int_32 _spot_mesh_created ;
	int_32 _should_place_new_spot ;
	float_32 _spot_x ;
	float_32 _spot_y ;
    mesh_id _spot_mesh_id ;
    vector_data _spot_position ;
} ;
