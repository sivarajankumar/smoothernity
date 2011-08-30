namespace shy_guts
{
    namespace consts
    {
        static so_called_platform_math_num_whole_type create_rows_per_frame = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_platform_math_num_whole_type land_grid = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_platform_math_num_whole_type scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static so_called_platform_math_num_whole_type modulator_1 = so_called_platform_math :: init_num_whole ( 32 ) ;
        static so_called_platform_math_num_whole_type modulator_2 = so_called_platform_math :: init_num_whole ( 64 ) ;
        static so_called_platform_math_num_whole_type modulator_3 = so_called_platform_math :: init_num_whole ( 128 ) ;
        static so_called_platform_math_num_whole_type multiplier_1 = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_platform_math_num_whole_type multiplier_2 = so_called_platform_math :: init_num_whole ( 4 ) ;
        static so_called_platform_math_num_whole_type multiplier_3 = so_called_platform_math :: init_num_whole ( 2 ) ;
        static so_called_platform_math_num_fract_type color_scale = so_called_platform_math :: init_num_fract ( 255 , 1 ) ;
        static so_called_platform_math_num_fract_type land_radius = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static so_called_platform_math_num_fract_type land_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_platform_math_num_fract_type land_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_platform_math_num_fract_type land_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
    }

    static void render_land ( ) ;
    static void create_land_mesh ( ) ;
    static void create_land_texture ( ) ;
    static void mesh_set_triangle_strip_index_value ( so_called_platform_math_num_whole_type offset , so_called_platform_math_num_whole_type index ) ;

    static so_called_platform_math_num_whole_type land_mesh_created ;
    static so_called_platform_math_num_whole_type land_texture_created ;
    static so_called_platform_math_num_whole_type land_prepare_permitted ;
    static so_called_platform_math_num_whole_type land_texture_creation_row ;
    static so_called_platform_math_num_fract_type land_scale ;
    static so_called_platform_math_num_whole_type texture_create_requested ;
    static so_called_platform_math_num_whole_type texture_create_replied ;
    static so_called_platform_math_num_whole_type mesh_create_requested ;
    static so_called_common_engine_render_mesh_id_type land_mesh_id ;
    static so_called_common_engine_render_texture_id_type land_texture_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_land > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_land ( )
{
    so_called_platform_matrix_data_type matrix ;
    so_called_platform_math_num_fract_type scale_step ;
    so_called_platform_math_num_fract_type increased_scale ;
    so_called_platform_math_num_fract_type fract_scale_in_frames ;
    
    {
        so_called_common_engine_render_texture_select_message texture_select_msg ;
        texture_select_msg . texture = shy_guts :: land_texture_id ;
        so_called_common_engine_render_texture_select_sender :: send ( texture_select_msg ) ;
    }
    so_called_platform_math :: make_fract_from_whole ( fract_scale_in_frames , shy_guts :: consts :: scale_in_frames ) ;
    so_called_platform_math :: div_fracts ( scale_step , so_called_platform_math_consts :: fract_1 , fract_scale_in_frames ) ;
    so_called_platform_math :: add_fracts ( increased_scale , shy_guts :: land_scale , scale_step ) ;
    if ( so_called_platform_conditions :: fract_less_than_fract ( increased_scale , so_called_platform_math_consts :: fract_1 ) )
        shy_guts :: land_scale = increased_scale ;
    else
        shy_guts :: land_scale = so_called_platform_math_consts :: fract_1 ;
    so_called_platform_matrix :: set_axis_x ( matrix , shy_guts :: land_scale , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , so_called_platform_math_consts :: fract_0 , shy_guts :: land_scale , so_called_platform_math_consts :: fract_0 ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , shy_guts :: land_scale ) ;
    so_called_platform_matrix :: set_origin ( matrix , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 , so_called_platform_math_consts :: fract_0 ) ;
    {
        so_called_common_engine_render_mesh_set_transform_message mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: land_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_common_engine_render_mesh_set_transform_sender :: send ( mesh_set_transform_msg ) ;
    }
    {
        so_called_common_engine_render_mesh_render_message mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: land_mesh_id ;
        so_called_common_engine_render_mesh_render_sender :: send ( mesh_render_msg ) ;
    }
}

void shy_guts :: create_land_mesh ( )
{
    so_called_platform_math_num_whole_type vertices_count ;
    so_called_platform_math_num_whole_type indices_count ;
    so_called_platform_math_num_whole_type ix ;
    so_called_platform_math_num_whole_type iz ;
    so_called_platform_math_num_whole_type ix_max ;
    so_called_platform_math_num_whole_type iz_max ;
    so_called_platform_math_num_fract_type grid_step ;
    so_called_platform_math_num_fract_type grid_origin_x ;
    so_called_platform_math_num_fract_type grid_origin_z ;
    so_called_platform_math_num_fract_type fract_land_grid ;
    so_called_platform_math_num_whole_type land_grid_plus_1 ;
    
    vertices_count = so_called_platform_math_consts :: whole_0 ;
    indices_count = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: make_fract_from_whole ( fract_land_grid , shy_guts :: consts :: land_grid ) ;
    so_called_platform_math :: mul_fracts ( grid_step , shy_guts :: consts :: land_radius , so_called_platform_math_consts :: fract_2 ) ;
    so_called_platform_math :: div_fract_by ( grid_step , fract_land_grid ) ;
    so_called_platform_math :: neg_fract ( grid_origin_x , shy_guts :: consts :: land_radius ) ;
    so_called_platform_math :: neg_fract ( grid_origin_z , shy_guts :: consts :: land_radius ) ;
    so_called_platform_math :: add_wholes ( land_grid_plus_1 , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
    
    for ( iz = so_called_platform_math_consts :: whole_0
        , iz_max = land_grid_plus_1
        ; so_called_platform_conditions :: whole_less_than_whole ( iz , iz_max )
        ; so_called_platform_math :: inc_whole ( iz )
        )
    {
        for ( ix = so_called_platform_math_consts :: whole_0
            , ix_max = land_grid_plus_1
            ; so_called_platform_conditions :: whole_less_than_whole ( ix , ix_max )
            ; so_called_platform_math :: inc_whole ( ix )
            )
        {
            so_called_platform_math_num_fract_type x ;
            so_called_platform_math_num_fract_type z ;
            so_called_platform_math_num_fract_type fract_ix ;
            so_called_platform_math_num_fract_type fract_iz ;
            so_called_platform_math_num_fract_type vertex_x ;
            so_called_platform_math_num_fract_type vertex_y ;
            so_called_platform_math_num_fract_type vertex_z ;
            so_called_platform_math_num_fract_type vertex_u ;
            so_called_platform_math_num_fract_type vertex_v ;
            so_called_platform_math_num_fract_type vertex_r ;
            so_called_platform_math_num_fract_type vertex_g ;
            so_called_platform_math_num_fract_type vertex_b ;
            so_called_platform_math_num_fract_type vertex_a ;
            
            so_called_platform_math :: make_fract_from_whole ( fract_ix , ix ) ;
            so_called_platform_math :: make_fract_from_whole ( fract_iz , iz ) ;
            so_called_platform_math :: mul_fracts ( x , grid_step , fract_ix ) ;
            so_called_platform_math :: mul_fracts ( z , grid_step , fract_iz ) ;
            so_called_platform_math :: add_to_fract ( x , grid_origin_x ) ;
            so_called_platform_math :: add_to_fract ( z , grid_origin_z ) ;
            vertex_x = x ;
            vertex_y = so_called_platform_math_consts :: fract_0 ;
            vertex_z = z ;
            so_called_platform_math :: div_fracts ( vertex_u , fract_iz , fract_land_grid ) ;
            so_called_platform_math :: div_fracts ( vertex_v , fract_ix , fract_land_grid ) ;
            vertex_r = shy_guts :: consts :: land_r ;
            vertex_g = shy_guts :: consts :: land_g ;
            vertex_b = shy_guts :: consts :: land_b ;
            vertex_a = so_called_platform_math_consts :: fract_1 ;
            
            so_called_common_engine_render_mesh_set_vertex_position_message set_pos_msg ;
            set_pos_msg . mesh = shy_guts :: land_mesh_id ;
            set_pos_msg . offset = vertices_count ;
            set_pos_msg . x = vertex_x ;
            set_pos_msg . y = vertex_y ;
            set_pos_msg . z = vertex_z ;
            so_called_common_engine_render_mesh_set_vertex_position_sender :: send ( set_pos_msg ) ;
            
            so_called_common_engine_render_mesh_set_vertex_color_message set_col_msg ;
            set_col_msg . mesh = shy_guts :: land_mesh_id ;
            set_col_msg . offset = vertices_count ;
            set_col_msg . r = vertex_r ;
            set_col_msg . g = vertex_g ;
            set_col_msg . b = vertex_b ;
            set_col_msg . a = vertex_a ;
            so_called_common_engine_render_mesh_set_vertex_color_sender :: send ( set_col_msg ) ;
            
            so_called_common_engine_render_mesh_set_vertex_tex_coord_message set_tex_msg ;
            set_tex_msg . mesh = shy_guts :: land_mesh_id ;
            set_tex_msg . offset = vertices_count ;
            set_tex_msg . u = vertex_u ;
            set_tex_msg . v = vertex_v ;
            so_called_common_engine_render_mesh_set_vertex_tex_coord_sender :: send ( set_tex_msg ) ;
            
            so_called_platform_math :: inc_whole ( vertices_count ) ;
        }
    }
    for ( iz = so_called_platform_math_consts :: whole_0
        , iz_max = shy_guts :: consts :: land_grid
        ; so_called_platform_conditions :: whole_less_than_whole ( iz , iz_max )
        ; so_called_platform_math :: inc_whole ( iz )
        )
    {
        for ( ix = so_called_platform_math_consts :: whole_0
            , ix_max = land_grid_plus_1
            ; so_called_platform_conditions :: whole_less_than_whole ( ix , ix_max )
            ; so_called_platform_math :: inc_whole ( ix )
            )
        {
            so_called_platform_math_num_whole_type index ;
            so_called_platform_math_num_whole_type row_size ;
            
            row_size = land_grid_plus_1 ;
            
            if ( so_called_platform_conditions :: whole_is_even ( iz ) )
            {
                so_called_platform_math :: mul_wholes ( index , row_size , iz ) ;
                so_called_platform_math :: add_to_whole ( index , ix ) ;
                shy_guts :: mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                so_called_platform_math :: inc_whole ( indices_count ) ;
                
                so_called_platform_math :: add_to_whole ( index , row_size ) ;
                shy_guts :: mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                so_called_platform_math :: inc_whole ( indices_count ) ;
            }
            else
            {
                so_called_platform_math :: mul_wholes ( index , row_size , iz ) ;
                so_called_platform_math :: add_to_whole ( index , shy_guts :: consts :: land_grid ) ;
                so_called_platform_math :: sub_from_whole ( index , ix ) ;
                so_called_platform_math :: add_to_whole ( index , row_size ) ;
                shy_guts :: mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                so_called_platform_math :: inc_whole ( indices_count ) ;
                
                so_called_platform_math :: sub_from_whole ( index , row_size ) ;
                shy_guts :: mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                so_called_platform_math :: inc_whole ( indices_count ) ;
            }
        }
    }
    so_called_common_engine_render_mesh_finalize_message mesh_finalize_msg ;
    mesh_finalize_msg . mesh = shy_guts :: land_mesh_id ;
    so_called_common_engine_render_mesh_finalize_sender :: send ( mesh_finalize_msg ) ;
    shy_guts :: land_mesh_created = so_called_platform_math_consts :: whole_true ;
}

void shy_guts :: create_land_texture ( )
{
    so_called_platform_math_num_whole_type texture_width ;
    so_called_platform_math_num_whole_type texture_height ;
    so_called_platform_math_num_whole_type prev_creation_row = shy_guts :: land_texture_creation_row ;

    texture_width = so_called_common_engine_render_consts :: texture_width ;
    texture_height = so_called_common_engine_render_consts :: texture_height ;
    for ( ; ; )
    {
        so_called_platform_math_num_whole_type rows_delta ;
        so_called_platform_math_num_whole_type y = shy_guts :: land_texture_creation_row ;
        
        so_called_platform_math :: sub_wholes ( rows_delta , shy_guts :: land_texture_creation_row , prev_creation_row ) ;
        if ( ! so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: land_texture_creation_row , texture_height )
          || ! so_called_platform_conditions :: whole_less_or_equal_to_whole ( rows_delta , shy_guts :: consts :: create_rows_per_frame )
           )
        {
            break ;
        }
        for ( so_called_platform_math_num_whole_type x = so_called_platform_math_consts :: whole_0
            ; so_called_platform_conditions :: whole_less_than_whole ( x , texture_width )
            ; so_called_platform_math :: inc_whole ( x )
            )
        {
            so_called_platform_math_num_whole_type c ;
            so_called_platform_math_num_whole_type texel_r ;
            so_called_platform_math_num_whole_type texel_g ;
            so_called_platform_math_num_whole_type texel_b ;
            so_called_platform_math_num_fract_type fract_r ;
            so_called_platform_math_num_fract_type fract_g ;
            so_called_platform_math_num_fract_type fract_b ;
            
            so_called_platform_math :: xor_wholes ( c , x , y ) ;
            so_called_platform_math :: mod_wholes ( texel_r , c , shy_guts :: consts :: modulator_1 ) ;
            so_called_platform_math :: mod_wholes ( texel_g , c , shy_guts :: consts :: modulator_2 ) ;
            so_called_platform_math :: mod_wholes ( texel_b , c , shy_guts :: consts :: modulator_3 ) ;
            so_called_platform_math :: mul_whole_by ( texel_r , shy_guts :: consts :: multiplier_1 ) ;
            so_called_platform_math :: mul_whole_by ( texel_g , shy_guts :: consts :: multiplier_2 ) ;
            so_called_platform_math :: mul_whole_by ( texel_b , shy_guts :: consts :: multiplier_3 ) ;

            so_called_platform_math :: make_fract_from_whole ( fract_r , texel_r ) ;
            so_called_platform_math :: make_fract_from_whole ( fract_g , texel_g ) ;
            so_called_platform_math :: make_fract_from_whole ( fract_b , texel_b ) ;
            so_called_platform_math :: div_fract_by ( fract_r , shy_guts :: consts :: color_scale ) ;
            so_called_platform_math :: div_fract_by ( fract_g , shy_guts :: consts :: color_scale ) ;
            so_called_platform_math :: div_fract_by ( fract_b , shy_guts :: consts :: color_scale ) ;
            
            so_called_common_engine_render_texture_set_texel_rgba_message texture_set_texel_rgba_msg ;
            texture_set_texel_rgba_msg . texture = shy_guts :: land_texture_id ;
            texture_set_texel_rgba_msg . x = x ;
            texture_set_texel_rgba_msg . y = y ;
            texture_set_texel_rgba_msg . r = fract_r ;
            texture_set_texel_rgba_msg . g = fract_g ;
            texture_set_texel_rgba_msg . b = fract_b ;
            texture_set_texel_rgba_msg . a = so_called_platform_math_consts :: fract_1 ;
            so_called_common_engine_render_texture_set_texel_rgba_sender :: send ( texture_set_texel_rgba_msg ) ;
        }
        so_called_platform_math :: inc_whole ( shy_guts :: land_texture_creation_row ) ;
    }
    if ( so_called_platform_conditions :: wholes_are_equal ( shy_guts :: land_texture_creation_row , texture_height ) )
    {
        so_called_common_engine_render_texture_finalize_message texture_finalize_msg ;
        texture_finalize_msg . texture = shy_guts :: land_texture_id ;
        so_called_common_engine_render_texture_finalize_sender :: send ( texture_finalize_msg ) ;
        shy_guts :: land_texture_created = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: mesh_set_triangle_strip_index_value ( so_called_platform_math_num_whole_type offset , so_called_platform_math_num_whole_type index )
{
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_message msg ;
    msg . mesh = shy_guts :: land_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    so_called_common_engine_render_mesh_set_triangle_strip_index_value_sender :: send ( msg ) ;
}

void _shy_common_logic_land :: receive ( so_called_common_engine_render_mesh_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: land_mesh_id = msg . mesh ;
        shy_guts :: create_land_mesh ( ) ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) )
            so_called_common_logic_land_prepared_sender :: send ( so_called_common_logic_land_prepared_message ( ) ) ;
    }
}

void _shy_common_logic_land :: receive ( so_called_common_engine_render_texture_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: land_texture_id = msg . texture ;
    }
}

void _shy_common_logic_land :: receive ( so_called_common_init_message )
{
    shy_guts :: land_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_texture_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: land_texture_creation_row = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: land_scale = so_called_platform_math_consts :: fract_0 ;
    shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_land :: receive ( so_called_common_logic_land_prepare_permit_message )
{
    shy_guts :: land_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_land :: receive ( so_called_common_logic_land_render_request_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: land_texture_created ) )
        shy_guts :: render_land ( ) ;
    so_called_common_logic_land_render_reply_sender :: send ( so_called_common_logic_land_render_reply_message ( ) ) ;
}

void _shy_common_logic_land :: receive ( so_called_common_logic_land_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_texture_created ) )
        {
            if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: texture_create_replied ) )
            {
                shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
                so_called_common_engine_render_texture_create_request_sender :: send ( so_called_common_engine_render_texture_create_request_message ( ) ) ;
            }
            else
                shy_guts :: create_land_texture ( ) ;
        }
        else if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        
            so_called_platform_math_num_whole_type total_vertices ;
            so_called_platform_math_num_whole_type total_indices ;
            
            so_called_platform_math :: add_wholes ( total_vertices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_vertices , total_vertices ) ;
            
            so_called_platform_math :: add_wholes ( total_indices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , shy_guts :: consts :: land_grid ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , so_called_platform_math_consts :: whole_2 ) ;
            
            so_called_common_engine_render_mesh_create_request_message mesh_create_msg ;
            mesh_create_msg . vertices = total_vertices ;
            mesh_create_msg . triangle_strip_indices = total_indices ;
            mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_common_engine_render_mesh_create_request_sender :: send ( mesh_create_msg ) ;
        }
    }
}

void _shy_common_logic_land :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

