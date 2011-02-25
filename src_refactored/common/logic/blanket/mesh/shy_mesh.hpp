namespace shy_guts
{
    namespace logic_blanket_mesh_consts
    {
        static const so_called_type_platform_math_num_whole vertices = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole triangle_strip_indices = so_called_platform_math :: init_num_whole ( 4 ) ;
        static const so_called_type_platform_math_num_whole triangle_fan_indices = so_called_platform_math :: init_num_whole ( 0 ) ;
    }

    namespace logic_blanket_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace engine_render_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole finalized ;
        static so_called_type_common_engine_render_mesh_id mesh ;
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

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_mesh_create_state :: requested ) )
    {
        shy_guts :: logic_blanket_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_mesh_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: replied ) )
    {
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_created ( ) ;
    }
}

void shy_guts :: request_mesh_create ( )
{
    shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_message_common_engine_render_mesh_create_request msg ;
    msg . vertices = shy_guts :: logic_blanket_mesh_consts :: vertices ;
    msg . triangle_strip_indices = shy_guts :: logic_blanket_mesh_consts :: triangle_strip_indices ;
    msg . triangle_fan_indices = shy_guts :: logic_blanket_mesh_consts :: triangle_fan_indices ;
    so_called_sender_common_engine_render_mesh_create_request :: send ( msg ) ;
}

void shy_guts :: mesh_created ( )
{
    shy_guts :: fill_mesh_contents ( ) ;
    shy_guts :: finalize_mesh ( ) ;
    shy_guts :: reply_creation_finished ( ) ;
}

void shy_guts :: fill_mesh_contents ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract z ;
    so_called_type_platform_math_num_fract color_r ;
    so_called_type_platform_math_num_fract color_g ;
    so_called_type_platform_math_num_fract color_b ;
    so_called_type_platform_math_num_fract color_a ;
    so_called_type_platform_math_num_whole current_index ;

    x_left = so_called_common_logic_blanket_consts :: mesh_vertex_x_left ;
    x_right = so_called_common_logic_blanket_consts :: mesh_vertex_x_right ;
    y_bottom = so_called_common_logic_blanket_consts :: mesh_vertex_y_bottom ;
    y_top = so_called_common_logic_blanket_consts :: mesh_vertex_y_top ;
    z = so_called_common_logic_blanket_consts :: mesh_vertex_z ;
    color_r = so_called_common_logic_blanket_consts :: mesh_color_r ;
    color_g = so_called_common_logic_blanket_consts :: mesh_color_g ;
    color_b = so_called_common_logic_blanket_consts :: mesh_color_b ;
    color_a = so_called_common_logic_blanket_consts :: mesh_color_a ;

    current_index = so_called_platform_math_consts :: whole_0 ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
}

void shy_guts :: finalize_mesh ( )
{
    shy_guts :: engine_render_mesh_create_state :: finalized = so_called_platform_math_consts :: whole_true ;
    so_called_message_common_engine_render_mesh_finalize msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    so_called_sender_common_engine_render_mesh_finalize :: send ( msg ) ;
}

void shy_guts :: reply_creation_finished ( )
{
    so_called_sender_common_logic_blanket_mesh_creation_finished :: send ( so_called_message_common_logic_blanket_mesh_creation_finished ( ) ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index )
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

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: requested ) )
    {
        shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_mesh_create_state :: mesh = msg . mesh ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_create )
{
    shy_guts :: logic_blanket_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: finalized ) )
    {
        so_called_message_common_engine_render_mesh_render msg ;
        msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
        so_called_sender_common_engine_render_mesh_render :: send ( msg ) ;
    }
    so_called_sender_common_logic_blanket_mesh_render_reply :: send ( so_called_message_common_logic_blanket_mesh_render_reply ( ) ) ;
}

void _shy_common_logic_blanket_mesh :: receive ( so_called_message_common_logic_blanket_mesh_set_transform msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: finalized ) )
    {
        so_called_message_common_engine_render_mesh_set_transform transform_msg ;
        transform_msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
        transform_msg . transform = msg . transform ;
        so_called_sender_common_engine_render_mesh_set_transform :: send ( transform_msg ) ;
    }
}
