namespace shy_guts
{
    namespace logic_main_menu_letters_rows_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole rows ;
    }
    
    namespace logic_main_menu_letters_cols_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole cols ;
    }

    namespace logic_main_menu_letter_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_row ;
        static so_called_type_platform_math_num_whole requested_col ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_logic_text_letter_id letter ;
    }

    namespace engine_render_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_render_mesh_id mesh ;
    }
    
    namespace logic_text_letter_big_tex_coords_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_common_logic_text_letter_id requested_letter ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract bottom ;
        static so_called_type_platform_math_num_fract left ;
        static so_called_type_platform_math_num_fract top ;
        static so_called_type_platform_math_num_fract right ;
    }

    static so_called_type_platform_math_num_whole first_mesh ;
    static so_called_type_platform_math_num_whole current_row ;
    static so_called_type_platform_math_num_whole current_col ;

    static void proceed_with_creation ( ) ;
    static void obtain_rows_count ( ) ;
    static void start_first_row ( ) ;
    static void start_first_col ( ) ;
    static void move_to_next_row ( ) ;
    static void move_to_next_col ( ) ;
    static void letter_state_received ( ) ;
    static void create_mesh ( ) ;
    static void obtain_tex_coords ( ) ;
    static void letter_tex_coords_received ( ) ;
    static void fill_mesh_content ( ) ;
    static void send_mesh_created_notification ( ) ;
    static void mesh_set_vertex_position 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract x
        , so_called_type_platform_math_num_fract y
        , so_called_type_platform_math_num_fract z 
        ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract u
        , so_called_type_platform_math_num_fract v 
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a 
        ) ;
    static void mesh_set_triangle_strip_index_value
        ( so_called_type_common_engine_render_mesh_id mesh
        , so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_whole index 
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: obtain_rows_count ( )
{
}

void shy_guts :: start_first_row ( )
{
}

void shy_guts :: start_first_col ( )
{
}

void shy_guts :: move_to_next_row ( )
{
}

void shy_guts :: move_to_next_col ( )
{
}

void shy_guts :: letter_state_received ( )
{
}

void shy_guts :: create_mesh ( )
{
}

void shy_guts :: obtain_tex_coords ( )
{
}

void shy_guts :: letter_tex_coords_received ( )
{
}

void shy_guts :: fill_mesh_content ( )
{
}

void shy_guts :: send_mesh_created_notification ( )
{
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z 
    )
{
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v 
    )
{
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a 
    )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index 
    )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_init )
{
    shy_guts :: current_row = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: current_col = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: first_mesh = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_logic_main_menu_letters_cols_reply )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_logic_main_menu_letters_letter_reply )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_create_next )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_logic_main_menu_letters_rows_reply )
{
}

void _shy_common_logic_main_menu_letters_meshes_creator :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_reply )
{
}
