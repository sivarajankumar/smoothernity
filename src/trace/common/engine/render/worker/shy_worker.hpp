namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_engine_render" ;
    }
}

void shy_trace_common_engine_render_worker :: meshes_in_use 
    ( so_called_type_platform_math_num_whole current 
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Meshes in use: " ) ;
    so_called_platform_trace :: trace_num_whole ( current ) ;
    so_called_platform_trace :: trace_string ( " of " ) ;
    so_called_platform_trace :: trace_num_whole ( total ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: meshes_overflow_error ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Meshes overflow error." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: meshes_underflow_error ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Meshes underflow error." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: mesh_index_out_of_range_error
    ( so_called_type_platform_math_num_whole current
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Mesh index subscript of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( current ) ;
    so_called_platform_trace :: trace_string_error ( " exceeds indices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( total ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: mesh_vertex_out_of_range_error
    ( so_called_type_platform_math_num_whole current
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Mesh vertex subscript of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( current ) ;
    so_called_platform_trace :: trace_string_error ( " exceeds vertices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( total ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: mesh_too_many_indices_error
    ( so_called_type_platform_math_num_whole current
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Requested mesh indices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( current ) ;
    so_called_platform_trace :: trace_string_error ( " exceeds maximum indices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( total ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: mesh_too_many_vertices_error
    ( so_called_type_platform_math_num_whole current
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Requested mesh vertices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( current ) ;
    so_called_platform_trace :: trace_string_error ( " exceeds maximum vertices count of " ) ;
    so_called_platform_trace :: trace_num_whole_error ( total ) ;
    so_called_platform_trace :: trace_string_error ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: trying_to_modify_finalized_mesh_error ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Error. Trying to modify mesh that has been already finalized." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: textures_in_use
    ( so_called_type_platform_math_num_whole current 
    , so_called_type_platform_math_num_whole total
    )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string ( "Textures in use: " ) ;
    so_called_platform_trace :: trace_num_whole ( current ) ;
    so_called_platform_trace :: trace_string ( " of " ) ;
    so_called_platform_trace :: trace_num_whole ( total ) ;
    so_called_platform_trace :: trace_string ( "." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}

void shy_trace_common_engine_render_worker :: textures_overflow_error ( )
{
    so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
    so_called_platform_trace :: trace_string_error ( "Textures overflow error." ) ;
    so_called_platform_trace :: trace_end ( ) ;
}
