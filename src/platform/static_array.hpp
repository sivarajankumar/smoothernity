template < typename platform_insider >
class shy_platform_static_array_insider ;

template < typename platform_insider >
class shy_platform_static_array
{
    typedef typename platform_insider :: platform_math :: const_int_32 const_int_32 ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
public :
    template < typename data_type , const_int_32 size >
    class static_array
    {
        friend class shy_platform_static_array ;
        friend class shy_platform_static_array_insider < platform_insider > ;
    private :
        typedef data_type _data_type ;
        static const_int_32 _array_size = size ;
        data_type _elements [ _array_size ] ;
    } ;
public :
    template < typename data_type , const_int_32 size >
    static data_type & array_element ( static_array < data_type , size > & array , num_whole index ) ;
    template < typename data_type , const_int_32 size >
    static const data_type & array_element ( const static_array < data_type , size > & array , num_whole index ) ;
} ;

template < typename platform_insider >
template < typename data_type , typename shy_platform_static_array < platform_insider > :: const_int_32 size >
inline data_type & shy_platform_static_array < platform_insider > :: array_element ( static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ platform_math_insider :: num_whole_unsafe_value_get ( index ) ] ;
}

template < typename platform_insider >
template < typename data_type , typename shy_platform_static_array < platform_insider > :: const_int_32 size >
inline const data_type & shy_platform_static_array < platform_insider > :: array_element ( const static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ platform_math_insider :: num_whole_unsafe_value_get ( index ) ] ;
}
