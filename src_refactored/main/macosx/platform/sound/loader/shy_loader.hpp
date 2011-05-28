void shy_macosx_platform_sound_loader :: create_stereo_resource_id 
    ( so_called_type_platform_sound_loader_stereo_resource_id & result 
    , so_called_type_platform_math_num_whole resource_index
    )
{
    so_called_lib_std_int32_t resource_index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( resource_index_int , resource_index ) ;
    result . _resource_id = resource_index_int ;
}

void shy_macosx_platform_sound_loader :: loader_ready ( so_called_type_platform_math_num_whole & result )
{
    void * void_loader = 0 ;
    so_called_platform_sound_loader_insider :: get_sound_loader ( void_loader ) ;
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( void_loader ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , [ loader loader_ready ] ) ;
}

void shy_macosx_platform_sound_loader :: loaded_samples_count ( so_called_type_platform_math_num_whole & result )
{
    void * void_loader = 0 ;
    so_called_platform_sound_loader_insider :: get_sound_loader ( void_loader ) ;
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( void_loader ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , [ loader loaded_samples_count ] ) ;
}

void shy_macosx_platform_sound_loader :: _load_stereo_sample_data
    ( const so_called_type_platform_sound_sample_stereo * samples_ptr
    , so_called_lib_std_int32_t samples_count
    , const so_called_type_platform_sound_loader_stereo_resource_id & resource_id 
    )
{
    void * void_loader = 0 ;
    so_called_platform_sound_loader_insider :: get_sound_loader ( void_loader ) ;
    shy_macosx_sound_loader * loader = reinterpret_cast < shy_macosx_sound_loader * > ( void_loader ) ;
    [ loader 
        load_16_bit_44100_khz_stereo_samples_from_resource : resource_id . _resource_id 
        to_buffer : ( void * ) samples_ptr
        with_max_samples_count_of : samples_count
    ] ;
}

