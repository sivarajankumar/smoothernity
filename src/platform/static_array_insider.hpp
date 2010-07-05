template < typename platform >
class shy_platform_static_array_insider
{
    typedef typename platform :: platform_math :: const_int_32 const_int_32 ;
public :
    template < typename static_array >
    static typename static_array :: _data_type * elements_ptr ( static_array & array ) ;
    
    template < typename static_array >
    static const typename static_array :: _data_type * elements_ptr ( const static_array & array ) ;
    
    template < typename static_array >
    static const_int_32 elements_count ( ) ;
} ;

template < typename platform >
template < typename static_array >
inline typename static_array :: _data_type * 
shy_platform_static_array_insider < platform > :: elements_ptr ( static_array & array )
{
    return array . _elements ;
}

template < typename platform >
template < typename static_array >
inline const typename static_array :: _data_type * 
shy_platform_static_array_insider < platform > :: elements_ptr ( const static_array & array )
{
    return array . _elements ;
}

template < typename platform >
template < typename static_array >
inline typename shy_platform_static_array_insider < platform > :: const_int_32
shy_platform_static_array_insider < platform > :: elements_count ( )
{
    return static_array :: _array_size ;
}
