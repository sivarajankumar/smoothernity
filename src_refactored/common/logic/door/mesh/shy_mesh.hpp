namespace shy_guts
{
    namespace logic_door_mesh_consts
    {
        static const so_called_type_platform_math_num_whole mesh_vertices_count = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole mesh_triangle_strip_indices_count = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole mesh_triangle_fan_indices_count = so_called_platform_math :: init_num_whole ( 0 ) ;
    }

    namespace engine_render_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole finalized ;
        static so_called_type_common_engine_render_mesh_id mesh ;
    }

    namespace logic_door_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    static void proceed_with_creation ( ) ;
    static void request_mesh_create ( ) ;
    static void mesh_created ( ) ;
    static void fill_mesh_contents ( ) ;
    static void finalize_mesh ( ) ;
    static void reply_creation_finished ( ) ;
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

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: request_mesh_create ( )
{
}

void shy_guts :: mesh_created ( )
{
}

void shy_guts :: fill_mesh_contents ( )
{
}

void shy_guts :: finalize_mesh ( )
{
}

void shy_guts :: reply_creation_finished ( )
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

void _shy_common_logic_door_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_door_mesh :: receive ( so_called_message_common_logic_door_mesh_create )
{
    shy_guts :: logic_door_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;    
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_door_mesh :: receive ( so_called_message_common_logic_door_mesh_render_request )
{
}

void _shy_common_logic_door_mesh :: receive ( so_called_message_common_logic_door_mesh_set_transform )
{
}
