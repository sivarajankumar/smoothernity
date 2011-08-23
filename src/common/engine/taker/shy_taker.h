template 
    < typename type_checker
    , typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
class shy_common_engine_taker
{
public :
    void init ( ) ;
    void request ( ) ;
    void should_handle ( so_called_type_platform_math_num_whole & , type_message_reply ) ;
public :
    type_message_reply msg_reply ;
    type_message_request msg_request ;
private :
    so_called_type_platform_math_num_whole _requested ;
} ;

template 
    < typename type_checker
    , typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void shy_common_engine_taker < type_checker , type_message_reply , type_message_request , type_sender_request > :: request ( )
{
    _requested = so_called_platform_math_consts :: whole_true ;
    type_sender_request :: send ( msg_request ) ;
}

template 
    < typename type_checker
    , typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void shy_common_engine_taker < type_checker , type_message_reply , type_message_request , type_sender_request > :: init ( )
{
    _requested = so_called_platform_math_consts :: whole_false ;
}

template 
    < typename type_checker
    , typename type_message_reply 
    , typename type_message_request
    , typename type_sender_request
    >
void shy_common_engine_taker < type_checker , type_message_reply , type_message_request , type_sender_request > :: should_handle
    ( so_called_type_platform_math_num_whole & result
    , type_message_reply msg
    )
{
    so_called_type_platform_math_num_whole match ;
    type_checker :: check ( match , msg_request , msg ) ;
    if ( so_called_platform_conditions :: whole_is_true ( _requested ) 
      && so_called_platform_conditions :: whole_is_true ( match )
       )
    {
        _requested = so_called_platform_math_consts :: whole_false ;
        msg_reply = msg ;
        result = so_called_platform_math_consts :: whole_true ;
    }
    else
        result = so_called_platform_math_consts :: whole_false ;
}

