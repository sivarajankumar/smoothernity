template < typename mediator >
class shy_logic_sound
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
    
    static const int_32 _music_rough_and_heavy_resource_index = 1 ;
    static const int_32 _max_stereo_sound_samples = platform :: stereo_sound_samples_per_second * 60 ;
    static const int_32 _max_mono_sound_samples = platform :: mono_sound_samples_per_second / 2 ;
    
public :
    shy_logic_sound ( mediator * arg_mediator ) ;
    void init ( ) ;
    void sound_prepare_permit ( ) ;
    void sound_update ( ) ;
private :
    void _load_sound ( ) ;
    float_32 _int_to_sample ( int_32 i ) ;
    void _create_stereo_sound ( ) ;
    void _create_mono_sound ( ) ;
private :
    mediator * _mediator ;
    int_32 _mono_sound_created ;
    int_32 _stereo_sound_created ;
    int_32 _stereo_sound_loaded ;
    int_32 _sound_prepare_permitted ;
    int_32 _loaded_stereo_sound_samples ;
    sound_source_id _stereo_sound_source ;
    sound_source_id _mono_sound_source ;
    stereo_sound_sample _stereo_sound_data [ _max_stereo_sound_samples ] ;
    mono_sound_sample _mono_sound_data [ _max_mono_sound_samples ] ;
} ;

template < typename mediator >
shy_logic_sound < mediator > :: shy_logic_sound ( mediator * arg_mediator )
: _mediator ( arg_mediator )
, _mono_sound_created ( false )
, _stereo_sound_created ( false )
, _stereo_sound_loaded ( false )
, _sound_prepare_permitted ( false )
, _loaded_stereo_sound_samples ( 0 )
{
}

template < typename mediator >
void shy_logic_sound < mediator > :: init ( )
{
    platform :: sound_set_listener_position ( platform :: vector_xyz ( 0 , 0 , 4 ) ) ;
    platform :: sound_set_listener_velocity ( platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
    platform :: sound_set_listener_orientation
        ( platform :: vector_xyz ( 0 , 0 , 1 )
        , platform :: vector_xyz ( 0 , 1 , 0 )
        ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: sound_prepare_permit ( )
{
    _sound_prepare_permitted = true ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: sound_update ( )
{
    if ( _sound_prepare_permitted )
    {
        if ( ! _stereo_sound_loaded )
        {
            if ( platform :: sound_loader_ready ( ) )
            {
                _load_sound ( ) ;
                _stereo_sound_loaded = true ;
            }
        }
        else
        {
            if ( platform :: sound_loader_ready ( ) )
            {
                if ( ! _stereo_sound_created )
                {
                    _create_stereo_sound ( ) ;
                    _stereo_sound_created = true ;
                    _mediator -> sound_prepared ( ) ;
                }
            }
        }
        if ( ! _mono_sound_created )
        {
            _create_mono_sound ( ) ;
            _mono_sound_created = true ;
        }
    }
    if ( _mono_sound_created )
    {
        if ( platform :: touch_occured ( ) || platform :: mouse_left_button_down ( ) )
        {
            platform :: sound_source_stop ( _mono_sound_source ) ;
            platform :: sound_source_play ( _mono_sound_source ) ;
        }
    }
}

template < typename mediator >
void shy_logic_sound < mediator > :: _load_sound ( )
{
    stereo_sound_resource_id music_resource_id = platform :: sound_create_stereo_resource_id 
        ( _music_rough_and_heavy_resource_index 
        ) ;
    platform :: sound_load_stereo_sample_data
        ( _stereo_sound_data
        , _max_stereo_sound_samples
        , _loaded_stereo_sound_samples
        , music_resource_id
        ) ;
}

template < typename mediator >
typename shy_logic_sound < mediator > :: float_32
shy_logic_sound < mediator > :: _int_to_sample ( int_32 i )
{
    return float_32 ( ( i % 256 ) - 128 ) / 128.0f ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_stereo_sound ( )
{            
    sound_buffer_id stereo_sound_buffer = platform :: sound_create_stereo_buffer 
        ( _stereo_sound_data 
        , _loaded_stereo_sound_samples - 2293 
        ) ;
    _stereo_sound_source = platform :: sound_create_source ( ) ;
    platform :: sound_set_source_pitch ( _stereo_sound_source , 1 ) ;
    platform :: sound_set_source_gain ( _stereo_sound_source , 0.7f ) ;
    platform :: sound_set_source_position ( _stereo_sound_source , platform :: vector_xyz ( 0 , 0 , - 2 ) ) ;
    platform :: sound_set_source_velocity ( _stereo_sound_source , platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
    platform :: sound_set_source_buffer ( _stereo_sound_source , stereo_sound_buffer ) ;
    platform :: sound_set_source_playback_looping ( _stereo_sound_source ) ;
    platform :: sound_source_play ( _stereo_sound_source ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_mono_sound ( )
{
    int_32 next_sample = 0 ;
    for ( int_32 i = 0 ; i < _max_mono_sound_samples ; ++ i )
    {
        next_sample += int_32 ( 128.0f * ( 1.0f + platform :: math_sin ( float_32 ( i ) * 2.0f * _mediator -> math_pi ( ) / float_32 ( platform :: mono_sound_samples_per_second ) ) ) ) ;
        platform :: sound_set_sample_value ( _mono_sound_data [ i ] , _int_to_sample ( next_sample ) ) ;
    }
    sound_buffer_id mono_sound_buffer = platform :: sound_create_mono_buffer 
        ( _mono_sound_data 
        , _max_mono_sound_samples
        ) ;
    _mono_sound_source = platform :: sound_create_source ( ) ;
    platform :: sound_set_source_pitch ( _mono_sound_source , 1 ) ;
    platform :: sound_set_source_gain ( _mono_sound_source , 1 ) ;
    platform :: sound_set_source_position ( _mono_sound_source , platform :: vector_xyz ( 0 , 0 , - 2 ) ) ;
    platform :: sound_set_source_velocity ( _mono_sound_source , platform :: vector_xyz ( 0 , 0 , 0 ) ) ;
    platform :: sound_set_source_buffer ( _mono_sound_source , mono_sound_buffer ) ;
    platform :: sound_set_source_playback_once ( _mono_sound_source ) ;
}
