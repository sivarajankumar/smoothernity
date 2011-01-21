class shy_guts
{
public :
    class consts
    {
    public :
        static const so_called_type_platform_math_num_whole texture_size_pow2_base ;
        static const so_called_type_platform_math_num_whole max_vertices ;
        static const so_called_type_platform_math_num_whole max_indices ;
        static so_called_type_platform_math_const_int_32 max_meshes = 100 ;
        static so_called_type_platform_math_const_int_32 max_textures = 10 ;
    } ;

    class texture_data
    {
    public :
        so_called_type_platform_static_array_data 
            < so_called_type_platform_render_texel_data 
            , so_called_common_engine_render_consts :: texture_size_int
            * so_called_common_engine_render_consts :: texture_size_int
            > texels ;
        so_called_type_platform_render_texture_id render_id ;
    } ;

    class mesh_data
    {
    public :
        so_called_type_platform_math_num_whole finalized ;
        
        so_called_type_platform_render_vertex_buffer_id vertex_buffer_id ;
        so_called_type_platform_render_index_buffer_id triangle_strip_index_buffer_id ;
        so_called_type_platform_render_index_buffer_id triangle_fan_index_buffer_id ;
        
        so_called_type_platform_render_vertex_buffer_mapped_data vertex_buffer_mapped_data ;
        so_called_type_platform_render_index_buffer_mapped_data triangle_strip_index_buffer_mapped_data ;
        so_called_type_platform_render_index_buffer_mapped_data triangle_fan_index_buffer_mapped_data ;
        
        so_called_type_platform_math_num_whole vertices_count ;
        so_called_type_platform_math_num_whole triangle_strip_indices_count ;
        so_called_type_platform_math_num_whole triangle_fan_indices_count ;
        
        so_called_type_platform_matrix_data transform ;
    } ;

    static so_called_type_platform_static_array_data < texture_data , consts :: max_textures > textures_datas ;
    static so_called_type_platform_static_array_data < mesh_data , consts :: max_meshes > meshes_datas ;
    static so_called_type_platform_static_array_data < so_called_type_platform_math_num_whole , consts :: max_meshes > vacant_mesh_ids ;
    static so_called_type_platform_math_num_whole next_texture_id ;
    static so_called_type_platform_math_num_whole next_vacant_mesh_id_index ;
} ;

const so_called_type_platform_math_num_whole shy_guts :: consts :: texture_size_pow2_base
    = so_called_platform_math :: init_num_whole ( so_called_common_engine_render_consts :: texture_size_pow2_base_int ) ;
const so_called_type_platform_math_num_whole shy_guts :: consts :: max_vertices 
    = so_called_platform_math :: init_num_whole ( 300 ) ;
const so_called_type_platform_math_num_whole shy_guts :: consts :: max_indices
    = so_called_platform_math :: init_num_whole ( 300 ) ;

so_called_type_platform_static_array_data < shy_guts :: texture_data , shy_guts :: consts :: max_textures >
    shy_guts :: textures_datas ;
so_called_type_platform_static_array_data < shy_guts :: mesh_data , shy_guts :: consts :: max_meshes >
    shy_guts :: meshes_datas ;
so_called_type_platform_static_array_data < so_called_type_platform_math_num_whole , shy_guts :: consts :: max_meshes >
    shy_guts :: vacant_mesh_ids ;
so_called_type_platform_math_num_whole shy_guts :: next_texture_id ;
so_called_type_platform_math_num_whole shy_guts :: next_vacant_mesh_id_index ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_render > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_aspect_request )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_blend_disable )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_blend_src_alpha_dst_one_minus_alpha )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_clear_screen )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_disable_depth_test )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_done )
{
    so_called_type_platform_math_num_whole whole_max_meshes ;
    so_called_platform_math :: make_num_whole ( whole_max_meshes , shy_guts :: consts :: max_meshes ) ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_meshes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , i ) ;
        
        so_called_platform_render :: delete_vertex_buffer ( mesh . get ( ) . vertex_buffer_id ) ;
        so_called_platform_render :: delete_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id ) ;
        so_called_platform_render :: delete_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id ) ;
    }

    so_called_type_platform_math_num_whole whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_textures )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , i ) ;
        so_called_platform_render :: delete_texture_id ( texture . get ( ) . render_id ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_enable_depth_test )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_enable_face_culling )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_fog_disable )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_fog_linear )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_frame_loss_request )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_init )
{
    shy_guts :: next_texture_id = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: next_vacant_mesh_id_index = so_called_platform_math_consts :: whole_0 ;
    
    so_called_type_platform_math_num_whole whole_max_meshes ;
    so_called_platform_math :: make_num_whole ( whole_max_meshes , shy_guts :: consts :: max_meshes ) ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_meshes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , i ) ;
        
        so_called_platform_render :: create_vertex_buffer ( mesh . get ( ) . vertex_buffer_id , shy_guts :: consts :: max_vertices ) ;
        so_called_platform_render :: create_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id , shy_guts :: consts :: max_indices ) ;
        so_called_platform_render :: create_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id , shy_guts :: consts :: max_indices ) ;

        so_called_type_platform_pointer_data < so_called_type_platform_math_num_whole > vacant_id ;
        so_called_platform_static_array :: element_ptr ( vacant_id , shy_guts :: vacant_mesh_ids , i ) ;
        vacant_id . get ( ) = i ;
    }
    
    so_called_type_platform_math_num_whole whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_textures )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , i ) ;
        so_called_platform_render :: create_texture_id ( texture . get ( ) . render_id , shy_guts :: consts :: texture_size_pow2_base ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_matrix_identity )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_matrix_load )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_matrix_mult )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_create_request )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_delete )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_finalize )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_render )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_transform )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_triangle_fan_index_value )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_triangle_strip_index_value )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_vertex_color )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_vertex_position )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_mesh_set_vertex_tex_coord )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_projection_frustum )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_projection_ortho )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_create_request )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_finalize )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_load_from_resource )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_loader_ready_request )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_mode_modulate )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_select )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_set_texel )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_set_texel_rgba )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_set_texels_rect )
{
}

void _shy_common_engine_render :: receive ( so_called_message_common_engine_render_texture_unselect )
{
}

