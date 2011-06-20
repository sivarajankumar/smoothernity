namespace shy_guts
{
    namespace logic_salutation_letters_meshes_generator_generate_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_generator > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_init )
{
    shy_guts :: logic_salutation_letters_meshes_generator_generate_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_generate )
{
    so_called_sender_common_logic_salutation_letters_meshes_generator_generate_finished :: send ( so_called_message_common_logic_salutation_letters_meshes_generator_generate_finished ( ) ) ;
}

void _shy_common_logic_salutation_letters_meshes_generator :: receive ( so_called_message_common_logic_salutation_letters_meshes_generator_update )
{
}

void _shy_common_logic_salutation_letters_meshes_generator :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
