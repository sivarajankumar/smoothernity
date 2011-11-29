class shy_platform_sound_openal
{
    friend class shy_platform_sound_openal_insider ;

public :
    static so_called_platform_math_const_int_32_type mono_sound_samples_per_second = 22050 ;
    static so_called_platform_math_const_int_32_type stereo_sound_samples_per_second = 44100 ;
    
public :
    static void set_sample_value ( so_called_platform_sound_sample_mono_type & , so_called_platform_math_num_fract_type ) ;
    
    static void set_listener_position ( so_called_platform_vector_data_type ) ;
    static void set_listener_velocity ( so_called_platform_vector_data_type ) ;
    static void set_listener_orientation ( so_called_platform_vector_data_type look_at , so_called_platform_vector_data_type up ) ;
    static void create_source ( so_called_platform_sound_source_id_type & ) ;
    static void set_source_pitch ( const so_called_platform_sound_source_id_type & , so_called_platform_math_num_fract_type ) ;
    static void set_source_gain ( const so_called_platform_sound_source_id_type & , so_called_platform_math_num_fract_type ) ;
    static void set_source_position ( const so_called_platform_sound_source_id_type & , so_called_platform_vector_data_type ) ;
    static void set_source_velocity ( const so_called_platform_sound_source_id_type & , so_called_platform_vector_data_type ) ;
    static void set_source_buffer ( const so_called_platform_sound_source_id_type & , so_called_platform_sound_buffer_id_type & ) ;
    static void set_source_playback_looping ( const so_called_platform_sound_source_id_type & ) ;
    static void set_source_playback_once ( const so_called_platform_sound_source_id_type & ) ;
    static void source_play ( const so_called_platform_sound_source_id_type & ) ;
    static void source_stop ( const so_called_platform_sound_source_id_type & ) ;
    
    template < typename samples_array >
    static void create_mono_buffer ( so_called_platform_sound_buffer_id_type & , const samples_array & , so_called_platform_math_num_whole_type ) ;
    
    template < typename samples_array >
    static void create_stereo_buffer ( so_called_platform_sound_buffer_id_type & , const samples_array & , so_called_platform_math_num_whole_type ) ;

private :
    static void _create_mono_buffer 
        ( so_called_platform_sound_buffer_id_type &  
        , const so_called_platform_sound_sample_mono_type *  
        , so_called_platform_math_num_whole_type  
        ) ;
    static void _create_stereo_buffer 
        ( so_called_platform_sound_buffer_id_type & 
        , const so_called_platform_sound_sample_stereo_type * 
        , so_called_platform_math_num_whole_type 
        ) ;
} ;

template < typename samples_array >
void shy_platform_sound_openal :: create_mono_buffer 
    ( so_called_platform_sound_buffer_id_type & result
    , const samples_array & samples 
    , so_called_platform_math_num_whole_type samples_count 
    )
{
    so_called_trace ( so_called_trace_platform_sound :: template check_args_create_mono_buffer < samples_array > ( samples_count ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: buffer_create ( ) ) ;
    so_called_lib_std_int32_t size = 0 ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( size ) ;
    const so_called_platform_sound_sample_mono_type * samples_ptr = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;

    _create_mono_buffer ( result , samples_ptr , samples_count ) ;
}
    
template < typename samples_array >
void shy_platform_sound_openal :: create_stereo_buffer 
    ( so_called_platform_sound_buffer_id_type & result
    , const samples_array & samples 
    , so_called_platform_math_num_whole_type samples_count 
    )
{
    so_called_trace ( so_called_trace_platform_sound :: template check_args_create_stereo_buffer < samples_array > ( samples_count ) ) ;
    so_called_profile ( so_called_profile_platform_sound :: buffer_create ( ) ) ;
    so_called_lib_std_int32_t size = 0 ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( size ) ;
    const so_called_platform_sound_sample_stereo_type * samples_ptr = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;

    _create_stereo_buffer ( result , samples_ptr , samples_count ) ;
}

