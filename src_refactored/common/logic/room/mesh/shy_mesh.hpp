namespace shy_guts
{
    namespace logic_room_mesh_consts
    {
        static const so_called_type_platform_math_num_whole vertices_count = so_called_platform_math :: init_num_whole ( 27 ) ;
        static const so_called_type_platform_math_num_whole triangle_strip_indices_count = so_called_platform_math :: init_num_whole ( 27 ) ;
    }

    namespace logic_room_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole current_index ;
    }

    namespace engine_render_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole finalized ;
        static so_called_type_common_engine_render_mesh_id mesh ;
    }

    static void proceed_with_creation ( ) ;
    static void request_mesh_creation ( ) ;
    static void mesh_created ( ) ;
    static void fill_mesh_contents ( ) ;
    static void transform_mesh ( ) ;
    static void reply_mesh_creation_finished ( ) ;
    static void add_cube_sides ( ) ;
    static void add_near_side ( ) ;
    static void add_far_side ( ) ;
    static void add_left_side ( ) ;
    static void add_right_side ( ) ;
    static void add_top_side ( ) ;
    static void add_bottom_side ( ) ;
    static void finalize_mesh ( ) ;
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
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: request_mesh_creation ( )
{
}

void shy_guts :: mesh_created ( )
{
}

void shy_guts :: fill_mesh_contents ( )
{
}

void shy_guts :: transform_mesh ( )
{
}

void shy_guts :: reply_mesh_creation_finished ( )
{
}

void shy_guts :: add_cube_sides ( )
{
}

void shy_guts :: add_near_side ( )
{
}

void shy_guts :: add_far_side ( )
{
}

void shy_guts :: add_left_side ( )
{
}

void shy_guts :: add_right_side ( )
{
}

void shy_guts :: add_top_side ( )
{
}

void shy_guts :: add_bottom_side ( )
{
}

void shy_guts :: finalize_mesh ( )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value 
    ( so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_whole index 
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

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_logic_room_mesh_create )
{
}

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_logic_room_mesh_render_request )
{
}
