class shy_platform_render_directx
{
public :
    static void init ( ) ;
    static void done ( ) ;

    static void set_texel_color 
        ( so_called_platform_render_directx_texel_data_type & texel 
        , so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void set_vertex_color 
        ( so_called_platform_render_directx_vertex_data_type & vertex 
        , so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    static void set_vertex_position 
        ( so_called_platform_render_directx_vertex_data_type & vertex 
        , so_called_platform_math_num_fract_type x 
        , so_called_platform_math_num_fract_type y 
        , so_called_platform_math_num_fract_type z 
        ) ;
    static void set_vertex_tex_coord 
        ( so_called_platform_render_directx_vertex_data_type & vertex 
        , so_called_platform_math_num_fract_type u 
        , so_called_platform_math_num_fract_type v 
        ) ;
    static void mapped_vertex_buffer_element 
        ( so_called_platform_pointer_data_type < so_called_platform_render_directx_vertex_data_type > & ptr 
        , so_called_platform_render_directx_vertex_buffer_mapped_data_type data 
        , so_called_platform_math_num_whole_type index 
        ) ;
    static void mapped_index_buffer_element 
        ( so_called_platform_pointer_data_type < so_called_platform_render_directx_index_data_type > & ptr 
        , so_called_platform_render_directx_index_buffer_mapped_data_type data 
        , so_called_platform_math_num_whole_type index 
        ) ;
    static void set_index_value 
        ( so_called_platform_render_directx_index_data_type & data 
        , so_called_platform_math_num_whole_type index 
        ) ;

    static void enable_face_culling ( ) ;
    
    static void enable_depth_test ( ) ;
    static void disable_depth_test ( ) ;
    
    static void fog_disable ( ) ;
    static void fog_linear 
        ( so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        , so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        , so_called_platform_math_num_fract_type a 
        ) ;
    
    static void blend_disable ( ) ;
    static void blend_src_alpha_dst_one_minus_alpha ( ) ;
    
    static void enable_texturing ( ) ;
    static void disable_texturing ( ) ;
    static void texture_mode_modulate ( ) ;
    static void use_texture ( so_called_platform_render_directx_texture_id_type arg_texture_id ) ;
    static void create_texture_id ( so_called_platform_render_directx_texture_id_type & arg_texture_id , so_called_platform_math_num_whole_type size_pow2_base ) ;

    static void clear_screen 
        ( so_called_platform_math_num_fract_type r 
        , so_called_platform_math_num_fract_type g 
        , so_called_platform_math_num_fract_type b 
        ) ;    
    static void projection_frustum 
        ( so_called_platform_math_num_fract_type left 
        , so_called_platform_math_num_fract_type right 
        , so_called_platform_math_num_fract_type bottom 
        , so_called_platform_math_num_fract_type top 
        , so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        ) ;
    static void projection_ortho 
        ( so_called_platform_math_num_fract_type left 
        , so_called_platform_math_num_fract_type right 
        , so_called_platform_math_num_fract_type bottom 
        , so_called_platform_math_num_fract_type top 
        , so_called_platform_math_num_fract_type znear 
        , so_called_platform_math_num_fract_type zfar 
        ) ;
        
    static void matrix_identity ( ) ;
    static void matrix_load ( const so_called_platform_matrix_data_type & matrix ) ;
    static void matrix_mult ( const so_called_platform_matrix_data_type & matrix ) ;
    static void matrix_push ( ) ;
    static void matrix_pop ( ) ;
    
    static void get_aspect_width ( so_called_platform_math_num_fract_type & result ) ;
    static void get_aspect_height ( so_called_platform_math_num_fract_type & result ) ;
    static void get_frame_loss ( so_called_platform_math_num_whole_type & result ) ;
    
    static void delete_vertex_buffer ( so_called_platform_render_directx_vertex_buffer_id_type & arg_buffer_id ) ;
    static void delete_index_buffer ( so_called_platform_render_directx_index_buffer_id_type & arg_buffer_id ) ;
    static void delete_texture_id ( so_called_platform_render_directx_texture_id_type & arg_texture_id ) ;
    
    template < typename texels_array >
    static void load_texture_subdata 
        ( so_called_platform_render_directx_texture_id_type arg_texture_id 
        , so_called_platform_math_num_whole_type x_offset 
        , so_called_platform_math_num_whole_type y_offset 
        , so_called_platform_math_num_whole_type width
        , so_called_platform_math_num_whole_type height
        , const texels_array & data 
        ) ;
    
    static void create_vertex_buffer 
        ( so_called_platform_render_directx_vertex_buffer_id_type & arg_buffer_id 
        , so_called_platform_math_num_whole_type elements 
        ) ;
    static void map_vertex_buffer 
        ( so_called_platform_render_directx_vertex_buffer_mapped_data_type & data 
        , so_called_platform_render_directx_vertex_buffer_id_type arg_buffer_id 
        ) ;
    static void unmap_vertex_buffer ( so_called_platform_render_directx_vertex_buffer_id_type arg_buffer_id ) ;
    
    static void create_index_buffer 
        ( so_called_platform_render_directx_index_buffer_id_type & arg_buffer_id 
        , so_called_platform_math_num_whole_type elements 
        ) ;
    static void map_index_buffer 
        ( so_called_platform_render_directx_index_buffer_mapped_data_type & data 
        , so_called_platform_render_directx_index_buffer_id_type arg_buffer_id 
        ) ;
    static void unmap_index_buffer ( so_called_platform_render_directx_index_buffer_id_type arg_buffer_id ) ;
    
    static void draw_triangle_strip 
        ( so_called_platform_render_directx_vertex_buffer_id_type vertices_buffer 
        , so_called_platform_render_directx_index_buffer_id_type indices_buffer 
        , so_called_platform_math_num_whole_type indices_count 
        ) ;
    static void draw_triangle_fan 
        ( so_called_platform_render_directx_vertex_buffer_id_type vertices_buffer 
        , so_called_platform_render_directx_index_buffer_id_type indices_buffer 
        , so_called_platform_math_num_whole_type indices_count 
        ) ;

private :
    static void _load_texture_subdata 
        ( so_called_platform_render_directx_texture_id_type arg_texture_id 
        , so_called_platform_math_num_whole_type x_offset 
        , so_called_platform_math_num_whole_type y_offset 
        , so_called_platform_math_num_whole_type width
        , so_called_platform_math_num_whole_type height
        , const so_called_platform_render_directx_texel_data_type * texels
        ) ;
} ;

template < typename texels_array >
void shy_platform_render_directx :: load_texture_subdata 
    ( so_called_platform_render_directx_texture_id_type arg_texture_id 
    , so_called_platform_math_num_whole_type x_offset 
    , so_called_platform_math_num_whole_type y_offset 
    , so_called_platform_math_num_whole_type width
    , so_called_platform_math_num_whole_type height
    , const texels_array & data 
    )
{
    so_called_profile ( so_called_profile_platform_render :: texture_subdata ( ) ) ;
    const so_called_platform_render_directx_texel_data_type * texels = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( texels , data ) ;

    _load_texture_subdata ( arg_texture_id , x_offset , y_offset , width , height , texels ) ;
}


