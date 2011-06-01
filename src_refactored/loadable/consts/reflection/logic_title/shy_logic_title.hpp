#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_title_consts :: value \
        )

void shy_loadable_consts_reflection_logic_title :: prepare ( )
{
    shy_bind_module_helper ( logic_title ) ;
    shy_bind_value_helper ( appear_pos_angle_periods ) ;
    shy_bind_value_helper ( appear_rubber_first ) ;
    shy_bind_value_helper ( appear_rubber_last ) ;
    shy_bind_value_helper ( appear_duration_in_frames ) ;
    shy_bind_value_helper ( disappear_pos_angle_periods ) ;
    shy_bind_value_helper ( disappear_rubber_first ) ;
    shy_bind_value_helper ( disappear_rubber_last ) ;
    shy_bind_value_helper ( disappear_duration_in_frames ) ;
    shy_bind_value_helper ( scene_scale_min ) ;
    shy_bind_value_helper ( scene_scale_max ) ;
    shy_bind_value_helper ( spin_radius_in_letters ) ;
    shy_bind_value_helper ( frames_between_letters ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
