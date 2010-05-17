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
public :
    shy_logic_fidget ( mediator * arg_mediator ) ;
    void fidget_prepare_permit ( ) ;
    void render_fidget ( ) ;
    void update ( ) ;
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
void shy_logic_fidget < mediator > :: render_fidget ( )
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
void shy_logic_fidget < mediator > :: update ( )
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
    static const int_32 SCALE_IN_FRAMES = 60 ;
    
    _mediator -> texture_unselect ( ) ;
    float_32 scale = float_32 ( _fidget_scale ) / float_32 ( SCALE_IN_FRAMES ) ;
    if ( _fidget_scale < SCALE_IN_FRAMES )
        _fidget_scale ++ ;
    matrix_data matrix ;
    platform :: matrix_set_axis_x
        ( matrix
        , platform :: math_cos ( _fidget_angle ) * scale
        , platform :: math_sin ( _fidget_angle ) * scale
        , 0.0f
        ) ;
    platform :: matrix_set_axis_y
        ( matrix
        , - platform :: math_sin ( _fidget_angle ) * scale
        , platform :: math_cos ( _fidget_angle ) * scale
        , 0.0f
        ) ;
    platform :: matrix_set_axis_z
        ( matrix
        , 0.0f
        , 0.0f
        , 1.0f
        ) ;
    platform :: matrix_set_origin
        ( matrix
        , 0.0f
        , platform :: render_get_aspect_height ( ) - 0.5f
        , - 3.0f
        ) ;
    _mediator -> mesh_set_transform ( _fidget_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _fidget_mesh_id ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{
    static const int_32 FIDGET_R = 255 ;
    static const int_32 FIDGET_G = 128 ;
    static const int_32 FIDGET_B = 0 ;
    
    static const float_32 fidget_size = 0.3f ;
    static const int_32 fidget_edges = 3 ;
    
    vertex_data vertices [ fidget_edges ] ;
    index_data indices [ fidget_edges ] ;
    
    for ( int_32 i = 0 ; i < fidget_edges ; i ++ )
    {
        float_32 angle = _mediator -> math_pi ( ) * 2.0f * float_32 ( i ) / float_32 ( fidget_edges ) ;
        platform :: render_set_vertex_position
            ( vertices [ i ]
            , fidget_size * platform :: math_cos ( angle )
            , fidget_size * platform :: math_sin ( angle )
            , 0.0f
            ) ;
        platform :: render_set_vertex_color
            ( vertices [ i ]
            , FIDGET_R
            , FIDGET_G
            , FIDGET_B
            , 255
            ) ;
        platform :: render_set_index_value
            ( indices [ i ]
            , i
            ) ;
    }
    _fidget_mesh_id = _mediator -> mesh_create ( vertices , 0 , indices , fidget_edges , 0 , fidget_edges ) ;
}
