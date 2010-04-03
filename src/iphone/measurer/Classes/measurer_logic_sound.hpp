template < typename mediator >
class shy_measurer_logic_sound
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: mono_sound_sample mono_sound_sample ;
    typedef typename mediator :: platform :: sound_buffer_id sound_buffer_id ;
    typedef typename mediator :: platform :: sound_source_id sound_source_id ;
    typedef typename mediator :: platform :: stereo_sound_resource_id stereo_sound_resource_id ;
    typedef typename mediator :: platform :: stereo_sound_sample stereo_sound_sample ;
    typedef typename mediator :: platform :: vector_data vector_data ;
    
    static const int_32 music_rough_and_heavy_resource_index = 1 ;
    
public :
    shy_measurer_logic_sound ( mediator * arg_mediator )
    : _mediator ( arg_mediator )
    , _sound_created ( false )
    {
    }
    void update ( )
    {
        if ( ! _sound_created )
        {
            _create_sound ( ) ;
            _sound_created = true ;
        }
    }
private :
    float_32 _int_to_sample ( int_32 i )
    {
        return float_32 ( ( i % 256 ) - 128 ) / 128.0f ;
    }
    void _create_sound ( )
    {
        platform :: sound_set_listener_position ( platform :: vector_xyz ( 0 , 0 , 4 ) ) ;
        platform :: sound_set_listener_velocity ( platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
        platform :: sound_set_listener_orientation
            ( platform :: vector_xyz ( 0 , 0 , 1 )
            , platform :: vector_xyz ( 0 , 1 , 0 )
            ) ;
            
        static mono_sound_sample mono_sound_data [ platform :: mono_sound_samples_per_second ] ;
        int_32 next_sample = 0 ;
        for ( int_32 i = 0 ; i < platform :: mono_sound_samples_per_second ; ++ i )
        {
            next_sample += int_32 ( 128.0f * ( 1.0f + platform :: math_sin ( float_32 ( i ) * 2.0f * PI / float_32 ( platform :: mono_sound_samples_per_second ) ) ) ) ;
            platform :: sound_set_sample_value ( mono_sound_data [ i ] , _int_to_sample ( next_sample ) ) ;
        }
        
        const int_32 max_stereo_sound_samples = platform :: stereo_sound_samples_per_second * 60 ;
        static stereo_sound_sample stereo_sound_data [ max_stereo_sound_samples ] ;
        int_32 loaded_stereo_sound_samples = 0 ;
        stereo_sound_resource_id music_resource_id = platform :: sound_create_stereo_resource_id 
            ( music_rough_and_heavy_resource_index 
            ) ;
        platform :: sound_load_stereo_sample_data
            ( stereo_sound_data
            , max_stereo_sound_samples
            , loaded_stereo_sound_samples
            , music_resource_id
            ) ;
        
        sound_buffer_id stereo_sound_buffer = platform :: sound_create_stereo_buffer 
            ( stereo_sound_data 
            , loaded_stereo_sound_samples - 2293 
            ) ;
        sound_buffer_id mono_sound_buffer = platform :: sound_create_mono_buffer 
            ( mono_sound_data 
            , platform :: mono_sound_samples_per_second 
            ) ;
        _sound_source = platform :: sound_create_source ( ) ;
        platform :: sound_set_source_pitch ( _sound_source , 1 ) ;
        platform :: sound_set_source_gain ( _sound_source , 1 ) ;
        platform :: sound_set_source_position ( _sound_source , platform :: vector_xyz ( 0 , 0 , - 2 ) ) ;
        platform :: sound_set_source_velocity ( _sound_source , platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
        platform :: sound_set_source_buffer ( _sound_source , stereo_sound_buffer ) ;
        platform :: sound_set_source_playback_looping ( _sound_source ) ;
        platform :: sound_source_play ( _sound_source ) ;
    }
private :
    sound_source_id _sound_source ;
    int_32 _sound_created ;
    mediator * _mediator ;
} ;
