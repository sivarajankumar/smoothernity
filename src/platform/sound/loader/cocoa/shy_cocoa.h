class shy_platform_sound_loader_cocoa
{
public :
    template < typename samples_array >
    static void load_stereo_sample_data ( const samples_array & , const so_called_platform_sound_loader_cocoa_stereo_resource_id_type & ) ;
    static void create_stereo_resource_id ( so_called_platform_sound_loader_cocoa_stereo_resource_id_type & , so_called_platform_math_num_whole_type ) ;
    static void loader_ready ( so_called_platform_math_num_whole_type & ) ;
    static void loaded_samples_count ( so_called_platform_math_num_whole_type & ) ;    
    static void init ( ) ;
    static void done ( ) ;
private :
    static void _load_stereo_sample_data 
        ( const so_called_platform_sound_sample_stereo_type *
        , so_called_lib_std_int32_t
        , const so_called_platform_sound_loader_cocoa_stereo_resource_id_type &
        ) ;
} ;

template < typename samples_array >
void shy_platform_sound_loader_cocoa :: load_stereo_sample_data
    ( const samples_array & samples 
    , const so_called_platform_sound_loader_cocoa_stereo_resource_id_type & resource_id 
    )
{
    so_called_trace ( so_called_trace_platform_sound_loader :: template check_args_load_stereo_sample_data < samples_array > ( resource_id ) ) ;
    const so_called_platform_sound_sample_stereo_type * samples_ptr = 0 ;
    so_called_lib_std_int32_t samples_count = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( samples_count ) ;

    _load_stereo_sample_data ( samples_ptr , samples_count , resource_id ) ;
}

