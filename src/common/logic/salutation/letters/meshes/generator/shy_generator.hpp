namespace shy_guts
{
    namespace logic_salutation_letters_meshes_generator_generate_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace logic_salutation_letters_meshes_generator_update_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    static void proceed_with_generation ( ) ;
    static void send_generate_finished ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_generation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: send_generate_finished ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested ) )
    {
        shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
    }
}

void shy_guts :: send_generate_finished ( )
{
    so_called_sender_common_logic_salutation_letters_meshes_generator_generate_finished :: send 
        ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished ( ) 
        ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_salutation_letters_meshes_generator_update_state :: requested = so_called_platform_math_consts :: whole_false ;
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

void _shy_common_logic_salutation_letters_meshes_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
