void shy_common_logic_salutation_letters_animation_layout_transform_checker :: check 
    ( so_called_type_platform_math_num_whole & result
    , so_called_message_common_logic_salutation_letters_animation_layout_transform_request msg_request
    , so_called_message_common_logic_salutation_letters_animation_layout_transform_reply msg_reply
    )
{
    if ( so_called_platform_conditions :: wholes_are_equal ( msg_request . letter , msg_reply . letter ) )
        result = so_called_platform_math_consts :: whole_true ;
    else
        result = so_called_platform_math_consts :: whole_false ;
}
