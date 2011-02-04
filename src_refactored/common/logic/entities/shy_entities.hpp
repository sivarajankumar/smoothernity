namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract entity_color_roof_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_color_roof_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_color_roof_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract entity_mesh_height = so_called_platform_math :: init_num_fract ( 2 , 1 ) ;
        static const so_called_type_platform_math_num_fract scale_wave = so_called_platform_math :: init_num_fract ( 2 , 1 ) ;
        static const so_called_type_platform_math_num_whole entity_mesh_spans = so_called_platform_math :: init_num_whole ( 50 ) ;
        static const so_called_type_platform_math_num_whole scale_in_frames = so_called_platform_math :: init_num_whole ( 120 ) ;
        static const so_called_type_platform_math_num_whole grid_step = so_called_platform_math :: init_num_whole ( 5 ) ;
        static const so_called_type_platform_math_num_whole color_bias = so_called_platform_math :: init_num_whole ( 21 ) ;
        static const so_called_type_platform_math_num_whole colors_max = so_called_platform_math :: init_num_whole ( 7 ) ;
        static const so_called_type_platform_math_num_whole frames_wait_before_render = so_called_platform_math :: init_num_whole ( 1 ) ;
        static const so_called_type_platform_math_num_whole frames_between_render_count_increases = so_called_platform_math :: init_num_whole ( 10 ) ;
        static so_called_type_platform_math_const_int_32 entity_mesh_grid = 5 ;
    }

    static void entities_render ( ) ;
    static void create_entity_mesh ( ) ;
    static void update_entity_grid ( ) ;
    static void get_entity_origin ( so_called_type_platform_vector_data & result , so_called_type_platform_math_num_whole index ) ;
    static void mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index ) ;
    static void mesh_set_triangle_fan_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index ) ;
    static void mesh_set_vertex_tex_coord 
        ( so_called_type_platform_math_num_whole offset 
        , so_called_type_platform_math_num_fract u
        , so_called_type_platform_math_num_fract v
        ) ;
    static void mesh_set_vertex_position 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract x
        , so_called_type_platform_math_num_fract y
        , so_called_type_platform_math_num_fract z
        ) ;
    static void mesh_set_vertex_color 
        ( so_called_type_platform_math_num_whole offset
        , so_called_type_platform_math_num_fract r
        , so_called_type_platform_math_num_fract g
        , so_called_type_platform_math_num_fract b
        , so_called_type_platform_math_num_fract a
        ) ;
    static void entity_color 
        ( so_called_type_platform_math_num_fract & r
        , so_called_type_platform_math_num_fract & g
        , so_called_type_platform_math_num_fract & b
        , so_called_type_platform_math_num_fract & a
        , so_called_type_platform_math_num_whole i
        ) ;

    static so_called_type_platform_math_num_whole entity_created ;
    static so_called_type_platform_math_num_whole entities_prepare_permitted ;
    static so_called_type_platform_math_num_whole grid_scale ;
    static so_called_type_platform_math_num_whole current_strip_mesh_span ;
    static so_called_type_platform_math_num_whole current_fan_mesh_span ;
    static so_called_type_platform_math_num_whole strip_indices_count ;
    static so_called_type_platform_math_num_whole fan_indices_count ;
    static so_called_type_platform_math_num_whole vertices_count ;
    static so_called_type_platform_math_num_whole entity_mesh_id_created ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
    static so_called_type_platform_math_num_whole frames_to_render ;
    static so_called_type_platform_math_num_whole entities_to_render ;
    static so_called_type_platform_math_num_whole frames_to_increase_render_count ;
    static so_called_type_common_engine_render_mesh_id entity_mesh_id ;
    static so_called_type_platform_static_array_data \
        < so_called_type_platform_matrix_data 
        , shy_guts :: consts :: entity_mesh_grid
        * shy_guts :: consts :: entity_mesh_grid
        > entities_grid_matrices ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_entities > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: entities_render ( )
{
}

void shy_guts :: create_entity_mesh ( )
{
}

void shy_guts :: update_entity_grid ( )
{
}

void shy_guts :: get_entity_origin ( so_called_type_platform_vector_data & result , so_called_type_platform_math_num_whole index )
{
}

void shy_guts :: mesh_set_triangle_strip_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index )
{
}

void shy_guts :: mesh_set_triangle_fan_index_value ( so_called_type_platform_math_num_whole offset , so_called_type_platform_math_num_whole index )
{
}

void shy_guts :: mesh_set_vertex_tex_coord 
    ( so_called_type_platform_math_num_whole offset 
    , so_called_type_platform_math_num_fract u
    , so_called_type_platform_math_num_fract v
    )
{
}

void shy_guts :: mesh_set_vertex_position 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract x
    , so_called_type_platform_math_num_fract y
    , so_called_type_platform_math_num_fract z
    )
{
}

void shy_guts :: mesh_set_vertex_color 
    ( so_called_type_platform_math_num_whole offset
    , so_called_type_platform_math_num_fract r
    , so_called_type_platform_math_num_fract g
    , so_called_type_platform_math_num_fract b
    , so_called_type_platform_math_num_fract a
    )
{
}

void shy_guts :: entity_color 
    ( so_called_type_platform_math_num_fract & r
    , so_called_type_platform_math_num_fract & g
    , so_called_type_platform_math_num_fract & b
    , so_called_type_platform_math_num_fract & a
    , so_called_type_platform_math_num_whole i
    )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: entity_mesh_id_created = so_called_platform_math_consts :: whole_true ;
        shy_guts :: entity_mesh_id = msg . mesh ;
    }
}

void _shy_common_logic_entities :: receive ( so_called_message_common_init )
{
    shy_guts :: entity_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: entities_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: grid_scale = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: current_strip_mesh_span = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: current_fan_mesh_span = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: strip_indices_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: fan_indices_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: vertices_count = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: entity_mesh_id_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: frames_to_render = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: entities_to_render = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: frames_to_increase_render_count = so_called_platform_math_consts :: whole_0 ;
    
    so_called_type_platform_math_num_whole matrices_count ;
    so_called_platform_math :: make_num_whole ( matrices_count , shy_guts :: consts :: entity_mesh_grid ) ;
    so_called_platform_math :: mul_whole_by ( matrices_count , matrices_count ) ;
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , matrices_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_vector_data zero ;
        so_called_type_platform_pointer_data < so_called_type_platform_matrix_data > matrix ;

        so_called_platform_static_array :: element_ptr ( matrix , shy_guts :: entities_grid_matrices , i ) ;
        so_called_platform_vector :: xyz 
            ( zero 
            , so_called_platform_math_consts :: fract_0 
            , so_called_platform_math_consts :: fract_0 
            , so_called_platform_math_consts :: fract_0 
            ) ;
        so_called_platform_matrix :: identity ( matrix . get ( ) ) ;
        so_called_platform_matrix :: set_axis_x ( matrix . get ( ) , zero ) ;
        so_called_platform_matrix :: set_axis_y ( matrix . get ( ) , zero ) ;
        so_called_platform_matrix :: set_axis_z ( matrix . get ( ) , zero ) ;
    }
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_height_request )
{
    so_called_message_common_logic_entities_height_reply entities_height_reply_msg ;
    entities_height_reply_msg . height = shy_guts :: consts :: entity_mesh_height ;
    so_called_sender_common_logic_entities_height_reply :: send ( entities_height_reply_msg ) ;
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_mesh_grid_request )
{
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_origin_request msg )
{
    so_called_message_common_logic_entities_origin_reply entities_origin_reply_msg ;
    shy_guts :: get_entity_origin ( entities_origin_reply_msg . origin , msg . index ) ;
    entities_origin_reply_msg . index = msg . index ;
    so_called_sender_common_logic_entities_origin_reply :: send ( entities_origin_reply_msg ) ;
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_prepare_permit )
{
    shy_guts :: entities_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_render_request )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entity_created ) )
        shy_guts :: entities_render ( ) ;
    so_called_sender_common_logic_entities_render_reply :: send ( so_called_message_common_logic_entities_render_reply ( ) ) ;
}

void _shy_common_logic_entities :: receive ( so_called_message_common_logic_entities_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entities_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: entity_created ) )
        {
            if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: entity_mesh_id_created ) )
            {
                shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
                
                so_called_type_platform_math_num_whole vertices_count ;
                so_called_type_platform_math_num_whole strip_indices_count ;
                so_called_type_platform_math_num_whole fan_indices_count ;
                
                so_called_platform_math :: add_wholes ( vertices_count , shy_guts :: consts :: entity_mesh_spans , so_called_platform_math_consts :: whole_1 ) ;
                so_called_platform_math :: mul_whole_by ( vertices_count , so_called_platform_math_consts :: whole_2 ) ;
                so_called_platform_math :: add_to_whole ( vertices_count , so_called_platform_math_consts :: whole_1 ) ;
                
                so_called_platform_math :: add_wholes ( strip_indices_count , shy_guts :: consts :: entity_mesh_spans , so_called_platform_math_consts :: whole_1 ) ;
                so_called_platform_math :: mul_whole_by ( strip_indices_count , so_called_platform_math_consts :: whole_2 ) ;
                
                so_called_platform_math :: add_wholes ( fan_indices_count , shy_guts :: consts :: entity_mesh_spans , so_called_platform_math_consts :: whole_2 ) ;
                
                so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
                mesh_create_msg . vertices = vertices_count ;
                mesh_create_msg . triangle_strip_indices = strip_indices_count ;
                mesh_create_msg . triangle_fan_indices = fan_indices_count ;
                so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
            }
            else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entity_mesh_id_created ) )
                shy_guts :: create_entity_mesh ( ) ;
        }
        else if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: entity_created ) )
            shy_guts :: update_entity_grid ( ) ;
    }
}
