class shy_platform_sound_openal
{
    friend class shy_platform_sound_openal_insider ;

public :
    static so_called_type_platform_math_const_int_32 mono_sound_samples_per_second = 22050 ;
    static so_called_type_platform_math_const_int_32 stereo_sound_samples_per_second = 44100 ;
    
public :
    static void set_sample_value ( so_called_type_platform_sound_sample_mono & , so_called_type_platform_math_num_fract ) ;
    
    static void set_listener_position ( so_called_type_platform_vector_data ) ;
    static void set_listener_velocity ( so_called_type_platform_vector_data ) ;
    static void set_listener_orientation ( so_called_type_platform_vector_data look_at , so_called_type_platform_vector_data up ) ;
    static void create_source ( so_called_type_platform_sound_source_id & ) ;
    static void set_source_pitch ( const so_called_type_platform_sound_source_id & , so_called_type_platform_math_num_fract ) ;
    static void set_source_gain ( const so_called_type_platform_sound_source_id & , so_called_type_platform_math_num_fract ) ;
    static void set_source_position ( const so_called_type_platform_sound_source_id & , so_called_type_platform_vector_data ) ;
    static void set_source_velocity ( const so_called_type_platform_sound_source_id & , so_called_type_platform_vector_data ) ;
    static void set_source_buffer ( const so_called_type_platform_sound_source_id & , so_called_type_platform_sound_buffer_id & ) ;
    static void set_source_playback_looping ( const so_called_type_platform_sound_source_id & ) ;
    static void set_source_playback_once ( const so_called_type_platform_sound_source_id & ) ;
    static void source_play ( const so_called_type_platform_sound_source_id & ) ;
    static void source_stop ( const so_called_type_platform_sound_source_id & ) ;
    
    template < typename samples_array >
    static void create_mono_buffer ( so_called_type_platform_sound_buffer_id & , const samples_array & , so_called_type_platform_math_num_whole ) ;
    
    template < typename samples_array >
    static void create_stereo_buffer ( so_called_type_platform_sound_buffer_id & , const samples_array & , so_called_type_platform_math_num_whole ) ;

private :
    static void _create_mono_buffer 
        ( so_called_type_platform_sound_buffer_id &  
        , const so_called_type_platform_sound_sample_mono *  
        , so_called_type_platform_math_num_whole  
        ) ;
    static void _create_stereo_buffer 
        ( so_called_type_platform_sound_buffer_id & 
        , const so_called_type_platform_sound_sample_stereo * 
        , so_called_type_platform_math_num_whole 
        ) ;
} ;

template < typename samples_array >
void shy_platform_sound_openal :: create_mono_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const samples_array & samples 
    , so_called_type_platform_math_num_whole samples_count 
    )
{
    const so_called_type_platform_sound_sample_mono * samples_ptr = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;

    _create_mono_buffer ( result , samples_ptr , samples_count ) ;
}
    
template < typename samples_array >
void shy_platform_sound_openal :: create_stereo_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const samples_array & samples 
    , so_called_type_platform_math_num_whole samples_count 
    )
{
    const so_called_type_platform_sound_sample_stereo * samples_ptr = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;

    _create_stereo_buffer ( result , samples_ptr , samples_count ) ;
}

