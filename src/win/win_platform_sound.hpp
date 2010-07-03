template < typename platform_insider >
class shy_win_platform_sound
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
        friend class shy_win_platform_sound ;
    public :
        mono_sound_sample ( ) ;
    private :
        int _dummy ;
    } ;
    
    class stereo_sound_sample
    {
        friend class shy_win_platform_sound ;
    public :
        stereo_sound_sample ( ) ;
    private :
        int _dummy ;
    } ;
    
    class sound_buffer_id
    {
        friend class shy_win_platform_sound ;
    public :
        sound_buffer_id ( ) ;
    private :
        int _dummy ;
    } ;
    
    class sound_source_id
    {
        friend class shy_win_platform_sound ;
    public :
        sound_source_id ( ) ;
    private :
        int _dummy ;
    } ;
    
    class stereo_sound_resource_id
    {
        friend class shy_win_platform_sound ;
    public :
        stereo_sound_resource_id ( ) ;
    private :
        int _resource_id ;
    } ;
    
public :
    static void set_listener_position ( vector_data position ) ;
    static void set_listener_velocity ( vector_data velocity ) ;
    static void set_listener_orientation ( vector_data look_at , vector_data up ) ;
    static void set_sample_value ( mono_sound_sample & sample , num_fract value ) ;
    static void create_stereo_resource_id ( stereo_sound_resource_id & result , num_whole resource_index ) ;
    static void loader_ready ( num_whole & result ) ;
    static void loaded_samples_count ( num_whole & result ) ;    
    static void create_source ( sound_source_id & result ) ;
    static void set_source_pitch ( const sound_source_id & source_id , num_fract pitch ) ;
    static void set_source_gain ( const sound_source_id & source_id , num_fract gain ) ;
    static void set_source_position ( const sound_source_id & source_id , vector_data position ) ;
    static void set_source_velocity ( const sound_source_id & source_id , vector_data velocity ) ;
    static void set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id ) ;
    static void set_source_playback_looping ( const sound_source_id & source_id ) ;
    static void set_source_playback_once ( const sound_source_id & source_id ) ;
    static void source_play ( const sound_source_id & source_id ) ;
    static void source_stop ( const sound_source_id & source_id ) ;
    
    template < typename samples_array >
    static void load_stereo_sample_data ( const samples_array & samples , const stereo_sound_resource_id & resource_id ) ;
    
    template < typename samples_array >
    static void create_mono_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;
    
    template < typename samples_array >
    static void create_stereo_buffer ( sound_buffer_id & result , const samples_array & samples , num_whole samples_count ) ;
} ;

template < typename platform_insider >
shy_win_platform_sound < platform_insider > :: mono_sound_sample :: mono_sound_sample ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_win_platform_sound < platform_insider > :: stereo_sound_sample :: stereo_sound_sample ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_win_platform_sound < platform_insider > :: sound_buffer_id :: sound_buffer_id ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_win_platform_sound < platform_insider > :: sound_source_id :: sound_source_id ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_win_platform_sound < platform_insider > :: stereo_sound_resource_id :: stereo_sound_resource_id ( )
: _resource_id ( platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_listener_position ( vector_data position )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_listener_velocity ( vector_data velocity )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_listener_orientation ( vector_data look_at , vector_data up )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_sample_value ( mono_sound_sample & sample , num_fract value )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: create_stereo_resource_id 
    ( stereo_sound_resource_id & result 
    , num_whole resource_index
    )
{
    result . _resource_id = platform_math_insider :: num_whole_unsafe_value_get ( resource_index ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_win_platform_sound < platform_insider > :: load_stereo_sample_data
    ( const samples_array & samples 
    , const stereo_sound_resource_id & resource_id 
    )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: loader_ready ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , true ) ;
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: loaded_samples_count ( num_whole & result )
{
    platform_math_insider :: num_whole_unsafe_value_set ( result , 0 ) ;
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_win_platform_sound < platform_insider > :: create_mono_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
}

template < typename platform_insider >
template < typename samples_array >
inline void shy_win_platform_sound < platform_insider > :: create_stereo_buffer 
    ( sound_buffer_id & result
    , const samples_array & samples 
    , num_whole samples_count 
    )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: create_source ( sound_source_id & result )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_pitch ( const sound_source_id & source_id , num_fract pitch )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_gain ( const sound_source_id & source_id , num_fract gain )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_position ( const sound_source_id & source_id , vector_data position )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_velocity ( const sound_source_id & source_id , vector_data velocity )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_buffer ( const sound_source_id & source_id , sound_buffer_id & buffer_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_playback_looping ( const sound_source_id & source_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: set_source_playback_once ( const sound_source_id & source_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: source_play ( const sound_source_id & source_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_sound < platform_insider > :: source_stop ( const sound_source_id & source_id )
{
}
