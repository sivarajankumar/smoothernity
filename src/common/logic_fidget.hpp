template < typename mediator >
class shy_logic_fidget
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;

    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _fidget_r = 255 ;
    static const_int_32 _fidget_g = 128 ;
    static const_int_32 _fidget_b = 0 ;    
    static const_int_32 _fidget_edges = 3 ;
    static const num_fract _fidget_size ( ) { num_fract n ; platform_math :: math_make_num_fract ( n , 3 , 10 ) ; return n ; }
public :
    shy_logic_fidget ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: fidget_done msg ) ;
    void receive ( typename messages :: fidget_prepare_permit msg ) ;
    void receive ( typename messages :: fidget_render msg ) ;
    void receive ( typename messages :: fidget_update msg ) ;
private :
    void _update_fidget ( ) ;
    void _render_fidget_mesh ( ) ;
    void _create_fidget_mesh ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_fract _fidget_angle ;
    num_whole _fidget_prepare_permitted ;
    num_whole _fidget_mesh_created ;
    num_whole _fidget_scale ;
    mesh_id _fidget_mesh_id ;
} ;

template < typename mediator >
shy_logic_fidget < mediator > :: shy_logic_fidget ( )
{
    platform_math :: math_make_num_fract ( _fidget_angle , 0 , 1 ) ;
    platform_math :: math_make_num_whole ( _fidget_prepare_permitted , false ) ;
    platform_math :: math_make_num_whole ( _fidget_mesh_created , false ) ;
    platform_math :: math_make_num_whole ( _fidget_scale , 0 ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_done msg )
{
    if ( platform_conditions :: condition_true ( _fidget_mesh_created ) )
    {
        typename messages :: mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _fidget_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_render msg )
{
    if ( platform_conditions :: condition_true ( _fidget_mesh_created ) )
        _render_fidget_mesh ( ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_prepare_permit msg )
{
    platform_math :: math_make_num_whole ( _fidget_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: receive ( typename messages :: fidget_update msg )
{
    if ( platform_conditions :: condition_true ( _fidget_prepare_permitted ) )
    {
        if ( platform_conditions :: condition_false ( _fidget_mesh_created ) )
        {
            _create_fidget_mesh ( ) ;
            platform_math :: math_make_num_whole ( _fidget_mesh_created , true ) ;
            _mediator . get ( ) . send ( typename messages :: fidget_prepared ( ) ) ;
        }
        else
            _update_fidget ( ) ;
    }
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _update_fidget ( )
{
    num_fract angle_delta ;
    platform_math :: math_make_num_fract ( angle_delta , 125 , 1000 ) ;
    platform_math :: math_add_to_fract ( _fidget_angle , angle_delta ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _render_fidget_mesh ( )
{    
    typename messages :: mesh_set_transform mesh_set_transform_msg ;
    typename messages :: mesh_render mesh_render_msg ;
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
    
    platform_math :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform_math :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform_math :: math_make_fract_from_whole ( fract_fidget_scale , _fidget_scale ) ;
    platform_math :: math_div_fracts ( scale , fract_fidget_scale , fract_scale_in_frames ) ;
    platform_render :: get_aspect_height ( height ) ;
    platform_math :: math_make_num_fract ( num_half , 1 , 2 ) ;
    platform_math :: math_cos ( angle_cos , _fidget_angle ) ;
    platform_math :: math_sin ( angle_sin , _fidget_angle ) ;
    platform_math :: math_mul_fracts ( cos_by_scale , angle_cos , scale ) ;
    platform_math :: math_mul_fracts ( sin_by_scale , angle_sin , scale ) ;
    platform_math :: math_neg_fract ( neg_sin_by_scale , sin_by_scale ) ;
    platform_math :: math_make_num_fract ( origin_x , 0 , 1 ) ;
    platform_math :: math_sub_fracts ( origin_y , height , num_half ) ;
    platform_math :: math_make_num_fract ( origin_z , - 3 , 1 ) ;
    platform_matrix :: matrix_set_axis_x ( matrix , cos_by_scale , sin_by_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: matrix_set_axis_y ( matrix , neg_sin_by_scale , cos_by_scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: matrix_set_axis_z ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , platform :: math_consts . fract_1 ) ;
    platform_matrix :: matrix_set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    
    mesh_set_transform_msg . mesh = _fidget_mesh_id ;
    mesh_set_transform_msg . transform = matrix ;
    mesh_render_msg . mesh = _fidget_mesh_id ;
    
    _mediator . get ( ) . send ( typename messages :: texture_unselect ( ) ) ;
    _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    _mediator . get ( ) . send ( mesh_render_msg ) ;

    if ( platform_conditions :: condition_whole_less_than_whole ( _fidget_scale , whole_scale_in_frames ) )
        platform_math :: math_inc_whole ( _fidget_scale ) ;
}

template < typename mediator >
void shy_logic_fidget < mediator > :: _create_fidget_mesh ( )
{    
    typename platform_static_array :: template static_array < vertex_data , _fidget_edges > vertices ;
    typename platform_static_array :: template static_array < index_data , _fidget_edges > indices ;
    num_whole i ;
    num_whole whole_fidget_edges ;
    num_fract fract_fidget_edges ;
    
    platform_math :: math_make_num_fract ( fract_fidget_edges , _fidget_edges , 1 ) ;
    platform_math :: math_make_num_whole ( whole_fidget_edges , _fidget_edges ) ;
    
    for ( platform_math :: math_make_num_whole ( i , 0 )
        ; platform_conditions :: condition_whole_less_than_whole ( i , whole_fidget_edges )
        ; platform_math :: math_inc_whole ( i )
        )
    {
        num_fract fract_i ;
        num_fract angle ;
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
        platform_math :: math_div_fract_by ( angle , fract_fidget_edges ) ;
        platform_math :: math_cos ( angle_cos , angle ) ;
        platform_math :: math_sin ( angle_sin , angle ) ;
        platform_math :: math_mul_fracts ( vertex_x , _fidget_size ( ) , angle_cos ) ;
        platform_math :: math_mul_fracts ( vertex_y , _fidget_size ( ) , angle_sin ) ;
        platform_math :: math_make_num_fract ( vertex_z , 0 , 1 ) ;
        platform_math :: math_make_num_fract ( vertex_r , _fidget_r , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_g , _fidget_g , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_b , _fidget_b , 255 ) ;
        platform_math :: math_make_num_fract ( vertex_a , 1 , 1 ) ;
        {
            vertex_data & vertex = platform_static_array :: element ( vertices , i ) ;
            platform_render :: set_vertex_position ( vertex , vertex_x , vertex_y , vertex_z ) ;
            platform_render :: set_vertex_color ( vertex , vertex_r , vertex_g , vertex_b , vertex_a ) ;
        }
        {
            index_data & index = platform_static_array :: element ( indices , i ) ;
            platform_render :: set_index_value ( index , i ) ;
        }
    }
    _mediator . get ( ) . mesh_create
        ( _fidget_mesh_id 
        , vertices 
        , indices
        , indices 
        , whole_fidget_edges 
        , platform :: math_consts . whole_0 
        , whole_fidget_edges 
        ) ;
}
