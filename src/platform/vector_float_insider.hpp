template < typename platform >
class shy_platform_vector_float_insider
{
    typedef typename platform :: platform_vector :: vector_data vector_data ;
public :
    static float x_get ( vector_data v ) ;
    static float y_get ( vector_data v ) ;
    static float z_get ( vector_data v ) ;
    static void x_set ( vector_data & v , float x ) ;
    static void y_set ( vector_data & v , float y ) ;
    static void z_set ( vector_data & v , float z ) ;
} ;

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: x_get ( vector_data v )
{
    return v . _x ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: y_get ( vector_data v )
{
    return v . _y ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: z_get ( vector_data v )
{
    return v . _z ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: x_set ( vector_data & v , float x )
{
    v . _x = x ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: y_set ( vector_data & v , float y )
{
    v . _y = y ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: z_set ( vector_data & v , float z )
{
    v . _z = z ;
}
