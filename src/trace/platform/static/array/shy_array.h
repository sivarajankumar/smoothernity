class shy_trace_platform_static_array
{
public :
    template < typename array_type >
    static void check_args_element_ptr ( so_called_platform_math_num_whole_type ) ;
private :
    static void _check_args_element_ptr 
        ( so_called_lib_std_int32_t array_size
        , so_called_platform_math_num_whole_type index
        ) ;
} ;

template < typename array_type >
void shy_trace_platform_static_array :: check_args_element_ptr ( so_called_platform_math_num_whole_type index )
{
    so_called_lib_std_int32_t array_size = 0 ;
    so_called_platform_static_array_insider :: template elements_count < array_type > ( array_size ) ;
    _check_args_element_ptr ( array_size , index ) ;
}
