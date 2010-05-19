template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;

    static const int_32 _scale_in_frames = 60 ;
    static const int_32 _fidget_r = 255 ;
    static const int_32 _fidget_g = 128 ;
    static const int_32 _fidget_b = 0 ;    
    static const int_32 _fidget_edges = 3 ;
    static const float_32 _fidget_size ( ) { return 0.3f ; }
public :
    shy_logic_fidget ( mediator * arg_mediator ) ;
    void fidget_prepare_permit ( ) ;
    void fidget_render ( ) ;
    void fidget_update ( ) ;
private :
    void _update_fidget ( ) ;
    void _render_fidget_mesh ( ) ;
    void _create_fidget_mesh ( ) ;
private :
    mediator * _mediator ;
    float_32 _fidget_angle ;
    int_32 _fidget_prepare_permitted ;
    int_32 _fidget_mesh_created ;
    int_32 _fidget_scale ;
    mesh_id _fidget_mesh_id ;
} ;

template < typename mediator >
shy_logic_fidget < mediator > :: shy_logic_fidget ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _fidget_angle ( 0 )
, _fidget_prepare_permitted ( false )
, _fidget_mesh_created ( false )
, _fidget_scale ( 0 )
{
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_render ( )
{
    if ( _fidget_mesh_created )
        _render_fidget_mesh ( ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_prepare_permit ( )
{
    _fidget_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_update ( )
{
    if ( _fidget_prepare_permitted )
    {
        if ( ! _fidget_mesh_created )
        {
            _create_fidget_mesh ( ) ;
            _fidget_mesh_created = true ;
            _mediator -> fidget_prepared ( ) ;
        }
        else
            _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _update_fidget ( )
{
    _fidget_angle += 0.125f ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _render_fidget_mesh ( )
{    
    _mediator -> texture_unselect ( ) ;
    float_32 scale = float_32 ( _fidget_scale ) / float_32 ( _scale_in_frames ) ;
    if ( _fidget_scale < _scale_in_frames )
        _fidget_scale ++ ;
    float_32 height ;
    float_32 angle_cos ;
    float_32 angle_sin ;
    matrix_data matrix ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_cos ( angle_cos , _fidget_angle ) ;
    platform :: math_sin ( angle_sin , _fidget_angle ) ;
    platform :: matrix_set_axis_x ( matrix , angle_cos * scale , angle_sin * scale , 0.0f ) ;
    platform :: matrix_set_axis_y ( matrix , - angle_sin * scale , angle_cos * scale , 0.0f ) ;
    platform :: matrix_set_axis_z ( matrix , 0.0f , 0.0f , 1.0f ) ;
    platform :: matrix_set_origin ( matrix , 0.0f , height - 0.5f , - 3.0f ) ;
    _mediator -> mesh_set_transform ( _fidget_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _fidget_mesh_id ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{    
    vertex_data vertices [ _fidget_edges ] ;
    index_data indices [ _fidget_edges ] ;
    
    for ( int_32 i = 0 ; i < _fidget_edges ; i ++ )
    {
        float_32 pi ;
        _mediator -> math_pi ( pi ) ;
        float_32 angle = pi * 2.0f * float_32 ( i ) / float_32 ( _fidget_edges ) ;
        float_32 angle_cos ;
        float_32 angle_sin ;
        platform :: math_cos ( angle_cos , angle ) ;
        platform :: math_sin ( angle_sin , angle ) ;
        platform :: render_set_vertex_position
            ( vertices [ i ]
            , _fidget_size ( ) * angle_cos
            , _fidget_size ( ) * angle_sin
            , 0.0f
            ) ;
        platform :: render_set_vertex_color
            ( vertices [ i ]
            , _fidget_r
            , _fidget_g
            , _fidget_b
            , 255
            ) ;
        platform :: render_set_index_value
            ( indices [ i ]
            , i
            ) ;
    }
    _mediator -> mesh_create ( _fidget_mesh_id , vertices , 0 , indices , _fidget_edges , 0 , _fidget_edges ) ;
}
