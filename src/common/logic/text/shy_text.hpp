namespace shy_guts
{
    namespace consts
    {
        static so_called_platform_math_const_int_32_type max_letters_in_alphabet = 32 ;

        static const so_called_platform_math_num_fract_type final_scale = so_called_platform_math :: init_num_fract ( 1 , 2 ) ;
        static const so_called_platform_math_num_fract_type canvas_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type canvas_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type canvas_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type canvas_a = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_platform_math_num_fract_type mesh_x = so_called_platform_math :: init_num_fract ( - 1 , 2 ) ;
        static const so_called_platform_math_num_fract_type mesh_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_platform_math_num_fract_type mesh_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
        static const so_called_platform_math_num_whole_type scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static const so_called_platform_math_num_whole_type small_size = so_called_platform_math :: init_num_whole ( 16 ) ;
        static const so_called_platform_math_num_whole_type big_size = so_called_platform_math :: init_num_whole ( 32 ) ;
    }

    class tex_coords
    {
    public :
        so_called_platform_math_num_fract_type left ;
        so_called_platform_math_num_fract_type bottom ;
        so_called_platform_math_num_fract_type right ;
        so_called_platform_math_num_fract_type top ;
    } ;

    typedef so_called_platform_static_array_data_type < shy_guts :: tex_coords , shy_guts :: consts :: max_letters_in_alphabet > letters_tex_coords ;

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
        ( so_called_platform_render_texel_data_type texel 
        ) ;
    static void mesh_set_triangle_strip_index_value
        ( so_called_platform_math_num_whole_type offset
        , so_called_platform_math_num_whole_type index
        ) ;
    static void store_tex_coords 
        ( so_called_common_logic_text_letter_id_type letter 
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void rasterize_letter 
        ( so_called_common_logic_text_letter_id_type letter 
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_platform_math_num_whole_type offset
        , so_called_platform_math_num_fract_type u
        , so_called_platform_math_num_fract_type v 
        ) ;
    static void rasterize_english_alphabet 
        ( so_called_platform_math_num_whole_type letter_size_x
        , so_called_platform_math_num_whole_type letter_size_y
        , shy_guts :: letters_tex_coords & letters_tex_coords 
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_platform_math_num_whole_type offset
        , so_called_platform_math_num_fract_type x
        , so_called_platform_math_num_fract_type y
        , so_called_platform_math_num_fract_type z 
        ) ;
    static void rasterize_rect 
        ( so_called_platform_math_num_whole_type x1
        , so_called_platform_math_num_whole_type y1
        , so_called_platform_math_num_whole_type x2
        , so_called_platform_math_num_whole_type y2
        ) ;
    static void rasterize_ellipse_in_rect 
        ( so_called_platform_math_num_whole_type x1
        , so_called_platform_math_num_whole_type y1
        , so_called_platform_math_num_whole_type x2
        , so_called_platform_math_num_whole_type y2
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_platform_math_num_whole_type offset 
        , so_called_platform_math_num_fract_type r
        , so_called_platform_math_num_fract_type g
        , so_called_platform_math_num_fract_type b
        , so_called_platform_math_num_fract_type a
        ) ;
    static void rasterize_triangle 
        ( so_called_platform_math_num_whole_type x1 
        , so_called_platform_math_num_whole_type y1
        , so_called_platform_math_num_whole_type x2
        , so_called_platform_math_num_whole_type y2 
        , so_called_platform_math_num_whole_type x3
        , so_called_platform_math_num_whole_type y3
        ) ;

    static so_called_platform_math_num_whole_type texture_create_requested ;
    static so_called_platform_math_num_whole_type texture_create_replied ;
    
    static so_called_platform_math_num_whole_type mesh_create_requested ;
    static so_called_platform_math_num_whole_type mesh_create_replied ;
    
    static so_called_platform_math_num_whole_type rasterize_finalize_requested ;
    static so_called_platform_math_num_whole_type rasterize_finalize_replied ;
    
    static so_called_platform_math_num_whole_type empty_texture_created ;
    static so_called_platform_math_num_whole_type small_letters_rasterized ;
    static so_called_platform_math_num_whole_type big_letters_rasterized ;
        
    static so_called_platform_math_num_whole_type text_mesh_created ;
    static so_called_platform_math_num_whole_type text_prepare_permitted ;
    static so_called_common_engine_render_mesh_id_type text_mesh_id ;
    static so_called_common_engine_render_texture_id_type text_texture_id ;
    static so_called_platform_render_texel_data_type filler ;
    static so_called_platform_render_texel_data_type eraser ;
    static so_called_platform_math_num_whole_type origin_x ;
    static so_called_platform_math_num_whole_type origin_y ;
    static so_called_platform_math_num_whole_type letter_size_x ;
    static so_called_platform_math_num_whole_type letter_size_y ;
    static so_called_platform_math_num_whole_type scale_frames ;
    static shy_guts :: letters_tex_coords letters_big ;
    static shy_guts :: letters_tex_coords letters_small ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_text_mesh ( )
{
    so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_sender :: send ( so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_message ( ) ) ;
    {
        so_called_common_engine_render_texture_select_message texture_select_msg ;
        texture_select_msg . texture = shy_guts :: text_texture_id ;
        so_called_common_engine_render_texture_select_sender :: send ( texture_select_msg ) ;
    }
    {
        so_called_common_engine_render_mesh_render_message mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: text_mesh_id ;
        so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
    }
    so_called_common_engine_render_blend_disable_sender :: send ( so_called_common_engine_render_blend_disable_message ( ) ) ;
}

void shy_guts :: update_text_mesh ( )
{
    so_called_platform_matrix_data_type matrix ;
    so_called_platform_math_num_fract_type fract_scale_frames ;    
    so_called_platform_math_num_fract_type fract_scale_in_frames ;
    so_called_platform_math_num_fract_type scale ;
    
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
        so_called_common_engine_render_mesh_set_transform_message mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: text_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;
    }
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: scale_frames , shy_guts :: consts :: scale_in_frames ) )
        so_called_platform_math :: inc_whole ( shy_guts :: scale_frames ) ;
}

void shy_guts :: create_text_mesh ( )
{
    so_called_platform_math_num_fract_type x_left ;
    so_called_platform_math_num_fract_type x_right ;
    so_called_platform_math_num_fract_type y_top ;
    so_called_platform_math_num_fract_type y_bottom ;
    so_called_platform_math_num_fract_type u_left ;
    so_called_platform_math_num_fract_type u_right ;
    so_called_platform_math_num_fract_type v_top ;
    so_called_platform_math_num_fract_type v_bottom ;
    so_called_platform_math_num_fract_type z ;
    so_called_platform_math_num_fract_type color_r ;
    so_called_platform_math_num_fract_type color_g ;
    so_called_platform_math_num_fract_type color_b ;
    so_called_platform_math_num_fract_type color_a ;

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

    so_called_common_engine_render_mesh_finalize_message mesh_finalize_msg ;
    mesh_finalize_msg . mesh = shy_guts :: text_mesh_id ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
}

void shy_guts :: create_text_texture ( )
{
    so_called_platform_math_num_whole_type texture_width ;
    so_called_platform_math_num_whole_type texture_height ;
    so_called_platform_math_num_fract_type filler_r ;
    so_called_platform_math_num_fract_type filler_g ;
    so_called_platform_math_num_fract_type filler_b ;
    so_called_platform_math_num_fract_type filler_a ;
    so_called_platform_math_num_fract_type eraser_r ;
    so_called_platform_math_num_fract_type eraser_g ;
    so_called_platform_math_num_fract_type eraser_b ;
    so_called_platform_math_num_fract_type eraser_a ;

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
    
    so_called_common_engine_render_texture_set_texels_rect_message set_texels_msg ;
    set_texels_msg . texel = shy_guts :: eraser ;
    set_texels_msg . texture = shy_guts :: text_texture_id ;
    set_texels_msg . left = so_called_platform_math_consts :: whole_0 ;
    set_texels_msg . bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: sub_wholes ( set_texels_msg . right , texture_width , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( set_texels_msg . top , texture_height , so_called_platform_math_consts :: whole_1 ) ;
    so_called_common_engine_render_texture_set_texels_rect_sender :: send ( set_texels_msg ) ;
    
    shy_guts :: origin_y = texture_height ;
}

void shy_guts :: proceed_with_create_text ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_prepare_permitted ) )
    {
        shy_guts :: text_prepare_permitted = so_called_platform_math_consts :: whole_false ;
        
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_engine_render_texture_create_request_sender :: send ( so_called_common_engine_render_texture_create_request_message ( ) ) ;
        
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        so_called_common_engine_render_mesh_create_request_message mesh_create_msg ;
        mesh_create_msg . vertices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
        mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
        so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;
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
        so_called_common_engine_rasterizer_finalize_request_sender :: send ( so_called_common_engine_rasterizer_finalize_request_message ( ) ) ;
    }
    else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: rasterize_finalize_replied ) )
    {
        shy_guts :: rasterize_finalize_replied = so_called_platform_math_consts :: whole_false ;
        
        so_called_common_engine_render_texture_finalize_message texture_finalize_msg ;
        texture_finalize_msg . texture = shy_guts :: text_texture_id ;
        so_called_common_engine_render_texture_finalize_sender :: send ( texture_finalize_msg ) ;
        
        shy_guts :: text_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_common_logic_text_prepared_sender :: send ( so_called_common_logic_text_prepared_message ( ) ) ;
    }
}

void shy_guts :: prepare_rasterizer_for_drawing ( )
{
    so_called_common_engine_rasterizer_use_texture_message rasterize_use_texture_msg ;
    rasterize_use_texture_msg . texture = shy_guts :: text_texture_id ;
    rasterize_use_texture_msg . origin_x = shy_guts :: origin_x ;
    rasterize_use_texture_msg . origin_y = shy_guts :: origin_y ;
    so_called_common_engine_rasterizer_use_texture_sender :: send ( rasterize_use_texture_msg ) ;
}

void shy_guts :: next_letter_col ( )
{
    so_called_platform_math_num_whole_type delta_x ;
    so_called_platform_math_num_whole_type texture_width ;
    so_called_platform_math_num_whole_type right_limit ;

    texture_width = so_called_common_engine_render_consts :: texture_width ;
    so_called_platform_math :: div_wholes ( delta_x , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_8 ) ;
    so_called_platform_math :: add_to_whole ( shy_guts :: origin_x , shy_guts :: letter_size_x ) ;
    so_called_platform_math :: add_to_whole ( shy_guts :: origin_x , delta_x ) ;
    so_called_platform_math :: sub_wholes ( right_limit , texture_width , shy_guts :: letter_size_x ) ;
    if ( so_called_platform_conditions :: whole_greater_or_equal_to_whole ( shy_guts :: origin_x , right_limit ) )
    {
        so_called_platform_math_num_whole_type delta_y ;
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
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type outer_top ;
    so_called_platform_math_num_whole_type outer_bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math_num_whole_type outer_center ;
    so_called_platform_math_num_whole_type outer_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math_num_whole_type outer_right ;
    so_called_platform_math :: sub_wholes ( outer_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: div_wholes ( outer_center , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: sub_wholes ( outer_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( outer_center , outer_top , outer_left , outer_bottom , outer_right , outer_bottom ) ;

    so_called_platform_math_num_whole_type inner_top ;
    so_called_platform_math_num_whole_type inner_bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math_num_whole_type inner_center ;
    so_called_platform_math_num_whole_type inner_left ;
    so_called_platform_math_num_whole_type inner_right ;
    so_called_platform_math :: mul_wholes ( inner_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( inner_top , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_wholes ( inner_center , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_wholes ( inner_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( inner_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( inner_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_triangle ( inner_center , inner_top , inner_left , inner_bottom , inner_right , inner_bottom ) ;

    so_called_platform_math_num_whole_type board_top ;
    so_called_platform_math_num_whole_type board_bottom ;    
    so_called_platform_math_num_whole_type outer_left_minus_center ;
    so_called_platform_math_num_whole_type outer_right_minus_center ;
    so_called_platform_math_num_whole_type outer_top_minus_board_top ;
    so_called_platform_math_num_whole_type outer_top_minus_board_bottom ;
    so_called_platform_math_num_whole_type outer_top_minus_bottom ;
    so_called_platform_math_num_whole_type board_top_left ;
    so_called_platform_math_num_whole_type board_bottom_left ;
    so_called_platform_math_num_whole_type board_top_right ;
    so_called_platform_math_num_whole_type board_bottom_right ;
    so_called_platform_math :: mul_wholes ( board_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( board_top , so_called_platform_math_consts :: whole_7 ) ;
    so_called_platform_math :: mul_wholes ( board_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( board_bottom , so_called_platform_math_consts :: whole_7 ) ;
    so_called_platform_math :: sub_wholes ( outer_left_minus_center , outer_left , outer_center ) ;
    so_called_platform_math :: sub_wholes ( outer_right_minus_center , outer_right , outer_center ) ;
    so_called_platform_math :: sub_wholes ( outer_top_minus_board_top , outer_top , board_top ) ;
    so_called_platform_math :: sub_wholes ( outer_top_minus_board_bottom , outer_top , board_bottom ) ;
    so_called_platform_math :: sub_wholes ( outer_top_minus_bottom , outer_top , outer_bottom ) ;    
    so_called_platform_math :: mul_wholes ( board_top_left , outer_left_minus_center , outer_top_minus_board_top ) ;
    so_called_platform_math :: div_whole_by ( board_top_left , outer_top_minus_bottom ) ;
    so_called_platform_math :: add_to_whole ( board_top_left , outer_center ) ;
    so_called_platform_math :: mul_wholes ( board_bottom_left , outer_left_minus_center , outer_top_minus_board_bottom ) ;
    so_called_platform_math :: div_whole_by ( board_bottom_left , outer_top_minus_bottom ) ;
    so_called_platform_math :: add_to_whole ( board_bottom_left , outer_center ) ;
    so_called_platform_math :: mul_wholes ( board_top_right , outer_right_minus_center , outer_top_minus_board_top ) ;
    so_called_platform_math :: div_whole_by ( board_top_right , outer_top_minus_bottom ) ;
    so_called_platform_math :: add_to_whole ( board_top_right , outer_center ) ;
    so_called_platform_math :: mul_wholes ( board_bottom_right , outer_right_minus_center , outer_top_minus_board_bottom ) ;
    so_called_platform_math :: div_whole_by ( board_bottom_right , outer_top_minus_bottom ) ;
    so_called_platform_math :: add_to_whole ( board_bottom_right , outer_center ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( board_top_left , board_top , board_bottom_left , board_bottom , board_bottom_right , board_bottom ) ;
    shy_guts :: rasterize_triangle ( board_top_left , board_top , board_top_right , board_top , board_bottom_right , board_bottom ) ;
}

void shy_guts :: rasterize_font_english_B ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type ellipse_y_top ;
    so_called_platform_math_num_whole_type ellipse_y_mid ;
    so_called_platform_math_num_whole_type ellipse_x_right ;
    so_called_platform_math :: sub_wholes ( ellipse_y_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: div_wholes ( ellipse_y_mid , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: sub_wholes ( ellipse_x_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , ellipse_x_right , ellipse_y_mid ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , ellipse_y_mid , ellipse_x_right , ellipse_y_top ) ;

    so_called_platform_math_num_whole_type spine_right ;
    so_called_platform_math_num_whole_type spine_top ;
    so_called_platform_math :: div_wholes ( spine_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: sub_wholes ( spine_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , spine_top , spine_right , so_called_platform_math_consts :: whole_0 ) ;
    
    so_called_platform_math_num_whole_type hole_divider ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_height ;
    so_called_platform_math_num_whole_type hole_top_minus_height ;
    so_called_platform_math_num_whole_type hole_bottom_plus_height ;
    so_called_platform_math :: make_num_whole ( hole_divider , 16 ) ;
    so_called_platform_math :: mul_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_left , hole_divider ) ;
    so_called_platform_math :: make_num_whole ( hole_right , 12 ) ;
    so_called_platform_math :: mul_whole_by ( hole_right , shy_guts :: letter_size_x ) ;
    so_called_platform_math :: div_whole_by ( hole_right , hole_divider ) ;
    so_called_platform_math :: make_num_whole ( hole_top , 13 ) ;
    so_called_platform_math :: mul_whole_by ( hole_top , shy_guts :: letter_size_y ) ;
    so_called_platform_math :: div_whole_by ( hole_top , hole_divider ) ;
    so_called_platform_math :: mul_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_bottom , hole_divider ) ;
    so_called_platform_math :: mul_wholes ( hole_height , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_height , hole_divider ) ;
    so_called_platform_math :: sub_wholes ( hole_top_minus_height , hole_top , hole_height ) ;
    so_called_platform_math :: add_wholes ( hole_bottom_plus_height , hole_bottom , hole_height ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_top_minus_height ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_bottom , hole_right , hole_bottom_plus_height ) ;
    
    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_top , hole_center_x , hole_top_minus_height ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_bottom , hole_center_x , hole_bottom_plus_height ) ;    
}

void shy_guts :: rasterize_font_english_C ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math_num_whole_type hole_center_top ;
    so_called_platform_math_num_whole_type hole_center_bottom ;
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: mul_wholes ( hole_center_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_whole_by ( hole_center_top , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_center_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_center_bottom , so_called_platform_math_consts :: whole_7 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
}

void shy_guts :: rasterize_font_english_D ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;

    so_called_platform_math_num_whole_type half_size_x ;
    so_called_platform_math :: div_wholes ( half_size_x , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , half_size_x , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_top , hole_center_x , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_E ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_mid_top ;
    so_called_platform_math_num_whole_type hole_mid_bottom ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( hole_mid_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_top , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( hole_mid_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_F ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_mid_top ;
    so_called_platform_math_num_whole_type hole_mid_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: sub_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_bottom , so_called_platform_math_consts :: whole_5 ) ;        
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_mid_bottom , hole_right , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_G ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math_num_whole_type hole_center_top ;
    so_called_platform_math_num_whole_type hole_center_bottom ;
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: mul_wholes ( hole_center_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_whole_by ( hole_center_top , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_center_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_center_bottom , so_called_platform_math_consts :: whole_7 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
    
    so_called_platform_math_num_whole_type brick_top ;
    so_called_platform_math_num_whole_type brick_bottom ;
    so_called_platform_math_num_whole_type brick_left ;
    so_called_platform_math_num_whole_type brick_right ;
    so_called_platform_math :: mul_wholes ( brick_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( brick_top , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( brick_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( brick_bottom , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( brick_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( brick_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( brick_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( brick_left , brick_top , brick_right , brick_bottom ) ;
}

void shy_guts :: rasterize_font_english_H ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;        
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_mid_top ;
    so_called_platform_math_num_whole_type hole_mid_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , top_limit , hole_right , hole_mid_top ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_mid_bottom , hole_right , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_I ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_6 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_7 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_mid_left ;
    so_called_platform_math_num_whole_type hole_mid_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math :: mul_wholes ( hole_mid_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_left , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_right , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , hole_top , hole_mid_left , hole_bottom ) ;
    shy_guts :: rasterize_rect ( hole_mid_right , hole_top , right , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_J ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math_num_whole_type circle_top ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( circle_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( circle_top , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , circle_top ) ;

    so_called_platform_math_num_whole_type circle_center_y ;
    so_called_platform_math :: div_wholes ( circle_center_y , circle_top , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , circle_center_y , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    so_called_platform_math_num_whole_type hole_center_y ;
    so_called_platform_math :: add_wholes ( hole_center_y , hole_top , hole_bottom ) ;
    so_called_platform_math :: div_whole_by ( hole_center_y , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , circle_top , hole_right , hole_center_y ) ;
    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , top_limit , hole_left , hole_center_y ) ;
}

void shy_guts :: rasterize_font_english_K ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math_num_whole_type half_size_y ;    
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: div_wholes ( half_size_y , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;

    so_called_platform_math_num_whole_type hole_1_left ;
    so_called_platform_math :: mul_wholes ( hole_1_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_1_left , so_called_platform_math_consts :: whole_9 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_triangle ( hole_1_left , half_size_y , right_limit , top_limit , right_limit , so_called_platform_math_consts :: whole_0 ) ;

    so_called_platform_math_num_whole_type hole_2_right ;
    so_called_platform_math :: mul_wholes ( hole_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_6 ) ;
    so_called_platform_math :: div_whole_by ( hole_2_right , so_called_platform_math_consts :: whole_9 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_triangle ( so_called_platform_math_consts :: whole_0 , top_limit , hole_2_right , top_limit , so_called_platform_math_consts :: whole_0 , half_size_y ) ;

    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_triangle ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , hole_2_right , so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , half_size_y ) ;

    so_called_platform_math_num_whole_type spine_right ;
    so_called_platform_math :: div_wholes ( spine_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , spine_right , top_limit ) ;
}

void shy_guts :: rasterize_font_english_L ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , top_limit , right , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_M ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type spine_1_right ;
    so_called_platform_math_num_whole_type spine_2_left ;
    so_called_platform_math_num_whole_type spine_2_right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( spine_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( spine_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( spine_2_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( spine_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( spine_2_right , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , spine_1_right , top_limit ) ;
    shy_guts :: rasterize_rect ( spine_2_left , so_called_platform_math_consts :: whole_0 , spine_2_right , top_limit ) ;

    so_called_platform_math_num_whole_type board_height ;
    so_called_platform_math_num_whole_type board_center_x ;
    so_called_platform_math_num_whole_type top_minus_board_height ;
    so_called_platform_math :: mul_wholes ( board_height , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( board_height , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( board_center_x , spine_2_right , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: sub_wholes ( top_minus_board_height , shy_guts :: letter_size_y , board_height ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( spine_1_right , top_limit , board_center_x , board_height , board_center_x , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , board_center_x , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( board_center_x , board_height , spine_2_left , top_limit , spine_2_left , top_minus_board_height ) ;
    shy_guts :: rasterize_triangle ( board_center_x , board_height , board_center_x , so_called_platform_math_consts :: whole_0 , spine_2_left , top_minus_board_height ) ;
}

void shy_guts :: rasterize_font_english_N ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type spine_1_right ;
    so_called_platform_math_num_whole_type spine_2_left ;
    so_called_platform_math_num_whole_type spine_2_right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( spine_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( spine_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( spine_2_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( spine_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( spine_2_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , spine_1_right , top_limit ) ;
    shy_guts :: rasterize_rect ( spine_2_left , so_called_platform_math_consts :: whole_0 , spine_2_right , top_limit ) ;
    
    so_called_platform_math_num_whole_type board_height ;
    so_called_platform_math_num_whole_type top_minus_board_height ;
    so_called_platform_math :: div_wholes ( board_height , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;    
    so_called_platform_math :: sub_wholes ( top_minus_board_height , shy_guts :: letter_size_y , board_height ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( spine_1_right , top_limit , spine_2_left , board_height , spine_2_left , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , spine_2_left , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_O ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_P ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type spine_right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( spine_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , spine_right , top_limit ) ;
    
    so_called_platform_math_num_whole_type ellipse_left ;
    so_called_platform_math_num_whole_type ellipse_right ;
    so_called_platform_math_num_whole_type ellipse_bottom ;
    so_called_platform_math :: div_wholes ( ellipse_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: sub_wholes ( ellipse_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( ellipse_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( ellipse_bottom , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( ellipse_left , top_limit , ellipse_right , ellipse_bottom ) ;
    
    so_called_platform_math_num_whole_type ellipse_center_x ;
    so_called_platform_math :: add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    so_called_platform_math :: div_whole_by ( ellipse_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( spine_right , top_limit , ellipse_center_x , ellipse_bottom ) ;

    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math :: mul_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_left , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    shy_guts :: rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_Q ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right_limit ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( right_limit , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right_limit , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    so_called_platform_math_num_whole_type board_width ;
    so_called_platform_math_num_whole_type board_left ;
    so_called_platform_math_num_whole_type board_top ;
    so_called_platform_math_num_whole_type right_minus_board_width ;
    so_called_platform_math_num_whole_type left_plus_board_width ;
    so_called_platform_math :: div_wholes ( board_width , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( board_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: mul_wholes ( board_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( board_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( right_minus_board_width , shy_guts :: letter_size_x , board_width ) ;
    so_called_platform_math :: add_wholes ( left_plus_board_width , board_left , board_width ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( board_left , board_top , right_minus_board_width , so_called_platform_math_consts :: whole_0 , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( board_left , board_top , left_plus_board_width , board_top , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_R ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type spine_right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( spine_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , spine_right , top_limit ) ;
    
    so_called_platform_math_num_whole_type ellipse_left ;
    so_called_platform_math_num_whole_type ellipse_right ;
    so_called_platform_math_num_whole_type ellipse_top ;
    so_called_platform_math_num_whole_type ellipse_bottom ;
    so_called_platform_math :: div_wholes ( ellipse_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: sub_wholes ( ellipse_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: sub_wholes ( ellipse_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( ellipse_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( ellipse_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;
    
    so_called_platform_math_num_whole_type ellipse_center_x ;
    so_called_platform_math :: add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    so_called_platform_math :: div_whole_by ( ellipse_center_x , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( spine_right , ellipse_top , ellipse_center_x , ellipse_bottom ) ;

    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math_num_whole_type hole_center_x ;
    so_called_platform_math :: mul_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_left , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    so_called_platform_math :: div_whole_by ( hole_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    shy_guts :: rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;

    so_called_platform_math_num_whole_type board_width ;
    so_called_platform_math_num_whole_type right_minus_board_width ;
    so_called_platform_math_num_whole_type spine_plus_board_width ;
    so_called_platform_math :: mul_wholes ( board_width , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( board_width , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: sub_wholes ( right_minus_board_width , shy_guts :: letter_size_x , board_width ) ;    
    so_called_platform_math :: add_wholes ( spine_plus_board_width , spine_right , board_width ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( spine_right , ellipse_bottom , right_minus_board_width , so_called_platform_math_consts :: whole_0 , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( spine_right , ellipse_bottom , spine_plus_board_width , ellipse_bottom , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_S ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type circle_high_left ;
    so_called_platform_math_num_whole_type circle_high_right ;
    so_called_platform_math_num_whole_type circle_high_top ;
    so_called_platform_math_num_whole_type circle_high_bottom ;
    circle_high_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( circle_high_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: sub_wholes ( circle_high_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( circle_high_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( circle_high_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( circle_high_left , circle_high_top , circle_high_right , circle_high_bottom ) ;
    
    so_called_platform_math_num_whole_type circle_low_left ;
    so_called_platform_math_num_whole_type circle_low_right ;
    so_called_platform_math_num_whole_type circle_low_top ;
    so_called_platform_math_num_whole_type circle_low_bottom ;
    so_called_platform_math :: div_wholes ( circle_low_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;    
    so_called_platform_math :: sub_wholes ( circle_low_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( circle_low_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( circle_low_top , so_called_platform_math_consts :: whole_5 ) ;    
    circle_low_bottom = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_ellipse_in_rect ( circle_low_left , circle_low_top , circle_low_right , circle_low_bottom ) ;

    so_called_platform_math_num_whole_type board_mid_left ;
    so_called_platform_math_num_whole_type board_mid_right ;
    so_called_platform_math_num_whole_type board_mid_top ;
    so_called_platform_math_num_whole_type board_mid_bottom ;
    so_called_platform_math :: div_wholes ( board_mid_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: mul_wholes ( board_mid_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( board_mid_right , so_called_platform_math_consts :: whole_4 ) ;    
    board_mid_top = circle_low_top ;
    board_mid_bottom = circle_high_bottom ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( board_mid_left , board_mid_top , board_mid_right , board_mid_bottom ) ;
    
    so_called_platform_math_num_whole_type board_high_left ;
    so_called_platform_math_num_whole_type board_high_right ;
    so_called_platform_math_num_whole_type board_high_top ;
    so_called_platform_math_num_whole_type board_high_bottom ;
    board_high_left = board_mid_left ;    
    so_called_platform_math :: mul_wholes ( board_high_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_8 ) ;
    so_called_platform_math :: div_whole_by ( board_high_right , so_called_platform_math_consts :: whole_9 ) ;
    so_called_platform_math :: sub_wholes ( board_high_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( board_high_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( board_high_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( board_high_left , board_high_top , board_high_right , board_high_bottom ) ;
    
    so_called_platform_math_num_whole_type board_low_left ;
    so_called_platform_math_num_whole_type board_low_right ;
    so_called_platform_math_num_whole_type board_low_top ;
    so_called_platform_math_num_whole_type board_low_bottom ;
    so_called_platform_math :: div_wholes ( board_low_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_9 ) ;    
    board_low_right = board_mid_right ;
    so_called_platform_math :: div_wholes ( board_low_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    board_low_bottom = so_called_platform_math_consts :: whole_0 ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( board_low_left , board_low_top , board_low_right , board_low_bottom ) ;
        
    so_called_platform_math_num_whole_type hole_high_left ;
    so_called_platform_math_num_whole_type hole_high_right ;
    so_called_platform_math_num_whole_type hole_high_top ;
    so_called_platform_math_num_whole_type hole_high_bottom ;
    so_called_platform_math :: div_wholes ( hole_high_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: div_wholes ( hole_high_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;    
    so_called_platform_math :: sub_wholes ( hole_high_top , board_high_bottom , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: add_wholes ( hole_high_bottom , board_mid_top , so_called_platform_math_consts :: whole_1 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_high_left , hole_high_top , hole_high_right , hole_high_bottom ) ;

    so_called_platform_math_num_whole_type hole_low_left ;
    so_called_platform_math_num_whole_type hole_low_right ;
    so_called_platform_math_num_whole_type hole_low_top ;
    so_called_platform_math_num_whole_type hole_low_bottom ;
    so_called_platform_math :: mul_wholes ( hole_low_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_low_left , so_called_platform_math_consts :: whole_3 ) ;    
    so_called_platform_math :: mul_wholes ( hole_low_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: div_whole_by ( hole_low_right , so_called_platform_math_consts :: whole_6 ) ;    
    so_called_platform_math :: sub_wholes ( hole_low_top , board_mid_bottom , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: add_wholes ( hole_low_bottom , board_low_top , so_called_platform_math_consts :: whole_1 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_low_left , hole_low_top , hole_low_right , hole_low_bottom ) ;
    
    so_called_platform_math_num_whole_type hole_high_center_x ;
    so_called_platform_math :: add_wholes ( hole_high_center_x , hole_high_left , hole_high_right ) ;
    so_called_platform_math :: div_whole_by ( hole_high_center_x , so_called_platform_math_consts :: whole_2 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_high_center_x , hole_high_top , circle_high_right , hole_high_bottom ) ;
    
    so_called_platform_math_num_whole_type hole_low_center_x ;
    so_called_platform_math :: add_wholes ( hole_low_center_x , hole_low_left , hole_low_right ) ;
    so_called_platform_math :: div_whole_by ( hole_low_center_x , so_called_platform_math_consts :: whole_2 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( circle_low_left , hole_low_top , hole_low_center_x , hole_low_bottom ) ;    
}

void shy_guts :: rasterize_font_english_T ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: mul_wholes ( right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_6 ) ;
    so_called_platform_math :: div_whole_by ( right , so_called_platform_math_consts :: whole_7 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( so_called_platform_math_consts :: whole_0 , so_called_platform_math_consts :: whole_0 , right , top_limit ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_mid_left ;
    so_called_platform_math_num_whole_type hole_mid_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    hole_left = so_called_platform_math_consts :: whole_0 ;
    hole_right = right ;    
    so_called_platform_math :: mul_wholes ( hole_mid_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_left , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_mid_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_mid_right , so_called_platform_math_consts :: whole_7 ) ;    
    so_called_platform_math :: mul_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hole_top , so_called_platform_math_consts :: whole_5 ) ;    
    hole_bottom = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_rect ( hole_left , hole_top , hole_mid_left , hole_bottom ) ;
    shy_guts :: rasterize_rect ( hole_mid_right , hole_top , hole_right , hole_bottom ) ;
}

void shy_guts :: rasterize_font_english_U ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type ellipse_left ;
    so_called_platform_math_num_whole_type ellipse_right ;
    so_called_platform_math_num_whole_type ellipse_top ;
    so_called_platform_math_num_whole_type ellipse_bottom ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    ellipse_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: mul_wholes ( ellipse_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( ellipse_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: div_wholes ( ellipse_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;    
    ellipse_bottom = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;    
    
    so_called_platform_math_num_whole_type ellipse_center_y ;
    so_called_platform_math :: div_wholes ( ellipse_center_y , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( ellipse_left , top_limit , ellipse_right , ellipse_center_y ) ;
    
    so_called_platform_math_num_whole_type hole_left ;
    so_called_platform_math_num_whole_type hole_right ;
    so_called_platform_math_num_whole_type hole_top ;
    so_called_platform_math_num_whole_type hole_bottom ;
    so_called_platform_math :: div_wholes ( hole_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: add_to_whole ( hole_left , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( hole_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( hole_right , so_called_platform_math_consts :: whole_5 ) ;
    so_called_platform_math :: sub_from_whole ( hole_right , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( hole_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: sub_from_whole ( hole_top , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( hole_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_6 ) ;
    so_called_platform_math :: add_to_whole ( hole_bottom , so_called_platform_math_consts :: whole_1 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: eraser ) ;
    shy_guts :: rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    shy_guts :: rasterize_rect ( hole_left , top_limit , hole_right , ellipse_center_y ) ;
}

void shy_guts :: rasterize_font_english_V ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type top_limit ;
    so_called_platform_math_num_whole_type high_1_left ;
    so_called_platform_math_num_whole_type high_1_right ;
    so_called_platform_math_num_whole_type high_2_left ;
    so_called_platform_math_num_whole_type high_2_right ;
    so_called_platform_math_num_whole_type low_left ;
    so_called_platform_math_num_whole_type low_right ;
    so_called_platform_math :: sub_wholes ( top_limit , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;
    high_1_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( high_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( high_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( high_2_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( high_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( low_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( low_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( low_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( low_right , so_called_platform_math_consts :: whole_5 ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( high_1_left , top_limit , high_1_right , top_limit , low_right , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( high_1_left , top_limit , low_left , so_called_platform_math_consts :: whole_0 , low_right , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( high_2_left , top_limit , high_2_right , top_limit , low_right , so_called_platform_math_consts :: whole_0 ) ;
    shy_guts :: rasterize_triangle ( high_2_left , top_limit , low_left , so_called_platform_math_consts :: whole_0 , low_right , so_called_platform_math_consts :: whole_0 ) ;
}

void shy_guts :: rasterize_font_english_W ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type high_1_left ;
    so_called_platform_math_num_whole_type high_1_right ;
    so_called_platform_math_num_whole_type high_2_left ;
    so_called_platform_math_num_whole_type high_2_right ;
    so_called_platform_math_num_whole_type high_3_left ;
    so_called_platform_math_num_whole_type high_3_right ;
    so_called_platform_math_num_whole_type low_1_left ;
    so_called_platform_math_num_whole_type low_1_right ;
    so_called_platform_math_num_whole_type low_2_left ;
    so_called_platform_math_num_whole_type low_2_right ;
    so_called_platform_math_num_whole_type high_top ;
    so_called_platform_math_num_whole_type low_bottom ;
    high_1_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( high_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( high_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( high_2_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( high_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( high_2_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( high_3_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( high_3_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( high_3_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: div_wholes ( low_1_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( low_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( low_1_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( low_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( low_2_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( low_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( low_2_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( high_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    low_bottom = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_1_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_1_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_1_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_2_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_3_left , high_top , high_3_right , high_top , low_2_right , low_bottom ) ;
    shy_guts :: rasterize_triangle ( high_3_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
}

void shy_guts :: rasterize_font_english_X ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type left_1 ;
    so_called_platform_math_num_whole_type right_1 ;
    so_called_platform_math_num_whole_type left_2 ;
    so_called_platform_math_num_whole_type right_2 ;
    so_called_platform_math_num_whole_type top_y ;
    so_called_platform_math_num_whole_type bottom_y ;
    left_1 = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( right_1 , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: mul_wholes ( left_2 , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( left_2 , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: sub_wholes ( right_2 , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: sub_wholes ( top_y , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    bottom_y = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( left_1 , top_y , right_1 , top_y , right_2 , bottom_y ) ;
    shy_guts :: rasterize_triangle ( left_1 , top_y , left_2 , bottom_y , right_2 , bottom_y ) ;
    shy_guts :: rasterize_triangle ( left_2 , top_y , right_2 , top_y , right_1 , bottom_y ) ;
    shy_guts :: rasterize_triangle ( left_2 , top_y , left_1 , bottom_y , right_1 , bottom_y ) ;
}

void shy_guts :: rasterize_font_english_Y ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;

    so_called_platform_math_num_whole_type high_1_left ;
    so_called_platform_math_num_whole_type high_1_right ;
    so_called_platform_math_num_whole_type high_2_left ;
    so_called_platform_math_num_whole_type high_2_right ;
    so_called_platform_math_num_whole_type high_top ;
    so_called_platform_math_num_whole_type low_left ;
    so_called_platform_math_num_whole_type low_right ;
    so_called_platform_math_num_whole_type low_bottom ;
    so_called_platform_math_num_whole_type mid_y ;
    high_1_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( high_1_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: mul_wholes ( high_2_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( high_2_left , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: sub_wholes ( high_2_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: sub_wholes ( high_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( low_left , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( low_left , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: mul_wholes ( low_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_3 ) ;
    so_called_platform_math :: div_whole_by ( low_right , so_called_platform_math_consts :: whole_5 ) ;    
    low_bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: div_wholes ( mid_y , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_2 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_right , mid_y ) ;
    shy_guts :: rasterize_triangle ( high_1_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_right , mid_y ) ;
    shy_guts :: rasterize_triangle ( high_2_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    shy_guts :: rasterize_rect ( low_left , mid_y , low_right , low_bottom ) ;
}

void shy_guts :: rasterize_font_english_Z ( )
{
    shy_guts :: prepare_rasterizer_for_drawing ( ) ;
    
    so_called_platform_math_num_whole_type hor_left ;
    so_called_platform_math_num_whole_type hor_right ;
    so_called_platform_math_num_whole_type high_top ;
    so_called_platform_math_num_whole_type high_bottom ;
    hor_left = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: mul_wholes ( hor_right , shy_guts :: letter_size_x , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( hor_right , so_called_platform_math_consts :: whole_5 ) ;    
    so_called_platform_math :: sub_wholes ( high_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_1 ) ;    
    so_called_platform_math :: mul_wholes ( high_bottom , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;
    so_called_platform_math :: div_whole_by ( high_bottom , so_called_platform_math_consts :: whole_5 ) ;    
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( hor_left , high_top , hor_right , high_bottom ) ;
    
    so_called_platform_math_num_whole_type low_top ;
    so_called_platform_math_num_whole_type low_bottom ;
    so_called_platform_math :: div_wholes ( low_top , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_5 ) ;    
    low_bottom = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_rect ( hor_left , low_top , hor_right , low_bottom ) ;
    
    so_called_platform_math_num_whole_type board_width ;
    so_called_platform_math_num_whole_type right_minus_board_width ;
    so_called_platform_math :: div_wholes ( board_width , shy_guts :: letter_size_y , so_called_platform_math_consts :: whole_4 ) ;    
    so_called_platform_math :: sub_wholes ( right_minus_board_width , hor_right , board_width ) ;
    shy_guts :: rasterize_use_texel ( shy_guts :: filler ) ;
    shy_guts :: rasterize_triangle ( right_minus_board_width , high_bottom , hor_right , high_bottom , board_width , low_top ) ;
    shy_guts :: rasterize_triangle ( right_minus_board_width , high_bottom , hor_left , low_top , board_width , low_top ) ;
}

void shy_guts :: rasterize_use_texel ( so_called_platform_render_texel_data_type texel )
{
    so_called_common_engine_rasterizer_use_texel_message rasterize_use_texel_msg ;
    rasterize_use_texel_msg . texel = texel ;
    so_called_common_engine_rasterizer_use_texel_sender :: send ( rasterize_use_texel_msg ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_whole_type index
    )
{
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

void shy_guts :: store_tex_coords 
    ( so_called_common_logic_text_letter_id_type letter 
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
    so_called_platform_math_num_whole_type letter_id ;
    so_called_platform_math_num_whole_type whole_left ;
    so_called_platform_math_num_whole_type whole_bottom ;
    so_called_platform_math_num_whole_type whole_right ;
    so_called_platform_math_num_whole_type whole_top ;
    so_called_platform_math_num_whole_type whole_texture_width ;
    so_called_platform_math_num_whole_type whole_texture_height ;
    so_called_platform_math_num_fract_type fract_texture_width ;
    so_called_platform_math_num_fract_type fract_texture_height ;
    so_called_platform_pointer_data_type < shy_guts :: tex_coords > coords ;

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
    ( so_called_common_logic_text_letter_id_type letter 
    , shy_guts :: letters_tex_coords & letters_tex_coords 
    )
{
    so_called_platform_math_num_whole_type match ;

    typedef so_called_common_logic_text_consts :: alphabet_english eng ;

    shy_guts :: store_tex_coords ( letter , letters_tex_coords ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: A ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_A ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: B ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_B ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: C ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_C ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: D ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_D ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: E ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_E ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: F ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_F ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: G ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_G ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: H ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_H ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: I ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_I ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: J ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_J ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: K ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_K ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: L ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_L ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: M ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_M ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: N ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_N ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: O ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_O ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: P ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_P ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: Q ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_Q ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: R ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_R ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: S ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_S ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: T ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_T ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: U ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_U ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: V ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_V ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: W ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_W ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: X ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_X ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: Y ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_Y ( ) ;
    so_called_common_logic_text_stateless :: are_letters_equal ( match , letter , eng :: Z ) ; if ( so_called_platform_conditions :: whole_is_true ( match ) ) shy_guts :: rasterize_font_english_Z ( ) ;
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type u
    , so_called_platform_math_num_fract_type v 
    )
{
    so_called_common_engine_render_mesh_set_vertex_tex_coord_message msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( msg ) ;
}

void shy_guts :: rasterize_english_alphabet 
    ( so_called_platform_math_num_whole_type letter_size_x
    , so_called_platform_math_num_whole_type letter_size_y
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
    ( so_called_platform_math_num_whole_type offset
    , so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z 
    )
{
    so_called_common_engine_render_mesh_set_vertex_position_message msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( msg ) ;
}

void shy_guts :: rasterize_rect 
    ( so_called_platform_math_num_whole_type x1
    , so_called_platform_math_num_whole_type y1
    , so_called_platform_math_num_whole_type x2
    , so_called_platform_math_num_whole_type y2
    )
{
    so_called_common_engine_rasterizer_draw_rect_message rasterize_rect_msg ;
    rasterize_rect_msg . x1 = x1 ;
    rasterize_rect_msg . y1 = y1 ;
    rasterize_rect_msg . x2 = x2 ;
    rasterize_rect_msg . y2 = y2 ;
    so_called_common_engine_rasterizer_draw_rect_sender :: send ( rasterize_rect_msg ) ;
}

void shy_guts :: rasterize_ellipse_in_rect 
    ( so_called_platform_math_num_whole_type x1
    , so_called_platform_math_num_whole_type y1
    , so_called_platform_math_num_whole_type x2
    , so_called_platform_math_num_whole_type y2
    )
{
    so_called_common_engine_rasterizer_draw_ellipse_in_rect_message rasterize_ellipse_in_rect_msg ;
    rasterize_ellipse_in_rect_msg . x1 = x1 ;
    rasterize_ellipse_in_rect_msg . y1 = y1 ;
    rasterize_ellipse_in_rect_msg . x2 = x2 ;
    rasterize_ellipse_in_rect_msg . y2 = y2 ;
    so_called_common_engine_rasterizer_draw_ellipse_in_rect_sender :: send ( rasterize_ellipse_in_rect_msg ) ;
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_platform_math_num_whole_type offset 
    , so_called_platform_math_num_fract_type r
    , so_called_platform_math_num_fract_type g
    , so_called_platform_math_num_fract_type b
    , so_called_platform_math_num_fract_type a
    )
{
    so_called_common_engine_render_mesh_set_vertex_color_message msg ;
    msg . mesh = shy_guts :: text_mesh_id ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( msg ) ;
}

void shy_guts :: rasterize_triangle 
    ( so_called_platform_math_num_whole_type x1 
    , so_called_platform_math_num_whole_type y1
    , so_called_platform_math_num_whole_type x2
    , so_called_platform_math_num_whole_type y2 
    , so_called_platform_math_num_whole_type x3
    , so_called_platform_math_num_whole_type y3
    )
{
    so_called_common_engine_rasterizer_draw_triangle_message rasterize_triangle_msg ;
    rasterize_triangle_msg . x1 = x1 ;
    rasterize_triangle_msg . y1 = y1 ;
    rasterize_triangle_msg . x2 = x2 ;
    rasterize_triangle_msg . y2 = y2 ;
    rasterize_triangle_msg . x3 = x3 ;
    rasterize_triangle_msg . y3 = y3 ;
    so_called_common_engine_rasterizer_draw_triangle_sender :: send ( rasterize_triangle_msg ) ;
}

void _shy_common_logic_text :: receive ( so_called_common_engine_rasterizer_finalize_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: rasterize_finalize_requested ) )
    {
        shy_guts :: rasterize_finalize_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: rasterize_finalize_replied = so_called_platform_math_consts :: whole_true ;
    }
}

void _shy_common_logic_text :: receive ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_mesh_id = msg . mesh ;
        shy_guts :: proceed_with_create_text ( ) ;
    }
}

void _shy_common_logic_text :: receive ( so_called_common_engine_render_texture_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: text_texture_id = msg . texture ;
        shy_guts :: proceed_with_create_text ( ) ;
    }
}

void _shy_common_logic_text :: receive ( so_called_common_init_message )
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

void _shy_common_logic_text :: receive ( so_called_common_logic_text_letter_big_tex_coords_request_message msg )
{
    so_called_common_logic_text_letter_big_tex_coords_reply_message reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: tex_coords > coords ;
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
    so_called_common_logic_text_letter_big_tex_coords_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_text :: receive ( so_called_common_logic_text_letter_small_tex_coords_request_message msg )
{
    so_called_common_logic_text_letter_small_tex_coords_reply_message reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: tex_coords > coords ;
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
    so_called_common_logic_text_letter_small_tex_coords_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_text :: receive ( so_called_common_logic_text_prepare_permit_message )
{
    shy_guts :: text_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_text :: receive ( so_called_common_logic_text_render_request_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
        shy_guts :: render_text_mesh ( ) ;
    so_called_common_logic_text_render_reply_sender :: send ( so_called_common_logic_text_render_reply_message ( ) ) ;
}

void _shy_common_logic_text :: receive ( so_called_common_logic_text_update_message )
{
    if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: text_mesh_created ) )
        shy_guts :: proceed_with_create_text ( ) ;    
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
        shy_guts :: update_text_mesh ( ) ;
}

void _shy_common_logic_text :: receive ( so_called_common_logic_text_use_text_texture_request_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: text_mesh_created ) )
    {
        so_called_common_engine_render_texture_select_message texture_select_msg ;
        texture_select_msg . texture = shy_guts :: text_texture_id ;
        so_called_common_engine_render_texture_select_sender :: send ( texture_select_msg ) ;
    }
    so_called_common_logic_text_use_text_texture_reply_sender :: send ( so_called_common_logic_text_use_text_texture_reply_message ( ) ) ;
}

void _shy_common_logic_text :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

