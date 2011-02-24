namespace shy_guts
{
    namespace logic_observer_animation_consts
    {
        static const so_called_type_platform_math_num_fract up_x = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
        static const so_called_type_platform_math_num_fract up_y = so_called_platform_math :: init_num_fract ( 1 , 1 ) ;
        static const so_called_type_platform_math_num_fract up_z = so_called_platform_math :: init_num_fract ( 0 , 1 ) ;
    }

    namespace logic_observer_animation_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_matrix_data transform ;
    }

    namespace logic_observer_animation_flight_transform_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_vector_data eye ;
        static so_called_type_platform_vector_data target ;
    }

    static void proceed_with_transform ( ) ;
    static void request_flight_transform ( ) ;
    static void reply_computed_transform ( ) ;
    static void compute_transform ( ) ;
    static void reply_transform ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_observer_animation > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_transform ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_transform_state :: requested ) )
    {
        shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_flight_transform ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_flight_transform_state :: replied ) )
    {
        shy_guts :: logic_observer_animation_flight_transform_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: reply_computed_transform ( ) ;
    }
}

void shy_guts :: request_flight_transform ( )
{
    shy_guts :: logic_observer_animation_flight_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_observer_animation_flight_transform_request :: send ( so_called_message_common_logic_observer_animation_flight_transform_request ( ) ) ;
}

void shy_guts :: reply_computed_transform ( )
{
    shy_guts :: compute_transform ( ) ;
    shy_guts :: reply_transform ( ) ;
}

void shy_guts :: compute_transform ( )
{
    so_called_type_platform_math_num_fract up_x ;
    so_called_type_platform_math_num_fract up_y ;
    so_called_type_platform_math_num_fract up_z ;
    so_called_type_platform_vector_data up ;
    so_called_type_platform_vector_data eye ;
    so_called_type_platform_vector_data target ;
    so_called_type_platform_matrix_data transform ;

    up_x = shy_guts :: logic_observer_animation_consts :: up_x ;
    up_y = shy_guts :: logic_observer_animation_consts :: up_y ;
    up_z = shy_guts :: logic_observer_animation_consts :: up_z ;
    eye = shy_guts :: logic_observer_animation_flight_transform_state :: eye ;
    target = shy_guts :: logic_observer_animation_flight_transform_state :: target ;

    so_called_platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    so_called_common_engine_camera_stateless :: matrix_look_at ( transform , eye , target , up ) ;

    shy_guts :: logic_observer_animation_transform_state :: transform = transform ;
}

void shy_guts :: reply_transform ( )
{
    so_called_message_common_logic_observer_animation_transform_reply msg ;
    msg . transform = shy_guts :: logic_observer_animation_transform_state :: transform ;
    so_called_sender_common_logic_observer_animation_transform_reply :: send ( msg ) ;
}

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_init )
{
}

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_logic_observer_animation_flight_transform_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_observer_animation_flight_transform_state :: requested ) )
    {
        shy_guts :: logic_observer_animation_flight_transform_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_observer_animation_flight_transform_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_observer_animation_flight_transform_state :: eye = msg . eye ;
        shy_guts :: logic_observer_animation_flight_transform_state :: target = msg . target ;
        shy_guts :: proceed_with_transform ( ) ;
    }
}

void _shy_common_logic_observer_animation :: receive ( so_called_message_common_logic_observer_animation_transform_request )
{
    shy_guts :: logic_observer_animation_transform_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_transform ( ) ;
}
