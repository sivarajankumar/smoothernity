template < typename platform >
class shy_platform_matrix_float_insider
{
    typedef typename platform :: platform_matrix :: matrix_data matrix_data ;
public :
    static GLfloat * matrix_elements_unsafe_ptr ( matrix_data & matrix ) ;
    static const GLfloat * matrix_elements_unsafe_ptr ( const matrix_data & matrix ) ;
} ;

template < typename platform >
inline GLfloat * shy_platform_matrix_float_insider < platform > :: matrix_elements_unsafe_ptr ( matrix_data & matrix )
{
    return matrix . _elements ;
}

template < typename platform >
inline const GLfloat * shy_platform_matrix_float_insider < platform > :: matrix_elements_unsafe_ptr ( const matrix_data & matrix )
{
    return matrix . _elements ;
}
