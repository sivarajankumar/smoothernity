namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_sound_loader" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_sound_loader :: check_stereo_resource_id_uninitialized ( so_called_platform_sound_loader_stereo_resource_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_sound_loader_insider :: stereo_resource_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized stereo resource id value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_sound_loader :: _check_args_load_stereo_sample_data
    ( so_called_lib_std_int32_t samples_count 
    , so_called_platform_sound_loader_stereo_resource_id_type resource_id
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_stereo_resource_id_uninitialized ( resource_id ) ;
        if ( samples_count <= 0 )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Supplied array of " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( samples_count ) ;
            so_called_platform_trace :: trace_string_error ( " samples." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}
