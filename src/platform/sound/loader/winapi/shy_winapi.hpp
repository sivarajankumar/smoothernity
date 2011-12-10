void shy_platform_sound_loader_winapi :: init ( )
{
}

void shy_platform_sound_loader_winapi :: done ( )
{
}

void shy_platform_sound_loader_winapi :: create_stereo_resource_id 
    ( so_called_platform_sound_loader_winapi_stereo_resource_id_type & result
    , so_called_platform_math_num_whole_type resource_index
    )
{
    so_called_trace ( so_called_trace_platform_sound_loader :: check_args_create_stereo_resource_id ( resource_index ) ) ;
    so_called_lib_std_int32_t resource_index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( resource_index_int , resource_index ) ;
    result . _resource_id = resource_index_int ;
}

void shy_platform_sound_loader_winapi :: loader_ready ( so_called_platform_math_num_whole_type & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , so_called_lib_std_true ) ;
}

void shy_platform_sound_loader_winapi :: loaded_samples_count ( so_called_platform_math_num_whole_type & count )
{
    so_called_platform_math_insider :: num_whole_value_set ( count , 0 ) ;
}

void shy_platform_sound_loader_winapi :: _load_stereo_sample_data
    ( const so_called_platform_sound_sample_stereo_type *
    , so_called_lib_std_int32_t
    , const so_called_platform_sound_loader_winapi_stereo_resource_id_type &
    )
{
}
