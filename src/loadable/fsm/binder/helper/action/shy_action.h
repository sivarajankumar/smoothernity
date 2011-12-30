#define shy_loadable_fsm_binder_helper_action(system,action) \
    so_called_loadable_fsm_binder :: bind_action \
        ( #action \
        , & so_called_common_##system##_fsm_actions :: action \
        )
