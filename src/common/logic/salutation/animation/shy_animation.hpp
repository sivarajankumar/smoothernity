namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_fract origin_x = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_type_platform_math_num_fract origin_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_type_platform_math_num_fract origin_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
    }

    namespace logic_salutation_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_animation_zoom_transform_state
    {
        static so_called_message_common_logic_salutation_animation_zoom_transform_reply msg_replied ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_replied ( ) ;
    }

    static void request_animation_zoom_transform ( ) ;
    static void send_computed_transform ( ) ;
    static void work ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: work ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_animation_transform_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_animation_zoom_transform_state :: replied ) )
    {
        shy_guts :: logic_salutation_animation_zoom_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_animation_zoom_transform_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_animation_transform_state :: on_requested ( )
{
    shy_guts :: request_animation_zoom_transform ( ) ;
}

void shy_guts :: logic_salutation_animation_zoom_transform_state :: on_replied ( )
{
    shy_guts :: send_computed_transform ( ) ;
}

void shy_guts :: request_animation_zoom_transform ( )
{
    shy_guts :: logic_salutation_animation_zoom_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_animation_zoom_transform_request :: send
        ( so_called_message_common_logic_salutation_animation_zoom_transform_request ( )
        ) ;
}

void shy_guts :: send_computed_transform ( )
{
    so_called_type_platform_vector_data origin ;
    so_called_platform_vector :: xyz 
        ( origin
        , shy_guts :: consts :: origin_x
        , shy_guts :: consts :: origin_y
        , shy_guts :: consts :: origin_z
        ) ;

    so_called_type_platform_math_num_fract scale ;
    scale = shy_guts :: logic_salutation_animation_zoom_transform_state :: msg_replied . scale ;

    so_called_type_platform_matrix_data transform ;
    so_called_common_engine_math_stateless :: scale ( transform , scale ) ;
    so_called_platform_matrix :: set_origin ( transform , origin ) ;

    so_called_message_common_logic_salutation_animation_transform_reply msg ;
    msg . transform = transform ;
    so_called_sender_common_logic_salutation_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_animation_zoom_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_animation_zoom_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_logic_salutation_animation_transform_request )
{
    shy_guts :: logic_salutation_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: work ( ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_message_common_logic_salutation_animation_zoom_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_animation_zoom_transform_state :: requested ) )
    {
        shy_guts :: logic_salutation_animation_zoom_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_animation_zoom_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_animation_zoom_transform_state :: msg_replied = msg ;
        shy_guts :: work ( ) ;
    }
}

void _shy_common_logic_salutation_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
