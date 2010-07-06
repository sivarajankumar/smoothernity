template < typename platform_insider >
class shy_macosx_platform_sound_insider ;

template < typename platform_insider >
class shy_macosx_platform_sound
{
    friend class shy_macosx_platform_sound_insider < platform_insider > ;

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
    shy_macosx_platform_sound ( ) ;
    
    static void set_sample_value ( mono_sound_sample & sample , num_fract value ) ;
    static void create_stereo_resource_id ( stereo_sound_resource_id & result , num_whole resource_index ) ;
    
    void set_listener_position ( vector_data position ) ;
    void set_listener_velocity ( vector_data velocity ) ;
    void set_listener_orientation ( vector_data look_at , vector_data up ) ;
    void loader_ready ( num_whole & result ) ;
    void loaded_samples_count ( num_whole & result ) ;    
    void create_source ( sound_source_id & result ) ;
    void set_source_pitch ( const sound_source_id & source_id , num_fract pitch ) ;
    void set_source_gain ( const sound_source_id & source_id , num_fract gain ) ;
    void set_source_position ( const sound_source_id & source_id , vector_data position ) ;
    void set_source_velocity ( const sound_source_id & source_id , vector_data velocity ) ;
    void set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id ) ;
    void set_source_playback_looping ( const sound_source_id & source_id ) ;
    void set_source_playback_once ( const sound_source_id & source_id ) ;
    void source_play ( const sound_source_id & source_id ) ;
    void source_stop ( const sound_source_id & source_id ) ;
    
    template < typename samples_array >
    void load_stereo_sample_data ( const samples_array & samples , const stereo_sound_resource_id & resource_id ) ;
    
    template < typename samples_array >
    void create_mono_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;
    
    template < typename samples_array >
    void create_stereo_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;

private :
    shy_macosx_sound_loader * _sound_loader ;
} ;

template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: shy_macosx_platform_sound ( )
: _sound_loader ( 0 )
{
}

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
: _buffer_id ( ALuint ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: sound_source_id :: sound_source_id ( )
: _source_id ( ALuint ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_macosx_platform_sound < platform_insider > :: stereo_sound_resource_id :: stereo_sound_resource_id ( )
: _resource_id ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_listener_position ( vector_data position )
{
    float x ;
    float y ;
    float z ;
    platform_vector_insider :: x_get ( x , position ) ;
    platform_vector_insider :: y_get ( y , position ) ;
    platform_vector_insider :: z_get ( z , position ) ;
    ALfloat al_position [ ] = { x , y , z } ;
    alListenerfv ( AL_POSITION , al_position ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_listener_velocity ( vector_data velocity )
{
    float x ;
    float y ;
    float z ;
    platform_vector_insider :: x_get ( x , velocity ) ;
    platform_vector_insider :: y_get ( y , velocity ) ;
    platform_vector_insider :: z_get ( z , velocity ) ;
    ALfloat al_velocity [ ] = { x , y , z } ;
    alListenerfv ( AL_VELOCITY , al_velocity ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_listener_orientation ( vector_data look_at , vector_data up )
{
    float look_at_x ;
    float look_at_y ;
    float look_at_z ;
    float up_x ;
    float up_y ;
    float up_z ;
    platform_vector_insider :: x_get ( look_at_x , look_at ) ;
    platform_vector_insider :: y_get ( look_at_y , look_at ) ;
    platform_vector_insider :: z_get ( look_at_z , look_at ) ;
    platform_vector_insider :: x_get ( up_x , up ) ;
    platform_vector_insider :: y_get ( up_y , up ) ;
    platform_vector_insider :: z_get ( up_z , up ) ;
    ALfloat al_orientation [ ] = 
        { look_at_x
        , look_at_y
        , look_at_z
        , up_x
        , up_y
        , up_z
        } ;
    alListenerfv ( AL_ORIENTATION , al_orientation ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_sample_value ( mono_sound_sample & sample , num_fract value )
{
    sample . _value = ( ALubyte ) ( ( platform_math_insider :: num_fract_value_get ( value ) * 127.0f ) + 127.0f ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: create_stereo_resource_id 
    ( stereo_sound_resource_id & result 
    , num_whole resource_index
    )
{
    int resource_index_int = 0 ;
    platform_math_insider :: num_whole_value_get ( resource_index_int , resource_index ) ;
    result . _resource_id = resource_index_int ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: load_stereo_sample_data
    ( const samples_array & samples 
    , const stereo_sound_resource_id & resource_id 
    )
{
    const stereo_sound_sample * samples_ptr = 0 ;
    int samples_count = 0 ;
    platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    platform_static_array_insider :: template elements_count < samples_array > ( samples_count ) ;
    [ _sound_loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) samples_ptr
        with_max_samples_count_of : samples_count
    ] ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: loader_ready ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , [ _sound_loader loader_ready ] ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: loaded_samples_count ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , [ _sound_loader loaded_samples_count ] ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: create_mono_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    union al_buffer_data_static_proc_type
    {
        void * void_ptr ;
        alBufferDataStaticProcPtr func_ptr ;
    } ;
    al_buffer_data_static_proc_type al_buffer_data_static_proc ;
    al_buffer_data_static_proc . void_ptr = alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    
    const mono_sound_sample * samples_ptr = 0 ;
    platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    
    int samples_count_int = 0 ;
    platform_math_insider :: num_whole_value_get ( samples_count_int , samples_count ) ;
    
    al_buffer_data_static_proc . func_ptr
        ( result . _buffer_id 
        , AL_FORMAT_MONO8 
        , ( ALvoid * ) samples_ptr
        , samples_count_int * sizeof ( mono_sound_sample )
        , mono_sound_samples_per_second
        ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_macosx_platform_sound < platform_insider > :: create_stereo_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
    union al_buffer_data_static_proc_type
    {
        void * void_ptr ;
        alBufferDataStaticProcPtr func_ptr ;
    } ;
    al_buffer_data_static_proc_type al_buffer_data_static_proc ;
    al_buffer_data_static_proc . void_ptr = alcGetProcAddress ( nil , ( const ALCchar * ) "alBufferDataStatic" ) ;
    
    alGenBuffers ( 1 , & result . _buffer_id ) ;
    
    const stereo_sound_sample * samples_ptr = 0 ;
    platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    
    int samples_count_int = 0 ;
    platform_math_insider :: num_whole_value_get ( samples_count_int , samples_count ) ;
    
    al_buffer_data_static_proc . func_ptr
        ( result . _buffer_id 
        , AL_FORMAT_STEREO16 
        , ( ALvoid * ) samples_ptr
        , samples_count_int * sizeof ( stereo_sound_sample )
        , stereo_sound_samples_per_second
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: create_source ( sound_source_id & result )
{
    alGenSources ( 1 , & result . _source_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_pitch ( const sound_source_id & source_id , num_fract pitch )
{
    alSourcef ( source_id . _source_id , AL_PITCH , platform_math_insider :: num_fract_value_get ( pitch ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_gain ( const sound_source_id & source_id , num_fract gain )
{
    alSourcef ( source_id . _source_id , AL_GAIN , platform_math_insider :: num_fract_value_get ( gain ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_position ( const sound_source_id & source_id , vector_data position )
{
    float x ;
    float y ;
    float z ;
    platform_vector_insider :: x_get ( x , position ) ;
    platform_vector_insider :: y_get ( y , position ) ;
    platform_vector_insider :: z_get ( z , position ) ;
    ALfloat al_position [ ] = { x , y , z } ;
    alSourcefv ( source_id . _source_id , AL_POSITION , al_position ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_velocity ( const sound_source_id & source_id , vector_data velocity )
{
    float x ;
    float y ;
    float z ;
    platform_vector_insider :: x_get ( x , velocity ) ;
    platform_vector_insider :: y_get ( y , velocity ) ;
    platform_vector_insider :: z_get ( z , velocity ) ;
    ALfloat al_velocity [ ] = { x , y , z } ;
    alSourcefv ( source_id . _source_id , AL_VELOCITY , al_velocity ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id )
{
    alSourcei ( source_id . _source_id , AL_BUFFER , buffer_id . _buffer_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_playback_looping ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_TRUE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: set_source_playback_once ( const sound_source_id & source_id )
{
    alSourcei ( source_id . _source_id , AL_LOOPING , AL_FALSE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: source_play ( const sound_source_id & source_id )
{
    alSourcePlay ( source_id . _source_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_sound < platform_insider > :: source_stop ( const sound_source_id & source_id )
{
    alSourceStop ( source_id . _source_id ) ;
}
