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
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
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
    
    class _logic_sound_consts_type
    {
    public :
        _logic_sound_consts_type ( ) ;
        num_fract gain ;
        num_fract magnitude ;
        num_whole music_rough_and_heavy_resource_index ;
        num_whole modulator ;
        num_whole half_modulator ;
        num_whole music_tail_cut ;
        static const_int_32 max_stereo_sound_samples = platform_sound :: stereo_sound_samples_per_second * 60 ;
        static const_int_32 max_mono_sound_samples = platform_sound :: mono_sound_samples_per_second / 2 ;
    } ;
    
public :
    shy_logic_sound ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: sound_prepare_permit ) ;
    void receive ( typename messages :: sound_update ) ;
private :
    shy_logic_sound < mediator > & operator= ( const shy_logic_sound < mediator > & ) ;
    void _load_sound ( ) ;
    void _int_to_sample ( num_fract & result , num_whole i ) ;
    void _create_stereo_sound ( ) ;
    void _create_mono_sound ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < platform_mouse > _platform_mouse ;
    typename platform_pointer :: template pointer < platform_sound > _platform_sound ;
    typename platform_pointer :: template pointer < platform_touch > _platform_touch ;
    const _logic_sound_consts_type _logic_sound_consts ;
    num_whole _mono_sound_created ;
    num_whole _stereo_sound_created ;
    num_whole _stereo_sound_loaded ;
    num_whole _sound_prepare_permitted ;
    sound_source_id _stereo_sound_source ;
    sound_source_id _mono_sound_source ;
    typename platform_static_array :: template static_array 
        < stereo_sound_sample 
        , _logic_sound_consts_type :: max_stereo_sound_samples 
        > _stereo_sound_data ;
    typename platform_static_array :: template static_array 
        < mono_sound_sample 
        , _logic_sound_consts_type :: max_mono_sound_samples 
        > _mono_sound_data ;
} ;

template < typename mediator >
shy_logic_sound < mediator > :: shy_logic_sound ( )
{
}

template < typename mediator >
shy_logic_sound < mediator > & shy_logic_sound < mediator > :: operator= ( const shy_logic_sound < mediator > & )
{
    return * this ;
}

template < typename mediator >
shy_logic_sound < mediator > :: _logic_sound_consts_type :: _logic_sound_consts_type ( )
{
    platform_math :: make_num_fract ( gain , 7 , 10 ) ;
    platform_math :: make_num_fract ( magnitude , 128 , 1 ) ;
    platform_math :: make_num_whole ( music_rough_and_heavy_resource_index , 1 ) ;
    platform_math :: make_num_whole ( modulator , 256 ) ;
    platform_math :: make_num_whole ( half_modulator , 128 ) ;
    platform_math :: make_num_whole ( music_tail_cut , 2293 ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _platform_mouse = platform_obj . get ( ) . mouse ;
    _platform_sound = platform_obj . get ( ) . sound ;
    _platform_touch = platform_obj . get ( ) . touch ;
    
    _mono_sound_created = _platform_math_consts . get ( ) . whole_false ;
    _stereo_sound_created = _platform_math_consts . get ( ) . whole_false ;
    _stereo_sound_loaded = _platform_math_consts . get ( ) . whole_false ;
    _sound_prepare_permitted = _platform_math_consts . get ( ) . whole_false ;
    
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
    
    pos_x = _platform_math_consts . get ( ) . fract_0 ;
    pos_y = _platform_math_consts . get ( ) . fract_0 ;
    pos_z = _platform_math_consts . get ( ) . fract_4 ;
    
    vel_x = _platform_math_consts . get ( ) . fract_0 ;
    vel_y = _platform_math_consts . get ( ) . fract_0 ;
    vel_z = _platform_math_consts . get ( ) . fract_0 ;
    
    look_at_x = _platform_math_consts . get ( ) . fract_0 ;
    look_at_y = _platform_math_consts . get ( ) . fract_0 ;
    look_at_z = _platform_math_consts . get ( ) . fract_1 ;
    
    up_x = _platform_math_consts . get ( ) . fract_0 ;
    up_y = _platform_math_consts . get ( ) . fract_1 ;
    up_z = _platform_math_consts . get ( ) . fract_0 ;
    
    platform_vector :: xyz ( listener_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( listener_vel , vel_x , vel_y , vel_z ) ;
    platform_vector :: xyz ( look_at , look_at_x , look_at_y , look_at_z ) ;
    platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    
    _platform_sound . get ( ) . set_listener_position ( listener_pos ) ;
    _platform_sound . get ( ) . set_listener_velocity ( listener_vel ) ;
    _platform_sound . get ( ) . set_listener_orientation ( look_at , up ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: sound_prepare_permit )
{
    _sound_prepare_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: receive ( typename messages :: sound_update )
{
    if ( platform_conditions :: whole_is_true ( _sound_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _stereo_sound_loaded ) )
        {
            num_whole ready ;
            _platform_sound . get ( ) . loader_ready ( ready ) ;
            if ( platform_conditions :: whole_is_true ( ready ) )
            {
                _load_sound ( ) ;
                _stereo_sound_loaded = _platform_math_consts . get ( ) . whole_true ;
            }
        }
        else
        {
            num_whole ready ;
            _platform_sound . get ( ) . loader_ready ( ready ) ;
            if ( platform_conditions :: whole_is_true ( ready ) )
            {
                if ( platform_conditions :: whole_is_false ( _stereo_sound_created ) )
                {
                    _create_stereo_sound ( ) ;
                    _stereo_sound_created = _platform_math_consts . get ( ) . whole_true ;
                    _mediator . get ( ) . send ( typename messages :: sound_prepared ( ) ) ;
                }
            }
        }
        if ( platform_conditions :: whole_is_false ( _mono_sound_created ) )
        {
            _create_mono_sound ( ) ;
            _mono_sound_created = _platform_math_consts . get ( ) . whole_true ;
        }
    }
    if ( platform_conditions :: whole_is_true ( _mono_sound_created ) )
    {
        num_whole touch ;
        num_whole mouse_button ;
        _platform_touch . get ( ) . occured ( touch ) ;
        _platform_mouse . get ( ) . left_button_down ( mouse_button ) ;
        if ( platform_conditions :: whole_is_true ( touch ) || platform_conditions :: whole_is_true ( mouse_button ) )
        {
            _platform_sound . get ( ) . source_stop ( _mono_sound_source ) ;
            _platform_sound . get ( ) . source_play ( _mono_sound_source ) ;
        }
    }
}

template < typename mediator >
void shy_logic_sound < mediator > :: _load_sound ( )
{
    stereo_sound_resource_id music_resource_id ;
    platform_sound :: create_stereo_resource_id ( music_resource_id , _logic_sound_consts . music_rough_and_heavy_resource_index ) ;
    _platform_sound . get ( ) . load_stereo_sample_data ( _stereo_sound_data , music_resource_id ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _int_to_sample ( num_fract & result , num_whole i )
{
    num_whole whole_sample ;
    num_fract fract_half_modulator ;
    platform_math :: make_fract_from_whole ( fract_half_modulator , _logic_sound_consts . half_modulator ) ;
    platform_math :: mod_wholes ( whole_sample , i , _logic_sound_consts . modulator ) ;
    platform_math :: sub_from_whole ( whole_sample , _logic_sound_consts . half_modulator ) ;
    platform_math :: make_fract_from_whole ( result , whole_sample ) ;
    platform_math :: div_fract_by ( result , fract_half_modulator ) ;
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_stereo_sound ( )
{
    num_fract pitch ;
    num_fract pos_x ;
    num_fract pos_y ;
    num_fract pos_z ;
    num_fract vel_x ;
    num_fract vel_y ;
    num_fract vel_z ;
    num_whole loaded_samples_count ;
    vector_data source_pos ;
    vector_data source_vel ;
    sound_buffer_id stereo_sound_buffer ;
        
    pitch = _platform_math_consts . get ( ) . fract_1 ;
    pos_x = _platform_math_consts . get ( ) . fract_0 ;
    pos_y = _platform_math_consts . get ( ) . fract_0 ;
    pos_z = _platform_math_consts . get ( ) . fract_minus_2 ;
    vel_x = _platform_math_consts . get ( ) . fract_0 ;
    vel_y = _platform_math_consts . get ( ) . fract_0 ;
    vel_z = _platform_math_consts . get ( ) . fract_0 ;
    platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( source_vel , vel_x , vel_y , vel_z ) ;
    
    _platform_sound . get ( ) . loaded_samples_count ( loaded_samples_count ) ;
    platform_math :: sub_from_whole ( loaded_samples_count , _logic_sound_consts . music_tail_cut ) ;
    
    num_whole max_music_samples ;
    platform_math :: make_num_whole ( max_music_samples , _logic_sound_consts_type :: max_stereo_sound_samples ) ;
    _platform_sound . get ( ) . create_stereo_buffer 
        ( stereo_sound_buffer
        , _stereo_sound_data 
        , loaded_samples_count
        ) ;
    _platform_sound . get ( ) . create_source ( _stereo_sound_source ) ;
    _platform_sound . get ( ) . set_source_gain ( _stereo_sound_source , _logic_sound_consts . gain ) ;
    _platform_sound . get ( ) . set_source_pitch ( _stereo_sound_source , pitch ) ;
    _platform_sound . get ( ) . set_source_buffer ( _stereo_sound_source , stereo_sound_buffer ) ;
    _platform_sound . get ( ) . set_source_playback_looping ( _stereo_sound_source ) ;
    _platform_sound . get ( ) . set_source_position ( _stereo_sound_source , source_pos ) ;
    _platform_sound . get ( ) . set_source_velocity ( _stereo_sound_source , source_vel ) ;    
    _platform_sound . get ( ) . source_play ( _stereo_sound_source ) ;    
}

template < typename mediator >
void shy_logic_sound < mediator > :: _create_mono_sound ( )
{
    num_whole next_sample ;
    num_whole whole_max_mono_sound_samples ;
    num_fract fract_mono_sound_samples_per_second ;
    platform_math :: make_num_whole ( whole_max_mono_sound_samples , _logic_sound_consts_type :: max_mono_sound_samples ) ;
    platform_math :: make_num_fract ( fract_mono_sound_samples_per_second , platform_sound :: mono_sound_samples_per_second , 1 ) ;
    next_sample = _platform_math_consts . get ( ) . whole_0 ;
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0 
        ; platform_conditions :: whole_less_than_whole ( i , whole_max_mono_sound_samples ) 
        ; platform_math :: inc_whole ( i )
        )
    {
        num_fract fract_i ;
        num_fract angle ;
        num_fract angle_sin ;
        num_fract fract_sample_delta ;
        num_fract sample ;
        num_whole whole_sample_delta ;
        platform_math :: make_fract_from_whole ( fract_i , i ) ;
        platform_math :: mul_fracts ( angle , fract_i , _platform_math_consts . get ( ) . fract_2pi ) ;
        platform_math :: div_fract_by ( angle , fract_mono_sound_samples_per_second ) ;        
        platform_math :: sin ( angle_sin , angle ) ;
        platform_math :: add_fracts ( fract_sample_delta , _platform_math_consts . get ( ) . fract_1 , angle_sin ) ;
        platform_math :: mul_fract_by ( fract_sample_delta , _logic_sound_consts . magnitude ) ;
        platform_math :: make_whole_from_fract ( whole_sample_delta , fract_sample_delta ) ;
        platform_math :: add_to_whole ( next_sample , whole_sample_delta ) ;
        _int_to_sample ( sample , next_sample ) ;
        typename platform_pointer :: template pointer < mono_sound_sample > sample_ptr ;
        platform_static_array :: element_ptr ( sample_ptr , _mono_sound_data , i ) ;
        platform_sound :: set_sample_value ( sample_ptr . get ( ) , sample ) ;
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
    
    gain = _platform_math_consts . get ( ) . fract_1 ;
    pitch = _platform_math_consts . get ( ) . fract_1 ;
    pos_x = _platform_math_consts . get ( ) . fract_0 ;
    pos_y = _platform_math_consts . get ( ) . fract_0 ;
    pos_z = _platform_math_consts . get ( ) . fract_minus_2 ;
    vel_x = _platform_math_consts . get ( ) . fract_0 ;
    vel_y = _platform_math_consts . get ( ) . fract_0 ;
    vel_z = _platform_math_consts . get ( ) . fract_0 ;
    platform_math :: make_num_whole ( max_sound_samples , _logic_sound_consts_type :: max_mono_sound_samples ) ;
    platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    platform_vector :: xyz ( source_vel , pos_x , pos_y , pos_z ) ;
    
    _platform_sound . get ( ) . create_mono_buffer ( mono_sound_buffer , _mono_sound_data , max_sound_samples ) ;
    _platform_sound . get ( ) . create_source ( _mono_sound_source ) ;
    _platform_sound . get ( ) . set_source_gain ( _mono_sound_source , gain ) ;
    _platform_sound . get ( ) . set_source_pitch ( _mono_sound_source , pitch ) ;
    _platform_sound . get ( ) . set_source_buffer ( _mono_sound_source , mono_sound_buffer ) ;
    _platform_sound . get ( ) . set_source_playback_once ( _mono_sound_source ) ;
    _platform_sound . get ( ) . set_source_position ( _mono_sound_source , source_pos ) ;
    _platform_sound . get ( ) . set_source_velocity ( _mono_sound_source , source_vel ) ;    
}
