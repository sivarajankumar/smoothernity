template < typename platform >
class shy_platform_vector_float_insider
{
    typedef typename platform :: platform_vector :: vector_data vector_data ;
public :
    static float x_unsafe_get ( vector_data v ) ;
    static float y_unsafe_get ( vector_data v ) ;
    static float z_unsafe_get ( vector_data v ) ;
    static void x_unsafe_set ( vector_data & v , float x ) ;
    static void y_unsafe_set ( vector_data & v , float y ) ;
    static void z_unsafe_set ( vector_data & v , float z ) ;
} ;

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: x_unsafe_get ( vector_data v )
{
    return v . _x ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: y_unsafe_get ( vector_data v )
{
    return v . _y ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: z_unsafe_get ( vector_data v )
{
    return v . _z ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: x_unsafe_set ( vector_data & v , float x )
{
    v . _x = x ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: y_unsafe_set ( vector_data & v , float y )
{
    v . _y = y ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: z_unsafe_set ( vector_data & v , float z )
{
    v . _z = z ;
}
