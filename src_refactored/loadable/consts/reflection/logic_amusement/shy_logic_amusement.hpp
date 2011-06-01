#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind \
        ( #value \
        , so_called_common_logic_amusement_consts :: value \
        )

void shy_loadable_consts_reflection_logic_amusement :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_amusement" ) ;
    shy_bind_value_helper ( renderer_clear_color_r ) ;
    shy_bind_value_helper ( renderer_clear_color_g ) ;
    shy_bind_value_helper ( renderer_clear_color_b ) ;
}

#undef shy_bind_value_helper
