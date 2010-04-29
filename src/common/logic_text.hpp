#define TEXT_TEXTURE_SIZE_POW2_BASE 8
#define TEXT_TEXTURE_SIZE ( 1 << TEXT_TEXTURE_SIZE_POW2_BASE )

template < typename mediator >
class shy_logic_text
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
public :
    shy_logic_text ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _text_mesh_created ( false )
    {
    }
    void render_text ( )
    {
        if ( _text_mesh_created )
            _render_text_mesh ( ) ;
    }
    void update ( )
    {
        if ( ! _text_mesh_created )
        {
            _create_text_mesh ( ) ;
            _create_text_texture ( ) ;
            _text_mesh_created = true ;
        }
    }
private :
    void _render_text_mesh ( )
    {
        platform :: render_enable_texturing ( ) ;
        platform :: render_use_texture ( _text_texture_id ) ;
        _mediator -> mesh_render ( _text_mesh_id ) ;
    }
    void _create_text_mesh ( )
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
    void _create_text_texture ( )
    {
        for ( int_32 x = 0 ; x < TEXT_TEXTURE_SIZE ; x ++ )
        {
            for ( int_32 y = 0 ; y < TEXT_TEXTURE_SIZE ; y ++ )
            {
                int_32 c = x ^ y ;
                platform :: render_set_texel_color
                    ( _text_texture_data [ x + TEXT_TEXTURE_SIZE * y ]
                    , ( c % 32 ) * 8
                    , ( c % 64 ) * 4
                    , ( c % 128 ) * 2
                    , ( c % 64 ) * 4
                    ) ;
            }
        }
        _generate_font_linear_english_A ( _text_texture_data , TEXT_TEXTURE_SIZE , TEXT_TEXTURE_SIZE , TEXT_TEXTURE_SIZE ) ;
        _generate_font_linear_english_A ( _text_texture_data + TEXT_TEXTURE_SIZE * ( TEXT_TEXTURE_SIZE - 32 ) , TEXT_TEXTURE_SIZE , 16 , 16 ) ;
        _generate_font_linear_english_A ( _text_texture_data + TEXT_TEXTURE_SIZE * ( TEXT_TEXTURE_SIZE - 32 ) + 32 , TEXT_TEXTURE_SIZE , 32 , 32 ) ;
        platform :: render_create_texture_id ( _text_texture_id ) ;
        platform :: render_load_texture_data ( _text_texture_id , TEXT_TEXTURE_SIZE_POW2_BASE , _text_texture_data ) ;
    }
    void _generate_font_linear_english_A 
        ( texel_data * starting_texel 
        , int_32 texels_in_row 
        , int_32 letter_size_x 
        , int_32 letter_size_y
        )
    {
        texel_data filler ;
        texel_data eraser ;
        platform :: render_set_texel_color ( filler , 255 , 255 , 255 , 255 ) ;
        platform :: render_set_texel_color ( eraser , 0 , 0 , 0 , 0 ) ;
        _mediator -> rasterize_triangle ( starting_texel , filler , texels_in_row
            , letter_size_x / 2 , letter_size_y - 1
            , 0 , 0
            , letter_size_x - 1 , 0
            ) ;
        _mediator -> rasterize_triangle ( starting_texel , eraser , texels_in_row
            , letter_size_x / 2 , ( letter_size_y * 2 ) / 3
            , letter_size_x / 5 , 0
            , ( letter_size_x * 4 ) / 5 , 0
            ) ;
        int_32 top = ( letter_size_y * 3 ) / 7 ;
        int_32 bottom = ( letter_size_y * 2 ) / 7 ;
        int_32 left = ( letter_size_x * 2 ) / 7 ;
        int_32 right = ( letter_size_x * 5 ) / 7 ;
        _mediator -> rasterize_triangle ( starting_texel , filler , texels_in_row , left , top , left , bottom , right , bottom ) ;
        _mediator -> rasterize_triangle ( starting_texel , filler , texels_in_row , left , top , right , top , right , bottom ) ;
    }
private :
    mediator * _mediator ;
    int_32 _text_mesh_created ;
    mesh_id _text_mesh_id ;
    render_texture_id _text_texture_id ;
    texel_data _text_texture_data [ TEXT_TEXTURE_SIZE * TEXT_TEXTURE_SIZE ] ;
} ;
