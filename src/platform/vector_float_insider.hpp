template < typename platform >
class shy_platform_vector_float_insider
{
    typedef typename platform :: platform_vector :: vector_data vector_data ;
public :
    static void x_get ( float & , vector_data ) ;
    static void y_get ( float & , vector_data ) ;
    static void z_get ( float & , vector_data ) ;
    static void x_set ( vector_data & , float ) ;
    static void y_set ( vector_data & , float ) ;
    static void z_set ( vector_data & , float ) ;
} ;

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: x_get ( float & x , vector_data v )
{
    x = v . _x ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: y_get ( float & y , vector_data v )
{
    y = v . _y ;
}

template < typename platform >
inline void shy_platform_vector_float_insider < platform > :: z_get ( float & z , vector_data v )
{
    z = v . _z ;
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
