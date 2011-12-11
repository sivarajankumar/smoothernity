class shy_common_engine_render_stateless
{
public :
    static so_called_common_engine_render_mesh_id_type init_mesh_id
        ( so_called_platform_math_const_int_32_type
        ) ;
    static void create_texture_resource_id 
        ( so_called_platform_render_texture_loader_resource_id_type & resource_id
        , so_called_platform_math_num_whole_type resource_index
        ) ;
    static void set_texel_color 
        ( so_called_platform_render_texel_data_type & texel
        , so_called_platform_math_num_fract_type r
        , so_called_platform_math_num_fract_type g
        , so_called_platform_math_num_fract_type b
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void clamp_texture_coords
        ( so_called_platform_math_num_whole_type & x
        , so_called_platform_math_num_whole_type & y
        ) ;
} ;
