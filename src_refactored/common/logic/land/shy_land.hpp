namespace shy_guts
{
    namespace consts
    {
        static so_called_type_platform_math_num_whole create_rows_per_frame = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole land_grid = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
        static so_called_type_platform_math_num_whole modulator_1 = so_called_platform_math :: init_num_whole ( 32 ) ;
        static so_called_type_platform_math_num_whole modulator_2 = so_called_platform_math :: init_num_whole ( 64 ) ;
        static so_called_type_platform_math_num_whole modulator_3 = so_called_platform_math :: init_num_whole ( 128 ) ;
        static so_called_type_platform_math_num_whole multiplier_1 = so_called_platform_math :: init_num_whole ( 8 ) ;
        static so_called_type_platform_math_num_whole multiplier_2 = so_called_platform_math :: init_num_whole ( 4 ) ;
        static so_called_type_platform_math_num_whole multiplier_3 = so_called_platform_math :: init_num_whole ( 2 ) ;
        static so_called_type_platform_math_num_fract color_scale = so_called_platform_math :: init_num_fract ( 255 , 1 ) ;
        static so_called_type_platform_math_num_fract land_radius = so_called_platform_math :: init_num_fract ( 10 , 1 ) ;
        static so_called_type_platform_math_num_fract land_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static so_called_type_platform_math_num_fract land_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
    }

    static void render_land ( ) ;
    static void create_land_mesh ( ) ;
    static void create_land_texture ( ) ;
    static void mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index ) ;

    static so_called_type_platform_math_num_whole land_mesh_created ;
    static so_called_type_platform_math_num_whole land_texture_created ;
    static so_called_type_platform_math_num_whole land_prepare_permitted ;
    static so_called_type_platform_math_num_whole land_texture_creation_row ;
    static so_called_type_platform_math_num_fract land_scale ;
    static so_called_type_platform_math_num_whole texture_create_requested ;
    static so_called_type_platform_math_num_whole texture_create_replied ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_common_engine_render_mesh_id land_mesh_id ;
    static so_called_type_common_engine_render_texture_id land_texture_id ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_land > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: render_land ( )
{
    so_called_type_platform_matrix_data matrix ;
    so_called_type_platform_math_num_fract scale_step ;
    so_called_type_platform_math_num_fract increased_scale ;
    so_called_type_platform_math_num_fract fract_scale_in_frames ;
    
    {
        so_called_message_common_engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = shy_guts :: land_texture_id ;
        so_called_sender_common_engine_render_texture_select :: send ( texture_select_msg ) ;
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
        so_called_message_common_engine_render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = shy_guts :: land_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        so_called_sender_common_engine_render_mesh_set_transform :: send ( mesh_set_transform_msg ) ;
    }
    {
        so_called_message_common_engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = shy_guts :: land_mesh_id ;
        so_called_sender_common_engine_render_mesh_render :: send ( mesh_render_msg ) ;
    }
}

void shy_guts :: create_land_mesh ( )
{
    so_called_type_platform_math_num_whole vertices_count ;
    so_called_type_platform_math_num_whole indices_count ;
    so_called_type_platform_math_num_whole ix ;
    so_called_type_platform_math_num_whole iz ;
    so_called_type_platform_math_num_whole ix_max ;
    so_called_type_platform_math_num_whole iz_max ;
    so_called_type_platform_math_num_fract grid_step ;
    so_called_type_platform_math_num_fract grid_origin_x ;
    so_called_type_platform_math_num_fract grid_origin_z ;
    so_called_type_platform_math_num_fract fract_land_grid ;
    so_called_type_platform_math_num_whole land_grid_plus_1 ;
    
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
            so_called_type_platform_math_num_fract x ;
            so_called_type_platform_math_num_fract z ;
            so_called_type_platform_math_num_fract fract_ix ;
            so_called_type_platform_math_num_fract fract_iz ;
/*
            num_fract vertex_x ;
            num_fract vertex_y ;
            num_fract vertex_z ;
            num_fract vertex_u ;
            num_fract vertex_v ;
            num_fract vertex_r ;
            num_fract vertex_g ;
            num_fract vertex_b ;
            num_fract vertex_a ;
            
            platform_math :: make_fract_from_whole ( fract_ix , ix ) ;
            platform_math :: make_fract_from_whole ( fract_iz , iz ) ;
            platform_math :: mul_fracts ( x , grid_step , fract_ix ) ;
            platform_math :: mul_fracts ( z , grid_step , fract_iz ) ;
            platform_math :: add_to_fract ( x , grid_origin_x ) ;
            platform_math :: add_to_fract ( z , grid_origin_z ) ;
            vertex_x = x ;
            vertex_y = _platform_math_consts . get ( ) . fract_0 ;
            vertex_z = z ;
            platform_math :: div_fracts ( vertex_u , fract_iz , fract_land_grid ) ;
            platform_math :: div_fracts ( vertex_v , fract_ix , fract_land_grid ) ;
            vertex_r = _logic_land_consts . land_r ;
            vertex_g = _logic_land_consts . land_g ;
            vertex_b = _logic_land_consts . land_b ;
            vertex_a = _platform_math_consts . get ( ) . fract_1 ;
            
            typename messages :: engine_render_mesh_set_vertex_position set_pos_msg ;
            set_pos_msg . mesh = _land_mesh_id ;
            set_pos_msg . offset = vertices_count ;
            set_pos_msg . x = vertex_x ;
            set_pos_msg . y = vertex_y ;
            set_pos_msg . z = vertex_z ;
            _mediator . get ( ) . send ( set_pos_msg ) ;
            
            typename messages :: engine_render_mesh_set_vertex_color set_col_msg ;
            set_col_msg . mesh = _land_mesh_id ;
            set_col_msg . offset = vertices_count ;
            set_col_msg . r = vertex_r ;
            set_col_msg . g = vertex_g ;
            set_col_msg . b = vertex_b ;
            set_col_msg . a = vertex_a ;
            _mediator . get ( ) . send ( set_col_msg ) ;
            
            typename messages :: engine_render_mesh_set_vertex_tex_coord set_tex_msg ;
            set_tex_msg . mesh = _land_mesh_id ;
            set_tex_msg . offset = vertices_count ;
            set_tex_msg . u = vertex_u ;
            set_tex_msg . v = vertex_v ;
            _mediator . get ( ) . send ( set_tex_msg ) ;
            
            platform_math :: inc_whole ( vertices_count ) ;
*/
        }
    }
/*    
    for ( iz = _platform_math_consts . get ( ) . whole_0
        , iz_max = land_grid_plus_1
        ; platform_conditions :: whole_less_than_whole ( iz , iz_max )
        ; platform_math :: inc_whole ( iz )
        )
    {
        for ( ix = _platform_math_consts . get ( ) . whole_0
            , ix_max = land_grid_plus_1
            ; platform_conditions :: whole_less_than_whole ( ix , ix_max )
            ; platform_math :: inc_whole ( ix )
            )
        {
            num_whole index ;
            num_whole row_size ;
            
            row_size = land_grid_plus_1 ;
            
            if ( platform_conditions :: whole_is_even ( iz ) )
            {
                platform_math :: mul_wholes ( index , row_size , iz ) ;
                platform_math :: add_to_whole ( index , ix ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
                
                platform_math :: add_to_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
            }
            else
            {
                platform_math :: mul_wholes ( index , row_size , iz ) ;
                platform_math :: add_to_whole ( index , _logic_land_consts . land_grid ) ;
                platform_math :: sub_from_whole ( index , ix ) ;
                platform_math :: add_to_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
                
                platform_math :: sub_from_whole ( index , row_size ) ;
                _mesh_set_triangle_strip_index_value ( indices_count , index ) ;
                platform_math :: inc_whole ( indices_count ) ;
            }
        }
    }
    typename messages :: engine_render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _land_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
    _land_mesh_created = _platform_math_consts . get ( ) . whole_true ;
*/
}

void shy_guts :: create_land_texture ( )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index )
{
}

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: land_mesh_id = msg . mesh ;
        shy_guts :: create_land_mesh ( ) ;
        if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) )
            so_called_sender_common_logic_land_prepared :: send ( so_called_message_common_logic_land_prepared ( ) ) ;
    }
}

void _shy_common_logic_land :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: texture_create_requested ) )
    {
        shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_create_replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: land_texture_id = msg . texture ;
    }
}

void _shy_common_logic_land :: receive ( so_called_message_common_init )
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

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_prepare_permit )
{
    shy_guts :: land_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_mesh_created ) && so_called_platform_conditions :: whole_is_true ( shy_guts :: land_texture_created ) )
        shy_guts :: render_land ( ) ;
    so_called_sender_common_logic_land_render_reply :: send ( so_called_message_common_logic_land_render_reply ( ) ) ;
}

void _shy_common_logic_land :: receive ( so_called_message_common_logic_land_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: land_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_texture_created ) )
        {
            if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: texture_create_replied ) )
            {
                shy_guts :: texture_create_requested = so_called_platform_math_consts :: whole_true ;
                so_called_sender_common_engine_render_texture_create_request :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
            }
            else
                shy_guts :: create_land_texture ( ) ;
        }
        else if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: land_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
        
            so_called_type_platform_math_num_whole total_vertices ;
            so_called_type_platform_math_num_whole total_indices ;
            
            so_called_platform_math :: add_wholes ( total_vertices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_vertices , total_vertices ) ;
            
            so_called_platform_math :: add_wholes ( total_indices , shy_guts :: consts :: land_grid , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , shy_guts :: consts :: land_grid ) ;
            so_called_platform_math :: mul_whole_by ( total_indices , so_called_platform_math_consts :: whole_2 ) ;
            
            so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = total_vertices ;
            mesh_create_msg . triangle_strip_indices = total_indices ;
            mesh_create_msg . triangle_fan_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
        }
    }
}
