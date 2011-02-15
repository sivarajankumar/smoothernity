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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_prepare_permitted ) )
    {
        shy_guts :: text_prepare_permitted = so_called_platform_math_consts :: whole_false ;
        
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_engine_render_texture_create_request :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
        
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
        mesh_create_msg . vertices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
        so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_replied )
      && so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_replied )
       )
    {
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: create_text_mesh ( ) ;
        shy_guts :: create_text_texture ( ) ;
        shy_guts :: empty_texture_created = so_called_platform_math_consts :: whole_true ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: empty_texture_created ) )
    {
        shy_guts :: empty_texture_created = so_called_platform_math_consts :: whole_false ;
        shy_guts :: small_letters_rasterized = so_called_platform_math_consts :: whole_true ;
        shy_guts :: rasterize_english_alphabet ( shy_guts :: consts :: small_size , shy_guts :: consts :: small_size , shy_guts :: letters_small ) ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: small_letters_rasterized ) )
    {
        shy_guts :: small_letters_rasterized = so_called_platform_math_consts :: whole_false ;
        shy_guts :: big_letters_rasterized = so_called_platform_math_consts :: whole_true ;
        shy_guts :: rasterize_english_alphabet ( shy_guts :: consts :: big_size , shy_guts :: consts :: big_size , shy_guts :: letters_big ) ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: big_letters_rasterized ) )
    {
        shy_guts :: big_letters_rasterized = so_called_platform_math_consts :: whole_false ;
        shy_guts :: rasterize_finalize_requested = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_engine_rasterizer_finalize_request :: send ( so_called_message_common_engine_rasterizer_finalize_request ( ) ) ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: rasterize_finalize_replied ) )
    {
        shy_guts :: rasterize_finalize_replied = so_called_platform_math_consts :: whole_false ;
        
        so_called_message_common_engine_render_texture_finalize texture_finalize_msg ;
        texture_finalize_msg . texture = shy_guts :: text_texture_id ;
        so_called_sender_common_engine_render_texture_finalize :: send ( texture_finalize_msg ) ;
        
        shy_guts :: text_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_text_prepared :: send ( so_called_message_common_logic_text_prepared ( ) ) ;
    }
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: rasterize_finalize_requested ) )
    {
        shy_guts :: rasterize_finalize_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: rasterize_finalize_replied = so_called_platform_math_consts :: whole_true ;
    }
}

void _shy_common_logic_text :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_mesh_id = msg . mesh ;
        shy_guts :: proceed_with_create_text ( ) ;
    }
}

void _shy_common_logic_text :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_texture_id = msg . texture ;
        shy_guts :: proceed_with_create_text ( ) ;
    }
}

void _shy_common_logic_text :: receive ( so_called_message_common_init )
{
    shy_guts :: empty_texture_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: small_letters_rasterized = so_called_platform_math_consts :: whole_false ;
    shy_guts :: big_letters_rasterized = so_called_platform_math_consts :: whole_false ;
    shy_guts :: rasterize_finalize_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: rasterize_finalize_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: text_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: text_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: scale_frames = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: letter_size_x = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: letter_size_y = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: origin_x = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: origin_y = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_request msg )
{
    so_called_message_common_logic_text_letter_big_tex_coords_reply reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: tex_coords > coords ;
        so_called_platform_static_array :: element_ptr ( coords , shy_guts :: letters_big , msg . letter . _letter_id ) ;
        reply_msg . left = coords . get ( ) . left ;
        reply_msg . bottom = coords . get ( ) . bottom ;
        reply_msg . right = coords . get ( ) . right ;
        reply_msg . top = coords . get ( ) . top ;
    }
    else
    {
        reply_msg . left = so_called_platform_math_consts :: fract_0 ;
        reply_msg . bottom = so_called_platform_math_consts :: fract_0 ;
        reply_msg . right = so_called_platform_math_consts :: fract_0 ;
        reply_msg . top = so_called_platform_math_consts :: fract_0 ;
    }
    so_called_sender_common_logic_text_letter_big_tex_coords_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_letter_small_tex_coords_request msg )
{
    so_called_message_common_logic_text_letter_small_tex_coords_reply reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: tex_coords > coords ;
        so_called_platform_static_array :: element_ptr ( coords , shy_guts :: letters_small , msg . letter . _letter_id ) ;
        reply_msg . left = coords . get ( ) . left ;
        reply_msg . bottom = coords . get ( ) . bottom ;
        reply_msg . right = coords . get ( ) . right ;
        reply_msg . top = coords . get ( ) . top ;
    }
    else
    {
        reply_msg . left = so_called_platform_math_consts :: fract_0 ;
        reply_msg . bottom = so_called_platform_math_consts :: fract_0 ;
        reply_msg . right = so_called_platform_math_consts :: fract_0 ;
        reply_msg . top = so_called_platform_math_consts :: fract_0 ;
    }
    so_called_sender_common_logic_text_letter_small_tex_coords_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_prepare_permit )
{
    shy_guts :: text_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
        shy_guts :: render_text_mesh ( ) ;
    so_called_sender_common_logic_text_render_reply :: send ( so_called_message_common_logic_text_render_reply ( ) ) ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_update )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: text_mesh_created ) )
        shy_guts :: proceed_with_create_text ( ) ;    
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
        shy_guts :: update_text_mesh ( ) ;
}

void _shy_common_logic_text :: receive ( so_called_message_common_logic_text_use_text_texture_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_message_common_engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = shy_guts :: text_texture_id ;
        so_called_sender_common_engine_render_texture_select :: send ( texture_select_msg ) ;
    }
    so_called_sender_common_logic_text_use_text_texture_reply :: send ( so_called_message_common_logic_text_use_text_texture_reply ( ) ) ;
}
