template < typename mediator >
class shy_logic_sound
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_mouse platform_mouse ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_sound platform_sound ;
    typedef typename mediator :: platform :: platform_sound :: mono_sound_sample mono_sound_sample ;
    typedef typename mediator :: platform :: platform_sound :: sound_buffer_id sound_buffer_id ;
    typedef typename mediator :: platform :: platform_sound :: sound_source_id sound_source_id ;
    typedef typename mediator :: platform :: platform_sound :: stereo_sound_resource_id stereo_sound_resource_id ;
    typedef typename mediator :: platform :: platform_sound :: stereo_sound_sample stereo_sound_sample ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: platform :: platform_touch platform_touch ;
    typedef typename mediator :: platform :: platform_vector platform_vector ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
    
    static const_int_32 _music_rough_and_heavy_resource_index = 1 ;
    static const_int_32 _max_stereo_sound_samples = platform_sound :: stereo_sound_samples_per_second * 60 ;
    static const_int_32 _max_mono_sound_samples = platform_sound :: mono_sound_samples_per_second / 2 ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: sound_prepare_permit msg ) ;
    void receive ( typename messages :: sound_update msg ) ;
private :
    void _load_sound ( ) ;
    void _int_to_sample ( num_fract & result , num_whole i ) ;
    void _create_stereo_sound ( ) ;
    void _create_mono_sound ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_whole _mono_sound_created ;
    num_whole _stereo_sound_created ;
    num_whole _stereo_sound_loaded ;
    num_whole _sound_prepare_permitted ;
    sound_source_id _stereo_sound_source ;
    sound_source_id _mono_sound_source ;
    typename platform_static_array :: template static_array < stereo_sound_sample , _max_stereo_sound_samples > _stereo_sound_data ;
    typename platform_static_array :: template static_array < mono_sound_sample , _max_mono_sound_samples > _mono_sound_data ;
} ;

template < typename mediator >
void shy_logic_sound < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: init msg )
{
    platform_math :: make_num_whole ( _mono_sound_created , false ) ;
    platform_math :: make_num_whole ( _stereo_sound_created , false ) ;
    platform_math :: make_num_whole ( _stereo_sound_loaded , false ) ;
    platform_math :: make_num_whole ( _sound_prepare_permitted , false ) ;
    
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    
    num_fract vel_x ;
    num_fract vel_y ;
    num_fract vel_z ;
    
    num_fract look_at_x ;
    num_fract look_at_y ;
    num_fract look_at_z ;
    
    num_fract up_x ;
    num_fract up_y ;
    num_fract up_z ;
    
    vector_data listener_pos ;
    vector_data listener_vel ;
    vector_data look_at ;
    vector_data up ;
    
    platform_math :: make_num_fract ( pos_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_z , 4 , 1 ) ;
    
    platform_math :: make_num_fract ( vel_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_z , 0 , 1 ) ;
    
    platform_math :: make_num_fract ( look_at_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( look_at_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( look_at_z , 1 , 1 ) ;
    
    platform_math :: make_num_fract ( up_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( up_y , 1 , 1 ) ;
    platform_math :: make_num_fract ( up_z , 0 , 1 ) ;
    
    platform_vector :: xyz ( listener_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( listener_vel , vel_x , vel_y , vel_z ) ;
    platform_vector :: xyz ( look_at , look_at_x , look_at_y , look_at_z ) ;
    platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    
    platform_sound :: set_listener_position ( listener_pos ) ;
    platform_sound :: set_listener_velocity ( listener_vel ) ;
    platform_sound :: set_listener_orientation ( look_at , up ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: sound_prepare_permit msg )
{
    platform_math :: make_num_whole ( _sound_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: sound_update msg )
{
    if ( platform_conditions :: whole_is_true ( _sound_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _stereo_sound_loaded ) )
        {
            num_whole ready ;
            platform_sound :: loader_ready ( ready ) ;
            if ( platform_conditions :: whole_is_true ( ready ) )
            {
                _load_sound ( ) ;
                platform_math :: make_num_whole ( _stereo_sound_loaded , true ) ;
            }
        }
        else
        {
            num_whole ready ;
            platform_sound :: loader_ready ( ready ) ;
            if ( platform_conditions :: whole_is_true ( ready ) )
            {
                if ( platform_conditions :: whole_is_false ( _stereo_sound_created ) )
                {
                    _create_stereo_sound ( ) ;
                    platform_math :: make_num_whole ( _stereo_sound_created , true ) ;
                    _mediator . get ( ) . send ( typename messages :: sound_prepared ( ) ) ;
                }
            }
        }
        if ( platform_conditions :: whole_is_false ( _mono_sound_created ) )
        {
            _create_mono_sound ( ) ;
            platform_math :: make_num_whole ( _mono_sound_created , true ) ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _mono_sound_created ) )
    {
        num_whole touch ;
        num_whole mouse_button ;
        platform_touch :: occured ( touch ) ;
        platform_mouse :: left_button_down ( mouse_button ) ;
        if ( platform_conditions :: whole_is_true ( touch ) || platform_conditions :: whole_is_true ( mouse_button ) )
        {
            platform_sound :: source_stop ( _mono_sound_source ) ;
            platform_sound :: source_play ( _mono_sound_source ) ;
        }
    }
}

template < typename mediator >
void shy_logic_sound < mediator > :: _load_sound ( )
{
    num_whole music_resource_index ;
    stereo_sound_resource_id music_resource_id ;
    platform_math :: make_num_whole ( music_resource_index , _music_rough_and_heavy_resource_index ) ;
    platform_sound :: create_stereo_resource_id ( music_resource_id , music_resource_index ) ;
    platform_sound :: load_stereo_sample_data ( _stereo_sound_data , music_resource_id ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _int_to_sample ( num_fract & result , num_whole i )
{
    num_whole whole_sample ;
    num_whole modulator ;
    num_whole half_modulator ;
    num_fract fract_half_modulator ;
    platform_math :: make_num_whole ( modulator , 256 ) ;
    platform_math :: make_num_whole ( half_modulator , 128 ) ;
    platform_math :: make_num_fract ( fract_half_modulator , 128 , 1 ) ;
    platform_math :: mod_wholes ( whole_sample , i , modulator ) ;
    platform_math :: sub_from_whole ( whole_sample , half_modulator ) ;
    platform_math :: make_fract_from_whole ( result , whole_sample ) ;
    platform_math :: div_fract_by ( result , fract_half_modulator ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_stereo_sound ( )
{
    num_fract gain ;
    num_fract pitch ;
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    num_fract vel_x ;
    num_fract vel_y ;
    num_fract vel_z ;
    num_whole music_tail_cut ;
    num_whole loaded_samples_count ;
    vector_data source_pos ;
    vector_data source_vel ;
    sound_buffer_id stereo_sound_buffer ;
        
    platform_math :: make_num_whole ( music_tail_cut , 2293 ) ;
    platform_math :: make_num_fract ( gain , 7 , 10 ) ;
    platform_math :: make_num_fract ( pitch , 1 , 1 ) ;
    platform_math :: make_num_fract ( pos_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_z , - 2 , 1 ) ;
    platform_math :: make_num_fract ( vel_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_z , 0 , 1 ) ;
    platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( source_vel , vel_x , vel_y , vel_z ) ;
    
    platform_sound :: loaded_samples_count ( loaded_samples_count ) ;
    platform_math :: sub_from_whole ( loaded_samples_count , music_tail_cut ) ;
    
    num_whole max_music_samples ;
    platform_math :: make_num_whole ( max_music_samples , _max_stereo_sound_samples ) ;
    platform_sound :: create_stereo_buffer 
        ( stereo_sound_buffer
        , _stereo_sound_data 
        , loaded_samples_count
        ) ;
    platform_sound :: create_source ( _stereo_sound_source ) ;
    platform_sound :: set_source_gain ( _stereo_sound_source , gain ) ;
    platform_sound :: set_source_pitch ( _stereo_sound_source , pitch ) ;
    platform_sound :: set_source_buffer ( _stereo_sound_source , stereo_sound_buffer ) ;
    platform_sound :: set_source_playback_looping ( _stereo_sound_source ) ;
    platform_sound :: set_source_position ( _stereo_sound_source , source_pos ) ;
    platform_sound :: set_source_velocity ( _stereo_sound_source , source_vel ) ;    
    platform_sound :: source_play ( _stereo_sound_source ) ;    
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_mono_sound ( )
{
    num_whole next_sample ;
    num_whole whole_max_mono_sound_samples ;
    num_fract fract_mono_sound_samples_per_second ;
    platform_math :: make_num_whole ( whole_max_mono_sound_samples , _max_mono_sound_samples ) ;
    platform_math :: make_num_fract ( fract_mono_sound_samples_per_second , platform_sound :: mono_sound_samples_per_second , 1 ) ;
    platform_math :: make_num_whole ( next_sample , 0 ) ;
    for ( num_whole i = platform :: math_consts . whole_0 
        ; platform_conditions :: whole_less_than_whole ( i , whole_max_mono_sound_samples ) 
        ; platform_math :: inc_whole ( i )
        )
    {
        num_fract fract_i ;
        num_fract angle ;
        num_fract num_1 ;
        num_fract magnitude ;
        num_fract angle_sin ;
        num_fract fract_sample_delta ;
        num_fract sample ;
        num_whole whole_sample_delta ;
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( angle , fract_i , platform :: math_consts . fract_2pi ) ;
        platform_math :: div_fract_by ( angle , fract_mono_sound_samples_per_second ) ;        
        platform_math :: make_num_fract ( num_1 , 1 , 1 ) ;
        platform_math :: make_num_fract ( magnitude , 128 , 1 ) ;
        platform_math :: sin ( angle_sin , angle ) ;
        platform_math :: add_fracts ( fract_sample_delta , num_1 , angle_sin ) ;
        platform_math :: mul_fract_by ( fract_sample_delta , magnitude ) ;
        platform_math :: make_whole_from_fract ( whole_sample_delta , fract_sample_delta ) ;
        platform_math :: add_to_whole ( next_sample , whole_sample_delta ) ;
        _int_to_sample ( sample , next_sample ) ;
        mono_sound_sample & sample_ptr = platform_static_array :: element ( _mono_sound_data , i ) ;
        platform_sound :: set_sample_value ( sample_ptr , sample ) ;
    }
    
    num_fract gain ;
    num_fract pitch ;
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    num_fract vel_x ;
    num_fract vel_y ;
    num_fract vel_z ;
    vector_data source_pos ;
    vector_data source_vel ;
    num_whole max_sound_samples ;
    sound_buffer_id mono_sound_buffer ;
    
    platform_math :: make_num_fract ( gain , 1 , 1 ) ;
    platform_math :: make_num_fract ( pitch , 1 , 1 ) ;
    platform_math :: make_num_fract ( pos_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( pos_z , - 2 , 1 ) ;
    platform_math :: make_num_fract ( vel_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( vel_z , 0 , 1 ) ;
    platform_math :: make_num_whole ( max_sound_samples , _max_mono_sound_samples ) ;
    platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( source_vel , pos_x , pos_y , pos_z ) ;
    
    platform_sound :: create_mono_buffer ( mono_sound_buffer , _mono_sound_data , max_sound_samples ) ;
    platform_sound :: create_source ( _mono_sound_source ) ;
    platform_sound :: set_source_gain ( _mono_sound_source , gain ) ;
    platform_sound :: set_source_pitch ( _mono_sound_source , pitch ) ;
    platform_sound :: set_source_buffer ( _mono_sound_source , mono_sound_buffer ) ;
    platform_sound :: set_source_playback_once ( _mono_sound_source ) ;
    platform_sound :: set_source_position ( _mono_sound_source , source_pos ) ;
    platform_sound :: set_source_velocity ( _mono_sound_source , source_vel ) ;    
}
