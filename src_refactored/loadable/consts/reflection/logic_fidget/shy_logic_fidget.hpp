#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_fidget_consts :: value \
        )

void shy_loadable_consts_reflection_logic_fidget :: prepare ( )
{
    shy_bind_module_helper ( logic_fidget ) ;
    shy_bind_value_helper ( fidget_size ) ;
    shy_bind_value_helper ( fidget_r ) ;
    shy_bind_value_helper ( fidget_g ) ;
    shy_bind_value_helper ( fidget_b ) ;
    shy_bind_value_helper ( mesh_x ) ;
    shy_bind_value_helper ( mesh_y_from_top ) ;
    shy_bind_value_helper ( mesh_z ) ;
    shy_bind_value_helper ( angle_delta ) ;
    shy_bind_value_helper ( fidget_edges ) ;
    shy_bind_value_helper ( scale_in_frames ) ;
    shy_bind_value_helper ( should_render_fidget ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
