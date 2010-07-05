template < typename platform >
class shy_platform_matrix_float_insider
{
    typedef typename platform :: platform_matrix :: matrix_data matrix_data ;
public :
    static float * elements_ptr ( matrix_data & matrix ) ;
    static const float * elements_ptr ( const matrix_data & matrix ) ;
} ;

template < typename platform >
inline float * shy_platform_matrix_float_insider < platform > :: elements_ptr ( matrix_data & matrix )
{
    return matrix . _elements ;
}

template < typename platform >
inline const float * shy_platform_matrix_float_insider < platform > :: elements_ptr ( const matrix_data & matrix )
{
    return matrix . _elements ;
}
