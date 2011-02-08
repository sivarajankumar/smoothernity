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
}

void _shy_common_logic_sound :: receive ( so_called_message_common_logic_sound_prepare_permit )
{
}

void _shy_common_logic_sound :: receive ( so_called_message_common_logic_sound_update )
{
}
