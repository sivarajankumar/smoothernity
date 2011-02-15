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
    so_called_sender_common_engine_render_blend_src_alpha_dst_one_minus_alpha :: send ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    {
        so_called_message_common_engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = shy_guts :: text_texture_id ;
        so_called_sender_common_engine_render_texture_select :: send ( texture_select_msg ) ;
    }
    {
        so_called_message_common_engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: text_mesh_id ;
        so_called_sender_common_engine_render_mesh_render :: send ( mesh_render_msg ) ;
    }
    so_called_sender_common_engine_render_blend_disable :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
}

void shy_guts :: update_text_mesh ( )
{
    so_called_type_platform_matrix_data matrix ;
    so_called_type_platform_math_num_fract fract_scale_frames ;    
    so_called_type_platform_math_num_fract fract_scale_in_frames ;
    so_called_type_platform_math_num_fract scale ;
    
    so_called_platform_math :: make_fract_from_whole ( fract_scale_frames , shy_guts :: scale_frames ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_scale_in_frames , shy_guts :: consts :: scale_in_frames ) ;
    so_called_common_engine_math_stateless :: lerp 
        ( scale 
        , fract_scale_frames 
        , so_called_platform_math_consts :: fract_0 
        , so_called_platform_math_consts :: fract_0 
        , shy_guts :: consts :: final_scale 
        , fract_scale_in_frames 
        ) ;
    so_called_platform_matrix :: set_axis_x ( matrix , scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , so_called_platform_math_consts :: fract_0 , scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , scale ) ;
    so_called_platform_matrix :: set_origin ( matrix , shy_guts :: consts :: mesh_x , shy_guts :: consts :: mesh_y , shy_guts :: consts :: mesh_z ) ;
    {
        so_called_message_common_engine_render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: text_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_sender_common_engine_render_mesh_set_transform :: send ( mesh_set_transform_msg ) ;
    }
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: scale_frames , shy_guts :: consts :: scale_in_frames ) )
        so_called_platform_math :: inc_whole ( shy_guts :: scale_frames ) ;
}

void shy_guts :: create_text_mesh ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract u_left ;
    so_called_type_platform_math_num_fract u_right ;
    so_called_type_platform_math_num_fract v_top ;
    so_called_type_platform_math_num_fract v_bottom ;
    so_called_type_platform_math_num_fract z ;
    so_called_type_platform_math_num_fract color_r ;
    so_called_type_platform_math_num_fract color_g ;
    so_called_type_platform_math_num_fract color_b ;
    so_called_type_platform_math_num_fract color_a ;

    x_left = so_called_platform_math_consts :: fract_minus_1 ;
    x_right = so_called_platform_math_consts :: fract_1 ;
    y_top = so_called_platform_math_consts :: fract_1 ;
    y_bottom = so_called_platform_math_consts :: fract_minus_1 ;
    u_left = so_called_platform_math_consts :: fract_0 ;
    u_right = so_called_platform_math_consts :: fract_1 ;
    v_top = so_called_platform_math_consts :: fract_1 ;
    v_bottom = so_called_platform_math_consts :: fract_0 ;
    z = so_called_platform_math_consts :: fract_0 ;
    color_r = shy_guts :: consts :: canvas_r ;
    color_g = shy_guts :: consts :: canvas_g ;
    color_b = shy_guts :: consts :: canvas_b ;
    color_a = shy_guts :: consts :: canvas_a ;

    shy_guts :: mesh_set_vertex_position            ( so_called_platform_math_consts :: whole_0 , x_left , y_top , z ) ;
    shy_guts :: mesh_set_vertex_color               ( so_called_platform_math_consts :: whole_0 , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( so_called_platform_math_consts :: whole_0 , u_left , v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 ) ;

    shy_guts :: mesh_set_vertex_position            ( so_called_platform_math_consts :: whole_1 , x_left , y_bottom , z ) ;
    shy_guts :: mesh_set_vertex_color               ( so_called_platform_math_consts :: whole_1 , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( so_called_platform_math_consts :: whole_1 , u_left , v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( so_called_platform_math_consts :: whole_1 , so_called_platform_math_consts :: whole_1 ) ;

    shy_guts :: mesh_set_vertex_position            ( so_called_platform_math_consts :: whole_2 , x_right , y_top , z ) ;
    shy_guts :: mesh_set_vertex_color               ( so_called_platform_math_consts :: whole_2 , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( so_called_platform_math_consts :: whole_2 , u_right , v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( so_called_platform_math_consts :: whole_2 , so_called_platform_math_consts :: whole_2 ) ;

    shy_guts :: mesh_set_vertex_position            ( so_called_platform_math_consts :: whole_3 , x_right , y_bottom , z ) ;
    shy_guts :: mesh_set_vertex_color               ( so_called_platform_math_consts :: whole_3 , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( so_called_platform_math_consts :: whole_3 , u_right , v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( so_called_platform_math_consts :: whole_3 , so_called_platform_math_consts :: whole_3 ) ;

    so_called_message_common_engine_render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = shy_guts :: text_mesh_id ;
    so_called_sender_common_engine_render_mesh_finalize :: send ( mesh_finalize_msg ) ;
}

void shy_guts :: create_text_texture ( )
{
    so_called_type_platform_math_num_whole texture_width ;
    so_called_type_platform_math_num_whole texture_height ;
    so_called_type_platform_math_num_fract filler_r ;
    so_called_type_platform_math_num_fract filler_g ;
    so_called_type_platform_math_num_fract filler_b ;
    so_called_type_platform_math_num_fract filler_a ;
    so_called_type_platform_math_num_fract eraser_r ;
    so_called_type_platform_math_num_fract eraser_g ;
    so_called_type_platform_math_num_fract eraser_b ;
    so_called_type_platform_math_num_fract eraser_a ;

    texture_width = so_called_common_engine_render_consts :: texture_width ;
    texture_height = so_called_common_engine_render_consts :: texture_height ;
    filler_r = so_called_platform_math_consts :: fract_1 ;
    filler_g = so_called_platform_math_consts :: fract_1 ;
    filler_b = so_called_platform_math_consts :: fract_1 ;
    filler_a = so_called_platform_math_consts :: fract_1 ;
    eraser_r = so_called_platform_math_consts :: fract_0 ;
    eraser_g = so_called_platform_math_consts :: fract_0 ;
    eraser_b = so_called_platform_math_consts :: fract_0 ;
    eraser_a = so_called_platform_math_consts :: fract_0 ;
    so_called_common_engine_render_stateless :: set_texel_color ( shy_guts :: filler , filler_r , filler_g , filler_b , filler_a ) ;
    so_called_common_engine_render_stateless :: set_texel_color ( shy_guts :: eraser , eraser_r , eraser_g , eraser_b , eraser_a ) ;
    
    so_called_message_common_engine_render_texture_set_texels_rect set_texels_msg ;
    set_texels_msg . texel = shy_guts :: eraser ;
    set_texels_msg . texture = shy_guts :: text_texture_id ;
    set_texels_msg . left = so_called_platform_math_consts :: whole_0 ;
    set_texels_msg . bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: sub_wholes ( set_texels_msg . right , texture_width , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( set_texels_msg . top , texture_height , so_called_platform_math_consts :: whole_1 ) ;
    so_called_sender_common_engine_render_texture_set_texels_rect :: send ( set_texels_msg ) ;
    
    shy_guts :: origin_y = texture_height ;
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
    so_called_type_platform_math_num_whole delta_x ;
    so_called_type_platform_math_num_whole texture_width ;
    so_called_type_platform_math_num_whole right_limit ;

    texture_width = so_called_common_engine_render_consts :: texture_width ;
    so_called_platform_math :: div_wholes ( delta_x , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_8 ) ;
    so_called_platform_math :: add_to_whole ( shy_guts :: origin_x , shy_guts :: letter_size_x ) ;
    so_called_platform_math :: add_to_whole ( shy_guts :: origin_x , delta_x ) ;
    so_called_platform_math :: sub_wholes ( right_limit , texture_width , shy_guts :: letter_size_x ) ;
    if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( shy_guts :: origin_x , right_limit ) )
    {
        so_called_type_platform_math_num_whole delta_y ;
        so_called_platform_math :: div_wholes ( delta_y , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
        so_called_platform_math :: sub_from_whole ( shy_guts :: origin_y , delta_y ) ;
        shy_guts :: next_letter_row ( ) ;
    }
}

void shy_guts :: next_letter_row ( )
{
    so_called_platform_math :: sub_from_whole ( shy_guts :: origin_y , shy_guts :: letter_size_y ) ;
    shy_guts :: origin_x = so_called_platform_math_consts :: whole_0 ;
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
    so_called_message_common_engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_sender_common_engine_render_mesh_set_triangle_strip_index_value :: send ( msg ) ;
}

void shy_guts :: store_tex_coords 
    ( so_called_type_common_logic_text_letter_id letter 
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
    so_called_type_platform_math_num_whole letter_id ;
    so_called_type_platform_math_num_whole whole_left ;
    so_called_type_platform_math_num_whole whole_bottom ;
    so_called_type_platform_math_num_whole whole_right ;
    so_called_type_platform_math_num_whole whole_top ;
    so_called_type_platform_math_num_whole whole_texture_width ;
    so_called_type_platform_math_num_whole whole_texture_height ;
    so_called_type_platform_math_num_fract fract_texture_width ;
    so_called_type_platform_math_num_fract fract_texture_height ;
    so_called_type_platform_pointer_data < shy_guts :: tex_coords > coords ;

    so_called_common_logic_text_stateless :: get_letter_id ( letter_id , letter ) ;
    so_called_platform_static_array :: element_ptr ( coords , letters_tex_coords , letter_id ) ;    
    
    whole_left = shy_guts :: origin_x ;
    whole_bottom = shy_guts :: origin_y ;
    so_called_platform_math :: add_wholes ( whole_right , shy_guts :: origin_x , shy_guts :: letter_size_x ) ;
    so_called_platform_math :: add_wholes ( whole_top , shy_guts :: origin_y , shy_guts :: letter_size_y ) ;
    whole_texture_width = so_called_common_engine_render_consts :: texture_width ;
    whole_texture_height = so_called_common_engine_render_consts :: texture_height ;
    so_called_platform_math :: make_fract_from_whole ( fract_texture_width , whole_texture_width ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_texture_height , whole_texture_height ) ;
    so_called_platform_math :: make_fract_from_whole ( coords . get ( ) . left , whole_left ) ;
    so_called_platform_math :: make_fract_from_whole ( coords . get ( ) . bottom , whole_bottom ) ;
    so_called_platform_math :: make_fract_from_whole ( coords . get ( ) . right , whole_right ) ;
    so_called_platform_math :: make_fract_from_whole ( coords . get ( ) . top , whole_top ) ;
    so_called_platform_math :: div_fract_by ( coords . get ( ) . left , fract_texture_width ) ;
    so_called_platform_math :: div_fract_by ( coords . get ( ) . bottom , fract_texture_height ) ;
    so_called_platform_math :: div_fract_by ( coords . get ( ) . right , fract_texture_width ) ;
    so_called_platform_math :: div_fract_by ( coords . get ( ) . top , fract_texture_height ) ;
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
    so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_sender_common_engine_render_mesh_set_vertex_tex_coord :: send ( msg ) ;
}

void shy_guts :: rasterize_english_alphabet 
    ( so_called_type_platform_math_num_whole letter_size_x
    , so_called_type_platform_math_num_whole letter_size_y
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
    typedef so_called_common_logic_text_consts :: alphabet_english eng ;
    shy_guts :: letter_size_x = letter_size_x ;
    shy_guts :: letter_size_y = letter_size_y ;
    shy_guts :: next_letter_row ( ) ;
    shy_guts :: rasterize_letter ( eng :: A , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: B , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: C , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: D , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: E , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: F , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: G , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: H , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: I , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: J , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: K , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: L , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: M , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: N , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: O , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: P , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: Q , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: R , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: S , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: T , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: U , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: V , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: W , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: X , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: Y , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: rasterize_letter ( eng :: Z , letters_tex_coords ) ; shy_guts :: next_letter_col ( ) ;
    shy_guts :: next_letter_row ( ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_sender_common_engine_render_mesh_set_vertex_position :: send ( msg ) ;
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
    so_called_message_common_engine_render_mesh_set_vertex_color msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_sender_common_engine_render_mesh_set_vertex_color :: send ( msg ) ;
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
