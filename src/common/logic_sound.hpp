template < typename mediator >
class shy_logic_sound
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: float_32 float_32 ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: mono_sound_sample mono_sound_sample ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
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
    void _int_to_sample ( num_fract & result , int_32 i ) ;
    void _create_stereo_sound ( ) ;
    void _create_mono_sound ( ) ;
private :
    mediator * _mediator ;
    int_32 _mono_sound_created ;
    int_32 _stereo_sound_created ;
    int_32 _stereo_sound_loaded ;
    int_32 _sound_prepare_permitted ;
    num_whole _loaded_stereo_sound_samples ;
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
{
}

template < typename mediator >
void shy_logic_sound < mediator > :: init ( )
{
    vector_data listener_pos ;
    platform :: vector_xyz ( listener_pos , 0 , 0 , 4 ) ;
    platform :: sound_set_listener_position ( listener_pos ) ;
    
    vector_data listener_vel ;
    platform :: vector_xyz ( listener_vel , 0 , 0 , 0 ) ;
    platform :: sound_set_listener_velocity ( listener_vel ) ;
    
    vector_data look_at ;
    vector_data up ;
    platform :: vector_xyz ( look_at , 0 , 0 , 1 ) ;
    platform :: vector_xyz ( up , 0 , 1 , 0 ) ;
    platform :: sound_set_listener_orientation ( look_at , up ) ;
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
            num_whole ready ;
            platform :: sound_loader_ready ( ready ) ;
            if ( platform :: condition_true ( ready ) )
            {
                _load_sound ( ) ;
                _stereo_sound_loaded = true ;
            }
        }
        else
        {
            num_whole ready ;
            platform :: sound_loader_ready ( ready ) ;
            if ( platform :: condition_true ( ready ) )
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
        int_32 touch ;
        int_32 mouse_button ;
        platform :: touch_occured ( touch ) ;
        platform :: mouse_left_button_down ( mouse_button ) ;
        if ( touch || mouse_button )
        {
            platform :: sound_source_stop ( _mono_sound_source ) ;
            platform :: sound_source_play ( _mono_sound_source ) ;
        }
    }
}

template < typename mediator >
void shy_logic_sound < mediator > :: _load_sound ( )
{
    num_whole music_tail_cut ;
    num_whole max_music_samples ;
    num_whole music_resource_index ;
    num_whole music_samples_loaded ;
    stereo_sound_resource_id music_resource_id ;
    platform :: math_make_num_whole ( music_tail_cut , 2293 ) ;
    platform :: math_make_num_whole ( max_music_samples , _max_stereo_sound_samples ) ;
    platform :: math_make_num_whole ( music_resource_index , _music_rough_and_heavy_resource_index ) ;
    platform :: sound_create_stereo_resource_id ( music_resource_id , music_resource_index ) ;
    platform :: sound_load_stereo_sample_data ( _stereo_sound_data , max_music_samples , music_samples_loaded , music_resource_id ) ;
    platform :: math_sub_wholes ( _loaded_stereo_sound_samples , music_samples_loaded , music_tail_cut ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _int_to_sample ( num_fract & result , int_32 i )
{
    platform :: math_make_num_fract ( result , ( i % 256 ) - 128 , 128 ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_stereo_sound ( )
{
    num_fract gain ;
    num_fract pitch ;
    sound_buffer_id stereo_sound_buffer ;
    platform :: math_make_num_fract ( gain , 7 , 10 ) ;
    platform :: math_make_num_fract ( pitch , 1 , 1 ) ;
    platform :: sound_create_stereo_buffer 
        ( stereo_sound_buffer
        , _stereo_sound_data 
        , _loaded_stereo_sound_samples
        ) ;
    platform :: sound_create_source ( _stereo_sound_source ) ;
    platform :: sound_set_source_gain ( _stereo_sound_source , gain ) ;
    platform :: sound_set_source_pitch ( _stereo_sound_source , pitch ) ;
    platform :: sound_set_source_buffer ( _stereo_sound_source , stereo_sound_buffer ) ;
    platform :: sound_set_source_playback_looping ( _stereo_sound_source ) ;
    platform :: sound_source_play ( _stereo_sound_source ) ;
    
    vector_data source_pos ;
    platform :: vector_xyz ( source_pos , 0 , 0 , - 2 ) ;
    platform :: sound_set_source_position ( _stereo_sound_source , source_pos ) ;
    
    vector_data source_vel ;
    platform :: vector_xyz ( source_vel , 0 , 0 , 0 ) ;
    platform :: sound_set_source_velocity ( _stereo_sound_source , source_vel ) ;    
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_mono_sound ( )
{
    int_32 next_sample = 0 ;
    for ( int_32 i = 0 ; i < _max_mono_sound_samples ; ++ i )
    {
        float_32 pi ;
        _mediator -> math_pi ( pi ) ;
        float_32 angle = float_32 ( i ) * 2.0f * pi / float_32 ( platform :: mono_sound_samples_per_second ) ;
        float_32 angle_sin ;
        platform :: math_sin ( angle_sin , angle ) ;
        next_sample += int_32 ( 128.0f * ( 1.0f + angle_sin ) ) ;
        num_fract sample ;
        _int_to_sample ( sample , next_sample ) ;
        platform :: sound_set_sample_value ( _mono_sound_data [ i ] , sample ) ;
    }
    num_fract gain ;
    num_fract pitch ;
    num_whole max_sound_samples ;
    sound_buffer_id mono_sound_buffer ;
    platform :: math_make_num_fract ( gain , 1 , 1 ) ;
    platform :: math_make_num_fract ( pitch , 1 , 1 ) ;
    platform :: math_make_num_whole ( max_sound_samples , _max_mono_sound_samples ) ;
    platform :: sound_create_mono_buffer ( mono_sound_buffer , _mono_sound_data , max_sound_samples ) ;
    platform :: sound_create_source ( _mono_sound_source ) ;
    platform :: sound_set_source_gain ( _mono_sound_source , gain ) ;
    platform :: sound_set_source_pitch ( _mono_sound_source , pitch ) ;
    platform :: sound_set_source_buffer ( _mono_sound_source , mono_sound_buffer ) ;
    platform :: sound_set_source_playback_once ( _mono_sound_source ) ;

    vector_data source_pos ;
    platform :: vector_xyz ( source_pos , 0 , 0 , - 2 ) ;
    platform :: sound_set_source_position ( _mono_sound_source , source_pos ) ;
    
    vector_data source_vel ;
    platform :: vector_xyz ( source_vel , 0 , 0 , 0 ) ;
    platform :: sound_set_source_velocity ( _mono_sound_source , source_vel ) ;    
}
