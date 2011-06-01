#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_blanket_animation_consts :: value \
        )

void shy_loadable_consts_reflection_logic_blanket_animation :: prepare ( )
{
    shy_bind_module_helper ( logic_blanket_animation ) ;
    shy_bind_value_helper ( animation_origin_x ) ;
    shy_bind_value_helper ( animation_origin_y ) ;
    shy_bind_value_helper ( animation_origin_z ) ;
    shy_bind_value_helper ( appear_scale_begin ) ;
    shy_bind_value_helper ( appear_scale_end ) ;
    shy_bind_value_helper ( appear_rotation_begin ) ;
    shy_bind_value_helper ( appear_rotation_end ) ;
    shy_bind_value_helper ( appear_time_from_begin_to_end ) ;
    shy_bind_value_helper ( disappear_scale_begin ) ;
    shy_bind_value_helper ( disappear_scale_end ) ;
    shy_bind_value_helper ( disappear_rotation_begin ) ;
    shy_bind_value_helper ( disappear_rotation_end ) ;
    shy_bind_value_helper ( disappear_time_from_begin_to_end ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
