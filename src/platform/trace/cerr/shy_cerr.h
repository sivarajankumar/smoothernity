class shy_platform_trace_cerr
{
public :
    static void init ( ) ;
    static void done ( ) ;
    static void trace_begin ( const so_called_lib_std_char * ) ;
    static void trace_end ( ) ;
    static void trace_num_whole ( so_called_type_platform_math_num_whole ) ;
    static void trace_num_whole_error ( so_called_type_platform_math_num_whole ) ;
    static void trace_string ( const so_called_lib_std_char * ) ;
    static void trace_string_name ( const so_called_lib_std_char * ) ;
    static void trace_string_name_error ( const so_called_lib_std_char * ) ;
    static void trace_string_error ( const so_called_lib_std_char * ) ;
} ;
