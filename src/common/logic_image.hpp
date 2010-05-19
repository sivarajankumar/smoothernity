template < typename mediator >
class shy_logic_image
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 _logo_resource_index = 1 ;
    static const int_32 _scale_in_frames = 60 ;
    static const int_32 _image_r = 255 ;
    static const int_32 _image_g = 255 ;
    static const int_32 _image_b = 255 ;
    static const int_32 _image_a = 255 ;
    static const float_32 _final_scale ( ) { return 0.5f ; }
public :
    shy_logic_image ( mediator * arg_mediator ) ;
    void image_render ( ) ;
    void image_update ( ) ;
    void image_prepare_permit ( ) ;
private :
    void _render_image_mesh ( ) ;
    void _update_image_mesh ( ) ;
    void _create_image_mesh ( ) ;
    void _create_image_texture ( ) ;
private :
    mediator * _mediator ;
    int_32 _image_mesh_created ;
    int_32 _image_texture_created ;
    int_32 _image_texture_loaded ;
    int_32 _image_prepare_permitted ;
    int_32 _scale_frames ;
    mesh_id _image_mesh_id ;
    texture_id _image_texture_id ;
} ;

template < typename mediator >
shy_logic_image < mediator > :: shy_logic_image ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _image_mesh_created ( false )
, _image_texture_loaded ( false )
, _image_prepare_permitted ( false )
, _scale_frames ( 0 )
{
}

template < typename mediator >
void shy_logic_image < mediator > :: image_render ( )
{
    if ( _image_mesh_created && _image_texture_loaded )
        _render_image_mesh ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: image_prepare_permit ( )
{
    _image_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_image < mediator > :: image_update ( )
{
    if ( _image_prepare_permitted )
    {
        if ( ! _image_mesh_created )
        {
            _create_image_mesh ( ) ;
            _image_mesh_created = true ;
        }
        if ( ! _image_texture_created )
        {
            _create_image_texture ( ) ;
            _image_texture_created = true ;
        }
        if ( ! _image_texture_loaded )
        {
            num_whole loader_ready ;
            platform :: render_texture_loader_ready ( loader_ready ) ;
            if ( platform :: condition_true ( loader_ready ) )
            {
                _mediator -> texture_finalize ( _image_texture_id ) ;
                _image_texture_loaded = true ;
                _mediator -> image_prepared ( ) ;
            }
        }
    }
    if ( _image_mesh_created && _image_texture_loaded )
        _update_image_mesh ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _update_image_mesh ( )
{
    if ( _scale_frames < _scale_in_frames )
        _scale_frames ++ ;
    float_32 scale ;
    matrix_data matrix ;
    _mediator -> math_lerp ( scale , 0 , 0 , _final_scale ( ) , _scale_in_frames , _scale_frames ) ;
    platform :: matrix_set_axis_x ( matrix , scale , 0 , 0 ) ;
    platform :: matrix_set_axis_y ( matrix , 0 , scale , 0 ) ;
    platform :: matrix_set_axis_z ( matrix , 0 , 0 , scale ) ;
    platform :: matrix_set_origin ( matrix , 0.5f , 0 , - 3 ) ;
    _mediator -> mesh_set_transform ( _image_mesh_id , matrix ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _render_image_mesh ( )
{
    platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    _mediator -> texture_select ( _image_texture_id ) ;
    _mediator -> mesh_render ( _image_mesh_id ) ;
    platform :: render_blend_disable ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_mesh ( )
{
    vertex_data vertices [ 4 ] ;
    index_data indices [ 4 ] ;

    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z ;
    num_whole color_r ;
    num_whole color_g ;
    num_whole color_b ;
    num_whole color_a ;
    num_whole index ;
    platform :: math_make_num_fract ( x_left , - 1 , 1 ) ;
    platform :: math_make_num_fract ( x_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_bottom , - 1 , 1 ) ;
    platform :: math_make_num_fract ( u_left , 0 , 1 ) ;
    platform :: math_make_num_fract ( u_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_bottom , 0 , 1 ) ;
    platform :: math_make_num_fract ( z , 0 , 1 ) ;
    platform :: math_make_num_whole ( color_r , _image_r ) ;
    platform :: math_make_num_whole ( color_g , _image_g ) ;
    platform :: math_make_num_whole ( color_b , _image_b ) ;
    platform :: math_make_num_whole ( color_a , _image_a ) ;

    platform :: math_make_num_whole ( index , 0 ) ;
    platform :: render_set_vertex_position  ( vertices [ 0 ] , x_left , y_top , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 0 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 0 ] , u_left , v_top ) ;
    platform :: render_set_index_value      ( indices  [ 0 ] , index ) ;

    platform :: math_make_num_whole ( index , 1 ) ;
    platform :: render_set_vertex_position  ( vertices [ 1 ] , x_left , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 1 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 1 ] , u_left , v_bottom ) ;
    platform :: render_set_index_value      ( indices  [ 1 ] , index ) ;

    platform :: math_make_num_whole ( index , 2 ) ;
    platform :: render_set_vertex_position  ( vertices [ 2 ] , x_right , y_top , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 2 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 2 ] , u_right , v_top ) ;
    platform :: render_set_index_value      ( indices  [ 2 ] , index ) ;

    platform :: math_make_num_whole ( index , 3 ) ;
    platform :: render_set_vertex_position  ( vertices [ 3 ] , x_right , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 3 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 3 ] , u_right , v_bottom ) ;
    platform :: render_set_index_value      ( indices  [ 3 ] , index ) ;

    _mediator -> mesh_create ( _image_mesh_id , vertices , indices , 0 , 4 , 4 , 0 ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_texture ( )
{
    num_whole resource_index ;
    texture_resource_id logo_resource_id ;
    platform :: math_make_num_whole ( resource_index , _logo_resource_index ) ;
    platform :: render_create_texture_resource_id ( logo_resource_id , resource_index ) ;
    _mediator -> texture_create ( _image_texture_id ) ;
    _mediator -> texture_load_from_resource ( _image_texture_id , logo_resource_id ) ;
}
