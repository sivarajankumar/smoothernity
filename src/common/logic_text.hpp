template < typename mediator >
class shy_logic_text
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
    shy_logic_text ( mediator * arg_mediator ) ;
    void render_text ( ) ;
    void update ( ) ;
private :
    void _render_text_mesh ( ) ;
    void _create_text_mesh ( ) ;
    void _create_text_texture ( ) ;
    void _next_letter_col ( ) ;
    void _next_letter_row ( ) ;
    void _rasterize_english_alphabet ( int_32 letter_size_x , int_32 letter_size_y ) ;
    void _rasterize_font_english_A ( ) ;
    void _rasterize_font_english_B ( ) ;
    void _rasterize_font_english_C ( ) ;
    void _rasterize_font_english_D ( ) ;
    void _rasterize_font_english_E ( ) ;
    void _rasterize_font_english_F ( ) ;
    void _rasterize_font_english_G ( ) ;
    void _rasterize_font_english_H ( ) ;
private :
    mediator * _mediator ;
    int_32 _text_mesh_created ;
    mesh_id _text_mesh_id ;
    texture_id _text_texture_id ;
    texel_data _filler ;
    texel_data _eraser ;
    int_32 _origin_x ;
    int_32 _origin_y ;
    int_32 _letter_size_x ;
    int_32 _letter_size_y ;
} ;

template < typename mediator >
shy_logic_text < mediator > :: shy_logic_text ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _text_mesh_created ( false )
, _origin_x ( 0 )
, _origin_y ( 0 )
, _letter_size_x ( 0 )
, _letter_size_y ( 0 )
{
}

template < typename mediator >
void shy_logic_text < mediator > :: render_text ( )
{
    if ( _text_mesh_created )
        _render_text_mesh ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: update ( )
{
    if ( ! _text_mesh_created )
    {
        _create_text_mesh ( ) ;
        _create_text_texture ( ) ;
        _text_mesh_created = true ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: _render_text_mesh ( )
{
    _mediator -> texture_select ( _text_texture_id ) ;
    _mediator -> mesh_render ( _text_mesh_id ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_mesh ( )
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

    _text_mesh_id = _mediator -> mesh_create ( vertices , indices , 0 , 4 , 4 , 0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_texture ( )
{
    platform :: render_set_texel_color ( _filler , 255 , 255 , 255 , 255 ) ;
    platform :: render_set_texel_color ( _eraser , 0 , 0 , 0 , 128 ) ;
    _text_texture_id = _mediator -> texture_create ( ) ;
    for ( int_32 x = 0 ; x < _mediator -> texture_width ( ) ; x ++ )
    {
        for ( int_32 y = 0 ; y < _mediator -> texture_height ( ) ; y ++ )
            _mediator -> texture_set_texel ( _text_texture_id , x , y , _eraser ) ;
    }
    _origin_y = _mediator -> texture_height ( ) ;
    _rasterize_english_alphabet ( 16 , 16 ) ;
    _rasterize_english_alphabet ( 32 , 32 ) ;
    _rasterize_english_alphabet ( 64 , 64 ) ;
    _mediator -> texture_finalize ( _text_texture_id ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_english_alphabet ( int_32 letter_size_x , int_32 letter_size_y )
{
    _letter_size_x = letter_size_x ;
    _letter_size_y = letter_size_y ;
    _next_letter_row ( ) ;
    _rasterize_font_english_A ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_B ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_C ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_D ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_E ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_F ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_G ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_H ( ) ; _next_letter_col ( ) ;
    _next_letter_row ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_col ( )
{
    _origin_x += _letter_size_x ;
    if ( _origin_x >= _mediator -> texture_width ( ) )
        _next_letter_row ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_row ( )
{
    _origin_y -= _letter_size_y ;
    _origin_x = 0 ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_A ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    int_32 outer_top = _letter_size_y - 1 ;
    int_32 outer_bottom = 0 ;
    int_32 outer_center = _letter_size_x / 2 ;
    int_32 outer_left = 0 ;
    int_32 outer_right = _letter_size_x - 1 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( outer_center , outer_top , outer_left , outer_bottom , outer_right , outer_bottom ) ;

    int_32 inner_top = ( _letter_size_y * 2 ) / 3 ;
    int_32 inner_bottom = 0 ;
    int_32 inner_center = _letter_size_x / 2 ;
    int_32 inner_left = _letter_size_x / 5 ;
    int_32 inner_right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_triangle ( inner_center , inner_top , inner_left , inner_bottom , inner_right , inner_bottom ) ;
    
    int_32 board_top = ( _letter_size_y * 3 ) / 7 ;
    int_32 board_bottom = ( _letter_size_y * 2 ) / 7 ;
    int_32 board_top_left     = outer_center + ( ( outer_left  - outer_center ) * ( outer_top - board_top    ) ) / ( outer_top - outer_bottom ) ;
    int_32 board_bottom_left  = outer_center + ( ( outer_left  - outer_center ) * ( outer_top - board_bottom ) ) / ( outer_top - outer_bottom ) ;
    int_32 board_top_right    = outer_center + ( ( outer_right - outer_center ) * ( outer_top - board_top    ) ) / ( outer_top - outer_bottom ) ;
    int_32 board_bottom_right = outer_center + ( ( outer_right - outer_center ) * ( outer_top - board_bottom ) ) / ( outer_top - outer_bottom ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( board_top_left , board_top , board_bottom_left , board_bottom , board_bottom_right , board_bottom ) ;
    _mediator -> rasterize_triangle ( board_top_left , board_top , board_top_right , board_top , board_bottom_right , board_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_B ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( 0 , 0 , _letter_size_x - 1 , _letter_size_y / 2 ) ;
    _mediator -> rasterize_ellipse_in_rect ( 0 , _letter_size_y / 2 , _letter_size_x - 1 , _letter_size_y - 1 ) ;

    int_32 spine_left = 0 ;
    int_32 spine_right = _letter_size_x / 2 ;
    int_32 spine_top = _letter_size_y - 1 ;
    int_32 spine_bottom = 0 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( spine_left , spine_top , spine_right , spine_bottom ) ;
            
    int_32 hole_left = ( _letter_size_x * 4 ) / 16 ;
    int_32 hole_right = ( _letter_size_x * 12 ) / 16 ;
    int_32 hole_top = ( _letter_size_y * 13 ) / 16 ;
    int_32 hole_bottom = ( _letter_size_y * 3 ) / 16 ;
    int_32 hole_height = ( _letter_size_y * 3 ) / 16 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_top - hole_height ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_bottom , hole_right , hole_bottom + hole_height ) ;

    int_32 hole_center_x = ( hole_left + hole_right ) / 2 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_center_x , hole_top - hole_height ) ;
    _mediator -> rasterize_rect ( hole_left , hole_bottom , hole_center_x , hole_bottom + hole_height ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_C ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( 0 , 0 , _letter_size_x - 1 , _letter_size_y - 1 ) ;
    
    int_32 hole_top = ( _letter_size_y * 4 ) / 5 ;
    int_32 hole_bottom = _letter_size_y / 5 ;
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    int_32 hole_center_x = ( hole_left + hole_right ) / 2 ;
    int_32 hole_center_top = ( _letter_size_y * 5 ) / 7 ;
    int_32 hole_center_bottom = ( _letter_size_y * 2 ) / 7 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_center_x , hole_center_top , _letter_size_x - 1 , hole_center_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_D ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( 0 , 0 , _letter_size_x - 1 , _letter_size_y - 1 ) ;

    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( 0 , 0 , _letter_size_x / 2 , _letter_size_y - 1 ) ;
    
    int_32 hole_top = ( _letter_size_y * 4 ) / 5 ;
    int_32 hole_bottom = _letter_size_y / 5 ;
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    int_32 hole_center_x = ( hole_left + hole_right ) / 2 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_center_x , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_E ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    int_32 right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( 0 , 0 , right , _letter_size_y - 1 ) ;
    
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = _letter_size_x - 1 ;
    int_32 hole_top = ( _letter_size_y * 4 ) / 5 ;
    int_32 hole_mid_top = ( _letter_size_y * 3 ) / 5 ;
    int_32 hole_mid_bottom = ( _letter_size_y * 2 ) / 5 ;
    int_32 hole_bottom = _letter_size_y / 5 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_F ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    int_32 right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( 0 , 0 , right , _letter_size_y - 1 ) ;
    
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = _letter_size_x - 1 ;
    int_32 hole_top = ( _letter_size_y * 4 ) / 5 ;
    int_32 hole_mid_top = ( _letter_size_y * 3 ) / 5 ;
    int_32 hole_mid_bottom = ( _letter_size_y * 2 ) / 5 ;
    int_32 hole_bottom = 0 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_G ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( 0 , 0 , _letter_size_x - 1 , _letter_size_y - 1 ) ;
    
    int_32 hole_top = ( _letter_size_y * 4 ) / 5 ;
    int_32 hole_bottom = _letter_size_y / 5 ;
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    int_32 hole_center_x = ( hole_left + hole_right ) / 2 ;
    int_32 hole_center_top = ( _letter_size_y * 5 ) / 7 ;
    int_32 hole_center_bottom = ( _letter_size_y * 3 ) / 7 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_center_x , hole_center_top , _letter_size_x - 1 , hole_center_bottom ) ;
    
    int_32 brick_top = ( _letter_size_y * 4 ) / 7 ;
    int_32 brick_bottom = ( _letter_size_y * 3 ) / 7 ;
    int_32 brick_left = ( _letter_size_x * 2 ) / 5 ;
    int_32 brick_right = _letter_size_x - 1 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( brick_left , brick_top , brick_right , brick_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_H ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    int_32 right = ( _letter_size_x * 4 ) / 5 ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( 0 , 0 , right , _letter_size_y - 1 ) ;
    
    int_32 hole_left = _letter_size_x / 5 ;
    int_32 hole_right = ( _letter_size_x * 3 ) / 5 ;
    int_32 hole_top = _letter_size_y - 1 ;
    int_32 hole_mid_top = ( _letter_size_y * 3 ) / 5 ;
    int_32 hole_mid_bottom = ( _letter_size_y * 2 ) / 5 ;
    int_32 hole_bottom = 0 ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

