class shy_macosx_platform_render
{
    friend class shy_macosx_platform_render_insider ;
public :
    static void set_texel_color 
        ( so_called_type_platform_render_texel_data & texel 
        , so_called_type_platform_math_num_fract r 
        , so_called_type_platform_math_num_fract g 
        , so_called_type_platform_math_num_fract b 
        , so_called_type_platform_math_num_fract a 
        ) ;
    static void set_vertex_color 
        ( so_called_type_platform_render_vertex_data & vertex 
        , so_called_type_platform_math_num_fract r 
        , so_called_type_platform_math_num_fract g 
        , so_called_type_platform_math_num_fract b 
        , so_called_type_platform_math_num_fract a 
        ) ;
    static void set_vertex_position 
        ( so_called_type_platform_render_vertex_data & vertex 
        , so_called_type_platform_math_num_fract x 
        , so_called_type_platform_math_num_fract y 
        , so_called_type_platform_math_num_fract z 
        ) ;
    static void set_vertex_tex_coord 
        ( so_called_type_platform_render_vertex_data & vertex 
        , so_called_type_platform_math_num_fract u 
        , so_called_type_platform_math_num_fract v 
        ) ;
    static void mapped_vertex_buffer_element 
        ( so_called_type_platform_pointer_data < so_called_type_platform_render_vertex_data > & ptr 
        , so_called_type_platform_render_vertex_buffer_mapped_data data 
        , so_called_type_platform_math_num_whole index 
        ) ;
    static void mapped_index_buffer_element 
        ( so_called_type_platform_pointer_data < so_called_type_platform_render_index_data > & ptr 
        , so_called_type_platform_render_index_buffer_mapped_data data 
        , so_called_type_platform_math_num_whole index 
        ) ;
    static void create_texture_resource_id 
        ( so_called_type_platform_render_texture_resource_id & resource_id 
        , so_called_type_platform_math_num_whole resource_index 
        ) ;
    static void set_index_value 
        ( so_called_type_platform_render_index_data & data 
        , so_called_type_platform_math_num_whole index 
        ) ;

    static void enable_face_culling ( ) ;
    
    static void enable_depth_test ( ) ;
    static void disable_depth_test ( ) ;
    
    static void fog_disable ( ) ;
    static void fog_linear 
        ( so_called_type_platform_math_num_fract znear 
        , so_called_type_platform_math_num_fract zfar 
        , so_called_type_platform_math_num_fract r 
        , so_called_type_platform_math_num_fract g 
        , so_called_type_platform_math_num_fract b 
        , so_called_type_platform_math_num_fract a 
        ) ;
    
    static void blend_disable ( ) ;
    static void blend_src_alpha_dst_one_minus_alpha ( ) ;
    
    static void enable_texturing ( ) ;
    static void disable_texturing ( ) ;
    static void texture_mode_modulate ( ) ;
    static void use_texture ( so_called_type_platform_render_texture_id arg_texture_id ) ;
    static void create_texture_id ( so_called_type_platform_render_texture_id & arg_texture_id , so_called_type_platform_math_num_whole size_pow2_base ) ;
    static void texture_loader_ready ( so_called_type_platform_math_num_whole & is_ready ) ;

    static void clear_screen 
        ( so_called_type_platform_math_num_fract r 
        , so_called_type_platform_math_num_fract g 
        , so_called_type_platform_math_num_fract b 
        ) ;    
    static void projection_frustum 
        ( so_called_type_platform_math_num_fract left 
        , so_called_type_platform_math_num_fract right 
        , so_called_type_platform_math_num_fract bottom 
        , so_called_type_platform_math_num_fract top 
        , so_called_type_platform_math_num_fract znear 
        , so_called_type_platform_math_num_fract zfar 
        ) ;
    static void projection_ortho 
        ( so_called_type_platform_math_num_fract left 
        , so_called_type_platform_math_num_fract right 
        , so_called_type_platform_math_num_fract bottom 
        , so_called_type_platform_math_num_fract top 
        , so_called_type_platform_math_num_fract znear 
        , so_called_type_platform_math_num_fract zfar 
        ) ;
        
    static void matrix_identity ( ) ;
    static void matrix_load ( const so_called_type_platform_matrix_data & matrix ) ;
    static void matrix_mult ( const so_called_type_platform_matrix_data & matrix ) ;
    static void matrix_push ( ) ;
    static void matrix_pop ( ) ;
    
    static void get_aspect_width ( so_called_type_platform_math_num_fract & result ) ;
    static void get_aspect_height ( so_called_type_platform_math_num_fract & result ) ;
    static void get_frame_loss ( so_called_type_platform_math_num_whole & result ) ;
    
    static void delete_vertex_buffer ( so_called_type_platform_render_vertex_buffer_id & arg_buffer_id ) ;
    static void delete_index_buffer ( so_called_type_platform_render_index_buffer_id & arg_buffer_id ) ;
    static void delete_texture_id ( so_called_type_platform_render_texture_id & arg_texture_id ) ;
    
    template < typename texels_array >
    static void load_texture_subdata 
        ( so_called_type_platform_render_texture_id arg_texture_id 
        , so_called_type_platform_math_num_whole x_offset 
        , so_called_type_platform_math_num_whole y_offset 
        , so_called_type_platform_math_num_whole width
        , so_called_type_platform_math_num_whole height
        , const texels_array & data 
        ) ;
    
    template < typename texels_array >
    static void load_texture_resource 
        ( so_called_type_platform_render_texture_resource_id resource_id 
        , so_called_type_platform_math_num_whole size_pow2_base 
        , texels_array & data 
        ) ;
    
    static void create_vertex_buffer 
        ( so_called_type_platform_render_vertex_buffer_id & arg_buffer_id 
        , so_called_type_platform_math_num_whole elements 
        ) ;
    static void map_vertex_buffer 
        ( so_called_type_platform_render_vertex_buffer_mapped_data & data 
        , so_called_type_platform_render_vertex_buffer_id arg_buffer_id 
        ) ;
    static void unmap_vertex_buffer ( so_called_type_platform_render_vertex_buffer_id arg_buffer_id ) ;
    
    static void create_index_buffer 
        ( so_called_type_platform_render_index_buffer_id & arg_buffer_id 
        , so_called_type_platform_math_num_whole elements 
        ) ;
    static void map_index_buffer 
        ( so_called_type_platform_render_index_buffer_mapped_data & data 
        , so_called_type_platform_render_index_buffer_id arg_buffer_id 
        ) ;
    static void unmap_index_buffer ( so_called_type_platform_render_index_buffer_id arg_buffer_id ) ;
    
    static void draw_triangle_strip 
        ( so_called_type_platform_render_vertex_buffer_id vertices_buffer 
        , so_called_type_platform_render_index_buffer_id indices_buffer 
        , so_called_type_platform_math_num_whole indices_count 
        ) ;
    static void draw_triangle_fan 
        ( so_called_type_platform_render_vertex_buffer_id vertices_buffer 
        , so_called_type_platform_render_index_buffer_id indices_buffer 
        , so_called_type_platform_math_num_whole indices_count 
        ) ;

private :
    static void _load_texture_resource 
        ( so_called_type_platform_render_texture_resource_id resource_id 
        , so_called_type_platform_math_num_whole size_pow2_base 
        , so_called_type_platform_render_texel_data * texels 
        ) ;
    static void _load_texture_subdata 
        ( so_called_type_platform_render_texture_id arg_texture_id 
        , so_called_type_platform_math_num_whole x_offset 
        , so_called_type_platform_math_num_whole y_offset 
        , so_called_type_platform_math_num_whole width
        , so_called_type_platform_math_num_whole height
        , const so_called_type_platform_render_texel_data * texels
        ) ;

private :
    static void * _texture_loader ;
    static float _aspect_width ;
    static float _aspect_height ;
    static so_called_type_platform_render_vertex_data _reference_vertex ;
    static void * _vertex_position_offset ;
    static void * _vertex_tex_coord_offset ;
    static void * _vertex_color_offset ;    
} ;

template < typename texels_array >
void shy_macosx_platform_render :: load_texture_subdata 
    ( so_called_type_platform_render_texture_id arg_texture_id 
    , so_called_type_platform_math_num_whole x_offset 
    , so_called_type_platform_math_num_whole y_offset 
    , so_called_type_platform_math_num_whole width
    , so_called_type_platform_math_num_whole height
    , const texels_array & data 
    )
{
    const so_called_type_platform_render_texel_data * texels = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( texels , data ) ;

    _load_texture_subdata ( arg_texture_id , x_offset , y_offset , width , height , texels ) ;
}

template < typename texels_array >
void shy_macosx_platform_render :: load_texture_resource
    ( so_called_type_platform_render_texture_resource_id resource_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    , texels_array & data 
    )
{
    so_called_type_platform_render_texel_data * texels = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( texels , data ) ;
    _load_texture_resource ( resource_id , size_pow2_base , texels ) ;
}
