class shy_platform_static_array
{
public :
    template < typename array_type , typename pointer_type >
    static void element_ptr ( pointer_type & , array_type & , so_called_platform_math_num_whole_type ) ;
} ;

template < typename array_type , typename pointer_type >
void shy_platform_static_array :: element_ptr ( pointer_type & element_ptr , array_type & array , so_called_platform_math_num_whole_type index )
{
    so_called_profile ( so_called_profile_platform_static_array :: element ( ) ) ;
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( element_ptr , array . _elements [ index_int ] ) ;
}
