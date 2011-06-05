#define shy_guts_bind_module(module) so_called_loadable_consts_binder_helper_module ( module )
#define shy_guts_bind_value(value) so_called_loadable_consts_binder_helper_value ( logic_fidget , value )

void shy_loadable_consts_reflection_logic_fidget :: prepare ( )
{
    shy_guts_bind_module ( logic_fidget ) ;
    shy_guts_bind_value ( fidget_size ) ;
    shy_guts_bind_value ( fidget_r ) ;
    shy_guts_bind_value ( fidget_g ) ;
    shy_guts_bind_value ( fidget_b ) ;
    shy_guts_bind_value ( mesh_x ) ;
    shy_guts_bind_value ( mesh_y_from_top ) ;
    shy_guts_bind_value ( mesh_z ) ;
    shy_guts_bind_value ( angle_delta ) ;
    shy_guts_bind_value ( fidget_edges ) ;
    shy_guts_bind_value ( scale_in_frames ) ;
    shy_guts_bind_value ( should_render_fidget ) ;
}
