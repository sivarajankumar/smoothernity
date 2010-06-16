template < typename platform >
class shy_platform_static_array_insider
{
    typedef typename platform :: const_int_32 const_int_32 ;
    typedef typename platform :: platform_static_array platform_static_array ;
public :
    template < typename data_type , const_int_32 size >
    static data_type * array_elements_unsafe_ptr ( typename platform_static_array :: template static_array < data_type , size > & array ) ;
    template < typename data_type , const_int_32 size >
    static const data_type * array_elements_unsafe_ptr ( const typename platform_static_array :: template static_array < data_type , size > & array ) ;
} ;

template < typename platform >
template < typename data_type , typename shy_platform_static_array_insider < platform > :: const_int_32 size >
inline data_type * shy_platform_static_array_insider < platform > :: array_elements_unsafe_ptr 
    ( typename platform_static_array :: template static_array < data_type , size > & array )
{
    return array . _elements ;
}

template < typename platform >
template < typename data_type , typename shy_platform_static_array_insider < platform > :: const_int_32 size >
inline const data_type * shy_platform_static_array_insider < platform > :: array_elements_unsafe_ptr 
    ( const typename platform_static_array :: template static_array < data_type , size > & array )
{
    return array . _elements ;
}
