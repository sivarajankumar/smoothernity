namespace shy_guts
{
    namespace logic_main_menu_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }
    
    namespace logic_main_menu_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_matrix_data view ;
    }

    namespace logic_ortho_planes_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_fract x_left ;
        static so_called_type_platform_math_num_fract x_right ;
        static so_called_type_platform_math_num_fract y_bottom ;
        static so_called_type_platform_math_num_fract y_top ;
        static so_called_type_platform_math_num_fract z_near ;
        static so_called_type_platform_math_num_fract z_far ;
    }

    namespace logic_fidget_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }
    
    namespace logic_text_use_text_texture_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }
    
    namespace logic_main_menu_letters_meshes_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }
    
    namespace logic_main_menu_selection_mesh_render_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static so_called_type_platform_math_num_whole permitted ;

    static void proceed_with_render ( ) ;
    static void render_started ( ) ;
    static void prepare_render_state ( ) ;
    static void restore_render_state ( ) ;
    static void clear_screen ( ) ;
    static void blue_screen ( ) ;
    static void request_ortho_planes ( ) ;
    static void request_animation_transform ( ) ;
    static void request_fidget_render ( ) ;
    static void animation_transform_received ( ) ;
    static void apply_animation_transform ( ) ;
    static void select_text_texture ( ) ;
    static void render_selection_mesh ( ) ;
    static void render_letters_meshes ( ) ;
    static void render_finished ( ) ;
    static void use_ortho_projection ( ) ;
}
    
typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_renderer > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_render ( )
{
}

void shy_guts :: render_started ( )
{
}

void shy_guts :: prepare_render_state ( )
{
}

void shy_guts :: restore_render_state ( )
{
}

void shy_guts :: clear_screen ( )
{
}

void shy_guts :: blue_screen ( )
{
}

void shy_guts :: request_ortho_planes ( )
{
}

void shy_guts :: request_animation_transform ( )
{
}

void shy_guts :: request_fidget_render ( )
{
}

void shy_guts :: animation_transform_received ( )
{
}

void shy_guts :: apply_animation_transform ( )
{
}

void shy_guts :: select_text_texture ( )
{
}

void shy_guts :: render_selection_mesh ( )
{
}

void shy_guts :: render_letters_meshes ( )
{
}

void shy_guts :: render_finished ( )
{
}

void shy_guts :: use_ortho_projection ( )
{
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_fidget_render_reply )
{
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_main_menu_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_main_menu_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_main_menu_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_main_menu_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_main_menu_animation_transform_state :: view = msg . view ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_main_menu_letters_meshes_render_reply )
{
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_main_menu_render )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: permitted ) )
    {
        shy_guts :: logic_main_menu_render_state :: requested = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_render ( ) ;
    }
    else
        shy_guts :: blue_screen ( ) ;
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_main_menu_render_permit )
{
    shy_guts :: permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_main_menu_selection_mesh_render_reply )
{
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_ortho_planes_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_ortho_planes_state :: requested ) )
    {
        shy_guts :: logic_ortho_planes_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_ortho_planes_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_ortho_planes_state :: x_left = msg . x_left ;
        shy_guts :: logic_ortho_planes_state :: x_right = msg . x_right ;
        shy_guts :: logic_ortho_planes_state :: y_bottom = msg . y_bottom ;
        shy_guts :: logic_ortho_planes_state :: y_top = msg . y_top ;
        shy_guts :: logic_ortho_planes_state :: z_near = msg . z_near ;
        shy_guts :: logic_ortho_planes_state :: z_far = msg . z_far ;
        shy_guts :: proceed_with_render ( ) ;
    }
}

void _shy_common_logic_main_menu_renderer :: receive ( so_called_message_common_logic_text_use_text_texture_reply )
{
}
