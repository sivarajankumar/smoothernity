template < typename platform >
class shy_platform_static_array_insider ;

template < typename platform >
class shy_platform_static_array
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: const_int_32 const_int_32 ;
    typedef typename platform :: num_whole num_whole ;
public :
    template < typename data_type , const_int_32 size >
    class static_array
    {
        friend class shy_platform_static_array ;
        friend class shy_platform_static_array_insider < platform > ;
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

template < typename platform >
template < typename data_type , typename shy_platform_static_array < platform > :: const_int_32 size >
inline data_type & shy_platform_static_array < platform > :: array_element ( static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ _platform_math_insider :: num_whole_unsafe_value_get ( index ) ] ;
}

template < typename platform >
template < typename data_type , typename shy_platform_static_array < platform > :: const_int_32 size >
inline const data_type & shy_platform_static_array < platform > :: array_element ( const static_array < data_type , size > & array , num_whole index )
{
    return array . _elements [ _platform_math_insider :: num_whole_unsafe_value_get ( index ) ] ;
}
