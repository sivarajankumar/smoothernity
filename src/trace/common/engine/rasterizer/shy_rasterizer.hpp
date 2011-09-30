namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "common_engine_rasterizer" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_common_engine_rasterizer :: coords_out_of_range_error
    ( so_called_platform_math_num_whole_type x
    , so_called_platform_math_num_whole_type y
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Texture coordinates X = " ) ;
        so_called_platform_trace :: trace_num_whole_error ( x ) ;
        so_called_platform_trace :: trace_string_error ( ", Y = " ) ;
        so_called_platform_trace :: trace_num_whole_error ( y ) ;
        so_called_platform_trace :: trace_string_error ( " are out of range 0 <= X < " ) ;
        so_called_platform_trace :: trace_num_whole_error ( so_called_common_engine_render_consts :: texture_width ) ;
        so_called_platform_trace :: trace_string_error ( ", 0 <= Y < " ) ;
        so_called_platform_trace :: trace_num_whole_error ( so_called_common_engine_render_consts :: texture_height ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}
