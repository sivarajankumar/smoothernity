template < typename platform_insider >
class shy_macosx_platform_sound
{
    typedef typename platform_insider :: platform_math :: const_int_32 const_int_32 ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    typedef typename platform_insider :: platform_static_array_insider platform_static_array_insider ;
    typedef typename platform_insider :: platform_vector :: vector_data vector_data ;
    typedef typename platform_insider :: platform_vector_insider platform_vector_insider ;

public :
    static const_int_32 mono_sound_samples_per_second = 22050 ;
    static const_int_32 stereo_sound_samples_per_second = 44100 ;
    
public :
    class mono_sound_sample
    {
        friend class shy_macosx_platform_sound ;
    public :
        mono_sound_sample ( ) ;
    private :
        ALubyte _value ;
    } ;
    
    class stereo_sound_sample
    {
        friend class shy_macosx_platform_sound ;
    public :
        stereo_sound_sample ( ) ;
    private :
        ALushort _left_channel_value ;
        ALushort _right_channel_value ; 
    } ;
    
    class sound_buffer_id
    {
        friend class shy_macosx_platform_sound ;
    public :
        sound_buffer_id ( ) ;
    private :
        ALuint _buffer_id ;
    } ;
    
    class sound_source_id
    {
        friend class shy_macosx_platform_sound ;
    public :
        sound_source_id ( ) ;
    private :
        ALuint _source_id ;
    } ;
    
    class stereo_sound_resource_id
    {
        friend class shy_macosx_platform_sound ;
    public :
        stereo_sound_resource_id ( ) ;
    private :
        int _resource_id ;
    } ;
    
public :
    static void sound_set_listener_position ( vector_data position ) ;
    static void sound_set_listener_velocity ( vector_data velocity ) ;
    static void sound_set_listener_orientation ( vector_data look_at , vector_data up ) ;
    static void sound_set_sample_value ( mono_sound_sample & sample , num_fract value ) ;
    static void sound_create_stereo_resource_id ( stereo_sound_resource_id & result , num_whole resource_index ) ;
    static void sound_loader_ready ( num_whole & result ) ;
    static void sound_loaded_samples_count ( num_whole & result ) ;    
    static void sound_create_source ( sound_source_id & result ) ;
    static void sound_set_source_pitch ( const sound_source_id & source_id , num_fract pitch ) ;
    static void sound_set_source_gain ( const sound_source_id & source_id , num_fract gain ) ;
    static void sound_set_source_position ( const sound_source_id & source_id , vector_data position ) ;
    static void sound_set_source_velocity ( const sound_source_id & source_id , vector_data velocity ) ;
    static void sound_set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id ) ;
    static void sound_set_source_playback_looping ( const sound_source_id & source_id ) ;
    static void sound_set_source_playback_once ( const sound_source_id & source_id ) ;
    static void sound_source_play ( const sound_source_id & source_id ) ;
    static void sound_source_stop ( const sound_source_id & source_id ) ;
    
    template < typename samples_array >
    static void sound_load_stereo_sample_data ( const samples_array & samples , const stereo_sound_resource_id & resource_id ) ;
    
    template < typename samples_array >
    static void sound_create_mono_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;
    
    template < typename samples_array >
    static void sound_create_stereo_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;
} ;

template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: mono_sound_sample :: mono_sound_sample ( )
: _value ( ( GLubyte ) platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: stereo_sound_sample :: stereo_sound_sample ( )
: _left_channel_value ( ( GLushort ) platform_insider :: uninitialized_value )
, _right_channel_value ( ( GLushort ) platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: sound_buffer_id :: sound_buffer_id ( )
: _buffer_id ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: sound_source_id :: sound_source_id ( )
: _source_id ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: stereo_sound_resource_id :: stereo_sound_resource_id ( )
: _resource_id ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_listener_position ( vector_data position )
{
    ALfloat al_position [ ] = 
        { platform_vector_insider :: x_unsafe_get ( position )
        , platform_vector_insider :: y_unsafe_get ( position )
        , platform_vector_insider :: z_unsafe_get ( position ) 
        } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_listener_velocity ( vector_data velocity )
{
    ALfloat al_velocity [ ] =
        { platform_vector_insider :: x_unsafe_get ( velocity )
        , platform_vector_insider :: y_unsafe_get ( velocity )
        , platform_vector_insider :: z_unsafe_get ( velocity ) 
        } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_listener_orientation ( vector_data look_at , vector_data up )
{
    ALfloat al_orientation [ ] = 
        { platform_vector_insider :: x_unsafe_get ( look_at )
        , platform_vector_insider :: y_unsafe_get ( look_at )
        , platform_vector_insider :: z_unsafe_get ( look_at )
        , platform_vector_insider :: x_unsafe_get ( up )
        , platform_vector_insider :: y_unsafe_get ( up )
        , platform_vector_insider :: z_unsafe_get ( up )
        } ;
    alListenerfv ( AL_ORIENTATION , al_orientation ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_sample_value ( mono_sound_sample & sample , num_fract value )
{
    sample . _value = ( ALubyte ) ( ( platform_math_insider :: num_fract_unsafe_value_get ( value ) * 127.0f ) + 127.0f ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_create_stereo_resource_id 
    ( stereo_sound_resource_id & result 
    , num_whole resource_index
    )
{
    result . _resource_id = platform_math_insider :: num_whole_unsafe_value_get ( resource_index ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: sound_load_stereo_sample_data
    ( const samples_array & samples 
    , const stereo_sound_resource_id & resource_id 
    )
{
    [ platform_insider :: sound_loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) platform_static_array_insider :: elements_unsafe_ptr ( samples )
        with_max_samples_count_of : platform_static_array_insider :: template elements_count < samples_array > ( )
    ] ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_loader_ready ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , [ platform_insider :: sound_loader loader_ready ] ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_loaded_samples_count ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , [ platform_insider :: sound_loader loaded_samples_count ] ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: sound_create_mono_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    al_buffer_data_static_proc
        ( result . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) platform_static_array_insider :: elements_unsafe_ptr ( samples )
        , platform_math_insider :: num_whole_unsafe_value_get ( samples_count ) * sizeof ( mono_sound_sample )
        , mono_sound_samples_per_second
        ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: sound_create_stereo_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    alBufferDataStaticProcPtr al_buffer_data_static_proc = 
        ( alBufferDataStaticProcPtr ) alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    al_buffer_data_static_proc
        ( result . _buffer_id 
        , AL_FORMAT_STEREO16 
        , ( ALvoid * ) platform_static_array_insider :: elements_unsafe_ptr ( samples )
        , platform_math_insider :: num_whole_unsafe_value_get ( samples_count ) * sizeof ( stereo_sound_sample )
        , stereo_sound_samples_per_second
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_create_source ( sound_source_id & result )
{
    alGenSources ( 1 , & result . _source_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_pitch ( const sound_source_id & source_id , num_fract pitch )
{
    alSourcef ( source_id . _source_id , AL_PITCH , platform_math_insider :: num_fract_unsafe_value_get ( pitch ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_gain ( const sound_source_id & source_id , num_fract gain )
{
    alSourcef ( source_id . _source_id , AL_GAIN , platform_math_insider :: num_fract_unsafe_value_get ( gain ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_position ( const sound_source_id & source_id , vector_data position )
{
    ALfloat al_position [ ] = 
        { platform_vector_insider :: x_unsafe_get ( position )
        , platform_vector_insider :: y_unsafe_get ( position )
        , platform_vector_insider :: z_unsafe_get ( position ) 
        } ;
    alSourcefv ( source_id . _source_id , AL_POSITION , al_position ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_velocity ( const sound_source_id & source_id , vector_data velocity )
{
    ALfloat al_velocity [ ] =
        { platform_vector_insider :: x_unsafe_get ( velocity )
        , platform_vector_insider :: y_unsafe_get ( velocity )
        , platform_vector_insider :: z_unsafe_get ( velocity ) 
        } ;
    alSourcefv ( source_id . _source_id , AL_VELOCITY , al_velocity ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id )
{
    alSourcei ( source_id . _source_id , AL_BUFFER , buffer_id . _buffer_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_playback_looping ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_TRUE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_set_source_playback_once ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_FALSE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_source_play ( const sound_source_id & source_id )
{
    alSourcePlay ( source_id . _source_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: sound_source_stop ( const sound_source_id & source_id )
{
    alSourceStop ( source_id . _source_id ) ;
}
