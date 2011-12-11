template < typename data_type , so_called_platform_math_const_int_32_type size >
class shy_platform_static_array_data_type
{
    friend class shy_platform_static_array ;
    friend class shy_platform_static_array_insider ;
private :
    typedef data_type _data_type ;
    static so_called_platform_math_const_int_32_type _array_size = size ;
    data_type _elements [ _array_size ] ;
} ;
