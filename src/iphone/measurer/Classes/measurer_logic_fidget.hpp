template < typename mediator >
class shy_measurer_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
public :
    shy_measurer_logic_fidget ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _fidget_angle ( 0 )
    , _fidget_mesh_created ( false )
    {
    }
    void render_fidget ( )
    {
        if ( _fidget_mesh_created )
            _render_fidget_mesh ( ) ;
    }
    void update ( )
    {
        if ( ! _fidget_mesh_created )
        {
            _create_fidget_mesh ( ) ;
            _fidget_mesh_created = true ;
        }
        else
            _update_fidget ( ) ;
    }
private :
    void _update_fidget ( )
    {
        _fidget_angle += 0.125f ;
    }
    void _render_fidget_mesh ( )
    {
        platform :: render_disable_depth_test ( ) ;
        platform :: render_matrix_identity ( ) ;
        matrix_data matrix ;
        platform :: matrix_set_axis_x
            ( matrix
            , platform :: math_cos ( _fidget_angle )
            , platform :: math_sin ( _fidget_angle )
            , 0.0f
            ) ;
        platform :: matrix_set_axis_y
            ( matrix
            , - platform :: math_sin ( _fidget_angle )
            , platform :: math_cos ( _fidget_angle )
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
            , 3.0f
            , - 3.0f
            ) ;
        _mediator -> mesh_set_transform ( _fidget_mesh_id , matrix ) ;
        _mediator -> mesh_render ( _fidget_mesh_id ) ;
        platform :: render_enable_depth_test ( ) ;
    }
    void _create_fidget_mesh ( )
    {
        static const int_32 FIDGET_R = 255 ;
        static const int_32 FIDGET_G = 128 ;
        static const int_32 FIDGET_B = 0 ;
        
        vertex_data vertices [ 3 ] ;
        index_data indices [ 3 ] ;
        
        for ( int_32 i = 0 ; i < 3 ; i ++ )
        {
            float_32 angle = PI * 2.0f * float_32 ( i ) / 3.0f ;
            platform :: render_set_vertex_position
                ( vertices [ i ]
                , platform :: math_cos ( angle )
                , platform :: math_sin ( angle )
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
        _fidget_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , 3 , 3 , 0 ) ;
    }
private :
    int_32 _fidget_mesh_created ;
    mesh_id _fidget_mesh_id ;
    float_32 _fidget_angle ;
    mediator * _mediator ;
} ;
