namespace shy_guts
{
    namespace logic_salutation_letters_animation_layout_transform_state
    {
        static so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg_replied ;
        static so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg_requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_animation_transform_state
    {
        static so_called_message_common_logic_salutation_letters_animation_transform_request msg_requested ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data transform ;
        static void on_requested ( ) ;
    }

    static void compute_transform ( );
    static void request_animation_layout_transform ( ) ;
    static void send_computed_transform ( ) ;
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_animation_transform_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_animation_layout_transform_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_animation_transform_state :: on_requested ( )
{
    shy_guts :: request_animation_layout_transform ( ) ;
}

void shy_guts :: logic_salutation_letters_animation_layout_transform_state :: on_replied ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: send_computed_transform ( ) ;
}

void shy_guts :: request_animation_layout_transform ( )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_requested . letter =
        shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested . letter ;

    so_called_sender_common_logic_salutation_letters_animation_layout_transform_request :: send
        ( shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_requested
        ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_type_platform_vector_data final_origin ;
    so_called_type_platform_math_num_fract final_scale ;
    so_called_type_platform_vector_data layout_origin ;
    so_called_type_platform_math_num_fract layout_scale ;
    so_called_type_platform_matrix_data transform ;

    layout_origin = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_replied . origin ;
    layout_scale = shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_replied . scale ;

    final_origin = layout_origin ;
    final_scale = layout_scale ;

    so_called_common_engine_math_stateless :: scale ( transform , final_scale ) ;
    so_called_platform_matrix :: set_origin ( transform , final_origin ) ;

    shy_guts :: logic_salutation_letters_animation_transform_state :: transform = transform ;
}

void shy_guts :: send_computed_transform ( )
{
    so_called_message_common_logic_salutation_letters_animation_transform_reply msg ;
    msg . letter = shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested . letter ;
    msg . transform = shy_guts :: logic_salutation_letters_animation_transform_state :: transform ;
    so_called_sender_common_logic_salutation_letters_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_animation_layout_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_animation_layout_transform_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_requested . letter , msg . letter )
       )
    {
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_letters_animation_layout_transform_state :: msg_replied = msg ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_letters_animation :: receive ( so_called_message_common_logic_salutation_letters_animation_transform_request msg )
{
    shy_guts :: logic_salutation_letters_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_animation_transform_state :: msg_requested = msg ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_letters_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
