void shy_common_logic_text_letter_mesh_create_checker :: check 
    ( so_called_type_platform_math_num_whole & result
    , so_called_message_common_logic_text_letter_mesh_create_request msg_request
    , so_called_message_common_logic_text_letter_mesh_create_reply msg_reply
    )
{
    so_called_common_logic_text_stateless :: are_letters_equal ( result , msg_request . letter , msg_reply . letter ) ;
}
