namespace shy_guts
{
    namespace consts
    {
        static so_called_platform_math_num_fract_type origin_x = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_platform_math_num_fract_type origin_y = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static so_called_platform_math_num_fract_type origin_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
    }

    namespace logic_salutation_animation_transform_state
    {
        static void on_request ( ) ;
    }

    namespace logic_salutation_animation_zoom_transform_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_animation_zoom_transform ) taker ;
        static void on_reply ( ) ;
    }

    static void request_animation_zoom_transform ( ) ;
    static void send_computed_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_animation_transform_state :: on_request ( )
{
    shy_guts :: request_animation_zoom_transform ( ) ;
}

void shy_guts :: logic_salutation_animation_zoom_transform_state :: on_reply ( )
{
    shy_guts :: send_computed_transform ( ) ;
}

void shy_guts :: request_animation_zoom_transform ( )
{
    shy_guts :: logic_salutation_animation_zoom_transform_state :: taker . request ( ) ;
}

void shy_guts :: send_computed_transform ( )
{
    so_called_platform_vector_data_type origin ;
    so_called_platform_vector :: xyz 
        ( origin
        , shy_guts :: consts :: origin_x
        , shy_guts :: consts :: origin_y
        , shy_guts :: consts :: origin_z
        ) ;

    so_called_platform_math_num_fract_type scale ;
    scale = shy_guts :: logic_salutation_animation_zoom_transform_state :: taker . msg_reply . scale ;

    so_called_platform_matrix_data_type transform ;
    so_called_common_engine_math_stateless :: scale ( transform , scale ) ;
    so_called_platform_matrix :: set_origin ( transform , origin ) ;

    so_called_common_logic_salutation_animation_transform_reply_message msg ;
    msg . transform = transform ;
    so_called_common_logic_salutation_animation_transform_reply_sender :: send ( msg ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_animation_zoom_transform_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_common_logic_salutation_animation_transform_request_message )
{
    shy_guts :: logic_salutation_animation_transform_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_animation :: receive ( so_called_common_logic_salutation_animation_zoom_transform_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_animation_zoom_transform_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_animation_zoom_transform_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_animation :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
