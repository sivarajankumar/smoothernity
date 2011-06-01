#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_application_consts :: value \
        )

void shy_loadable_consts_reflection_logic_application :: prepare ( )
{
    shy_bind_module_helper ( logic_application ) ;
    shy_bind_value_helper ( skip_amusement ) ;
    shy_bind_value_helper ( skip_main_menu ) ;
    shy_bind_value_helper ( skip_salutation ) ;
    shy_bind_value_helper ( skip_title ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
