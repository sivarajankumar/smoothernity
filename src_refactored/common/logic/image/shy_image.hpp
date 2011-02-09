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
}

void shy_guts :: update_image_mesh ( )
{
}

void shy_guts :: create_image_mesh ( )
{
}

void shy_guts :: create_image_texture ( )
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

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_texture_create_reply )
{
}

void _shy_common_logic_image :: receive ( so_called_message_common_engine_render_texture_loader_ready_reply )
{
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
}

void _shy_common_logic_image :: receive ( so_called_message_common_logic_image_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: image_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: image_texture_loaded ) )
        shy_guts :: render_image_mesh ( ) ;
    so_called_sender_common_logic_image_render_reply :: send ( so_called_message_common_logic_image_render_reply ( ) ) ;
}

void _shy_common_logic_image :: receive ( so_called_message_common_logic_image_update )
{
}
