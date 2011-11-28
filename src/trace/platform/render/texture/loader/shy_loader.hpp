namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_int32_t max_texture_pow2 = 16 ;
        static const so_called_lib_std_char module_name [ ] = "platform_render_texture_loader" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_render_texture_loader :: check_resource_id_uninitialized ( so_called_platform_render_texture_loader_resource_id_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_render_texture_loader_insider :: resource_id_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized resource id value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_render_texture_loader :: _check_args_load_resource
    ( so_called_platform_render_texture_loader_cocoa_resource_id_type resource_id 
    , so_called_platform_math_num_whole_type size_pow2_base 
    , so_called_lib_std_int32_t texels_count
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_resource_id_uninitialized ( resource_id ) ;
        so_called_trace_platform_math :: check_num_whole_uninitialized ( size_pow2_base ) ;

        so_called_lib_std_int32_t size_pow2_base_int = 0 ;
        so_called_platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;

        so_called_lib_std_int32_t texture_size = ( 1 << size_pow2_base_int ) * 2 ;

        if ( texture_size > texels_count )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Resource texels count " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( texture_size ) ;
            so_called_platform_trace :: trace_string_error ( " exceeds supplied array of " ) ;
            so_called_platform_trace :: trace_const_int_32_error ( texels_count ) ;
            so_called_platform_trace :: trace_string_error ( " texels." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }

        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( size_pow2_base , 0 , shy_guts :: consts :: max_texture_pow2 ) ;
    }
}

