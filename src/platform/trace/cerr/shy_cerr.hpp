namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_int32_t digits_per_frame = 4 ;
        static const so_called_lib_std_char divide = '/' ;
        static void trace_stamp ( so_called_lib_std_string & , so_called_lib_std_string , so_called_lib_std_string ) ;
    }
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

    so_called_platform_trace_consts :: module_name_begin ( name_begin ) ;
    so_called_platform_trace_consts :: module_name_end ( name_end ) ;
    so_called_platform_trace_consts :: number_begin ( number_begin ) ;
    so_called_platform_trace_consts :: number_end ( number_end ) ;

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

void shy_platform_trace_cerr :: trace_num_whole ( so_called_platform_math_num_whole_type num )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_int32_t num_int = 0 ;

    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    so_called_platform_trace_consts :: number_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num_int ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_whole_error ( so_called_platform_math_num_whole_type num )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_int32_t num_int = 0 ;

    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    so_called_platform_trace_consts :: number_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num_int ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_const_int_32 ( so_called_platform_math_const_int_32_type num )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: number_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_const_int_32_error ( so_called_platform_math_const_int_32_type num )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: number_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << num ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_fract 
    ( so_called_platform_math_const_int_32_type numerator
    , so_called_platform_math_const_int_32_type denominator
    )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: number_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << numerator ;
    so_called_lib_std_cerr << shy_guts :: consts :: divide ;
    so_called_lib_std_cerr << denominator ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_fract ( so_called_platform_math_num_fract_type value )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_float value_float = 0 ;

    so_called_platform_math_insider :: num_fract_value_get ( value_float , value ) ;
    so_called_platform_trace_consts :: number_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << value_float ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_fract_error
    ( so_called_platform_math_const_int_32_type numerator
    , so_called_platform_math_const_int_32_type denominator
    )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: number_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << numerator ;
    so_called_lib_std_cerr << shy_guts :: consts :: divide ;
    so_called_lib_std_cerr << denominator ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_num_fract_error ( so_called_platform_math_num_fract_type value )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;
    so_called_lib_std_float value_float = 0 ;

    so_called_platform_math_insider :: num_fract_value_get ( value_float , value ) ;
    so_called_platform_trace_consts :: number_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: number_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << value_float ;
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

    so_called_platform_trace_consts :: string_name_begin ( str_begin ) ;
    so_called_platform_trace_consts :: string_name_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_string_name_error ( const so_called_lib_std_char * s )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: string_name_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: string_name_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}

void shy_platform_trace_cerr :: trace_string_error ( const so_called_lib_std_char * s )
{
    so_called_lib_std_string str_begin ;
    so_called_lib_std_string str_end ;

    so_called_platform_trace_consts :: string_error_begin ( str_begin ) ;
    so_called_platform_trace_consts :: string_error_end ( str_end ) ;

    so_called_lib_std_cerr << str_begin ;
    so_called_lib_std_cerr << s ;
    so_called_lib_std_cerr << str_end ;
}
