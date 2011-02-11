namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_const_int_32 max_letters_in_alphabet = 32 ;

        static const so_called_type_platform_math_num_fract final_scale = so_called_platform_math :: init_num_fract ( 1 , 2 ) ;
        static const so_called_type_platform_math_num_fract canvas_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract canvas_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract canvas_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract canvas_a = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract mesh_x = so_called_platform_math :: init_num_fract ( - 1 , 2 ) ;
        static const so_called_type_platform_math_num_fract mesh_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract mesh_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
        static const so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static const so_called_type_platform_math_num_whole small_size = so_called_platform_math :: init_num_whole ( 16 ) ;
        static const so_called_type_platform_math_num_whole big_size = so_called_platform_math :: init_num_whole ( 32 ) ;
    }

    class tex_coords
    {
    public :
        so_called_type_platform_math_num_fract left ;
        so_called_type_platform_math_num_fract bottom ;
        so_called_type_platform_math_num_fract right ;
        so_called_type_platform_math_num_fract top ;
    } ;

    typedef so_called_type_platform_static_array_data < shy_guts :: tex_coords , shy_guts :: consts :: max_letters_in_alphabet > letters_tex_coords ;

    static void render_text_mesh ( ) ;
    static void update_text_mesh ( ) ;
    static void create_text_mesh ( ) ;
    static void create_text_texture ( ) ;
    static void proceed_with_create_text ( ) ;
    static void prepare_rasterizer_for_drawing ( ) ;
    static void next_letter_col ( ) ;
    static void next_letter_row ( ) ;
    static void rasterize_font_english_A ( ) ;
    static void rasterize_font_english_B ( ) ;
    static void rasterize_font_english_C ( ) ;
    static void rasterize_font_english_D ( ) ;
    static void rasterize_font_english_E ( ) ;
    static void rasterize_font_english_F ( ) ;
    static void rasterize_font_english_G ( ) ;
    static void rasterize_font_english_H ( ) ;
    static void rasterize_font_english_I ( ) ;
    static void rasterize_font_english_J ( ) ;
    static void rasterize_font_english_K ( ) ;
    static void rasterize_font_english_L ( ) ;
    static void rasterize_font_english_M ( ) ;
    static void rasterize_font_english_N ( ) ;
    static void rasterize_font_english_O ( ) ;
    static void rasterize_font_english_P ( ) ;
    static void rasterize_font_english_Q ( ) ;
    static void rasterize_font_english_R ( ) ;
    static void rasterize_font_english_S ( ) ;
    static void rasterize_font_english_T ( ) ;
    static void rasterize_font_english_U ( ) ;
    static void rasterize_font_english_V ( ) ;
    static void rasterize_font_english_W ( ) ;
    static void rasterize_font_english_X ( ) ;
    static void rasterize_font_english_Y ( ) ;
    static void rasterize_font_english_Z ( ) ;
    static void rasterize_use_texel 
        ( so_called_type_platform_render_texel_data texel 
        ) ;
    static void mesh_set_triangle_strip_index_value
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_whole index
        ) ;
    static void store_tex_coords 
        ( so_called_type_common_logic_text_letter_id letter 
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void rasterize_letter 
        ( so_called_type_common_logic_text_letter_id letter 
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract u
        , so_called_type_platform_math_num_fract v 
        ) ;
    static void rasterize_english_alphabet 
        ( so_called_type_platform_math_num_whole letter_size_x
        , so_called_type_platform_math_num_whole letter_size_y
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract x
        , so_called_type_platform_math_num_fract y
        , so_called_type_platform_math_num_fract z 
        ) ;
    static void rasterize_rect 
        ( so_called_type_platform_math_num_whole x1
        , so_called_type_platform_math_num_whole y1
        , so_called_type_platform_math_num_whole x2
        , so_called_type_platform_math_num_whole y2
        ) ;
    static void rasterize_ellipse_in_rect 
        ( so_called_type_platform_math_num_whole x1
        , so_called_type_platform_math_num_whole y1
        , so_called_type_platform_math_num_whole x2
        , so_called_type_platform_math_num_whole y2
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_type_platform_math_num_whole offset 
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a
        ) ;
    static void rasterize_triangle 
        ( so_called_type_platform_math_num_whole x1 
        , so_called_type_platform_math_num_whole y1
        , so_called_type_platform_math_num_whole x2
        , so_called_type_platform_math_num_whole y2 
        , so_called_type_platform_math_num_whole x3
        , so_called_type_platform_math_num_whole y3
        ) ;

    static so_called_type_platform_math_num_whole texture_create_requested ;
    static so_called_type_platform_math_num_whole texture_create_replied ;
    
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_platform_math_num_whole mesh_create_replied ;
    
    static so_called_type_platform_math_num_whole rasterize_finalize_requested ;
    static so_called_type_platform_math_num_whole rasterize_finalize_replied ;
    
    static so_called_type_platform_math_num_whole empty_texture_created ;
    static so_called_type_platform_math_num_whole small_letters_rasterized ;
    static so_called_type_platform_math_num_whole big_letters_rasterized ;
        
    static so_called_type_platform_math_num_whole text_mesh_created ;
    static so_called_type_platform_math_num_whole text_prepare_permitted ;
    static so_called_type_common_engine_render_mesh_id text_mesh_id ;
    static so_called_type_common_engine_render_texture_id text_texture_id ;
    static so_called_type_platform_render_texel_data filler ;
    static so_called_type_platform_render_texel_data eraser ;
    static so_called_type_platform_math_num_whole origin_x ;
    static so_called_type_platform_math_num_whole origin_y ;
    static so_called_type_platform_math_num_whole letter_size_x ;
    static so_called_type_platform_math_num_whole letter_size_y ;
    static so_called_type_platform_math_num_whole scale_frames ;
    static shy_guts :: letters_tex_coords letters_big ;
    static shy_guts :: letters_tex_coords letters_small ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_text_mesh ( )
{
}

void shy_guts :: update_text_mesh ( )
{
}

void shy_guts :: create_text_mesh ( )
{
}

void shy_guts :: create_text_texture ( )
{
}

void shy_guts :: proceed_with_create_text ( )
{
}

void shy_guts :: prepare_rasterizer_for_drawing ( )
{
}

void shy_guts :: next_letter_col ( )
{
}

void shy_guts :: next_letter_row ( )
{
}

void shy_guts :: rasterize_font_english_A ( )
{
}

void shy_guts :: rasterize_font_english_B ( )
{
}

void shy_guts :: rasterize_font_english_C ( )
{
}

void shy_guts :: rasterize_font_english_D ( )
{
}

void shy_guts :: rasterize_font_english_E ( )
{
}

void shy_guts :: rasterize_font_english_F ( )
{
}

void shy_guts :: rasterize_font_english_G ( )
{
}

void shy_guts :: rasterize_font_english_H ( )
{
}

void shy_guts :: rasterize_font_english_I ( )
{
}

void shy_guts :: rasterize_font_english_J ( )
{
}

void shy_guts :: rasterize_font_english_K ( )
{
}

void shy_guts :: rasterize_font_english_L ( )
{
}

void shy_guts :: rasterize_font_english_M ( )
{
}

void shy_guts :: rasterize_font_english_N ( )
{
}

void shy_guts :: rasterize_font_english_O ( )
{
}

void shy_guts :: rasterize_font_english_P ( )
{
}

void shy_guts :: rasterize_font_english_Q ( )
{
}

void shy_guts :: rasterize_font_english_R ( )
{
}

void shy_guts :: rasterize_font_english_S ( )
{
}

void shy_guts :: rasterize_font_english_T ( )
{
}

void shy_guts :: rasterize_font_english_U ( )
{
}

void shy_guts :: rasterize_font_english_V ( )
{
}

void shy_guts :: rasterize_font_english_W ( )
{
}

void shy_guts :: rasterize_font_english_X ( )
{
}

void shy_guts :: rasterize_font_english_Y ( )
{
}

void shy_guts :: rasterize_font_english_Z ( )
{
}

void shy_guts :: rasterize_use_texel ( so_called_type_platform_render_texel_data texel )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index
    )
{
}

void shy_guts :: store_tex_coords 
    ( so_called_type_common_logic_text_letter_id letter 
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
}

void shy_guts :: rasterize_letter 
    ( so_called_type_common_logic_text_letter_id letter 
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v 
    )
{
}

void shy_guts :: rasterize_english_alphabet 
    ( so_called_type_platform_math_num_whole letter_size_x
    , so_called_type_platform_math_num_whole letter_size_y
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z 
    )
{
}

void shy_guts :: rasterize_rect 
    ( so_called_type_platform_math_num_whole x1
    , so_called_type_platform_math_num_whole y1
    , so_called_type_platform_math_num_whole x2
    , so_called_type_platform_math_num_whole y2
    )
{
}

void shy_guts :: rasterize_ellipse_in_rect 
    ( so_called_type_platform_math_num_whole x1
    , so_called_type_platform_math_num_whole y1
    , so_called_type_platform_math_num_whole x2
    , so_called_type_platform_math_num_whole y2
    )
{
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a
    )
{
}

void shy_guts :: rasterize_triangle 
    ( so_called_type_platform_math_num_whole x1 
    , so_called_type_platform_math_num_whole y1
    , so_called_type_platform_math_num_whole x2
    , so_called_type_platform_math_num_whole y2 
    , so_called_type_platform_math_num_whole x3
    , so_called_type_platform_math_num_whole y3
    )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_engine_rasterizer_finalize_reply )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_engine_render_texture_create_reply )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_request )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_letter_small_tex_coords_request )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_prepare_permit )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_render_request )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_update )
{
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_use_text_texture_request )
{
}
