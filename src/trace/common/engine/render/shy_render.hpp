namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_engine_render" ;
        static const so_called_platform_math_num_whole_type trace_enabled = so_called_platform_math :: init_num_whole ( so_called_lib_std_true ) ;
    }
}

void shy_trace_common_engine_render :: meshes_in_use 
    ( so_called_platform_math_num_whole_type current 
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Meshes in use: " ) ;
        so_called_platform_trace :: trace_num_whole ( current ) ;
        so_called_platform_trace :: trace_string ( " of " ) ;
        so_called_platform_trace :: trace_num_whole ( total ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: meshes_overflow_error ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Meshes overflow error." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: meshes_underflow_error ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Meshes underflow error." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: mesh_index_offset_out_of_range_error
    ( so_called_platform_math_num_whole_type current
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Mesh index offset of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds indices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: mesh_index_value_out_of_range_error
    ( so_called_platform_math_num_whole_type current
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Mesh index value of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds vertices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: mesh_vertex_out_of_range_error
    ( so_called_platform_math_num_whole_type current
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Mesh vertex subscript of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds vertices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: mesh_too_many_indices_error
    ( so_called_platform_math_num_whole_type current
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Requested mesh indices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds maximum indices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: mesh_too_many_vertices_error
    ( so_called_platform_math_num_whole_type current
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Requested mesh vertices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( current ) ;
        so_called_platform_trace :: trace_string_error ( " exceeds maximum vertices count of " ) ;
        so_called_platform_trace :: trace_num_whole_error ( total ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: trying_to_modify_finalized_mesh_error ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Trying to modify mesh that has been already finalized." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: textures_in_use
    ( so_called_platform_math_num_whole_type current 
    , so_called_platform_math_num_whole_type total
    )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Textures in use: " ) ;
        so_called_platform_trace :: trace_num_whole ( current ) ;
        so_called_platform_trace :: trace_string ( " of " ) ;
        so_called_platform_trace :: trace_num_whole ( total ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_common_engine_render :: textures_overflow_error ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: consts :: trace_enabled ) )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Textures overflow error." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
