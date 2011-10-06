template 
    < typename checker_type
    , typename message_reply_type 
    , typename message_request_type
    , typename sender_request_type
    >
class shy_common_engine_taker
{
public :
    void init ( ) ;
    void request ( ) ;
    void should_handle ( so_called_platform_math_num_whole_type & , message_reply_type ) ;
public :
    message_reply_type msg_reply ;
    message_request_type msg_request ;
private :
    so_called_platform_math_num_whole_type _requested ;
} ;

template 
    < typename checker_type
    , typename message_reply_type 
    , typename message_request_type
    , typename sender_request_type
    >
void shy_common_engine_taker < checker_type , message_reply_type , message_request_type , sender_request_type > :: request ( )
{
    _requested = so_called_platform_math_consts :: whole_true ;
    sender_request_type :: send ( msg_request ) ;
}

template 
    < typename checker_type
    , typename message_reply_type 
    , typename message_request_type
    , typename sender_request_type
    >
void shy_common_engine_taker < checker_type , message_reply_type , message_request_type , sender_request_type > :: init ( )
{
    _requested = so_called_platform_math_consts :: whole_false ;
}

template 
    < typename checker_type
    , typename message_reply_type 
    , typename message_request_type
    , typename sender_request_type
    >
void shy_common_engine_taker < checker_type , message_reply_type , message_request_type , sender_request_type > :: should_handle
    ( so_called_platform_math_num_whole_type & result
    , message_reply_type msg
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( _requested ) )
    {
        so_called_platform_math_num_whole_type match ;
        checker_type :: check ( match , msg_request , msg ) ;
        if ( so_called_platform_conditions :: whole_is_true ( match ) )
        {
            _requested = so_called_platform_math_consts :: whole_false ;
            msg_reply = msg ;
            result = so_called_platform_math_consts :: whole_true ;
        }
    }
    else
        result = so_called_platform_math_consts :: whole_false ;
}

