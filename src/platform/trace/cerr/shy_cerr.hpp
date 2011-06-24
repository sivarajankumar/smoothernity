namespace shy_guts
{
    namespace consts
    {
        static void trace_finished ( so_called_lib_std_string & ) ;
        static void trace_stamp ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void trace_started ( so_called_lib_std_string & ) ;
    }
}

void shy_guts :: consts :: trace_finished ( so_called_lib_std_string & result )
{
    result = "Trace finished." ;
}

void shy_guts :: consts :: trace_stamp 
    ( so_called_lib_std_string & result
    , so_called_lib_std_string frame
    , so_called_lib_std_string module
    )
{
    result . clear ( ) ;
    result += "Frame " ;
    result += frame ;
    result += ". Module \"" ;
    result += module ;
    result += "\". " ;
}

void shy_guts :: consts :: trace_started ( so_called_lib_std_string & result )
{
    result = "Trace started." ;
}

void shy_platform_trace_cerr :: init ( )
{
    so_called_lib_std_string str ;
    shy_guts :: consts :: trace_started ( str ) ;
    so_called_lib_std_cerr << str ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_platform_trace_cerr :: done ( )
{
    so_called_lib_std_string str ;
    shy_guts :: consts :: trace_finished ( str ) ;
    so_called_lib_std_cerr << str ;
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_platform_trace_cerr :: trace_begin ( const so_called_lib_std_char * module )
{
    so_called_lib_std_int32_t current_frame ;
    so_called_lib_std_ostringstream current_frame_stream ;
    so_called_lib_std_string stamp ;

    so_called_platform_trace_insider :: get_current_frame ( current_frame ) ;
    current_frame_stream << current_frame ;
    shy_guts :: consts :: trace_stamp ( stamp , current_frame_stream . str ( ) , module ) ;
    so_called_lib_std_cerr << stamp ;
}

void shy_platform_trace_cerr :: trace_end ( )
{
    so_called_lib_std_cerr << so_called_lib_std_endl ;
}

void shy_platform_trace_cerr :: trace_num_whole ( so_called_type_platform_math_num_whole num )
{
    so_called_lib_std_int32_t num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    so_called_lib_std_cerr << num_int ;
}

void shy_platform_trace_cerr :: trace_string ( const so_called_lib_std_char * s )
{
    so_called_lib_std_cerr << s ;
}
