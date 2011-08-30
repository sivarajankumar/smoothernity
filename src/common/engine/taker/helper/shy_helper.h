#define shy_common_engine_taker_helper(what) \
    so_called_common_engine_taker \
        < so_called_common_##what##_checker \
        , so_called_common_##what##_reply_message \
        , so_called_common_##what##_request_message \
        , so_called_common_##what##_request_sender \
        >
