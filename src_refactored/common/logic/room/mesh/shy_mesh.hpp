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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_create_state :: requested ) )
    {
        shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_mesh_creation ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: replied ) )
    {
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: mesh_created ( ) ;
    }
}

void shy_guts :: request_mesh_creation ( )
{
    shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_message_common_engine_render_mesh_create_request msg ;
    msg . vertices = shy_guts :: logic_room_mesh_consts :: vertices_count ;
    msg . triangle_strip_indices = shy_guts :: logic_room_mesh_consts :: triangle_strip_indices_count ;
    msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
    so_called_sender_common_engine_render_mesh_create_request :: send ( msg ) ;
}

void shy_guts :: mesh_created ( )
{
    shy_guts :: fill_mesh_contents ( ) ;
    shy_guts :: transform_mesh ( ) ;
    shy_guts :: reply_mesh_creation_finished ( ) ;
}

void shy_guts :: fill_mesh_contents ( )
{
    shy_guts :: add_cube_sides ( ) ;
    shy_guts :: finalize_mesh ( ) ;
}

void shy_guts :: transform_mesh ( )
{
    so_called_type_platform_math_num_fract position_x ;
    so_called_type_platform_math_num_fract position_y ;
    so_called_type_platform_math_num_fract position_z ;
    so_called_type_platform_matrix_data transform ;

    position_x = so_called_common_logic_room_consts :: mesh_position_x ;
    position_y = so_called_common_logic_room_consts :: mesh_position_y ;
    position_z = so_called_common_logic_room_consts :: mesh_position_z ;

    so_called_platform_matrix :: identity ( transform ) ;
    so_called_platform_matrix :: set_origin ( transform , position_x , position_y , position_z ) ;

    so_called_message_common_engine_render_mesh_set_transform msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    msg . transform = transform ;
    so_called_sender_common_engine_render_mesh_set_transform :: send ( msg ) ;
}

void shy_guts :: reply_mesh_creation_finished ( )
{
    so_called_sender_common_logic_room_mesh_creation_finished :: send ( so_called_message_common_logic_room_mesh_creation_finished ( ) ) ;
}

void shy_guts :: add_cube_sides ( )
{
    shy_guts :: logic_room_mesh_create_state :: current_index = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: add_near_side ( ) ;
    shy_guts :: add_right_side ( ) ;
    shy_guts :: add_far_side ( ) ;
    shy_guts :: add_left_side ( ) ;
    shy_guts :: add_top_side ( ) ;
    shy_guts :: add_bottom_side ( ) ;
}

void shy_guts :: add_near_side ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract near_side_u_left ;
    so_called_type_platform_math_num_fract near_side_u_right ;
    so_called_type_platform_math_num_fract near_side_v_top ;
    so_called_type_platform_math_num_fract near_side_v_bottom ;
    so_called_type_platform_math_num_fract z_near ;
    so_called_type_platform_math_num_fract color_near_r ;
    so_called_type_platform_math_num_fract color_near_g ;
    so_called_type_platform_math_num_fract color_near_b ;
    so_called_type_platform_math_num_fract color_near_a ; 
    so_called_type_platform_math_num_whole current_index ;
    
    x_left = so_called_common_logic_room_consts :: mesh_x_left ;
    x_right = so_called_common_logic_room_consts :: mesh_x_right ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    near_side_u_left = so_called_common_logic_room_consts :: mesh_near_side_u_left ;
    near_side_u_right = so_called_common_logic_room_consts :: mesh_near_side_u_right ;
    near_side_v_top = so_called_common_logic_room_consts :: mesh_near_side_v_top ;
    near_side_v_bottom = so_called_common_logic_room_consts :: mesh_near_side_v_bottom ;
    z_near = so_called_common_logic_room_consts :: mesh_z_near ;

    color_near_r = so_called_common_logic_room_consts :: mesh_color_near_r ;
    color_near_g = so_called_common_logic_room_consts :: mesh_color_near_g ;
    color_near_b = so_called_common_logic_room_consts :: mesh_color_near_b ;
    color_near_a = so_called_common_logic_room_consts :: mesh_color_near_a ;

    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , near_side_u_left , near_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , near_side_u_left , near_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , near_side_u_right , near_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_near_r , color_near_g , color_near_b , color_near_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , near_side_u_right , near_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: add_far_side ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract far_side_u_left ;
    so_called_type_platform_math_num_fract far_side_u_right ;
    so_called_type_platform_math_num_fract far_side_v_top ;
    so_called_type_platform_math_num_fract far_side_v_bottom ;
    so_called_type_platform_math_num_fract z_far ;
    so_called_type_platform_math_num_fract color_far_r ;
    so_called_type_platform_math_num_fract color_far_g ;
    so_called_type_platform_math_num_fract color_far_b ;
    so_called_type_platform_math_num_fract color_far_a ; 
    so_called_type_platform_math_num_whole current_index ;
    
    x_left = so_called_common_logic_room_consts :: mesh_x_left ;
    x_right = so_called_common_logic_room_consts :: mesh_x_right ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    far_side_u_left = so_called_common_logic_room_consts :: mesh_far_side_u_left ;
    far_side_u_right = so_called_common_logic_room_consts :: mesh_far_side_u_right ;
    far_side_v_top = so_called_common_logic_room_consts :: mesh_far_side_v_top ;
    far_side_v_bottom = so_called_common_logic_room_consts :: mesh_far_side_v_bottom ;
    z_far = so_called_common_logic_room_consts :: mesh_z_far ;

    color_far_r = so_called_common_logic_room_consts :: mesh_color_far_r ;
    color_far_g = so_called_common_logic_room_consts :: mesh_color_far_g ;
    color_far_b = so_called_common_logic_room_consts :: mesh_color_far_b ;
    color_far_a = so_called_common_logic_room_consts :: mesh_color_far_a ;

    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , far_side_u_left , far_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , far_side_u_left , far_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
    
    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , far_side_u_right , far_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_far_r , color_far_g , color_far_b , color_far_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , far_side_u_right , far_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: add_left_side ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract left_side_u_left ;
    so_called_type_platform_math_num_fract left_side_u_right ;
    so_called_type_platform_math_num_fract left_side_v_top ;
    so_called_type_platform_math_num_fract left_side_v_bottom ;
    so_called_type_platform_math_num_fract z_near ;
    so_called_type_platform_math_num_fract z_far ;
    so_called_type_platform_math_num_fract color_left_r ;
    so_called_type_platform_math_num_fract color_left_g ;
    so_called_type_platform_math_num_fract color_left_b ;
    so_called_type_platform_math_num_fract color_left_a ;
    so_called_type_platform_math_num_whole current_index ;
    
    x_left = so_called_common_logic_room_consts :: mesh_x_left ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    left_side_u_left = so_called_common_logic_room_consts :: mesh_left_side_u_left ;
    left_side_u_right = so_called_common_logic_room_consts :: mesh_left_side_u_right ;
    left_side_v_top = so_called_common_logic_room_consts :: mesh_left_side_v_top ;
    left_side_v_bottom = so_called_common_logic_room_consts :: mesh_left_side_v_bottom ;
    z_near = so_called_common_logic_room_consts :: mesh_z_near ;
    z_far = so_called_common_logic_room_consts :: mesh_z_far ;

    color_left_r = so_called_common_logic_room_consts :: mesh_color_left_r ;
    color_left_g = so_called_common_logic_room_consts :: mesh_color_left_g ;
    color_left_b = so_called_common_logic_room_consts :: mesh_color_left_b ;
    color_left_a = so_called_common_logic_room_consts :: mesh_color_left_a ;
    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , left_side_u_left , left_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , left_side_u_left , left_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
    
    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , left_side_u_right , left_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_left_r , color_left_g , color_left_b , color_left_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , left_side_u_right , left_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: add_right_side ( )
{
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract right_side_u_left ;
    so_called_type_platform_math_num_fract right_side_u_right ;
    so_called_type_platform_math_num_fract right_side_v_top ;
    so_called_type_platform_math_num_fract right_side_v_bottom ;
    so_called_type_platform_math_num_fract z_near ;
    so_called_type_platform_math_num_fract z_far ;
    so_called_type_platform_math_num_fract color_right_r ;
    so_called_type_platform_math_num_fract color_right_g ;
    so_called_type_platform_math_num_fract color_right_b ;
    so_called_type_platform_math_num_fract color_right_a ;
    so_called_type_platform_math_num_whole current_index ;
    
    x_right = so_called_common_logic_room_consts :: mesh_x_right ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    right_side_u_left = so_called_common_logic_room_consts :: mesh_right_side_u_left ;
    right_side_u_right = so_called_common_logic_room_consts :: mesh_right_side_u_right ;
    right_side_v_top = so_called_common_logic_room_consts :: mesh_right_side_v_top ;
    right_side_v_bottom = so_called_common_logic_room_consts :: mesh_right_side_v_bottom ;
    z_near = so_called_common_logic_room_consts :: mesh_z_near ;
    z_far = so_called_common_logic_room_consts :: mesh_z_far ;

    color_right_r = so_called_common_logic_room_consts :: mesh_color_right_r ;
    color_right_g = so_called_common_logic_room_consts :: mesh_color_right_g ;
    color_right_b = so_called_common_logic_room_consts :: mesh_color_right_b ;
    color_right_a = so_called_common_logic_room_consts :: mesh_color_right_a ;

    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , right_side_u_left , right_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , right_side_u_left , right_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
    
    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , right_side_u_right , right_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_right_r , color_right_g , color_right_b , color_right_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , right_side_u_right , right_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: add_top_side ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract top_side_u_left ;
    so_called_type_platform_math_num_fract top_side_u_right ;
    so_called_type_platform_math_num_fract top_side_v_top ;
    so_called_type_platform_math_num_fract top_side_v_bottom ;
    so_called_type_platform_math_num_fract z_near ;
    so_called_type_platform_math_num_fract z_far ;
    so_called_type_platform_math_num_fract color_top_r ;
    so_called_type_platform_math_num_fract color_top_g ;
    so_called_type_platform_math_num_fract color_top_b ;
    so_called_type_platform_math_num_fract color_top_a ;
    so_called_type_platform_math_num_whole current_index ;
    
    x_left = so_called_common_logic_room_consts :: mesh_x_left ;
    x_right = so_called_common_logic_room_consts :: mesh_x_right ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    top_side_u_left = so_called_common_logic_room_consts :: mesh_top_side_u_left ;
    top_side_u_right = so_called_common_logic_room_consts :: mesh_top_side_u_right ;
    top_side_v_top = so_called_common_logic_room_consts :: mesh_top_side_v_top ;
    top_side_v_bottom = so_called_common_logic_room_consts :: mesh_top_side_v_bottom ;
    z_near = so_called_common_logic_room_consts :: mesh_z_near ;
    z_far = so_called_common_logic_room_consts :: mesh_z_far ;

    color_top_r = so_called_common_logic_room_consts :: mesh_color_top_r ;
    color_top_g = so_called_common_logic_room_consts :: mesh_color_top_g ;
    color_top_b = so_called_common_logic_room_consts :: mesh_color_top_b ;
    color_top_a = so_called_common_logic_room_consts :: mesh_color_top_a ;
    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , top_side_u_left , top_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , top_side_u_left , top_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
    
    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , top_side_u_right , top_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_top_r , color_top_g , color_top_b , color_top_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , top_side_u_right , top_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: add_bottom_side ( )
{
    so_called_type_platform_math_num_fract x_left ;
    so_called_type_platform_math_num_fract x_right ;
    so_called_type_platform_math_num_fract y_top ;
    so_called_type_platform_math_num_fract y_bottom ;
    so_called_type_platform_math_num_fract bottom_side_u_left ;
    so_called_type_platform_math_num_fract bottom_side_u_right ;
    so_called_type_platform_math_num_fract bottom_side_v_top ;
    so_called_type_platform_math_num_fract bottom_side_v_bottom ;
    so_called_type_platform_math_num_fract z_near ;
    so_called_type_platform_math_num_fract z_far ;
    so_called_type_platform_math_num_fract color_bottom_r ;
    so_called_type_platform_math_num_fract color_bottom_g ;
    so_called_type_platform_math_num_fract color_bottom_b ;
    so_called_type_platform_math_num_fract color_bottom_a ;
    so_called_type_platform_math_num_whole current_index ;
    
    x_left = so_called_common_logic_room_consts :: mesh_x_left ;
    x_right = so_called_common_logic_room_consts :: mesh_x_right ;
    y_top = so_called_common_logic_room_consts :: mesh_y_top ; 
    y_bottom = so_called_common_logic_room_consts :: mesh_y_bottom ; 
    bottom_side_u_left = so_called_common_logic_room_consts :: mesh_bottom_side_u_left ;
    bottom_side_u_right = so_called_common_logic_room_consts :: mesh_bottom_side_u_right ;
    bottom_side_v_top = so_called_common_logic_room_consts :: mesh_bottom_side_v_top ;
    bottom_side_v_bottom = so_called_common_logic_room_consts :: mesh_bottom_side_v_bottom ;
    z_near = so_called_common_logic_room_consts :: mesh_z_near ;
    z_far = so_called_common_logic_room_consts :: mesh_z_far ;

    color_bottom_r = so_called_common_logic_room_consts :: mesh_color_bottom_r ;
    color_bottom_g = so_called_common_logic_room_consts :: mesh_color_bottom_g ;
    color_bottom_b = so_called_common_logic_room_consts :: mesh_color_bottom_b ;
    color_bottom_a = so_called_common_logic_room_consts :: mesh_color_bottom_a ;
    current_index = shy_guts :: logic_room_mesh_create_state :: current_index ;

    //
    // connection from top side
    //

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_top , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    //
    // bottom side
    //

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_right , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_right , bottom_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;
    
    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_far ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_left , bottom_side_v_top ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: mesh_set_vertex_position            ( current_index , x_left , y_bottom , z_near ) ;
    shy_guts :: mesh_set_vertex_color               ( current_index , color_bottom_r , color_bottom_g , color_bottom_b , color_bottom_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( current_index , bottom_side_u_left , bottom_side_v_bottom ) ;
    shy_guts :: mesh_set_triangle_strip_index_value ( current_index , current_index ) ;
    so_called_platform_math :: inc_whole            ( current_index ) ;

    shy_guts :: logic_room_mesh_create_state :: current_index = current_index ;
}

void shy_guts :: finalize_mesh ( )
{
    shy_guts :: engine_render_mesh_create_state :: finalized = so_called_platform_math_consts :: whole_true ;
    so_called_message_common_engine_render_mesh_finalize msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    so_called_sender_common_engine_render_mesh_finalize :: send ( msg ) ;
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
    so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_sender_common_engine_render_mesh_set_vertex_tex_coord :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_sender_common_engine_render_mesh_set_vertex_position :: send ( msg ) ;
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

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: requested ) )
    {
        shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_mesh_create_state :: mesh = msg . mesh ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_logic_room_mesh_create )
{
    shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_room_mesh :: receive ( so_called_message_common_logic_room_mesh_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: finalized ) )
    {
        so_called_message_common_engine_render_mesh_render render_msg ;
        render_msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
        so_called_sender_common_engine_render_mesh_render :: send ( render_msg ) ;
    }
    so_called_sender_common_logic_room_mesh_render_reply :: send ( so_called_message_common_logic_room_mesh_render_reply ( ) ) ;
}
