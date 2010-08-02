template < typename platform >
class shy_platform_matrix_float_insider
{
    typedef typename platform :: platform_matrix :: matrix_data matrix_data ;
public :
    static void elements_ptr ( float * & , matrix_data & ) ;
    static void elements_ptr ( const float * & , const matrix_data & ) ;
} ;

template < typename platform >
inline void shy_platform_matrix_float_insider < platform > :: elements_ptr ( float * & result , matrix_data & matrix )
{
    result = matrix . _elements ;
}

template < typename platform >
inline void shy_platform_matrix_float_insider < platform > :: elements_ptr ( const float * & result , const matrix_data & matrix )
{
    result = matrix . _elements ;
}
