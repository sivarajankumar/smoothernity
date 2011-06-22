namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_whole mesh_vertices = so_called_platform_math :: init_num_whole ( 4 ) ;
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

    namespace logic_text_letter_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_common_logic_text_letter_id letter ;
        static so_called_type_platform_math_num_fract size ;
        static so_called_type_platform_math_num_fract color_r ;
        static so_called_type_platform_math_num_fract color_g ;
        static so_called_type_platform_math_num_fract color_b ;
        static so_called_type_platform_math_num_fract color_a ;
    }

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
    static void fill_mesh_content ( ) ;
    static void proceed_with_creation ( ) ;
    static void replied_letter_tex_coords ( ) ;
    static void request_mesh_create ( ) ;
    static void request_tex_coords ( ) ;
    static void send_engine_render_mesh_finalize ( ) ;
    static void send_letter_mesh_create_reply ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text_letter_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_position msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    so_called_sender_common_engine_render_mesh_set_vertex_position :: send ( msg ) ;
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_message_common_engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    so_called_sender_common_engine_render_mesh_set_vertex_tex_coord :: send ( msg ) ;
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
    so_called_message_common_engine_render_mesh_set_vertex_color msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    so_called_sender_common_engine_render_mesh_set_vertex_color :: send ( msg ) ;
}

void shy_guts :: mesh_set_triangle_strip_index_value
    ( so_called_type_common_engine_render_mesh_id mesh
    , so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_whole index 
    )
{
    so_called_message_common_engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = mesh ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_sender_common_engine_render_mesh_set_triangle_strip_index_value :: send ( msg ) ;
}

void shy_guts :: fill_mesh_content ( )
{
    so_called_type_common_engine_render_mesh_id mesh ;
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
    
    mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    
    so_called_platform_math :: div_fracts ( half_size , shy_guts :: logic_text_letter_mesh_create_state :: size , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: mul_fracts ( x_left , half_size , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( y_bottom , half_size , so_called_platform_math_consts :: fract_minus_1 ) ;
    so_called_platform_math :: mul_fracts ( x_right , half_size , so_called_platform_math_consts :: fract_1 ) ;
    so_called_platform_math :: mul_fracts ( y_top , half_size , so_called_platform_math_consts :: fract_1 ) ;
    z = so_called_platform_math_consts :: fract_0 ;
    
    u_left = shy_guts :: logic_text_letter_big_tex_coords_state :: left ;
    u_right = shy_guts :: logic_text_letter_big_tex_coords_state :: right ;
    v_bottom = shy_guts :: logic_text_letter_big_tex_coords_state :: bottom ;
    v_top = shy_guts :: logic_text_letter_big_tex_coords_state :: top ;
    
    color_r = shy_guts :: logic_text_letter_mesh_create_state :: color_r ;
    color_g = shy_guts :: logic_text_letter_mesh_create_state :: color_g ;
    color_b = shy_guts :: logic_text_letter_mesh_create_state :: color_b ;
    color_a = shy_guts :: logic_text_letter_mesh_create_state :: color_a ;

    index_left_top = so_called_platform_math_consts :: whole_0 ;
    index_left_bottom = so_called_platform_math_consts :: whole_1 ;
    index_right_top = so_called_platform_math_consts :: whole_2 ;
    index_right_bottom = so_called_platform_math_consts :: whole_3 ;
    
    shy_guts :: mesh_set_triangle_strip_index_value ( mesh , index_left_top , index_left_top ) ;
    shy_guts :: mesh_set_vertex_color               ( mesh , index_left_top , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( mesh , index_left_top , u_left , v_top ) ;
    shy_guts :: mesh_set_vertex_position            ( mesh , index_left_top , x_left , y_top , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( mesh , index_left_bottom , index_left_bottom ) ;
    shy_guts :: mesh_set_vertex_color               ( mesh , index_left_bottom , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( mesh , index_left_bottom , u_left , v_bottom ) ;
    shy_guts :: mesh_set_vertex_position            ( mesh , index_left_bottom , x_left , y_bottom , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( mesh , index_right_top , index_right_top ) ;
    shy_guts :: mesh_set_vertex_color               ( mesh , index_right_top , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( mesh , index_right_top , u_right , v_top ) ;
    shy_guts :: mesh_set_vertex_position            ( mesh , index_right_top , x_right , y_top , z ) ;

    shy_guts :: mesh_set_triangle_strip_index_value ( mesh , index_right_bottom , index_right_bottom ) ;
    shy_guts :: mesh_set_vertex_color               ( mesh , index_right_bottom , color_r , color_g , color_b , color_a ) ;
    shy_guts :: mesh_set_vertex_tex_coord           ( mesh , index_right_bottom , u_right , v_bottom ) ;
    shy_guts :: mesh_set_vertex_position            ( mesh , index_right_bottom , x_right , y_bottom , z ) ;
}
    
void shy_guts :: send_engine_render_mesh_finalize ( )
{
    so_called_message_common_engine_render_mesh_finalize msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    so_called_sender_common_engine_render_mesh_finalize :: send ( msg ) ;
}

void shy_guts :: request_tex_coords ( )
{
    shy_guts :: logic_text_letter_big_tex_coords_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_text_letter_big_tex_coords_state :: requested_letter = shy_guts :: logic_text_letter_mesh_create_state :: letter ;

    so_called_message_common_logic_text_letter_big_tex_coords_request msg ;
    msg . letter = shy_guts :: logic_text_letter_mesh_create_state :: letter ;
    so_called_sender_common_logic_text_letter_big_tex_coords_request :: send ( msg ) ;
}

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_mesh_create_state :: requested ) )
    {
        shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_mesh_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: replied ) )
    {
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_tex_coords ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_big_tex_coords_state :: replied ) )
    {
        shy_guts :: logic_text_letter_big_tex_coords_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: replied_letter_tex_coords ( ) ;
    }
}

void shy_guts :: replied_letter_tex_coords ( )
{
    shy_guts :: fill_mesh_content ( ) ;
    shy_guts :: send_engine_render_mesh_finalize ( ) ;
    shy_guts :: send_letter_mesh_create_reply ( ) ;
}

void shy_guts :: request_mesh_create ( )
{
    shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;

    so_called_message_common_engine_render_mesh_create_request msg ;
    msg . vertices = shy_guts :: consts :: mesh_vertices ;
    msg . triangle_strip_indices = shy_guts :: consts :: mesh_vertices ;
    msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
    so_called_sender_common_engine_render_mesh_create_request :: send ( msg ) ;
}

void shy_guts :: send_letter_mesh_create_reply ( )
{
    so_called_message_common_logic_text_letter_mesh_create_reply msg ;
    msg . mesh = shy_guts :: engine_render_mesh_create_state :: mesh ;
    so_called_sender_common_logic_text_letter_mesh_create_reply :: send ( msg ) ;
}

void _shy_common_logic_text_letter_mesh :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_mesh_create_state :: requested ) )
    {
        shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_mesh_create_state :: mesh = msg . mesh ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_text_letter_mesh :: receive ( so_called_message_common_init )
{
    shy_guts :: engine_render_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_big_tex_coords_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_big_tex_coords_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_text_letter_mesh :: receive ( so_called_message_common_logic_text_letter_big_tex_coords_reply msg )
{
    so_called_type_platform_math_num_whole letters_are_equal ;
    so_called_common_logic_text_stateless :: are_letters_equal ( letters_are_equal , shy_guts :: logic_text_letter_big_tex_coords_state :: requested_letter , msg . letter ) ;
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_text_letter_big_tex_coords_state :: requested )
      && so_called_platform_conditions :: whole_is_true ( letters_are_equal )
       )
    {
        shy_guts :: logic_text_letter_big_tex_coords_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_text_letter_big_tex_coords_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_text_letter_big_tex_coords_state :: bottom = msg . bottom ;
        shy_guts :: logic_text_letter_big_tex_coords_state :: left = msg . left ;
        shy_guts :: logic_text_letter_big_tex_coords_state :: top = msg . top ;
        shy_guts :: logic_text_letter_big_tex_coords_state :: right = msg . right ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_text_letter_mesh :: receive ( so_called_message_common_logic_text_letter_mesh_create_request msg )
{
    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_text_letter_mesh_create_state :: letter = msg . letter ;
    shy_guts :: logic_text_letter_mesh_create_state :: size = msg . size ;
    shy_guts :: logic_text_letter_mesh_create_state :: color_r = msg . color_r ;
    shy_guts :: logic_text_letter_mesh_create_state :: color_g = msg . color_g ;
    shy_guts :: logic_text_letter_mesh_create_state :: color_b = msg . color_b ;
    shy_guts :: logic_text_letter_mesh_create_state :: color_a = msg . color_a ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_text_letter_mesh :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

