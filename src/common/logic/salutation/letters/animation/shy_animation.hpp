namespace shy_guts
{
    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_animation_layout_transform ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_animation_transform_state
    {
        static so_called_common_logic_salutation_letters_animation_transform_request_message msg_request ;
        static so_called_type_platform_matrix_data transform ;
        static void on_request ( ) ;
    }

    static void compute_transform ( );
    static void request_animation_layout_transform ( ) ;
    static void send_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_animation_transform_state :: on_request ( )
{
    shy_guts :: request_animation_layout_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_reply ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: send_computed_transform ( ) ;
}

void shy_guts :: request_animation_layout_transform ( )
{
    so_called_type_platform_math_num_whole letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_request . letter = letter ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . request ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_type_platform_vector_data final_origin ;
    so_called_type_platform_math_num_fract final_scale ;
    so_called_type_platform_vector_data layout_origin ;
    so_called_type_platform_math_num_fract layout_scale ;
    so_called_type_platform_matrix_data transform ;

    layout_origin = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_reply . origin ;
    layout_scale = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . msg_reply . scale ;

    final_origin = layout_origin ;
    final_scale = layout_scale ;

    so_called_common_engine_math_stateless :: scale ( transform , final_scale ) ;
    so_called_platform_matrix :: set_origin ( transform , final_origin ) ;

    shy_guts :: logic_salutation_letters_animation_transform_state :: transform = transform ;
}

void shy_guts :: send_computed_transform ( )
{
    so_called_common_logic_salutation_letters_animation_transform_reply_message msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request . letter ;
    msg . transform = shy_guts :: logic_salutation_letters_animation_transform_state :: transform ;
    so_called_common_logic_salutation_letters_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_layout_transform_reply_message msg )
{
    so_called_type_platform_math_num_whole should_handle ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_common_logic_salutation_letters_animation_transform_request_message msg )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: msg_request = msg ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
