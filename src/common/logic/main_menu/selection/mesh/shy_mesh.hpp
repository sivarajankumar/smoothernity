namespace shy_guts
{
    static so_called_type_platform_math_num_whole animation_transform_requested ;
    static so_called_type_platform_math_num_whole creation_requested ;
    static so_called_type_common_engine_render_mesh_id mesh ;

    static void bake_mesh ( ) ;
    static void fill_mesh_content ( ) ;
    static void place_mesh ( ) ;
    static void finalize_mesh ( ) ;
    static void render_mesh ( ) ;
    static void destroy_mesh ( ) ;
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
    static void mesh_set_triangle_strip_index_value
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_whole index
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_selection_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: bake_mesh ( )
{
    shy_guts :: fill_mesh_content ( ) ;
    shy_guts :: finalize_mesh ( ) ;
    shy_guts :: place_mesh ( ) ;
}

void shy_guts :: fill_mesh_content ( )
{
    so_called_type_platform_math_num_fract half_size ;
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract u_left ;
    so_called_type_platform_math_num_fract u_right ;
    so_called_type_platform_math_num_fract v_bottom ;
    so_called_type_platform_math_num_fract v_top ;
    so_called_type_platform_math_num_fract z ;
    so_called_type_platform_math_num_fract color_r ;
    so_called_type_platform_math_num_fract color_g ;
    so_called_type_platform_math_num_fract color_b ;
    so_called_type_platform_math_num_fract color_a ;
    so_called_type_platform_math_num_whole index_left_top ;
    so_called_type_platform_math_num_whole index_left_bottom ;
    so_called_type_platform_math_num_whole index_right_top ;
    so_called_type_platform_math_num_whole index_right_bottom ;
    
    so_called_platform_math :: div_fracts ( half_size , so_called_common_logic_main_menu_selection_consts :: mesh_size , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: mul_fracts ( x_left , half_size , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( y_bottom , half_size , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( x_right , half_size , so_called_platform_math_consts :: fract_1 ) ;
    so_called_platform_math :: mul_fracts ( y_top , half_size , so_called_platform_math_consts :: fract_1 ) ;
    z = so_called_platform_math_consts :: fract_0 ;
    
    color_r = so_called_common_logic_main_menu_selection_consts :: mesh_color_r ;
    color_g = so_called_common_logic_main_menu_selection_consts :: mesh_color_g ;
    color_b = so_called_common_logic_main_menu_selection_consts :: mesh_color_b ;
    color_a = so_called_common_logic_main_menu_selection_consts :: mesh_color_a ;

    index_left_top = so_called_platform_math_consts :: whole_0 ;
    index_left_bottom = so_called_platform_math_consts :: whole_1 ;
    index_right_top = so_called_platform_math_consts :: whole_2 ;
    index_right_bottom = so_called_platform_math_consts :: whole_3 ;
    
    shy_guts :: mesh_set_triangle_strip_index_value ( index_left_top , index_left_top ) ;
    shy_guts :: mesh_set_vertex_color               ( index_left_top , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_position            ( index_left_top , x_left , y_top , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( index_left_bottom , index_left_bottom ) ;
    shy_guts :: mesh_set_vertex_color               ( index_left_bottom , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_position            ( index_left_bottom , x_left , y_bottom , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( index_right_top , index_right_top ) ;
    shy_guts :: mesh_set_vertex_color               ( index_right_top , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_position            ( index_right_top , x_right , y_top , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( index_right_bottom , index_right_bottom ) ;
    shy_guts :: mesh_set_vertex_color               ( index_right_bottom , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_position            ( index_right_bottom , x_right , y_bottom , z ) ;    
}

void shy_guts :: place_mesh ( )
{
    so_called_type_platform_matrix_data transform ;
    so_called_type_platform_math_num_fract origin_x ;
    so_called_type_platform_math_num_fract origin_y ;
    so_called_type_platform_math_num_fract origin_z ;
    
    origin_x = so_called_platform_math_consts :: fract_0 ;
    origin_y = so_called_platform_math_consts :: fract_0 ;
    origin_z = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_matrix :: identity ( transform ) ;
    so_called_platform_matrix :: set_origin ( transform , origin_x , origin_y , origin_z ) ;

    so_called_message_common_engine_render_mesh_set_transform msg ;
    msg . mesh = shy_guts :: mesh ;
    msg . transform = transform ;
    so_called_common_engine_render_mesh_set_transform_sender :: send ( msg ) ;
}

void shy_guts :: finalize_mesh ( )
{
    so_called_message_common_engine_render_mesh_finalize msg ;
    msg . mesh = shy_guts :: mesh ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( msg ) ;
}

void shy_guts :: render_mesh ( )
{
    so_called_common_engine_render_texture_unselect_sender :: send ( so_called_message_common_engine_render_texture_unselect ( ) ) ;

    so_called_message_common_engine_render_mesh_render msg ;
    msg . mesh = shy_guts :: mesh ;
    so_called_common_engine_render_mesh_render_sender :: send ( msg ) ;
}

void shy_guts :: destroy_mesh ( )
{
    so_called_message_common_engine_render_mesh_delete msg ;
    msg . mesh = shy_guts :: mesh ;
    so_called_common_engine_render_mesh_delete_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = shy_guts :: mesh ;
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
    msg . mesh = shy_guts :: mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( msg ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_message_common_engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = shy_guts :: mesh ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_init )
{
    shy_guts :: animation_transform_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: creation_requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: creation_requested ) )
    {
        shy_guts :: creation_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh = msg . mesh ;
        shy_guts :: bake_mesh ( ) ;
        so_called_common_logic_main_menu_selection_mesh_create_finished_sender :: send ( so_called_message_common_logic_main_menu_selection_mesh_create_finished ( ) ) ;
    }
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: animation_transform_requested ) )
    {
        shy_guts :: animation_transform_requested = so_called_platform_math_consts :: whole_false ;

        so_called_message_common_engine_render_mesh_set_transform transform_msg ;
        transform_msg . mesh = shy_guts :: mesh ;
        transform_msg . transform = msg . transform ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( transform_msg ) ;
    }
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_create )
{
    shy_guts :: creation_requested = so_called_platform_math_consts :: whole_true ;

    so_called_message_common_engine_render_mesh_create_request msg ;
    msg . vertices = so_called_platform_math_consts :: whole_4 ;
    msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
    msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
    so_called_common_engine_render_mesh_create_request_sender :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_destroy_request )
{
    shy_guts :: destroy_mesh ( ) ;
    so_called_common_logic_main_menu_selection_mesh_destroy_reply_sender :: send ( so_called_message_common_logic_main_menu_selection_mesh_destroy_reply ( ) ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_place )
{
    shy_guts :: animation_transform_requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_main_menu_selection_animation_transform_request_sender :: send ( so_called_message_common_logic_main_menu_selection_animation_transform_request ( ) ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_render_request )
{
    shy_guts :: render_mesh ( ) ;
    so_called_common_logic_main_menu_selection_mesh_render_reply_sender :: send ( so_called_message_common_logic_main_menu_selection_mesh_render_reply ( ) ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

