class shy_macosx_platform_render_texture_loader
{
    friend class shy_macosx_platform_render_texture_loader_insider ;
public :
    template < typename texels_array >
    static void load_resource 
        ( so_called_type_platform_render_texture_loader_resource_id resource_id 
        , so_called_type_platform_math_num_whole size_pow2_base 
        , texels_array & data 
        ) ;
    static void create_resource_id 
        ( so_called_type_platform_render_texture_loader_resource_id &
        , so_called_type_platform_math_num_whole
        ) ;
    static void ready ( so_called_type_platform_math_num_whole & ) ;
private :
    static void _load_resource 
        ( so_called_type_platform_render_texture_loader_resource_id resource_id 
        , so_called_type_platform_math_num_whole size_pow2_base 
        , so_called_type_platform_render_texel_data * texels 
        ) ;
} ;

template < typename texels_array >
void shy_macosx_platform_render_texture_loader :: load_resource
    ( so_called_type_platform_render_texture_loader_resource_id resource_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    , texels_array & data 
    )
{
    so_called_type_platform_render_texel_data * texels = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( texels , data ) ;
    _load_resource ( resource_id , size_pow2_base , texels ) ;
}

