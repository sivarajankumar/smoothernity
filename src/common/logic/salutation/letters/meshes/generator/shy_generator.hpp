namespace shy_guts
{
    namespace logic_salutation_letters_meshes_creator_create_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole requested_letter_index ;
        static void on_replied ( ) ;
    }

    namespace logic_salutation_letters_meshes_generator_generate_state
    {
        static so_called_type_platform_math_num_whole letter_current ;
        static so_called_type_platform_math_num_whole requested ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_meshes_generator_update_state
    {
        static so_called_type_platform_math_num_whole enabled ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_fract time ;
        static void on_requested ( ) ;
    }

    namespace logic_salutation_letters_text_storage_size_state
    {
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole size ;
        static void on_replied ( ) ;
    }

    static void advance_time ( ) ;
    static void generate_by_time ( ) ;
    static void generate_next_mesh ( ) ;
    static void handle_generation_time ( ) ;
    static void send_generate_finished ( ) ;
    static void update_state ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_state ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_size_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_text_storage_size_state :: on_replied ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: on_requested ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_creator_create_state :: replied ) )
    {
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_replied ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: on_requested ( )
{
    shy_guts :: logic_salutation_letters_text_storage_size_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_sender_common_logic_salutation_letters_text_storage_size_request :: send
        ( so_called_message_common_logic_salutation_letters_text_storage_size_request ( )
        ) ;
}

void shy_guts :: logic_salutation_letters_text_storage_size_state :: on_replied ( )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void shy_guts :: logic_salutation_letters_meshes_generator_update_state :: on_requested ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled ) )
    {
        shy_guts :: advance_time ( ) ;
        shy_guts :: generate_by_time ( ) ;
    }
}

void shy_guts :: logic_salutation_letters_meshes_creator_create_state :: on_replied ( )
{
    shy_guts :: generate_by_time ( ) ;
}

void shy_guts :: handle_generation_time ( )
{
    so_called_type_platform_math_num_whole letter_current ;
    so_called_type_platform_math_num_whole letters_total ;

    letter_current = shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current ;
    letters_total = shy_guts :: logic_salutation_letters_text_storage_size_state :: size ;

    if ( so_called_platform_conditions :: whole_less_than_whole ( letter_current , letters_total ) )
        shy_guts :: generate_next_mesh ( ) ;
    else
        shy_guts :: send_generate_finished ( ) ;
}

void shy_guts :: generate_next_mesh ( )
{
    so_called_type_platform_math_num_whole letter_index ;
    letter_index = shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current ;

    so_called_platform_math :: inc_whole
        ( shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: letter_current
        ) ;

    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested_letter_index = letter_index ;

    so_called_message_common_logic_salutation_letters_meshes_creator_create_request msg ;
    msg . letter_index = letter_index ;
    so_called_sender_common_logic_salutation_letters_meshes_creator_create_request :: send ( msg ) ;
}

void shy_guts :: generate_by_time ( )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract time_to_create ;

    time = shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time ;
    time_to_create = so_called_common_logic_salutation_letters_meshes_consts :: time_between_creation ;

    if ( so_called_platform_conditions :: fract_greater_than_fract ( time , time_to_create ) )
    {
        so_called_platform_math :: sub_from_fract ( time , time_to_create ) ;
        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time = time ;
        shy_guts :: handle_generation_time ( ) ;
    }
}

void shy_guts :: advance_time ( )
{
    so_called_type_platform_math_num_fract time ;
    so_called_type_platform_math_num_fract time_step ;

    time = shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time ;
    so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;
    so_called_platform_math :: add_to_fract ( time , time_step ) ;

    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: time = time ;
}

void shy_guts :: send_generate_finished ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_generator_generate_finished :: send 
        ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished ( ) 
        ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: enabled = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_text_storage_size_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_generate )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: update_state ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_update )
{
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: update_state ( ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_creator_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested )
      && so_called_platform_conditions :: wholes_are_equal ( shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested_letter_index , msg . letter_index )
       )
    {
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_meshes_creator_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: update_state ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_text_storage_size_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_text_storage_size_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_text_storage_size_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_salutation_letters_text_storage_size_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: logic_salutation_letters_text_storage_size_state :: size = msg . size ;
        shy_guts :: update_state ( ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
