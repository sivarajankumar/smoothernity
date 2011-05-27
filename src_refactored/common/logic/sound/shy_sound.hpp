namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract gain = so_called_platform_math :: init_num_fract ( 7 , 10 ) ;
        static const so_called_type_platform_math_num_fract magnitude = so_called_platform_math :: init_num_fract ( 128 , 1 ) ;
        static const so_called_type_platform_math_num_whole music_rough_and_heavy_resource_index = so_called_platform_math :: init_num_whole ( 1 ) ;
        static const so_called_type_platform_math_num_whole modulator = so_called_platform_math :: init_num_whole ( 256 ) ;
        static const so_called_type_platform_math_num_whole half_modulator = so_called_platform_math :: init_num_whole ( 128 ) ;
        static const so_called_type_platform_math_num_whole music_tail_cut = so_called_platform_math :: init_num_whole ( 2293 ) ;
        static so_called_type_platform_math_const_int_32 max_stereo_sound_samples = so_called_platform_sound :: stereo_sound_samples_per_second * 60 ;
        static so_called_type_platform_math_const_int_32 max_mono_sound_samples = so_called_platform_sound :: mono_sound_samples_per_second / 2 ;
    }

    static void load_sound ( ) ;
    static void int_to_sample ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_whole i ) ;
    static void create_stereo_sound ( ) ;
    static void create_mono_sound ( ) ;

    static so_called_type_platform_math_num_whole mono_sound_created ;
    static so_called_type_platform_math_num_whole stereo_sound_created ;
    static so_called_type_platform_math_num_whole stereo_sound_loaded ;
    static so_called_type_platform_math_num_whole sound_prepare_permitted ;
    static so_called_type_platform_sound_source_id stereo_sound_source ;
    static so_called_type_platform_sound_source_id mono_sound_source ;
    static so_called_type_platform_static_array_data 
        < so_called_type_platform_sound_sample_stereo
        , shy_guts :: consts :: max_stereo_sound_samples 
        > stereo_sound_data ;
    static so_called_type_platform_static_array_data 
        < so_called_type_platform_sound_sample_mono 
        , shy_guts :: consts :: max_mono_sound_samples 
        > mono_sound_data ;
}
   
typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_sound > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: load_sound ( )
{
    so_called_type_platform_sound_stereo_resource_id music_resource_id ;
    so_called_platform_sound_loader :: create_stereo_resource_id ( music_resource_id , shy_guts :: consts :: music_rough_and_heavy_resource_index ) ;
    so_called_platform_sound_loader :: load_stereo_sample_data ( shy_guts :: stereo_sound_data , music_resource_id ) ;
}

void shy_guts :: int_to_sample ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_whole i )
{
    so_called_type_platform_math_num_whole whole_sample ;
    so_called_type_platform_math_num_fract fract_half_modulator ;
    so_called_platform_math :: make_fract_from_whole ( fract_half_modulator , shy_guts :: consts :: half_modulator ) ;
    so_called_platform_math :: mod_wholes ( whole_sample , i , shy_guts :: consts :: modulator ) ;
    so_called_platform_math :: sub_from_whole ( whole_sample , shy_guts :: consts :: half_modulator ) ;
    so_called_platform_math :: make_fract_from_whole ( result , whole_sample ) ;
    so_called_platform_math :: div_fract_by ( result , fract_half_modulator ) ;
}

void shy_guts :: create_stereo_sound ( )
{
    so_called_type_platform_math_num_fract pitch ;
    so_called_type_platform_math_num_fract pos_x ;
    so_called_type_platform_math_num_fract pos_y ;
    so_called_type_platform_math_num_fract pos_z ;
    so_called_type_platform_math_num_fract vel_x ;
    so_called_type_platform_math_num_fract vel_y ;
    so_called_type_platform_math_num_fract vel_z ;
    so_called_type_platform_math_num_whole loaded_samples_count ;
    so_called_type_platform_vector_data source_pos ;
    so_called_type_platform_vector_data source_vel ;
    so_called_type_platform_sound_buffer_id stereo_sound_buffer ;
        
    pitch = so_called_platform_math_consts :: fract_1 ;
    pos_x = so_called_platform_math_consts :: fract_0 ;
    pos_y = so_called_platform_math_consts :: fract_0 ;
    pos_z = so_called_platform_math_consts :: fract_minus_2 ;
    vel_x = so_called_platform_math_consts :: fract_0 ;
    vel_y = so_called_platform_math_consts :: fract_0 ;
    vel_z = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    so_called_platform_vector :: xyz ( source_vel , vel_x , vel_y , vel_z ) ;
    
    so_called_platform_sound_loader :: loaded_samples_count ( loaded_samples_count ) ;
    so_called_platform_math :: sub_from_whole ( loaded_samples_count , shy_guts :: consts :: music_tail_cut ) ;
    
    so_called_type_platform_math_num_whole max_music_samples ;
    so_called_platform_math :: make_num_whole ( max_music_samples , shy_guts :: consts :: max_stereo_sound_samples ) ;
    so_called_platform_sound :: create_stereo_buffer 
        ( stereo_sound_buffer
        , shy_guts :: stereo_sound_data 
        , loaded_samples_count
        ) ;
    so_called_platform_sound :: create_source ( shy_guts :: stereo_sound_source ) ;
    so_called_platform_sound :: set_source_gain ( shy_guts :: stereo_sound_source , shy_guts :: consts :: gain ) ;
    so_called_platform_sound :: set_source_pitch ( shy_guts :: stereo_sound_source , pitch ) ;
    so_called_platform_sound :: set_source_buffer ( shy_guts :: stereo_sound_source , stereo_sound_buffer ) ;
    so_called_platform_sound :: set_source_playback_looping ( shy_guts :: stereo_sound_source ) ;
    so_called_platform_sound :: set_source_position ( shy_guts :: stereo_sound_source , source_pos ) ;
    so_called_platform_sound :: set_source_velocity ( shy_guts :: stereo_sound_source , source_vel ) ;    
    so_called_platform_sound :: source_play ( shy_guts :: stereo_sound_source ) ;    
}

void shy_guts :: create_mono_sound ( )
{
    so_called_type_platform_math_num_whole next_sample ;
    so_called_type_platform_math_num_whole whole_max_mono_sound_samples ;
    so_called_type_platform_math_num_fract fract_mono_sound_samples_per_second ;

    so_called_platform_math :: make_num_whole ( whole_max_mono_sound_samples , shy_guts :: consts :: max_mono_sound_samples ) ;
    so_called_platform_math :: make_num_fract ( fract_mono_sound_samples_per_second , so_called_platform_sound :: mono_sound_samples_per_second , 1 ) ;
    next_sample = so_called_platform_math_consts :: whole_0 ;

    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0 
        ; so_called_platform_conditions :: whole_less_than_whole ( i , whole_max_mono_sound_samples ) 
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_math_num_fract fract_i ;
        so_called_type_platform_math_num_fract angle ;
        so_called_type_platform_math_num_fract angle_sin ;
        so_called_type_platform_math_num_fract fract_sample_delta ;
        so_called_type_platform_math_num_fract sample ;
        so_called_type_platform_math_num_whole whole_sample_delta ;

        so_called_platform_math :: make_fract_from_whole ( fract_i , i ) ;
        so_called_platform_math :: mul_fracts ( angle , fract_i , so_called_platform_math_consts :: fract_2pi ) ;
        so_called_platform_math :: div_fract_by ( angle , fract_mono_sound_samples_per_second ) ;        
        so_called_platform_math :: sin ( angle_sin , angle ) ;
        so_called_platform_math :: add_fracts ( fract_sample_delta , so_called_platform_math_consts :: fract_1 , angle_sin ) ;
        so_called_platform_math :: mul_fract_by ( fract_sample_delta , shy_guts :: consts :: magnitude ) ;
        so_called_platform_math :: make_whole_from_fract ( whole_sample_delta , fract_sample_delta ) ;
        so_called_platform_math :: add_to_whole ( next_sample , whole_sample_delta ) ;
        shy_guts :: int_to_sample ( sample , next_sample ) ;

        so_called_type_platform_pointer_data < so_called_type_platform_sound_sample_mono > sample_ptr ;
        so_called_platform_static_array :: element_ptr ( sample_ptr , shy_guts :: mono_sound_data , i ) ;
        so_called_platform_sound :: set_sample_value ( sample_ptr . get ( ) , sample ) ;
    }
    
    so_called_type_platform_math_num_fract gain ;
    so_called_type_platform_math_num_fract pitch ;
    so_called_type_platform_math_num_fract pos_x ;
    so_called_type_platform_math_num_fract pos_y ;
    so_called_type_platform_math_num_fract pos_z ;
    so_called_type_platform_math_num_fract vel_x ;
    so_called_type_platform_math_num_fract vel_y ;
    so_called_type_platform_math_num_fract vel_z ;
    so_called_type_platform_vector_data source_pos ;
    so_called_type_platform_vector_data source_vel ;
    so_called_type_platform_math_num_whole max_sound_samples ;
    so_called_type_platform_sound_buffer_id mono_sound_buffer ;
    
    gain = so_called_platform_math_consts :: fract_1 ;
    pitch = so_called_platform_math_consts :: fract_1 ;
    pos_x = so_called_platform_math_consts :: fract_0 ;
    pos_y = so_called_platform_math_consts :: fract_0 ;
    pos_z = so_called_platform_math_consts :: fract_minus_2 ;
    vel_x = so_called_platform_math_consts :: fract_0 ;
    vel_y = so_called_platform_math_consts :: fract_0 ;
    vel_z = so_called_platform_math_consts :: fract_0 ;
    so_called_platform_math :: make_num_whole ( max_sound_samples , shy_guts :: consts :: max_mono_sound_samples ) ;
    so_called_platform_vector :: xyz ( source_pos , pos_x , pos_y , pos_z ) ;
    so_called_platform_vector :: xyz ( source_vel , pos_x , pos_y , pos_z ) ;
    
    so_called_platform_sound :: create_mono_buffer ( mono_sound_buffer , shy_guts :: mono_sound_data , max_sound_samples ) ;
    so_called_platform_sound :: create_source ( shy_guts :: mono_sound_source ) ;
    so_called_platform_sound :: set_source_gain ( shy_guts :: mono_sound_source , gain ) ;
    so_called_platform_sound :: set_source_pitch ( shy_guts :: mono_sound_source , pitch ) ;
    so_called_platform_sound :: set_source_buffer ( shy_guts :: mono_sound_source , mono_sound_buffer ) ;
    so_called_platform_sound :: set_source_playback_once ( shy_guts :: mono_sound_source ) ;
    so_called_platform_sound :: set_source_position ( shy_guts :: mono_sound_source , source_pos ) ;
    so_called_platform_sound :: set_source_velocity ( shy_guts :: mono_sound_source , source_vel ) ;    
}

void _shy_common_logic_sound :: receive ( so_called_message_common_init )
{
    shy_guts :: mono_sound_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: stereo_sound_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: stereo_sound_loaded = so_called_platform_math_consts :: whole_false ;
    shy_guts :: sound_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    
    so_called_type_platform_math_num_fract pos_x ;
    so_called_type_platform_math_num_fract pos_y ;
    so_called_type_platform_math_num_fract pos_z ;
    
    so_called_type_platform_math_num_fract vel_x ;
    so_called_type_platform_math_num_fract vel_y ;
    so_called_type_platform_math_num_fract vel_z ;
    
    so_called_type_platform_math_num_fract look_at_x ;
    so_called_type_platform_math_num_fract look_at_y ;
    so_called_type_platform_math_num_fract look_at_z ;
    
    so_called_type_platform_math_num_fract up_x ;
    so_called_type_platform_math_num_fract up_y ;
    so_called_type_platform_math_num_fract up_z ;
    
    so_called_type_platform_vector_data listener_pos ;
    so_called_type_platform_vector_data listener_vel ;
    so_called_type_platform_vector_data look_at ;
    so_called_type_platform_vector_data up ;
    
    pos_x = so_called_platform_math_consts :: fract_0 ;
    pos_y = so_called_platform_math_consts :: fract_0 ;
    pos_z = so_called_platform_math_consts :: fract_4 ;
    
    vel_x = so_called_platform_math_consts :: fract_0 ;
    vel_y = so_called_platform_math_consts :: fract_0 ;
    vel_z = so_called_platform_math_consts :: fract_0 ;
    
    look_at_x = so_called_platform_math_consts :: fract_0 ;
    look_at_y = so_called_platform_math_consts :: fract_0 ;
    look_at_z = so_called_platform_math_consts :: fract_1 ;
    
    up_x = so_called_platform_math_consts :: fract_0 ;
    up_y = so_called_platform_math_consts :: fract_1 ;
    up_z = so_called_platform_math_consts :: fract_0 ;
    
    so_called_platform_vector :: xyz ( listener_pos , pos_x , pos_y , pos_z ) ;
    so_called_platform_vector :: xyz ( listener_vel , vel_x , vel_y , vel_z ) ;
    so_called_platform_vector :: xyz ( look_at , look_at_x , look_at_y , look_at_z ) ;
    so_called_platform_vector :: xyz ( up , up_x , up_y , up_z ) ;
    
    so_called_platform_sound :: set_listener_position ( listener_pos ) ;
    so_called_platform_sound :: set_listener_velocity ( listener_vel ) ;
    so_called_platform_sound :: set_listener_orientation ( look_at , up ) ;
}

void _shy_common_logic_sound :: receive ( so_called_message_common_logic_sound_prepare_permit )
{
    shy_guts :: sound_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_sound :: receive ( so_called_message_common_logic_sound_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: sound_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: stereo_sound_loaded ) )
        {
            so_called_type_platform_math_num_whole ready ;
            so_called_platform_sound_loader :: loader_ready ( ready ) ;
            if ( so_called_platform_conditions :: whole_is_true ( ready ) )
            {
                shy_guts :: load_sound ( ) ;
                shy_guts :: stereo_sound_loaded = so_called_platform_math_consts :: whole_true ;
            }
        }
        else
        {
            so_called_type_platform_math_num_whole ready ;
            so_called_platform_sound_loader :: loader_ready ( ready ) ;
            if ( so_called_platform_conditions :: whole_is_true ( ready ) )
            {
                if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: stereo_sound_created ) )
                {
                    shy_guts :: create_stereo_sound ( ) ;
                    shy_guts :: stereo_sound_created = so_called_platform_math_consts :: whole_true ;
                    so_called_sender_common_logic_sound_prepared :: send ( so_called_message_common_logic_sound_prepared ( ) ) ;
                }
            }
        }
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: mono_sound_created ) )
        {
            shy_guts :: create_mono_sound ( ) ;
            shy_guts :: mono_sound_created = so_called_platform_math_consts :: whole_true ;
        }
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mono_sound_created ) )
    {
        so_called_type_platform_math_num_whole touch ;
        so_called_type_platform_math_num_whole mouse_button ;
        so_called_platform_touch :: occured ( touch ) ;
        so_called_platform_mouse :: left_button_down ( mouse_button ) ;
        if ( so_called_platform_conditions :: whole_is_true ( touch ) || so_called_platform_conditions :: whole_is_true ( mouse_button ) )
        {
            so_called_platform_sound :: source_stop ( shy_guts :: mono_sound_source ) ;
            so_called_platform_sound :: source_play ( shy_guts :: mono_sound_source ) ;
        }
    }
}

void _shy_common_logic_sound :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

