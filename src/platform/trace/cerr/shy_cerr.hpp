namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_int32_t digits_per_frame = 4 ;
        static void trace_finished ( so_called_lib_std_string & ) ;
        static void trace_module_name_begin ( so_called_lib_std_string & ) ;
        static void trace_module_name_end ( so_called_lib_std_string & ) ;
        static void trace_number_begin ( so_called_lib_std_string & ) ;
        static void trace_number_end ( so_called_lib_std_string & ) ;
        static void trace_number_error_begin ( so_called_lib_std_string & ) ;
        static void trace_number_error_end ( so_called_lib_std_string & ) ;
        static void trace_stamp ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
        static void trace_started ( so_called_lib_std_string & ) ;
        static void trace_string_error_begin ( so_called_lib_std_string & ) ;
        static void trace_string_error_end ( so_called_lib_std_string & ) ;
        static void trace_string_name_begin ( so_called_lib_std_string & ) ;
        static void trace_string_name_end ( so_called_lib_std_string & ) ;
        static void trace_string_name_error_begin ( so_called_lib_std_string & ) ;
        static void trace_string_name_error_end ( so_called_lib_std_string & ) ;
    }
}

void shy_guts :: consts :: trace_module_name_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_cyan ;
}

void shy_guts :: consts :: trace_module_name_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: trace_number_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_blue ;
}

void shy_guts :: consts :: trace_number_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: trace_number_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_yellow ;
}

void shy_guts :: consts :: trace_number_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: trace_string_name_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_green ;
}

void shy_guts :: consts :: trace_string_name_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: trace_string_name_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: background_color_default ;
    result += so_called_platform_terminal_consts :: text_color_magenta ;
}

void shy_guts :: consts :: trace_string_name_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
}

void shy_guts :: consts :: trace_string_error_begin ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: bright ;
    result += so_called_platform_terminal_consts :: background_color_red ;
    result += so_called_platform_terminal_consts :: text_color_white ;
}

void shy_guts :: consts :: trace_string_error_end ( so_called_lib_std_string & result )
{
    result = so_called_platform_terminal_consts :: reset_to_default ;
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
    so_called_lib_std_string name_begin ;
    so_called_lib_std_string name_end ;
    so_called_lib_std_string number_begin ;
    so_called_lib_std_string number_end ;

    shy_guts :: consts :: trace_module_name_begin ( name_begin ) ;
    shy_guts :: consts :: trace_module_name_end ( name_end ) ;
    shy_guts :: consts :: trace_number_begin ( number_begin ) ;
    shy_guts :: consts :: trace_number_end ( number_end ) ;

    result . clear ( ) ;
    result += "Frame " ;
    result += number_begin ;
    result += frame ;
    result += number_end ;
    result += ". Module " ;
    result += name_begin ;
    result += "\"" ;
    result += module ;
    result += "\"" ;
    result += name_end ;
    result += ". " ;
}

void shy_guts :: consts :: trace_started ( so_called_lib_std_string & result )
{
    result . clear ( ) ;
    result += so_called_platform_terminal_consts :: reset_to_default ;
    result += "Trace started." ;
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
    current_frame_stream . width ( shy_guts :: consts :: digits_per_frame ) ;
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
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_int32_t num_int = 0 ;

    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    shy_guts :: consts :: trace_number_begin ( str_begin ) ;
    shy_guts :: consts :: trace_number_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num_int ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_whole_error ( so_called_type_platform_math_num_whole num )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_int32_t num_int = 0 ;

    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    shy_guts :: consts :: trace_number_error_begin ( str_begin ) ;
    shy_guts :: consts :: trace_number_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num_int ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_string ( const so_called_lib_std_char * s )
{
    so_called_lib_std_cerr << s ;
}

void shy_platform_trace_cerr :: trace_string_name ( const so_called_lib_std_char * s )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    shy_guts :: consts :: trace_string_name_begin ( str_begin ) ;
    shy_guts :: consts :: trace_string_name_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_string_name_error ( const so_called_lib_std_char * s )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    shy_guts :: consts :: trace_string_name_error_begin ( str_begin ) ;
    shy_guts :: consts :: trace_string_name_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_string_error ( const so_called_lib_std_char * s )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    shy_guts :: consts :: trace_string_error_begin ( str_begin ) ;
    shy_guts :: consts :: trace_string_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}
