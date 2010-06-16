template < typename platform >
class shy_platform_matrix_float_insider ;

template < typename platform >
class shy_platform_matrix_float
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: vector_data vector_data ;
public :
    class matrix_data
    {
        friend class shy_platform_matrix_float ;
        friend class shy_platform_matrix_float_insider < platform > ;
    public :
        matrix_data ( ) ;
    private :
        GLfloat _elements [ 16 ] ;
    } ;
public :
    static void matrix_set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void matrix_set_axis_x ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_axis_y ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_axis_z ( matrix_data & matrix , vector_data v ) ;
    static void matrix_set_origin ( matrix_data & matrix , vector_data v ) ;
    static void matrix_get_axis_x ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_axis_y ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_axis_z ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_get_origin ( vector_data & result , const matrix_data & matrix ) ;
    static void matrix_identity ( matrix_data & matrix ) ;
    static void matrix_inverse_rotation_translation ( matrix_data & matrix ) ;
private :
    template < typename type >
    static void _swap_values ( type & a , type & b ) ;
    
    static int _uninitialized_value ( ) ;
} ;

template < typename platform >
int shy_platform_matrix_float < platform > :: _uninitialized_value ( )
{
    return platform :: _uninitialized_value ;
}

template < typename platform >
shy_platform_matrix_float < platform > :: matrix_data :: matrix_data ( )
{
    for ( int i = 0 ; i < 16 ; i ++ )
        _elements [ i ] = shy_platform_matrix_float < platform > :: _uninitialized_value ( ) ;
}
    
template < typename platform >
template < typename type >
inline void shy_platform_matrix_float < platform > :: _swap_values ( type & a , type & b )
{
    type c = b ;
    b = a ;
    a = c ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 0 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 1 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 2 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 3 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 4 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 5 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 6 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 7 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [  8 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [  9 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 10 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 11 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 12 ] = _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 13 ] = _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 14 ] = _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 15 ] = 1 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_x ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 0 ] = v . _x ;
    matrix . _elements [ 1 ] = v . _y ;
    matrix . _elements [ 2 ] = v . _z ;
    matrix . _elements [ 3 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_y ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 4 ] = v . _x ;
    matrix . _elements [ 5 ] = v . _y ;
    matrix . _elements [ 6 ] = v . _z ;
    matrix . _elements [ 7 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_axis_z ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [  8 ] = v . _x ;
    matrix . _elements [  9 ] = v . _y ;
    matrix . _elements [ 10 ] = v . _z ;
    matrix . _elements [ 11 ] = 0 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_set_origin ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 12 ] = v . _x ;
    matrix . _elements [ 13 ] = v . _y ;
    matrix . _elements [ 14 ] = v . _z ;
    matrix . _elements [ 15 ] = 1 ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_get_axis_x ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 0 ] ;
    result . _y = matrix . _elements [ 1 ] ;
    result . _z = matrix . _elements [ 2 ] ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_get_axis_y ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 4 ] ;
    result . _y = matrix . _elements [ 5 ] ;
    result . _z = matrix . _elements [ 6 ] ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_get_axis_z ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 8 ] ;
    result . _y = matrix . _elements [ 9 ] ;
    result . _z = matrix . _elements [ 10 ] ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_get_origin ( vector_data & result , const matrix_data & matrix )
{
    result . _x = matrix . _elements [ 12 ] ;
    result . _y = matrix . _elements [ 13 ] ;
    result . _z = matrix . _elements [ 14 ] ;
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_identity ( matrix_data & matrix )
{
    for ( int i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

template < typename platform >
inline void shy_platform_matrix_float < platform > :: matrix_inverse_rotation_translation ( matrix_data & matrix )
{
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    vector_data origin ;
    matrix_get_axis_x ( axis_x , matrix ) ;
    matrix_get_axis_y ( axis_y , matrix ) ;
    matrix_get_axis_z ( axis_z , matrix ) ;
    matrix_get_origin ( origin , matrix ) ;
    
    num_fract dot_x ;
    num_fract dot_y ;
    num_fract dot_z ;
    platform :: vector_dot_product ( dot_x , origin , axis_x ) ;
    platform :: vector_dot_product ( dot_y , origin , axis_y ) ;
    platform :: vector_dot_product ( dot_z , origin , axis_z ) ;
    
    vector_data new_origin ;
    new_origin . _x = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_x ) ;
    new_origin . _y = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_y ) ;
    new_origin . _z = - _platform_math_insider :: num_fract_unsafe_value_get ( dot_z ) ;
    
    matrix_set_origin ( matrix , new_origin ) ;
    _swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    _swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    _swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
