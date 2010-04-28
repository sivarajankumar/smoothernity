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
        _generate_font_linear_english_A ( _text_texture_data , TEXT_TEXTURE_SIZE , 16 , 16 ) ;
        _generate_font_linear_english_A ( _text_texture_data + 32 , TEXT_TEXTURE_SIZE , 32 , 32 ) ;
        platform :: render_create_texture_id ( _text_texture_id ) ;
        platform :: render_load_texture_data ( _text_texture_id , TEXT_TEXTURE_SIZE_POW2_BASE , _text_texture_data ) ;
    }
    void _generate_top_triangle_part
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x_top
        , int_32 y_top
        , int_32 x_mid
        , int_32 y_mid
        , int_32 x_bottom
        , int_32 y_bottom
        )
    {
        for ( int_32 y = y_top ; y > y_mid ; y -- )
        {
            int_32 x_top_mid    = x_top + ( ( y_top - y ) * ( x_mid    - x_top ) ) / ( y_top - y_mid    ) ;
            int_32 x_top_bottom = x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
            int_32 x_left  = _mediator -> math_min ( x_top_mid , x_top_bottom ) ;
            int_32 x_right = _mediator -> math_max ( x_top_mid , x_top_bottom ) ;
            for ( int_32 x = x_left ; x <= x_right ; x ++ )
                starting_texel [ x + texels_in_row * y ] = filler ;
        }
    }
    void _generate_bottom_triangle_part
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x_top
        , int_32 y_top
        , int_32 x_mid
        , int_32 y_mid
        , int_32 x_bottom
        , int_32 y_bottom
        )
    {
        for ( int_32 y = y_mid ; y > y_bottom ; y -- )
        {
            int_32 x_mid_bottom = x_mid + ( ( y_mid - y ) * ( x_mid - x_bottom ) ) / ( y_mid - y_bottom ) ;
            int_32 x_top_bottom = x_top + ( ( y_top - y ) * ( x_bottom - x_top ) ) / ( y_top - y_bottom ) ;
            int_32 x_left  = _mediator -> math_min ( x_mid_bottom , x_top_bottom ) ;
            int_32 x_right = _mediator -> math_max ( x_mid_bottom , x_top_bottom ) ;
            for ( int_32 x = x_left ; x <= x_right ; x ++ )
                starting_texel [ x + texels_in_row * y ] = filler ;
        }
    }
    void _generate_triangle
        ( texel_data * starting_texel
        , const texel_data & filler
        , int_32 texels_in_row
        , int_32 x1
        , int_32 y1
        , int_32 x2
        , int_32 y2
        , int_32 x3
        , int_32 y3
        )
    {
        if ( y1 >= y2 && y2 >= y3 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x1 , y1 , x2 , y2 , x3 , y3 ) ;
        }
        else if ( y1 >= y3 && y3 >= y2 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x1 , y1 , x3 , y3 , x2 , y2 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x1 , y1 , x3 , y3 , x2 , y2 ) ;
        }
        else if ( y3 >= y1 && y1 >= y2 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x3 , y3 , x1 , y1 , x2 , y2 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x3 , y3 , x1 , y1 , x2 , y2 ) ;
        }
        else if ( y3 >= y2 && y2 >= y1 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x3 , y3 , x2 , y2 , x1 , y1 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x3 , y3 , x2 , y2 , x1 , y1 ) ;
        }
        else if ( y2 >= y1 && y1 >= y3 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x2 , y2 , x1 , y1 , x3 , y3 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x2 , y2 , x1 , y1 , x3 , y3 ) ;
        }
        else if ( y2 >= y3 && y3 >= y1 )
        {
            _generate_top_triangle_part    ( starting_texel , filler , texels_in_row , x2 , y2 , x3 , y3 , x1 , y1 ) ;
            _generate_bottom_triangle_part ( starting_texel , filler , texels_in_row , x2 , y2 , x3 , y3 , x1 , y1 ) ;
        }
    }
    void _generate_font_linear_english_A 
        ( texel_data * starting_texel 
        , int_32 texels_in_row 
        , int_32 letter_size_x 
        , int_32 letter_size_y
        )
    {
        texel_data filler ;
        platform :: render_set_texel_color ( filler , 255 , 255 , 255 , 255 ) ;
        _generate_triangle ( starting_texel , filler , texels_in_row 
            , 0 , 0 
            , letter_size_x - 1 , 0 
            , letter_size_x - 1 , letter_size_y - 1 
            ) ;
    }
private :
    mediator * _mediator ;
    int_32 _text_mesh_created ;
    mesh_id _text_mesh_id ;
    render_texture_id _text_texture_id ;
    texel_data _text_texture_data [ TEXT_TEXTURE_SIZE * TEXT_TEXTURE_SIZE ] ;
} ;
