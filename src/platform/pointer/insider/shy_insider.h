class shy_platform_pointer_insider
{
public :
    template < typename pointer_type >
    static void data_uninitialized ( so_called_lib_std_bool & , pointer_type ) ;
} ;

template < typename pointer_type >
void shy_platform_pointer_insider :: data_uninitialized ( so_called_lib_std_bool & result , pointer_type pointer )
{
    pointer_type uninitialized_pointer ;
    result = pointer . _data_ptr == uninitialized_pointer . _data_ptr ;
}
