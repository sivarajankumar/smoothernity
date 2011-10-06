class shy_trace_platform_pointer
{
public :
    template < typename pointer_type >
    static void check_data_uninitialized ( pointer_type ) ;
private :
    static void _check_data_uninitialized ( so_called_lib_std_bool ) ;
} ;

template < typename pointer_type >
void shy_trace_platform_pointer :: check_data_uninitialized ( pointer_type value )
{
    so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
    so_called_platform_pointer_insider :: data_uninitialized ( uninitialized , value ) ;
    shy_trace_platform_pointer :: _check_data_uninitialized ( uninitialized ) ;
}
