class shy_platform_static_array
{
public :
    template < typename array_type , typename pointer_type >
    static void element_ptr ( pointer_type & , array_type & , so_called_type_platform_math_num_whole ) ;
} ;

template < typename array_type , typename pointer_type >
void shy_platform_static_array :: element_ptr ( pointer_type & element_ptr , array_type & array , so_called_type_platform_math_num_whole index )
{
    int index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( element_ptr , array . _elements [ index_int ] ) ;
}
