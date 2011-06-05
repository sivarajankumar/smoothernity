template < typename data_type , so_called_type_platform_math_const_int_32 size >
class shy_type_platform_static_array_data
{
    friend class shy_platform_static_array ;
    friend class shy_platform_static_array_insider ;
private :
    typedef data_type _data_type ;
    static so_called_type_platform_math_const_int_32 _array_size = size ;
    data_type _elements [ _array_size ] ;
} ;
