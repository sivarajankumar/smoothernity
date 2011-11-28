class shy_trace_platform_render_texture_loader
{
public :
    template < typename texels_array >
    static void check_args_load_resource
        ( so_called_platform_render_texture_loader_resource_id_type resource_id 
        , so_called_platform_math_num_whole_type size_pow2_base 
        ) ;
    static void check_args_create_resource_id ( so_called_platform_math_num_whole_type index ) ;

    static void check_resource_id_uninitialized ( so_called_platform_render_texture_loader_resource_id_type ) ;

private :
    static void _check_args_load_resource
        ( so_called_platform_render_texture_loader_resource_id_type resource_id 
        , so_called_platform_math_num_whole_type size_pow2_base 
        , so_called_lib_std_int32_t texels_count
        ) ;
} ;

template < typename texels_array >
void shy_trace_platform_render_texture_loader :: check_args_load_resource
    ( so_called_platform_render_texture_loader_resource_id_type resource_id 
    , so_called_platform_math_num_whole_type size_pow2_base 
    )
{
    so_called_lib_std_int32_t texels_count = 0 ;
    so_called_platform_static_array_insider :: template elements_count < texels_array > ( texels_count ) ;
    _check_args_load_resource ( resource_id , size_pow2_base , texels_count ) ;
}
