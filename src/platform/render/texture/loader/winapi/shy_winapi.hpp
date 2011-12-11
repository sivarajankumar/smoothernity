void shy_platform_render_texture_loader_winapi :: init ( )
{
}

void shy_platform_render_texture_loader_winapi :: done ( )
{
}

void shy_platform_render_texture_loader_winapi :: _load_resource
    ( so_called_platform_render_texture_loader_winapi_resource_id_type resource_id 
    , so_called_platform_math_num_whole_type size_pow2_base 
    , so_called_platform_render_texel_data_type * texels 
    )
{
}

void shy_platform_render_texture_loader_winapi :: create_resource_id 
    ( so_called_platform_render_texture_loader_winapi_resource_id_type & resource_id 
    , so_called_platform_math_num_whole_type resource_index 
    )
{
    so_called_trace ( so_called_trace_platform_render_texture_loader :: check_args_create_resource_id ( resource_index ) ) ;
    so_called_platform_math_insider :: num_whole_value_get ( resource_id . _resource_id , resource_index ) ;
}

void shy_platform_render_texture_loader_winapi :: ready ( so_called_platform_math_num_whole_type & is_ready )
{
    so_called_platform_math_insider :: num_whole_value_set ( is_ready , so_called_lib_std_true ) ;
}
