void * shy_macosx_platform_render_texture_loader :: _texture_loader = 0 ;

void shy_macosx_platform_render_texture_loader :: _load_resource
    ( so_called_type_platform_render_texture_loader_resource_id resource_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    , so_called_type_platform_render_texel_data * texels 
    )
{
    so_called_lib_std_int32_t size_pow2_base_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    shy_macosx_texture_loader * loader = reinterpret_cast < shy_macosx_texture_loader * > ( _texture_loader ) ;
    [ loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) texels
        with_side_size_of : 1 << size_pow2_base_int
    ] ;
}

void shy_macosx_platform_render_texture_loader :: create_resource_id 
    ( so_called_type_platform_render_texture_loader_resource_id & resource_id 
    , so_called_type_platform_math_num_whole resource_index 
    )
{
    so_called_platform_math_insider :: num_whole_value_get ( resource_id . _resource_id , resource_index ) ;
}

void shy_macosx_platform_render_texture_loader :: ready ( so_called_type_platform_math_num_whole & is_ready )
{
    shy_macosx_texture_loader * loader = reinterpret_cast < shy_macosx_texture_loader * > ( _texture_loader ) ;
    so_called_platform_math_insider :: num_whole_value_set ( is_ready , [ loader loader_ready ] ) ;
}
