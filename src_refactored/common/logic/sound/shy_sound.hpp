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
    so_called_platform_sound :: create_stereo_resource_id ( music_resource_id , shy_guts :: consts :: music_rough_and_heavy_resource_index ) ;
    so_called_platform_sound :: load_stereo_sample_data ( shy_guts :: stereo_sound_data , music_resource_id ) ;
}

void shy_guts :: int_to_sample ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_whole i )
{
}

void shy_guts :: create_stereo_sound ( )
{
}

void shy_guts :: create_mono_sound ( )
{
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
            so_called_platform_sound :: loader_ready ( ready ) ;
            if ( so_called_platform_conditions :: whole_is_true ( ready ) )
            {
                shy_guts :: load_sound ( ) ;
                shy_guts :: stereo_sound_loaded = so_called_platform_math_consts :: whole_true ;
            }
        }
        else
        {
            so_called_type_platform_math_num_whole ready ;
            so_called_platform_sound :: loader_ready ( ready ) ;
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
