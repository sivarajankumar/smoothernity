void shy_common_logic_salutation_letters_animation_layout_transform_checker :: check 
    ( so_called_platform_math_num_whole_type & result
    , so_called_common_logic_salutation_letters_animation_layout_transform_request_message msg_request
    , so_called_common_logic_salutation_letters_animation_layout_transform_reply_message msg_reply
    )
{
    if ( so_called_platform_conditions :: wholes_are_equal ( msg_request . letter , msg_reply . letter ) )
        result = so_called_platform_math_consts :: whole_true ;
    else
        result = so_called_platform_math_consts :: whole_false ;
}
