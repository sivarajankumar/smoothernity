#ifndef _shy_platform_static_array_included
#define _shy_platform_static_array_included

class shy_platform_static_array
{
public :
    template < typename data_type , so_called_type_platform_math_const_int_32 size >
    class static_array
    {
        friend class shy_platform_static_array ;
        friend class shy_platform_static_array_insider ;
    private :
        typedef data_type _data_type ;
        static so_called_type_platform_math_const_int_32 _array_size = size ;
        data_type _elements [ _array_size ] ;
    } ;
public :
    template < typename array_type , typename pointer_type >
    static void element_ptr ( pointer_type & , array_type & , num_whole ) ;
} ;

template < typename array_type , typename pointer_type >
void shy_platform_static_array :: element_ptr ( pointer_type & element_ptr , array_type & array , num_whole index )
{
    int index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( element_ptr , array . _elements [ index_int ] ) ;
}

#endif

