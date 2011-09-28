namespace shy_guts
{
    namespace consts
    {
        static const so_called_platform_math_num_whole_type texture_size_pow2_base
            = so_called_platform_math :: init_num_whole ( so_called_common_engine_render_consts :: texture_size_pow2_base_int ) ;
        static const so_called_platform_math_num_whole_type max_vertices
            = so_called_platform_math :: init_num_whole ( 300 ) ;
        static const so_called_platform_math_num_whole_type max_indices
            = so_called_platform_math :: init_num_whole ( 300 ) ;
        static so_called_platform_math_const_int_32_type max_textures = 10 ;
    }

    class texture_data
    {
    public :
        so_called_platform_static_array_data_type 
            < so_called_platform_render_texel_data_type 
            , so_called_common_engine_render_consts :: texture_size_int
            * so_called_common_engine_render_consts :: texture_size_int
            > texels ;
        so_called_platform_render_texture_id_type render_id ;
    } ;

    class mesh_data
    {
    public :
        so_called_platform_math_num_whole_type finalized ;
        
        so_called_platform_render_vertex_buffer_id_type vertex_buffer_id ;
        so_called_platform_render_index_buffer_id_type triangle_strip_index_buffer_id ;
        so_called_platform_render_index_buffer_id_type triangle_fan_index_buffer_id ;
        
        so_called_platform_render_vertex_buffer_mapped_data_type vertex_buffer_mapped_data ;
        so_called_platform_render_index_buffer_mapped_data_type triangle_strip_index_buffer_mapped_data ;
        so_called_platform_render_index_buffer_mapped_data_type triangle_fan_index_buffer_mapped_data ;
        
        so_called_platform_math_num_whole_type vertices_count ;
        so_called_platform_math_num_whole_type triangle_strip_indices_count ;
        so_called_platform_math_num_whole_type triangle_fan_indices_count ;
        
        so_called_platform_matrix_data_type transform ;
    } ;

    static so_called_platform_static_array_data_type < texture_data , consts :: max_textures > textures_datas ;
    static so_called_platform_static_array_data_type < mesh_data , so_called_common_engine_render_consts :: max_meshes_int > meshes_datas ;
    static so_called_platform_static_array_data_type < so_called_platform_math_num_whole_type , so_called_common_engine_render_consts :: max_meshes_int > vacant_mesh_ids ;
    static so_called_platform_math_num_whole_type next_texture_id ;
    static so_called_platform_math_num_whole_type next_vacant_mesh_id_index ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_engine_render , 3000 > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_engine_render :: receive ( so_called_common_engine_render_aspect_request_message )
{
    so_called_common_engine_render_aspect_reply_message reply_msg ;
    so_called_platform_render :: get_aspect_width ( reply_msg . width ) ;
    so_called_platform_render :: get_aspect_height ( reply_msg . height ) ;
    so_called_common_engine_render_aspect_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_blend_disable_message )
{
    so_called_platform_render :: blend_disable ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_blend_src_alpha_dst_one_minus_alpha_message )
{
    so_called_platform_render :: blend_src_alpha_dst_one_minus_alpha ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_clear_screen_message msg )
{
    so_called_platform_render :: clear_screen ( msg . r , msg . g , msg . b ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_disable_depth_test_message )
{
    so_called_platform_render :: disable_depth_test ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_done_message )
{
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_common_engine_render_consts :: max_meshes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , i ) ;
        
        so_called_platform_render :: delete_vertex_buffer ( mesh . get ( ) . vertex_buffer_id ) ;
        so_called_platform_render :: delete_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id ) ;
        so_called_platform_render :: delete_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id ) ;
    }

    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_textures )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , i ) ;
        so_called_platform_render :: delete_texture_id ( texture . get ( ) . render_id ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_enable_depth_test_message )
{
    so_called_platform_render :: enable_depth_test ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_enable_face_culling_message )
{
    so_called_platform_render :: enable_face_culling ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_fog_disable_message )
{
    so_called_platform_render :: fog_disable ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_fog_linear_message msg )
{
    so_called_platform_render :: fog_linear ( msg . z_near , msg . z_far , msg . r , msg . g , msg . b , msg . a ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_frame_loss_request_message )
{
    so_called_common_engine_render_frame_loss_reply_message reply_msg ;
    so_called_platform_render :: get_frame_loss ( reply_msg . frame_loss ) ;
    so_called_common_engine_render_frame_loss_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_init_message )
{
    shy_guts :: next_texture_id = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: next_vacant_mesh_id_index = so_called_platform_math_consts :: whole_0 ;
    
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , so_called_common_engine_render_consts :: max_meshes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , i ) ;
        
        so_called_platform_render :: create_vertex_buffer ( mesh . get ( ) . vertex_buffer_id , shy_guts :: consts :: max_vertices ) ;
        so_called_platform_render :: create_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id , shy_guts :: consts :: max_indices ) ;
        so_called_platform_render :: create_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id , shy_guts :: consts :: max_indices ) ;

        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > vacant_id ;
        so_called_platform_static_array :: element_ptr ( vacant_id , shy_guts :: vacant_mesh_ids , i ) ;
        vacant_id . get ( ) = i ;
    }
    
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_textures )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , i ) ;
        so_called_platform_render :: create_texture_id ( texture . get ( ) . render_id , shy_guts :: consts :: texture_size_pow2_base ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_matrix_identity_message )
{
    so_called_platform_render :: matrix_identity ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_matrix_load_message msg )
{
    so_called_platform_render :: matrix_load ( msg . matrix ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_matrix_mult_message msg )
{
    so_called_platform_render :: matrix_mult ( msg . matrix ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_create_request_message msg )
{
    so_called_common_engine_render_mesh_id_type created_mesh ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: next_vacant_mesh_id_index , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > vacant_mesh_id ;
        so_called_platform_static_array :: element_ptr ( vacant_mesh_id , shy_guts :: vacant_mesh_ids , shy_guts :: next_vacant_mesh_id_index ) ;
        
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , vacant_mesh_id . get ( ) ) ;

        mesh . get ( ) . finalized = so_called_platform_math_consts :: whole_false ;
        mesh . get ( ) . vertices_count = msg . vertices ;
        mesh . get ( ) . triangle_strip_indices_count = msg . triangle_strip_indices ;
        mesh . get ( ) . triangle_fan_indices_count = msg . triangle_fan_indices ;
        so_called_platform_matrix :: identity ( mesh . get ( ) . transform ) ;

        if ( so_called_platform_conditions :: whole_greater_than_whole ( msg . vertices , shy_guts :: consts :: max_vertices ) )
        {
            mesh . get ( ) . vertices_count = shy_guts :: consts :: max_vertices ;
            so_called_trace ( so_called_trace_common_engine_render :: mesh_too_many_vertices_error ( msg . vertices , shy_guts :: consts :: max_vertices ) ) ;
        }

        if ( so_called_platform_conditions :: whole_greater_than_whole ( msg . triangle_strip_indices , shy_guts :: consts :: max_indices ) )
        {
            mesh . get ( ) . triangle_strip_indices_count = shy_guts :: consts :: max_indices ;
            so_called_trace ( so_called_trace_common_engine_render :: mesh_too_many_indices_error ( msg . triangle_strip_indices , shy_guts :: consts :: max_indices ) ) ;
        }

        if ( so_called_platform_conditions :: whole_greater_than_whole ( msg . triangle_fan_indices , shy_guts :: consts :: max_indices ) )
        {
            mesh . get ( ) . triangle_fan_indices_count = shy_guts :: consts :: max_indices ;
            so_called_trace ( so_called_trace_common_engine_render :: mesh_too_many_indices_error ( msg . triangle_fan_indices , shy_guts :: consts :: max_indices ) ) ;
        }
          
        so_called_platform_render :: map_vertex_buffer ( mesh . get ( ) . vertex_buffer_mapped_data , mesh . get ( ) . vertex_buffer_id ) ;
        so_called_platform_render :: map_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_mapped_data , mesh . get ( ) . triangle_strip_index_buffer_id ) ;
        so_called_platform_render :: map_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_mapped_data , mesh . get ( ) . triangle_fan_index_buffer_id ) ;
        
        created_mesh . _mesh_id = vacant_mesh_id . get ( ) ;
        so_called_platform_math :: inc_whole ( shy_guts :: next_vacant_mesh_id_index ) ;
        so_called_trace ( so_called_trace_common_engine_render :: meshes_in_use ( shy_guts :: next_vacant_mesh_id_index , so_called_common_engine_render_consts :: max_meshes ) ) ;
    }
    else
    {
        created_mesh = so_called_common_engine_render_consts :: null_mesh ;
        so_called_trace ( so_called_trace_common_engine_render :: meshes_overflow_error ( ) ) ;
    }

    so_called_common_engine_render_mesh_create_reply_message reply_msg ;
    reply_msg . mesh = created_mesh ;
    so_called_common_engine_render_mesh_create_reply_sender :: send ( reply_msg ) ;    
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_delete_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        if ( so_called_platform_conditions :: whole_greater_than_zero ( shy_guts :: next_vacant_mesh_id_index ) )
        {
            so_called_platform_math :: dec_whole ( shy_guts :: next_vacant_mesh_id_index ) ;
            so_called_trace ( so_called_trace_common_engine_render :: meshes_in_use ( shy_guts :: next_vacant_mesh_id_index , so_called_common_engine_render_consts :: max_meshes ) ) ;
            so_called_platform_pointer_data_type < so_called_platform_math_num_whole_type > vacant_mesh_id ;
            so_called_platform_static_array :: element_ptr ( vacant_mesh_id , shy_guts :: vacant_mesh_ids , shy_guts :: next_vacant_mesh_id_index ) ;
            vacant_mesh_id . get ( ) = msg . mesh . _mesh_id ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: meshes_underflow_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_finalize_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        mesh . get ( ) . finalized = so_called_platform_math_consts :: whole_true ;
        so_called_platform_render :: unmap_vertex_buffer ( mesh . get ( ) . vertex_buffer_id ) ;
        so_called_platform_render :: unmap_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id ) ;
        so_called_platform_render :: unmap_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_render_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_true ( mesh . get ( ) . finalized ) )
        {
            so_called_platform_render :: matrix_push ( ) ;
            so_called_platform_render :: matrix_mult ( mesh . get ( ) . transform ) ;
            if ( so_called_platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_strip_indices_count ) )
            {
                so_called_platform_render :: draw_triangle_strip 
                    ( mesh . get ( ) . vertex_buffer_id 
                    , mesh . get ( ) . triangle_strip_index_buffer_id 
                    , mesh . get ( ) . triangle_strip_indices_count
                    ) ;
            }
            if ( so_called_platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_fan_indices_count ) )
            {
                so_called_platform_render :: draw_triangle_fan 
                    ( mesh . get ( ) . vertex_buffer_id 
                    , mesh . get ( ) . triangle_fan_index_buffer_id 
                    , mesh . get ( ) . triangle_fan_indices_count
                    ) ;
            }
            so_called_platform_render :: matrix_pop ( ) ;
        }
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_transform_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        mesh . get ( ) . transform = msg . transform ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_triangle_fan_index_value_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_pointer_data_type < so_called_platform_render_index_data_type > index ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) )
        {
            if ( so_called_platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . triangle_fan_indices_count ) )
            {
                if ( so_called_platform_conditions :: whole_less_than_whole ( msg . index , mesh . get ( ) . vertices_count ) )
                {
                    so_called_platform_render :: mapped_index_buffer_element ( index , mesh . get ( ) . triangle_fan_index_buffer_mapped_data , msg . offset ) ;
                    so_called_platform_render :: set_index_value ( index . get ( ) , msg . index ) ;
                }
                else
                    so_called_trace ( so_called_trace_common_engine_render :: mesh_index_value_out_of_range_error ( msg . index , mesh . get ( ) . vertices_count ) ) ;
            }
            else
                so_called_trace ( so_called_trace_common_engine_render :: mesh_index_offset_out_of_range_error ( msg . offset , mesh . get ( ) . triangle_fan_indices_count ) ) ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_pointer_data_type < so_called_platform_render_index_data_type > index ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) )
        {
            if ( so_called_platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . triangle_strip_indices_count ) )
            {
                if ( so_called_platform_conditions :: whole_less_than_whole ( msg . index , mesh . get ( ) . vertices_count ) )
                {
                    so_called_platform_render :: mapped_index_buffer_element ( index , mesh . get ( ) . triangle_strip_index_buffer_mapped_data , msg . offset ) ;
                    so_called_platform_render :: set_index_value ( index . get ( ) , msg . index ) ;
                }
                else
                    so_called_trace ( so_called_trace_common_engine_render :: mesh_index_value_out_of_range_error ( msg . index , mesh . get ( ) . vertices_count ) ) ;
            }
            else
                so_called_trace ( so_called_trace_common_engine_render :: mesh_index_offset_out_of_range_error ( msg . offset , mesh . get ( ) . triangle_strip_indices_count ) ) ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_vertex_color_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_pointer_data_type < so_called_platform_render_vertex_data_type > vertex ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) )
        {
            if ( so_called_platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count ) )
            {
                so_called_platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
                so_called_platform_render :: set_vertex_color ( vertex . get ( ) , msg . r , msg . g , msg . b , msg . a ) ;
            }
            else
                so_called_trace ( so_called_trace_common_engine_render :: mesh_vertex_out_of_range_error ( msg . offset , mesh . get ( ) . vertices_count ) ) ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_vertex_position_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_pointer_data_type < so_called_platform_render_vertex_data_type > vertex ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) )
        {
            if ( so_called_platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count ) )
            {
                so_called_platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
                so_called_platform_render :: set_vertex_position ( vertex . get ( ) , msg . x , msg . y , msg . z ) ;
            }
            else
                so_called_trace ( so_called_trace_common_engine_render :: mesh_vertex_out_of_range_error ( msg . offset , mesh . get ( ) . vertices_count ) ) ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_mesh_set_vertex_tex_coord_message msg )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . mesh . _mesh_id , so_called_common_engine_render_consts :: max_meshes ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_data > mesh ;
        so_called_platform_pointer_data_type < so_called_platform_render_vertex_data_type > vertex ;
        so_called_platform_static_array :: element_ptr ( mesh , shy_guts :: meshes_datas , msg . mesh . _mesh_id ) ;
        if ( so_called_platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) )
        {
            if ( so_called_platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count ) )
            {
                so_called_platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
                so_called_platform_render :: set_vertex_tex_coord ( vertex . get ( ) , msg . u , msg . v ) ;
            }
            else
                so_called_trace ( so_called_trace_common_engine_render :: mesh_vertex_out_of_range_error ( msg . offset , mesh . get ( ) . vertices_count ) ) ;
        }
        else
            so_called_trace ( so_called_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( ) ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_projection_frustum_message msg )
{
    so_called_platform_render :: projection_frustum ( msg . x_left , msg . x_right , msg . y_bottom , msg . y_top , msg . z_near , msg . z_far ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_projection_ortho_message msg )
{
    so_called_platform_render :: projection_ortho ( msg . x_left , msg . x_right , msg . y_bottom , msg . y_top , msg . z_near , msg . z_far ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_create_request_message )
{
    so_called_common_engine_render_texture_id_type created_texture ;
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: next_texture_id , whole_max_textures ) )
    {
        created_texture . _texture_id = shy_guts :: next_texture_id ;
        so_called_platform_math :: inc_whole ( shy_guts :: next_texture_id ) ;
        so_called_trace ( so_called_trace_common_engine_render :: textures_in_use ( shy_guts :: next_texture_id , whole_max_textures ) ) ;
    }
    else
    {
        created_texture . _texture_id = whole_max_textures ;
        so_called_trace ( so_called_trace_common_engine_render :: textures_overflow_error ( ) ) ;
    }

    so_called_common_engine_render_texture_create_reply_message reply_msg ;
    reply_msg . texture = created_texture ;
    so_called_common_engine_render_texture_create_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_finalize_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        so_called_platform_render :: load_texture_subdata 
            ( texture . get ( ) . render_id 
            , so_called_platform_math_consts :: whole_0
            , so_called_platform_math_consts :: whole_0
            , so_called_common_engine_render_consts :: texture_width
            , so_called_common_engine_render_consts :: texture_height
            , texture . get ( ) . texels 
            ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_load_from_resource_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_math_num_whole_type size_pow2_base ;
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        so_called_platform_render_texture_loader :: load_resource 
            ( msg . resource 
            , shy_guts :: consts :: texture_size_pow2_base 
            , texture . get ( ) . texels 
            ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_loader_ready_request_message msg )
{
    so_called_common_engine_render_texture_loader_ready_reply_message reply_msg ;
    so_called_platform_render_texture_loader :: ready ( reply_msg . ready ) ;
    so_called_common_engine_render_texture_loader_ready_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_mode_modulate_message )
{
    so_called_platform_render :: texture_mode_modulate ( ) ;
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_select_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        so_called_platform_render :: enable_texturing ( ) ;
        so_called_platform_render :: use_texture ( texture . get ( ) . render_id ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_set_texel_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_math_num_whole_type texel_offset ;
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_pointer_data_type < so_called_platform_render_texel_data_type > texel ;
        
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        so_called_platform_math :: mul_wholes ( texel_offset , so_called_common_engine_render_consts :: texture_width , msg . y ) ;
        so_called_platform_math :: add_to_whole ( texel_offset , msg . x ) ;
        so_called_platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
        texel . get ( ) = msg . texel ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_set_texel_rgba_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_math_num_whole_type texel_offset ;
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_pointer_data_type < so_called_platform_render_texel_data_type > texel ;

        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        so_called_platform_math :: mul_wholes ( texel_offset , so_called_common_engine_render_consts :: texture_width , msg . y ) ;
        so_called_platform_math :: add_to_whole ( texel_offset , msg . x ) ;
        so_called_platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
        so_called_platform_render :: set_texel_color ( texel . get ( ) , msg . r , msg . g , msg . b , msg . a ) ;
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_set_texels_rect_message msg )
{
    so_called_platform_math_num_whole_type whole_max_textures ;
    so_called_platform_math :: make_num_whole ( whole_max_textures , shy_guts :: consts :: max_textures ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . texture . _texture_id , whole_max_textures ) )
    {
        so_called_platform_math_num_whole_type texel_offset ;
        so_called_platform_pointer_data_type < shy_guts :: texture_data > texture ;
        so_called_platform_static_array :: element_ptr ( texture , shy_guts :: textures_datas , msg . texture . _texture_id ) ;
        for ( so_called_platform_math_num_whole_type y = msg . bottom
            ; so_called_platform_conditions :: whole_less_or_equal_to_whole ( y , msg . top )
            ; so_called_platform_math :: inc_whole ( y )
            )
        {
            for ( so_called_platform_math_num_whole_type x = msg . left
                ; so_called_platform_conditions :: whole_less_or_equal_to_whole ( x , msg . right )
                ; so_called_platform_math :: inc_whole ( x )
                )
            {
                so_called_platform_pointer_data_type < so_called_platform_render_texel_data_type > texel ;
                so_called_platform_math :: mul_wholes ( texel_offset , so_called_common_engine_render_consts :: texture_width , y ) ;
                so_called_platform_math :: add_to_whole ( texel_offset , x ) ;
                so_called_platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
                texel . get ( ) = msg . texel ;
            }
        }
    }
}

void _shy_common_engine_render :: receive ( so_called_common_engine_render_texture_unselect_message )
{
    so_called_platform_render :: disable_texturing ( ) ;
}

void _shy_common_engine_render :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
