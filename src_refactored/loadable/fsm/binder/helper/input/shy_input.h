#define shy_loadable_fsm_binder_helper_input(system,input) \
    so_called_loadable_fsm_binder :: bind_input \
        ( #input \
        , reinterpret_cast < so_called_type_loadable_fsm_content_input_binding > ( & so_called_type_common_##system##_fsm_inputs :: input ) \
        )
