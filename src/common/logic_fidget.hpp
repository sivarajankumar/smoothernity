template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;

    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _fidget_r = 255 ;
    static const_int_32 _fidget_g = 128 ;
    static const_int_32 _fidget_b = 0 ;    
    static const_int_32 _fidget_edges = 3 ;
    static const num_fract _fidget_size ( ) { num_fract n ; platform :: math_make_num_fract ( n , 3 , 10 ) ; return n ; }
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
    num_fract _fidget_angle ;
    num_whole _fidget_prepare_permitted ;
    num_whole _fidget_mesh_created ;
    num_whole _fidget_scale ;
    mesh_id _fidget_mesh_id ;
} ;

template < typename mediator >
shy_logic_fidget < mediator > :: shy_logic_fidget ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_fract ( _fidget_angle , 0 , 1 ) ;
    platform :: math_make_num_whole ( _fidget_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _fidget_mesh_created , false ) ;
    platform :: math_make_num_whole ( _fidget_scale , 0 ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_render ( )
{
    if ( platform :: condition_true ( _fidget_mesh_created ) )
        _render_fidget_mesh ( ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_prepare_permit ( )
{
    platform :: math_make_num_whole ( _fidget_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: fidget_update ( )
{
    if ( platform :: condition_true ( _fidget_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _fidget_mesh_created ) )
        {
            _create_fidget_mesh ( ) ;
            platform :: math_make_num_whole ( _fidget_mesh_created , true ) ;
            _mediator -> fidget_prepared ( ) ;
        }
        else
            _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _update_fidget ( )
{
    num_fract angle_delta ;
    platform :: math_make_num_fract ( angle_delta , 125 , 1000 ) ;
    platform :: math_add_to_fract ( _fidget_angle , angle_delta ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _render_fidget_mesh ( )
{    
    matrix_data matrix ;
    num_whole whole_scale_in_frames ;
    num_fract fract_scale_in_frames ;
    num_fract fract_fidget_scale ;
    num_fract scale ;
    num_fract height ;
    num_fract angle_cos ;
    num_fract angle_sin ;
    num_fract cos_by_scale ;
    num_fract sin_by_scale ;
    num_fract neg_sin_by_scale ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract num_half ;
    
    platform :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform :: math_make_fract_from_whole ( fract_fidget_scale , _fidget_scale ) ;
    platform :: math_div_fracts ( scale , fract_fidget_scale , fract_scale_in_frames ) ;
    platform :: render_get_aspect_height ( height ) ;
    platform :: math_make_num_fract ( num_half , 1 , 2 ) ;
    platform :: math_cos ( angle_cos , _fidget_angle ) ;
    platform :: math_sin ( angle_sin , _fidget_angle ) ;
    platform :: math_mul_fracts ( cos_by_scale , angle_cos , scale ) ;
    platform :: math_mul_fracts ( sin_by_scale , angle_sin , scale ) ;
    platform :: math_neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
    platform :: math_make_num_fract ( origin_x , 0 , 1 ) ;
    platform :: math_sub_fracts ( origin_y , height , num_half ) ;
    platform :: math_make_num_fract ( origin_z , - 3 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , cos_by_scale , sin_by_scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , platform :: fract_1 ) ;
    platform :: matrix_set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    _mediator -> texture_unselect ( ) ;
    _mediator -> mesh_set_transform ( _fidget_mesh_id , matrix ) ;
    _mediator -> mesh_render ( _fidget_mesh_id ) ;
    if ( platform :: condition_whole_less_than_whole ( _fidget_scale , whole_scale_in_frames ) )
        platform :: math_inc_whole ( _fidget_scale ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{    
    typename platform :: template static_array < vertex_data , _fidget_edges > vertices ;
    index_data indices [ _fidget_edges ] ;
    num_whole i ;
    num_whole whole_fidget_edges ;
    num_fract fract_fidget_edges ;
    
    platform :: math_make_num_fract ( fract_fidget_edges , _fidget_edges , 1 ) ;
    platform :: math_make_num_whole ( whole_fidget_edges , _fidget_edges ) ;
    
    for ( platform :: math_make_num_whole ( i , 0 )
        ; platform :: condition_whole_less_than_whole ( i , whole_fidget_edges )
        ; platform :: math_inc_whole ( i )
        )
    {
        num_fract fract_i ;
        num_fract angle ;
        num_fract angle_cos ;
        num_fract angle_sin ;
        num_fract vertex_x ;
        num_fract vertex_y ;
        num_fract vertex_z ;
        num_whole vertex_r ;
        num_whole vertex_g ;
        num_whole vertex_b ;
        num_whole vertex_a ;
        num_whole index ;
        index_data * index_ptr = 0 ;
        platform :: math_make_fract_from_whole ( fract_i , i ) ;
        platform :: math_mul_fracts ( angle , platform :: fract_2pi , fract_i ) ;
        platform :: math_div_fract_by ( angle , fract_fidget_edges ) ;
        platform :: math_cos ( angle_cos , angle ) ;
        platform :: math_sin ( angle_sin , angle ) ;
        platform :: math_mul_fracts ( vertex_x , _fidget_size ( ) , angle_cos ) ;
        platform :: math_mul_fracts ( vertex_y , _fidget_size ( ) , angle_sin ) ;
        platform :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform :: math_make_num_whole ( vertex_r , _fidget_r ) ;
        platform :: math_make_num_whole ( vertex_g , _fidget_g ) ;
        platform :: math_make_num_whole ( vertex_b , _fidget_b ) ;
        platform :: math_make_num_whole ( vertex_a , 255 ) ;
        {
            vertex_data & vertex = platform :: array_element ( vertices , i ) ;
            platform :: render_set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform :: render_set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        platform :: memory_pointer_offset ( index_ptr , indices , i ) ;
        platform :: render_set_index_value ( * index_ptr , i ) ;
    }
    _mediator -> mesh_create
        ( _fidget_mesh_id 
        , vertices 
        , 0 
        , indices 
        , whole_fidget_edges 
        , platform :: whole_0 
        , whole_fidget_edges 
        ) ;
}
