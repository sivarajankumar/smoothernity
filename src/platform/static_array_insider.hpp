template < typename platform >
class shy_platform_static_array_insider
{
public :
    template < typename static_array >
    static void elements_ptr ( typename static_array :: _data_type * & result , static_array & array ) ;
    
    template < typename static_array >
    static void elements_ptr ( const typename static_array :: _data_type * & result , const static_array & array ) ;
    
    template < typename static_array >
    static void elements_count ( int & count ) ;
} ;

template < typename platform >
template < typename static_array >
inline void shy_platform_static_array_insider < platform > :: elements_ptr 
    ( typename static_array :: _data_type * & result , static_array & array )
{
    result = array . _elements ;
}

template < typename platform >
template < typename static_array >
inline void shy_platform_static_array_insider < platform > :: elements_ptr 
    ( const typename static_array :: _data_type * & result , const static_array & array )
{
    result = array . _elements ;
}

template < typename platform >
template < typename static_array >
inline void shy_platform_static_array_insider < platform > :: elements_count ( int & count )
{
    count = int ( static_array :: _array_size ) ;
}
