#define shy_common_engine_taker_helper(what) \
    so_called_common_engine_taker \
        < so_called_common_##what##_checker \
        , so_called_message_common_##what##_reply \
        , so_called_message_common_##what##_request \
        , so_called_sender_common_##what##_request \
        >

#define shy_common_engine_taker_helper_new(what) \
    so_called_common_engine_taker \
        < so_called_common_##what##_checker \
        , so_called_message_common_##what##_reply \
        , so_called_message_common_##what##_request \
        , so_called_common_##what##_request_sender \
        >
