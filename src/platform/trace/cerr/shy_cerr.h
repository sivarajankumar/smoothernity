class shy_platform_trace_cerr
{
public :
    static void trace_begin ( const so_called_lib_std_char * ) ;
    static void trace_end ( ) ;
    static void trace_const_int_32 ( so_called_platform_math_const_int_32_type ) ;
    static void trace_const_int_32_error ( so_called_platform_math_const_int_32_type ) ;
    static void trace_num_fract ( so_called_platform_math_num_fract_type ) ;
    static void trace_num_fract ( so_called_platform_math_const_int_32_type , so_called_platform_math_const_int_32_type ) ;
    static void trace_num_fract_error ( so_called_platform_math_num_fract_type ) ;
    static void trace_num_fract_error ( so_called_platform_math_const_int_32_type , so_called_platform_math_const_int_32_type ) ;
    static void trace_num_whole ( so_called_platform_math_num_whole_type ) ;
    static void trace_num_whole_error ( so_called_platform_math_num_whole_type ) ;
    static void trace_string ( const so_called_lib_std_char * ) ;
    static void trace_string_name ( const so_called_lib_std_char * ) ;
    static void trace_string_name_error ( const so_called_lib_std_char * ) ;
    static void trace_string_error ( const so_called_lib_std_char * ) ;
} ;
