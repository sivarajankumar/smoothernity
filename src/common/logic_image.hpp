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
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const int_32 logo_resource_index = 1 ;
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
            int_32 loader_ready = false ;
            platform :: render_texture_loader_ready ( loader_ready ) ;
            if ( loader_ready )
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
    static const float_32 final_scale = 0.5f ;
    static const int_32 scale_in_frames = 60 ;
    if ( _scale_frames < scale_in_frames )
        _scale_frames ++ ;
    float_32 scale = _mediator -> math_lerp ( 0 , 0 , final_scale , scale_in_frames , _scale_frames ) ;
    matrix_data matrix ;
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

    static const int_32 red = 255 ;
    static const int_32 green = 255 ;
    static const int_32 blue = 255 ;
    static const int_32 alpha = 255 ;

    platform :: render_set_vertex_position  ( vertices [ 0 ] , - 1 , 1 , 0 ) ;
    platform :: render_set_vertex_color     ( vertices [ 0 ] , red , green , blue , alpha ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 0 ] , 0 , 1 ) ;
    platform :: render_set_index_value      ( indices  [ 0 ] , 0 ) ;

    platform :: render_set_vertex_position  ( vertices [ 1 ] , - 1 , - 1 , 0 ) ;
    platform :: render_set_vertex_color     ( vertices [ 1 ] , red , green , blue , alpha ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 1 ] , 0 , 0 ) ;
    platform :: render_set_index_value      ( indices  [ 1 ] , 1 ) ;

    platform :: render_set_vertex_position  ( vertices [ 2 ] , 1 , 1 , 0 ) ;
    platform :: render_set_vertex_color     ( vertices [ 2 ] , red , green , blue , alpha ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 2 ] , 1 , 1 ) ;
    platform :: render_set_index_value      ( indices  [ 2 ] , 2 ) ;

    platform :: render_set_vertex_position  ( vertices [ 3 ] , 1 , - 1 , 0 ) ;
    platform :: render_set_vertex_color     ( vertices [ 3 ] , red , green , blue , alpha ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 3 ] , 1 , 0 ) ;
    platform :: render_set_index_value      ( indices  [ 3 ] , 3 ) ;

    _image_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , 4 , 4 , 0 ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_texture ( )
{
    _image_texture_id = _mediator -> texture_create ( ) ;
    texture_resource_id logo_resource_id ;
    platform :: render_create_texture_resource_id ( logo_resource_id , logo_resource_index ) ;
    _mediator -> texture_load_from_resource ( _image_texture_id , logo_resource_id ) ;
}
