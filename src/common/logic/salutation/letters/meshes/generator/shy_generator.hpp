namespace shy_guts
{
    namespace logic_salutation_letters_meshes_creator_create_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_meshes_creator_create ) taker ;
        static void on_reply ( ) ;
    }

    namespace logic_salutation_letters_meshes_generator_generate_state
    {
        static so_called_platform_math_num_whole_type letter_current ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_meshes_generator_update
    {
        static so_called_platform_math_num_whole_type enabled ;
        static so_called_platform_math_num_fract_type time ;
        static void on_request ( ) ;
    }

    namespace logic_salutation_letters_text_storage_size_state
    {
        static so_called_common_engine_taker_helper ( logic_salutation_letters_text_storage_size ) taker ;
        static void on_reply ( ) ;
    }

    static void advance_time ( ) ;
    static void generate ( ) ;
    static void generate_by_time ( ) ;
    static void generate_next_mesh ( ) ;
    static void request_letters_amount_in_storage ( ) ;
    static void send_generate_finished ( ) ;
    static void start_generation ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: on_request ( )
{
    shy_guts :: request_letters_amount_in_storage ( ) ;
}

void shy_guts :: logic_salutation_letters_text_storage_size_state :: on_reply ( )
{
    shy_guts :: start_generation ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_generator_update :: on_request ( )
{
    shy_guts :: advance_time ( ) ;
    shy_guts :: generate_by_time ( ) ;
}

void shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_reply ( )
{
    shy_guts :: generate_by_time ( ) ;
}

void shy_guts :: start_generation ( )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: logic_salutation_letters_meshes_generator_update :: enabled = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_generator_update :: time = so_called_platform_math_consts :: fract_0 ;
}

void shy_guts :: request_letters_amount_in_storage ( )
{
    shy_guts :: logic_salutation_letters_text_storage_size_state :: taker . request ( ) ;
}

void shy_guts :: generate_by_time ( )
{
    so_called_platform_math_num_fract_type time ;
    so_called_platform_math_num_fract_type time_to_create ;

    time = shy_guts :: logic_salutation_letters_meshes_generator_update :: time ;
    time_to_create = so_called_common_logic_salutation_letters_meshes_consts :: time_between_creation ;

    if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_to_create ) )
    {
        so_called_platform_math :: sub_from_fract ( time , time_to_create ) ;
        shy_guts :: logic_salutation_letters_meshes_generator_update :: time = time ;
        shy_guts :: generate ( ) ;
    }
}

void shy_guts :: generate ( )
{
    so_called_platform_math_num_whole_type letter_current ;
    so_called_platform_math_num_whole_type letters_total ;

    letter_current = shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current ;
    letters_total = shy_guts :: logic_salutation_letters_text_storage_size_state :: taker . msg_reply . size ;

    if ( so_called_platform_conditions :: whole_less_than_whole ( letter_current , letters_total ) )
        shy_guts :: generate_next_mesh ( ) ;
    else
        shy_guts :: send_generate_finished ( ) ;
}

void shy_guts :: generate_next_mesh ( )
{
    so_called_platform_math_num_whole_type letter_index ;
    letter_index = shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current ;

    so_called_platform_math :: inc_whole
        ( shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current
        ) ;

    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: taker . msg_request . letter_index = letter_index ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: taker . request ( ) ;
}

void shy_guts :: advance_time ( )
{
    so_called_common_engine_math_stateless :: add_frame_to_time
        ( shy_guts :: logic_salutation_letters_meshes_generator_update :: time
        ) ;
}

void shy_guts :: send_generate_finished ( )
{
    so_called_common_logic_salutation_letters_meshes_generator_generate_finished_sender :: send 
        ( so_called_common_logic_salutation_letters_meshes_generator_generate_finished_message ( ) 
        ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: taker . init ( ) ;
    shy_guts :: logic_salutation_letters_meshes_generator_update :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: taker . init ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_common_logic_salutation_letters_meshes_generator_generate_message )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_common_logic_salutation_letters_meshes_generator_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update :: enabled ) )
        shy_guts :: logic_salutation_letters_meshes_generator_update :: on_request ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_common_logic_salutation_letters_meshes_creator_create_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_common_logic_salutation_letters_text_storage_size_reply_message msg )
{
    so_called_platform_math_num_whole_type should_handle ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: taker . should_handle ( should_handle , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( should_handle ) )
        shy_guts :: logic_salutation_letters_text_storage_size_state :: on_reply ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
