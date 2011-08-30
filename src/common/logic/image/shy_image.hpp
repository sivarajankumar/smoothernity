namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static const so_called_type_platform_math_num_whole logo_resource_index = so_called_platform_math :: init_num_whole ( 1 ) ;
        static const so_called_type_platform_math_num_fract final_scale = so_called_platform_math :: init_num_fract ( 1 , 2 ) ;
        static const so_called_type_platform_math_num_fract image_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract image_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract image_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract image_a = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract mesh_x = so_called_platform_math :: init_num_fract ( 1 , 2 ) ;
        static const so_called_type_platform_math_num_fract mesh_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract mesh_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
    }

    static void render_image_mesh ( ) ;
    static void update_image_mesh ( ) ;
    static void create_image_mesh ( ) ;
    static void create_image_texture ( ) ;
    static void mesh_set_triangle_strip_index_value 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_whole index
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract u
        , so_called_type_platform_math_num_fract v
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract x
        , so_called_type_platform_math_num_fract y
        , so_called_type_platform_math_num_fract z
        ) ;
    static void mesh_set_vertex_color
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a 
        ) ;

    static so_called_type_platform_math_num_whole image_mesh_created ;
    static so_called_type_platform_math_num_whole image_texture_created ;
    static so_called_type_platform_math_num_whole image_texture_loaded ;
    static so_called_type_platform_math_num_whole image_prepare_permitted ;
    static so_called_type_platform_math_num_whole texture_create_requested ;
    static so_called_type_platform_math_num_whole texture_loader_ready_requested ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_platform_math_num_whole scale_frames ;
    static so_called_type_common_engine_render_mesh_id image_mesh_id ;
    static so_called_type_common_engine_render_texture_id image_texture_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_image > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_image_mesh ( )
{
    so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_sender :: send ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    {
        so_called_message_common_engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = shy_guts :: image_texture_id ;
        so_called_common_engine_render_texture_select_sender :: send ( texture_select_msg ) ;
    }
    {
        so_called_message_common_engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: image_mesh_id ;
        so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
    }
    so_called_common_engine_render_blend_disable_sender :: send ( so_called_message_common_engine_render_blend_disable ( ) ) ;
}

void shy_guts :: update_image_mesh ( )
{
    so_called_type_platform_matrix_data matrix ;
    so_called_type_platform_math_num_fract scale ;
    so_called_type_platform_math_num_fract fract_scale_frames ;
    so_called_type_platform_math_num_fract fract_scale_in_frames ;

    so_called_platform_math :: make_fract_from_whole ( fract_scale_in_frames , shy_guts :: consts :: scale_in_frames ) ;
    so_called_platform_math :: make_fract_from_whole ( fract_scale_frames , shy_guts :: scale_frames ) ;
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
        mesh_set_transform_msg . mesh = shy_guts :: image_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;
    }
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: scale_frames , shy_guts :: consts :: scale_in_frames ) )
        so_called_platform_math :: inc_whole ( shy_guts :: scale_frames ) ;
}

void shy_guts :: create_image_mesh ( )
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
    so_called_type_platform_math_num_whole index ;
    
    x_left = so_called_platform_math_consts :: fract_minus_1 ;
    x_right = so_called_platform_math_consts :: fract_1 ;
    y_top = so_called_platform_math_consts :: fract_1 ;
    y_bottom = so_called_platform_math_consts :: fract_minus_1 ;
    u_left = so_called_platform_math_consts :: fract_0 ;
    u_right = so_called_platform_math_consts :: fract_1 ;
    v_top = so_called_platform_math_consts :: fract_1 ;
    v_bottom = so_called_platform_math_consts :: fract_0 ;
    z = so_called_platform_math_consts :: fract_0 ;
    color_r = shy_guts :: consts :: image_r ;
    color_g = shy_guts :: consts :: image_g ;
    color_b = shy_guts :: consts :: image_b ;
    color_a = shy_guts :: consts :: image_a ;

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
    mesh_finalize_msg . mesh = shy_guts :: image_mesh_id ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
}

void shy_guts :: create_image_texture ( )
{
    so_called_type_platform_render_texture_loader_resource_id logo_resource_id ;
    so_called_common_engine_render_stateless :: create_texture_resource_id ( logo_resource_id , shy_guts :: consts :: logo_resource_index ) ;
    {
        so_called_message_common_engine_render_texture_load_from_resource texture_load_from_resource_msg ;
        texture_load_from_resource_msg . texture = shy_guts :: image_texture_id ;
        texture_load_from_resource_msg . resource = logo_resource_id ;
        so_called_common_engine_render_texture_load_from_resource_sender :: send ( texture_load_from_resource_msg ) ;
    }
}

void shy_guts :: mesh_set_triangle_strip_index_value 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_message_common_engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = shy_guts :: image_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = shy_guts :: image_mesh_id ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = shy_guts :: image_mesh_id ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( msg ) ;
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
    msg . mesh = shy_guts :: image_mesh_id ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( msg ) ;
}

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: image_mesh_id = msg . mesh ;
        shy_guts :: create_image_mesh ( ) ;
        shy_guts :: image_mesh_created = so_called_platform_math_consts :: whole_true ;
    }
}

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: image_texture_created = so_called_platform_math_consts :: whole_true ;
        shy_guts :: image_texture_id = msg . texture ;
        shy_guts :: create_image_texture ( ) ;
    }
}

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_texture_loader_ready_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_loader_ready_requested ) )
    {
        shy_guts :: texture_loader_ready_requested = so_called_platform_math_consts :: whole_false ;
        if ( so_called_platform_conditions :: whole_is_true ( msg . ready ) )
        {
            {
                so_called_message_common_engine_render_texture_finalize texture_finalize_msg ;
                texture_finalize_msg . texture = shy_guts :: image_texture_id ;
                so_called_common_engine_render_texture_finalize_sender :: send ( texture_finalize_msg ) ;
            }
            shy_guts :: image_texture_loaded = so_called_platform_math_consts :: whole_true ;
            so_called_common_logic_image_prepared_sender :: send ( so_called_message_common_logic_image_prepared ( ) ) ;
        }
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: image_texture_loaded ) )
            shy_guts :: update_image_mesh ( ) ;
    }
}

void _shy_common_logic_image :: receive ( so_called_message_common_init )
{
    shy_guts :: image_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: image_texture_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: image_texture_loaded = so_called_platform_math_consts :: whole_false ;
    shy_guts :: image_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_loader_ready_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: scale_frames = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_image :: receive ( so_called_message_common_logic_image_prepare_permit )
{
    shy_guts :: image_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_image :: receive ( so_called_message_common_logic_image_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: image_texture_loaded ) )
        shy_guts :: render_image_mesh ( ) ;
    so_called_common_logic_image_render_reply_sender :: send ( so_called_message_common_logic_image_render_reply ( ) ) ;
}

void _shy_common_logic_image :: receive ( so_called_message_common_logic_image_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: image_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
            
            so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = so_called_platform_math_consts :: whole_4 ;
            mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
            mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;        
        }
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: image_texture_created ) )
        {
            shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
            so_called_common_engine_render_texture_create_request_sender :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
        }
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_texture_created ) 
          && so_called_platform_conditions :: whole_is_false ( shy_guts :: image_texture_loaded )
           )
        {
            shy_guts :: texture_loader_ready_requested = so_called_platform_math_consts :: whole_true ;
            so_called_common_engine_render_texture_loader_ready_request_sender :: send ( so_called_message_common_engine_render_texture_loader_ready_request ( ) ) ;
        }
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: image_texture_loaded ) )
        shy_guts :: update_image_mesh ( ) ;
}

void _shy_common_logic_image :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

