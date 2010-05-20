template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
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
    matrix_data matrix ;
    num_fract height ;
    num_fract num_scale ;
    num_fract angle_cos ;
    num_fract angle_sin ;
    num_fract cos_by_scale ;
    num_fract sin_by_scale ;
    num_fract neg_sin_by_scale ;
    num_fract zero ;
    num_fract z_dist ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract angle ;
    num_fract num_half ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_make_num_fract ( num_half , 1 , 2 ) ;
    platform :: math_make_num_fract ( num_scale , int_32 ( scale * 1000.0f ) , 1000 ) ;
    platform :: math_make_num_fract ( angle , int_32 ( _fidget_angle * 1000.0f ) , 1000 ) ;
    platform :: math_cos ( angle_cos , angle ) ;
    platform :: math_sin ( angle_sin , angle ) ;
    platform :: math_make_num_fract ( zero , 0 , 1 ) ;
    platform :: math_make_num_fract ( z_dist , 1 , 1 ) ;
    platform :: math_mul_fracts ( cos_by_scale , angle_cos , num_scale ) ;
    platform :: math_mul_fracts ( sin_by_scale , angle_sin , num_scale ) ;
    platform :: math_neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
    platform :: math_make_num_fract ( origin_x , 0 , 1 ) ;
    platform :: math_sub_fracts ( origin_y , height , num_half ) ;
    platform :: math_make_num_fract ( origin_z , - 3 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , cos_by_scale , sin_by_scale , zero ) ;
    platform :: matrix_set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , zero ) ;
    platform :: matrix_set_axis_z ( matrix , zero , zero , z_dist ) ;
    platform :: matrix_set_origin ( matrix , origin_x , origin_y , origin_z ) ;
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
        num_fract angle_cos ;
        num_fract angle_sin ;
        num_fract num_angle ;
        num_fract num_size ;
        num_fract vertex_x ;
        num_fract vertex_y ;
        num_fract vertex_z ;
        num_whole vertex_r ;
        num_whole vertex_g ;
        num_whole vertex_b ;
        num_whole vertex_a ;
        num_whole index ;
        platform :: math_make_num_fract ( num_angle , int_32 ( angle * 1000.0f ) , 1000 ) ;
        platform :: math_make_num_fract ( num_size , int_32 ( _fidget_size ( ) * 1000.0f ) , 1000 ) ;
        platform :: math_cos ( angle_cos , num_angle ) ;
        platform :: math_sin ( angle_sin , num_angle ) ;
        platform :: math_mul_fracts ( vertex_x , num_size , angle_cos ) ;
        platform :: math_mul_fracts ( vertex_y , num_size , angle_sin ) ;
        platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform :: math_make_num_whole ( vertex_r , _fidget_r ) ;
        platform :: math_make_num_whole ( vertex_g , _fidget_g ) ;
        platform :: math_make_num_whole ( vertex_b , _fidget_b ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        platform :: math_make_num_whole ( index , i ) ;
        platform :: render_set_vertex_position ( vertices [ i ] , vertex_x , vertex_y , vertex_z ) ;
        platform :: render_set_vertex_color ( vertices [ i ] , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        platform :: render_set_index_value ( indices [ i ] , index ) ;
    }
    _mediator -> mesh_create ( _fidget_mesh_id , vertices , 0 , indices , _fidget_edges , 0 , _fidget_edges ) ;
}
