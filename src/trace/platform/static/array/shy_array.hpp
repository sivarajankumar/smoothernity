namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_static_array" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_static_array :: _check_args_element_ptr 
    ( so_called_lib_std_int32_t array_size
    , so_called_platform_math_num_whole_type index
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_whole_uninitialized ( index ) ;
        so_called_trace_platform_math :: check_num_whole_exceeds_range_int ( index , 0 , array_size - 1 ) ;
    }
}
