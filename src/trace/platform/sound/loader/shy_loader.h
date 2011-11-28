class shy_trace_platform_sound_loader
{
public :
    template < typename samples_array >
    static void check_args_load_stereo_sample_data ( so_called_platform_sound_loader_stereo_resource_id_type ) ;
    static void check_stereo_resource_id_uninitialized ( so_called_platform_sound_loader_stereo_resource_id_type ) ;
private :
    static void _check_args_load_stereo_sample_data ( so_called_lib_std_int32_t samples_count , so_called_platform_sound_loader_stereo_resource_id_type resource_id ) ;
} ;

template < typename samples_array >
void shy_trace_platform_sound_loader :: check_args_load_stereo_sample_data ( so_called_platform_sound_loader_stereo_resource_id_type resource_id )
{
    so_called_lib_std_int32_t samples_count = 0 ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( samples_count ) ;
    _check_args_load_stereo_sample_data ( samples_count , resource_id ) ;
}
