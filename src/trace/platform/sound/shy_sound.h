class shy_trace_platform_sound
{
public :
    template < typename samples_array >
    static void check_args_create_mono_buffer ( so_called_platform_math_num_whole_type ) ;

    template < typename samples_array >
    static void check_args_create_stereo_buffer ( so_called_platform_math_num_whole_type ) ;

    static void check_buffer_id_uninitialized ( so_called_platform_sound_buffer_id_type ) ;
    static void check_source_id_uninitialized ( so_called_platform_sound_source_id_type ) ;
private :
    static void _check_args_create_buffer 
        ( so_called_lib_std_int32_t array_size
        , so_called_platform_math_num_whole_type samples_count 
        ) ;
} ;

template < typename samples_array >
void shy_trace_platform_sound :: check_args_create_mono_buffer ( so_called_platform_math_num_whole_type samples_count )
{
    so_called_lib_std_int32_t array_size = 0 ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( array_size ) ;
    _check_args_create_buffer ( array_size , samples_count ) ;
}

template < typename samples_array >
void shy_trace_platform_sound :: check_args_create_stereo_buffer ( so_called_platform_math_num_whole_type samples_count )
{
    so_called_lib_std_int32_t array_size = 0 ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( array_size ) ;
    _check_args_create_buffer ( array_size , samples_count ) ;
}
