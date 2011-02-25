namespace shy_guts
{
    namespace logic_blanket_place_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_blanket_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_matrix_data transform ;
    }

    static void proceed_with_place ( ) ;
    static void request_animation_transform ( ) ;
    static void transform_mesh ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_blanket_placement > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_place ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_place_state :: requested ) )
    {
        shy_guts :: logic_blanket_place_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_animation_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_transform_state :: replied ) )
    {
        shy_guts :: logic_blanket_animation_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: transform_mesh ( ) ;
    }
}

void shy_guts :: request_animation_transform ( )
{
    shy_guts :: logic_blanket_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_blanket_animation_transform_request :: send ( so_called_message_common_logic_blanket_animation_transform_request ( ) ) ;
}

void shy_guts :: transform_mesh ( )
{
    so_called_message_common_logic_blanket_mesh_set_transform msg ;
    msg . transform = shy_guts :: logic_blanket_animation_transform_state :: transform ;
    so_called_sender_common_logic_blanket_mesh_set_transform :: send ( msg ) ;
}

void _shy_common_logic_blanket_placement :: receive ( so_called_message_common_logic_blanket_animation_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_blanket_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_blanket_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_blanket_animation_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_blanket_animation_transform_state :: transform = msg . transform ;
        shy_guts :: proceed_with_place ( ) ;
    }
}

void _shy_common_logic_blanket_placement :: receive ( so_called_message_common_logic_blanket_place )
{
    shy_guts :: logic_blanket_place_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_place ( ) ;
}
