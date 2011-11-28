class shy_platform_render_texture_loader_winapi
{
public :
    template < typename texels_array >
    static void load_resource 
        ( so_called_platform_render_texture_loader_winapi_resource_id_type resource_id 
        , so_called_platform_math_num_whole_type size_pow2_base 
        , texels_array & data 
        ) ;
    static void create_resource_id 
        ( so_called_platform_render_texture_loader_winapi_resource_id_type &
        , so_called_platform_math_num_whole_type
        ) ;
    static void ready ( so_called_platform_math_num_whole_type & ) ;
    static void init ( ) ;
    static void done ( ) ;
private :
    static void _load_resource 
        ( so_called_platform_render_texture_loader_winapi_resource_id_type resource_id 
        , so_called_platform_math_num_whole_type size_pow2_base 
        , so_called_platform_render_texel_data_type * texels 
        ) ;
} ;

template < typename texels_array >
void shy_platform_render_texture_loader_winapi :: load_resource
    ( so_called_platform_render_texture_loader_winapi_resource_id_type resource_id 
    , so_called_platform_math_num_whole_type size_pow2_base 
    , texels_array & data 
    )
{
    so_called_trace ( so_called_trace_platform_render_texture_loader :: template check_args_load_resource < texels_array > ( resource_id , size_pow2_base, data ) ) ;
    so_called_platform_render_texel_data_type * texels = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( texels , data ) ;
    _load_resource ( resource_id , size_pow2_base , texels ) ;
}


