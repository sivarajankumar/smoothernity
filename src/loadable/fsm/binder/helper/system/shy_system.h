#define shy_loadable_fsm_binder_helper_system(system) \
    so_called_loadable_fsm_binder :: bind_system \
        ( #system \
        , & so_called_common_##system##_fsm_binding \
        )
