void shy_common_logic_text_stateless :: are_letters_equal
    ( so_called_platform_math_num_whole_type & result
    , so_called_common_logic_text_letter_id_type a
    , so_called_common_logic_text_letter_id_type b
    )
{
    so_called_platform_math :: make_num_whole ( result , so_called_platform_conditions :: wholes_are_equal ( a . _letter_id , b . _letter_id ) ) ;
}

so_called_common_logic_text_letter_id_type shy_common_logic_text_stateless :: init_letter_id ( so_called_platform_math_const_int_32_type num )
{
    so_called_common_logic_text_letter_id_type letter ;
    so_called_platform_math :: make_num_whole ( letter . _letter_id , num ) ;
    return letter ;
}

void shy_common_logic_text_stateless :: get_letter_id ( so_called_platform_math_num_whole_type & result , so_called_common_logic_text_letter_id_type letter )
{
    result = letter . _letter_id ;
}
