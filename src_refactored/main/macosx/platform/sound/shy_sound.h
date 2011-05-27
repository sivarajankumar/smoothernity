class shy_macosx_platform_sound
{
    friend class shy_macosx_platform_sound_insider ;

public :
    static so_called_type_platform_math_const_int_32 mono_sound_samples_per_second = 22050 ;
    static so_called_type_platform_math_const_int_32 stereo_sound_samples_per_second = 44100 ;
    
public :
    static void set_sample_value ( so_called_type_platform_sound_sample_mono & sample , so_called_type_platform_math_num_fract value ) ;
    static void create_stereo_resource_id ( so_called_type_platform_sound_stereo_resource_id & result , so_called_type_platform_math_num_whole resource_index ) ;
    
    static void set_listener_position ( so_called_type_platform_vector_data position ) ;
    static void set_listener_velocity ( so_called_type_platform_vector_data velocity ) ;
    static void set_listener_orientation ( so_called_type_platform_vector_data look_at , so_called_type_platform_vector_data up ) ;
    static void loader_ready ( so_called_type_platform_math_num_whole & result ) ;
    static void loaded_samples_count ( so_called_type_platform_math_num_whole & result ) ;    
    static void create_source ( so_called_type_platform_sound_source_id & result ) ;
    static void set_source_pitch ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract pitch ) ;
    static void set_source_gain ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_math_num_fract gain ) ;
    static void set_source_position ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data position ) ;
    static void set_source_velocity ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_vector_data velocity ) ;
    static void set_source_buffer ( const so_called_type_platform_sound_source_id & source_id , so_called_type_platform_sound_buffer_id & buffer_id ) ;
    static void set_source_playback_looping ( const so_called_type_platform_sound_source_id & source_id ) ;
    static void set_source_playback_once ( const so_called_type_platform_sound_source_id & source_id ) ;
    static void source_play ( const so_called_type_platform_sound_source_id & source_id ) ;
    static void source_stop ( const so_called_type_platform_sound_source_id & source_id ) ;
    
    template < typename samples_array >
    static void load_stereo_sample_data ( const samples_array & samples , const so_called_type_platform_sound_stereo_resource_id & resource_id ) ;
    
    template < typename samples_array >
    static void create_mono_buffer ( so_called_type_platform_sound_buffer_id & result , const samples_array & samples , so_called_type_platform_math_num_whole samples_count ) ;
    
    template < typename samples_array >
    static void create_stereo_buffer ( so_called_type_platform_sound_buffer_id & result , const samples_array & samples , so_called_type_platform_math_num_whole samples_count ) ;

private :
    static void _load_stereo_sample_data 
        ( const so_called_type_platform_sound_sample_stereo * samples_ptr 
        , so_called_lib_std_int32_t samples_count 
        , const so_called_type_platform_sound_stereo_resource_id & resource_id 
        ) ;
    static void _create_mono_buffer 
        ( so_called_type_platform_sound_buffer_id & result 
        , const so_called_type_platform_sound_sample_mono * samples_ptr 
        , so_called_type_platform_math_num_whole samples_count 
        ) ;
    static void _create_stereo_buffer 
        ( so_called_type_platform_sound_buffer_id & result 
        , const so_called_type_platform_sound_sample_stereo * samples_ptr 
        , so_called_type_platform_math_num_whole samples_count 
        ) ;
private :
    static void * _sound_loader ;
} ;

template < typename samples_array >
void shy_macosx_platform_sound :: load_stereo_sample_data
    ( const samples_array & samples 
    , const so_called_type_platform_sound_stereo_resource_id & resource_id 
    )
{
    const so_called_type_platform_sound_sample_stereo * samples_ptr = 0 ;
    int samples_count = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( samples_count ) ;

    _load_stereo_sample_data ( samples_ptr , samples_count , resource_id ) ;
}

template < typename samples_array >
void shy_macosx_platform_sound :: create_mono_buffer 
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
void shy_macosx_platform_sound :: create_stereo_buffer 
    ( so_called_type_platform_sound_buffer_id & result
    , const samples_array & samples 
    , so_called_type_platform_math_num_whole samples_count 
    )
{
    const so_called_type_platform_sound_sample_stereo * samples_ptr = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;

    _create_stereo_buffer ( result , samples_ptr , samples_count ) ;
}
