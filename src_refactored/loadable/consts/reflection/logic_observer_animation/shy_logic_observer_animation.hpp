#define shy_bind_module_helper(module) \
    so_called_loadable_consts_binder :: bind_module \
        ( #module \
        , & so_called_common_##module##_consts :: binding \
        )

#define shy_bind_value_helper(value) \
    so_called_loadable_consts_binder :: bind_value \
        ( #value \
        , so_called_common_logic_observer_animation_consts :: value \
        )

void shy_loadable_consts_reflection_logic_observer_animation :: prepare ( )
{
    shy_bind_module_helper ( logic_observer_animation ) ;
    shy_bind_value_helper ( flight_target_z ) ;
    shy_bind_value_helper ( flight_horizontal_offset_period ) ;
    shy_bind_value_helper ( flight_horizontal_offset_amplitude ) ;
    shy_bind_value_helper ( flight_vertical_offset_period ) ;
    shy_bind_value_helper ( flight_vertical_offset_amplitude ) ;
}

#undef shy_bind_module_helper
#undef shy_bind_value_helper
