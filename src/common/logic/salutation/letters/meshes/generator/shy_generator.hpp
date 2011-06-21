namespace shy_guts
{
    namespace logic_salutation_letters_meshes_generator_generate_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_salutation_letters_meshes_generator_update_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole enabled ;
        static so_called_type_platform_math_num_fract time ;
    }

    namespace logic_salutation_letters_text_storage_size_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole size ;
    }

    static void handle_update ( ) ;
    static void proceed_with_generation ( ) ;
    static void request_letters_text_storage_size ( ) ;
    static void send_generate_finished ( ) ;
    static void start_generation ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_generation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_letters_text_storage_size ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_size_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: start_generation ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: handle_update ( ) ;
    }
}

void shy_guts :: handle_update ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled ) )
    {
        so_called_type_platform_math_num_fract time ;
        so_called_type_platform_math_num_fract time_step ;
        so_called_type_platform_math_num_fract time_to_create ;

        time = shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time ;
        time_to_create = so_called_common_logic_salutation_letters_meshes_consts :: time_between_creation ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        while ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_to_create ) )
        {
            so_called_platform_math :: sub_from_fract ( time , time_to_create ) ;
        }

        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time = time ;
        shy_guts :: send_generate_finished ( ) ;
    }
}

void shy_guts :: request_letters_text_storage_size ( )
{
    shy_guts :: logic_salutation_letters_text_storage_size_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_letters_text_storage_size_request :: send
        ( so_called_message_common_logic_salutation_letters_text_storage_size_request ( )
        ) ;
}

void shy_guts :: send_generate_finished ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_generator_generate_finished :: send 
        ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished ( ) 
        ) ;
}

void shy_guts :: start_generation ( )
{
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_generate )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_generation ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_update )
{
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_generation ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_text_storage_size_reply msg )
{
    shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: size = msg . size ;
    shy_guts :: proceed_with_generation ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
