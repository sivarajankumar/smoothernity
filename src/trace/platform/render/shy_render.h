class shy_trace_platform_render
{
public :
    static void check_args_projection_frustum
        ( so_called_platform_math_num_fract_type left 
        , so_called_platform_math_num_fract_type right 
        , so_called_platform_math_num_fract_type bottom 
        , so_called_platform_math_num_fract_type top 
        , so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        ) ;
    static void check_args_projection_ortho
        ( so_called_platform_math_num_fract_type left 
        , so_called_platform_math_num_fract_type right 
        , so_called_platform_math_num_fract_type bottom 
        , so_called_platform_math_num_fract_type top 
        , so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        ) ;
    static void check_args_fog_linear
        ( so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        , so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void check_args_set_texel_color
        ( so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void check_args_set_vertex_color
        ( so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void check_args_set_vertex_position
        ( so_called_platform_math_num_fract_type x
        , so_called_platform_math_num_fract_type y
        , so_called_platform_math_num_fract_type z
        ) ;
    static void check_args_clear_screen
        ( so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        ) ;
    static void check_args_draw_triangle_fan
        ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
        , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
        , so_called_platform_math_num_whole_type indices_count 
        ) ;
    static void check_args_draw_triangle_strip
        ( so_called_platform_render_opengl_vertex_buffer_id_type vertices_buffer 
        , so_called_platform_render_opengl_index_buffer_id_type indices_buffer 
        , so_called_platform_math_num_whole_type indices_count 
        ) ;
    static void check_args_set_vertex_tex_coord
        ( so_called_platform_math_num_fract_type u
        , so_called_platform_math_num_fract_type v
        ) ;
    static void check_args_mapped_index_buffer_element
        ( so_called_platform_render_opengl_index_buffer_mapped_data_type
        , so_called_platform_math_num_whole_type 
        ) ;
    static void check_args_mapped_vertex_buffer_element
        ( so_called_platform_render_opengl_vertex_buffer_mapped_data_type
        , so_called_platform_math_num_whole_type 
        ) ;
    static void check_args_create_index_buffer ( so_called_platform_math_num_whole_type ) ;
    static void check_args_create_texture_id ( so_called_platform_math_num_whole_type ) ;
    static void check_args_create_vertex_buffer ( so_called_platform_math_num_whole_type ) ;
    static void check_args_map_index_buffer ( so_called_platform_render_index_buffer_id_type ) ;
    static void check_args_map_vertex_buffer ( so_called_platform_render_vertex_buffer_id_type ) ;
    static void check_args_matrix_load ( so_called_platform_matrix_data_type ) ;
    static void check_args_matrix_mult ( so_called_platform_matrix_data_type ) ;
    static void check_args_set_index_value ( so_called_platform_math_num_whole_type ) ;
    static void check_args_unmap_index_buffer ( so_called_platform_render_index_buffer_id_type ) ;
    static void check_args_unmap_vertex_buffer ( so_called_platform_render_vertex_buffer_id_type ) ;
    static void check_args_use_texture ( so_called_platform_render_texture_id_type ) ;
    static void check_index_buffer_id_uninitialized ( so_called_platform_render_index_buffer_id_type ) ;
    static void check_index_buffer_mapped_data_uninitialized ( so_called_platform_render_index_buffer_mapped_data_type ) ;
    static void check_texture_id_uninitialized ( so_called_platform_render_texture_id_type ) ;
    static void check_vertex_buffer_id_uninitialized ( so_called_platform_render_vertex_buffer_id_type ) ;
    static void check_vertex_buffer_mapped_data_uninitialized ( so_called_platform_render_vertex_buffer_mapped_data_type ) ;

    template < typename texels_array >
    static void check_args_load_texture_subdata
        ( so_called_platform_render_opengl_texture_id_type arg_texture_id 
        , so_called_platform_math_num_whole_type x_offset 
        , so_called_platform_math_num_whole_type y_offset 
        , so_called_platform_math_num_whole_type width
        , so_called_platform_math_num_whole_type height
        ) ;
private :
    static void _check_args_load_texture_subdata
        ( so_called_lib_std_int32_t texels_count
        , so_called_platform_render_opengl_texture_id_type arg_texture_id 
        , so_called_platform_math_num_whole_type x_offset 
        , so_called_platform_math_num_whole_type y_offset 
        , so_called_platform_math_num_whole_type width
        , so_called_platform_math_num_whole_type height
        ) ;
} ;

template < typename texels_array >
void shy_trace_platform_render :: check_args_load_texture_subdata
    ( so_called_platform_render_opengl_texture_id_type arg_texture_id 
    , so_called_platform_math_num_whole_type x_offset 
    , so_called_platform_math_num_whole_type y_offset 
    , so_called_platform_math_num_whole_type width
    , so_called_platform_math_num_whole_type height
    )
{
    so_called_lib_std_int32_t texels_count = 0 ;
    so_called_platform_static_array_insider :: template elements_count < texels_array > ( texels_count ) ;
    _check_args_load_texture_subdata ( texels_count , arg_texture_id , x_offset , y_offset , width , height ) ;
}
