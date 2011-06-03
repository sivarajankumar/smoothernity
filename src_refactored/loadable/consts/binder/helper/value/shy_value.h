#define shy_loadable_consts_binder_helper_value(module,value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_##module##_consts :: value \
        )
