void shy_common_logic_salutation_letters_text_storage_letter_checker :: check 
    ( so_called_type_platform_math_num_whole & result
    , so_called_message_common_logic_salutation_letters_text_storage_letter_request msg_request
    , so_called_message_common_logic_salutation_letters_text_storage_letter_reply msg_reply
    )
{
    if ( so_called_platform_conditions :: wholes_are_equal ( msg_request . letter_index , msg_reply . letter_index ) )
        result = so_called_platform_math_consts :: whole_true ;
    else
        result = so_called_platform_math_consts :: whole_false ;
}