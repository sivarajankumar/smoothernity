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
}

void shy_guts :: fill_mesh_content ( )
{
}

void shy_guts :: place_mesh ( )
{
}

void shy_guts :: finalize_mesh ( )
{
}

void shy_guts :: render_mesh ( )
{
}

void shy_guts :: destroy_mesh ( )
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

void shy_guts :: mesh_set_vertex_color
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a
    )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index
    )
{
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: creation_requested ) )
    {
        shy_guts :: creation_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh = msg . mesh ;
        shy_guts :: bake_mesh ( ) ;
        so_called_sender_common_logic_main_menu_selection_mesh_create_finished :: send ( so_called_message_common_logic_main_menu_selection_mesh_create_finished ( ) ) ;
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
        so_called_sender_common_engine_render_mesh_set_transform :: send ( transform_msg ) ;
    }
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_create )
{
    shy_guts :: creation_requested = so_called_platform_math_consts :: whole_true ;

    so_called_message_common_engine_render_mesh_create_request msg ;
    msg . vertices = so_called_platform_math_consts :: whole_4 ;
    msg . triangle_strip_indices = so_called_platform_math_consts :: whole_4 ;
    msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
    so_called_sender_common_engine_render_mesh_create_request :: send ( msg ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_destroy_request )
{
    shy_guts :: destroy_mesh ( ) ;
    so_called_sender_common_logic_main_menu_selection_mesh_destroy_reply :: send ( so_called_message_common_logic_main_menu_selection_mesh_destroy_reply ( ) ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_place )
{
    shy_guts :: animation_transform_requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_main_menu_selection_animation_transform_request :: send ( so_called_message_common_logic_main_menu_selection_animation_transform_request ( ) ) ;
}

void _shy_common_logic_main_menu_selection_mesh :: receive ( so_called_message_common_logic_main_menu_selection_mesh_render_request )
{
    shy_guts :: render_mesh ( ) ;
    so_called_sender_common_logic_main_menu_selection_mesh_render_reply :: send ( so_called_message_common_logic_main_menu_selection_mesh_render_reply ( ) ) ;
}
