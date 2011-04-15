void shy_loadable_consts_reflection_logic_fidget :: prepare ( )
{
    so_called_loadable_consts_binder :: module ( "logic_fidget" ) ;
    so_called_loadable_consts_binder :: bind ( "fidget_size" , so_called_common_logic_fidget_consts :: fidget_size ) ;
    so_called_loadable_consts_binder :: bind ( "fidget_r" , so_called_common_logic_fidget_consts :: fidget_r ) ;
    so_called_loadable_consts_binder :: bind ( "fidget_g" , so_called_common_logic_fidget_consts :: fidget_g ) ;
    so_called_loadable_consts_binder :: bind ( "fidget_b" , so_called_common_logic_fidget_consts :: fidget_b ) ;
    so_called_loadable_consts_binder :: bind ( "mesh_x" , so_called_common_logic_fidget_consts :: mesh_x ) ;
    so_called_loadable_consts_binder :: bind ( "mesh_y_from_top" , so_called_common_logic_fidget_consts :: mesh_y_from_top ) ;
    so_called_loadable_consts_binder :: bind ( "mesh_z" , so_called_common_logic_fidget_consts :: mesh_z ) ;
    so_called_loadable_consts_binder :: bind ( "angle_delta" , so_called_common_logic_fidget_consts :: angle_delta ) ;
    so_called_loadable_consts_binder :: bind ( "fidget_edges" , so_called_common_logic_fidget_consts :: fidget_edges ) ;
    so_called_loadable_consts_binder :: bind ( "scale_in_frames" , so_called_common_logic_fidget_consts :: scale_in_frames ) ;
    so_called_loadable_consts_binder :: bind ( "should_render_fidget" , so_called_common_logic_fidget_consts :: should_render_fidget ) ;
}
