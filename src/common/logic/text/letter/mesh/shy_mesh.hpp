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

    static void proceed_with_creation ( ) ;
    static void request_mesh_create ( ) ;
    static void send_letter_mesh_create_reply ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_text_letter_mesh > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

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
        shy_guts :: send_letter_mesh_create_reply ( ) ;
    }
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
    shy_guts :: logic_text_letter_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
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

