template < typename mediator >
class shy_logic_image
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
public :
    shy_logic_image ( mediator * arg_mediator ) ;
    void render_image ( ) ;
    void update ( ) ;
private :
    void _render_image_mesh ( ) ;
    void _create_image_mesh ( ) ;
    void _create_image_texture ( ) ;
private :
    mediator * _mediator ;
    int_32 _image_mesh_created ;
    mesh_id _image_mesh_id ;
    texture_id _image_texture_id ;
} ;

template < typename mediator >
shy_logic_image < mediator > :: shy_logic_image ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _image_mesh_created ( false )
{
}

template < typename mediator >
void shy_logic_image < mediator > :: render_image ( )
{
    if ( _image_mesh_created )
        _render_image_mesh ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: update ( )
{
    if ( ! _image_mesh_created )
    {
        _create_image_mesh ( ) ;
        _create_image_texture ( ) ;
        _image_mesh_created = true ;
    }
}

template < typename mediator >
void shy_logic_image < mediator > :: _render_image_mesh ( )
{
    _mediator -> texture_select ( _image_texture_id ) ;
    _mediator -> mesh_render ( _image_mesh_id ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_mesh ( )
{
    vertex_data vertices [ 4 ] ;
    index_data indices [ 4 ] ;

    platform :: render_set_vertex_position  ( vertices [ 0 ] , - 1 , 1 , - 3 ) ;
    platform :: render_set_vertex_color     ( vertices [ 0 ] , 255 , 255 , 255 , 255 ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 0 ] , 0 , 1 ) ;
    platform :: render_set_index_value      ( indices  [ 0 ] , 0 ) ;

    platform :: render_set_vertex_position  ( vertices [ 1 ] , - 1 , - 1 , - 3 ) ;
    platform :: render_set_vertex_color     ( vertices [ 1 ] , 255 , 255 , 255 , 255 ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 1 ] , 0 , 0 ) ;
    platform :: render_set_index_value      ( indices  [ 1 ] , 1 ) ;

    platform :: render_set_vertex_position  ( vertices [ 2 ] , 1 , 1 , - 3 ) ;
    platform :: render_set_vertex_color     ( vertices [ 2 ] , 255 , 255 , 255 , 255 ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 2 ] , 1 , 1 ) ;
    platform :: render_set_index_value      ( indices  [ 2 ] , 2 ) ;

    platform :: render_set_vertex_position  ( vertices [ 3 ] , 1 , - 1 , - 3 ) ;
    platform :: render_set_vertex_color     ( vertices [ 3 ] , 255 , 255 , 255 , 255 ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 3 ] , 1 , 0 ) ;
    platform :: render_set_index_value      ( indices  [ 3 ] , 3 ) ;

    _image_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , 4 , 4 , 0 ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_texture ( )
{
    _image_texture_id = _mediator -> texture_create ( ) ;
    texel_data filler ;
    platform :: render_set_texel_color ( filler , 0 , 255 , 0 , 128 ) ;
    for ( int_32 x = 0 ; x < _mediator -> texture_width ( ) ; x ++ )
    {
        for ( int_32 y = 0 ; y < _mediator -> texture_height ( ) ; y ++ )
            _mediator -> texture_set_texel ( _image_texture_id , x , y , filler ) ;
    }
    _mediator -> texture_finalize ( _image_texture_id ) ;
}
