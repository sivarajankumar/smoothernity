template < typename platform >
class shy_platform_vector_float_insider
{
    typedef typename platform :: platform_vector :: vector_data vector_data ;
public :
    static float vector_x_unsafe_get ( vector_data v ) ;
    static float vector_y_unsafe_get ( vector_data v ) ;
    static float vector_z_unsafe_get ( vector_data v ) ;
    static void vector_x_unsafe_set ( vector_data & v , float x ) ;
    static void vector_y_unsafe_set ( vector_data & v , float y ) ;
    static void vector_z_unsafe_set ( vector_data & v , float z ) ;
} ;

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: vector_x_unsafe_get ( vector_data v )
{
    return v . _x ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: vector_y_unsafe_get ( vector_data v )
{
    return v . _y ;
}

template < typename platform >
inline float shy_platform_vector_float_insider < platform > :: vector_z_unsafe_get ( vector_data v )
{
    return v . _z ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: vector_x_unsafe_set ( vector_data & v , float x )
{
    v . _x = x ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: vector_y_unsafe_set ( vector_data & v , float y )
{
    v . _y = y ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: vector_z_unsafe_set ( vector_data & v , float z )
{
    v . _z = z ;
}
