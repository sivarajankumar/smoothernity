class shy_macosx_platform_sound_loader
{
public :
    static void create_stereo_resource_id ( so_called_type_platform_sound_stereo_resource_id & , so_called_type_platform_math_num_whole ) ;

    template < typename samples_array >
    static void load_stereo_sample_data ( const samples_array & , const so_called_type_platform_sound_stereo_resource_id & ) ;

    static void loader_ready ( so_called_type_platform_math_num_whole & ) ;
    static void loaded_samples_count ( so_called_type_platform_math_num_whole & ) ;    
private :
    static void _load_stereo_sample_data 
        ( const so_called_type_platform_sound_sample_stereo *
        , so_called_lib_std_int32_t
        , const so_called_type_platform_sound_stereo_resource_id &
        ) ;
} ;

template < typename samples_array >
void shy_macosx_platform_sound_loader :: load_stereo_sample_data
    ( const samples_array & samples 
    , const so_called_type_platform_sound_stereo_resource_id & resource_id 
    )
{
    const so_called_type_platform_sound_sample_stereo * samples_ptr = 0 ;
    so_called_lib_std_int32_t samples_count = 0 ;
    so_called_platform_static_array_insider :: elements_ptr ( samples_ptr , samples ) ;
    so_called_platform_static_array_insider :: template elements_count < samples_array > ( samples_count ) ;

    _load_stereo_sample_data ( samples_ptr , samples_count , resource_id ) ;
}
