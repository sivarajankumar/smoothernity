template < typename platform_insider >
class shy_platform_matrix_float_insider ;

template < typename platform_insider >
class shy_platform_matrix_float
{
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    typedef typename platform_insider :: platform_vector_insider platform_vector_insider ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_vector platform_vector ;
    typedef typename platform_insider :: platform_vector :: vector_data vector_data ;
public :
    class matrix_data
    {
        friend class shy_platform_matrix_float ;
        friend class shy_platform_matrix_float_insider < platform_insider > ;
    public :
        matrix_data ( ) ;
    private :
        float _elements [ 16 ] ;
    } ;
public :
    static void set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z ) ;
    static void set_axis_x ( matrix_data & matrix , vector_data v ) ;
    static void set_axis_y ( matrix_data & matrix , vector_data v ) ;
    static void set_axis_z ( matrix_data & matrix , vector_data v ) ;
    static void set_origin ( matrix_data & matrix , vector_data v ) ;
    static void get_axis_x ( vector_data & result , const matrix_data & matrix ) ;
    static void get_axis_y ( vector_data & result , const matrix_data & matrix ) ;
    static void get_axis_z ( vector_data & result , const matrix_data & matrix ) ;
    static void get_origin ( vector_data & result , const matrix_data & matrix ) ;
    static void identity ( matrix_data & matrix ) ;
    static void inverse_rotation_translation ( matrix_data & matrix ) ;
private :
    template < typename type >
    static void _swap_values ( type & a , type & b ) ;
} ;

template < typename platform_insider >
shy_platform_matrix_float < platform_insider > :: matrix_data :: matrix_data ( )
{
    for ( int i = 0 ; i < 16 ; i ++ )
        _elements [ i ] = platform_insider :: uninitialized_value ;
}
    
template < typename platform_insider >
template < typename type >
inline void shy_platform_matrix_float < platform_insider > :: _swap_values ( type & a , type & b )
{
    type c = b ;
    b = a ;
    a = c ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_x ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 0 ] = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 1 ] = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 2 ] = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 3 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_y ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 4 ] = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 5 ] = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 6 ] = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 7 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_z ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [  8 ] = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [  9 ] = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 10 ] = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 11 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_origin ( matrix_data & matrix , num_fract x , num_fract y , num_fract z )
{
    matrix . _elements [ 12 ] = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    matrix . _elements [ 13 ] = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    matrix . _elements [ 14 ] = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
    matrix . _elements [ 15 ] = 1 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_x ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 0 ] = platform_vector_insider :: x_unsafe_get ( v ) ;
    matrix . _elements [ 1 ] = platform_vector_insider :: y_unsafe_get ( v ) ;
    matrix . _elements [ 2 ] = platform_vector_insider :: z_unsafe_get ( v ) ;
    matrix . _elements [ 3 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_y ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 4 ] = platform_vector_insider :: x_unsafe_get ( v ) ;
    matrix . _elements [ 5 ] = platform_vector_insider :: y_unsafe_get ( v ) ;
    matrix . _elements [ 6 ] = platform_vector_insider :: z_unsafe_get ( v ) ;
    matrix . _elements [ 7 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_axis_z ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [  8 ] = platform_vector_insider :: x_unsafe_get ( v ) ;
    matrix . _elements [  9 ] = platform_vector_insider :: y_unsafe_get ( v ) ;
    matrix . _elements [ 10 ] = platform_vector_insider :: z_unsafe_get ( v ) ;
    matrix . _elements [ 11 ] = 0 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: set_origin ( matrix_data & matrix , vector_data v )
{
    matrix . _elements [ 12 ] = platform_vector_insider :: x_unsafe_get ( v ) ;
    matrix . _elements [ 13 ] = platform_vector_insider :: y_unsafe_get ( v ) ;
    matrix . _elements [ 14 ] = platform_vector_insider :: z_unsafe_get ( v ) ;
    matrix . _elements [ 15 ] = 1 ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: get_axis_x ( vector_data & result , const matrix_data & matrix )
{
    platform_vector_insider :: x_unsafe_set ( result , matrix . _elements [ 0 ] ) ;
    platform_vector_insider :: y_unsafe_set ( result , matrix . _elements [ 1 ] ) ;
    platform_vector_insider :: z_unsafe_set ( result , matrix . _elements [ 2 ] ) ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: get_axis_y ( vector_data & result , const matrix_data & matrix )
{
    platform_vector_insider :: x_unsafe_set ( result , matrix . _elements [ 4 ] ) ;
    platform_vector_insider :: y_unsafe_set ( result , matrix . _elements [ 5 ] ) ;
    platform_vector_insider :: z_unsafe_set ( result , matrix . _elements [ 6 ] ) ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: get_axis_z ( vector_data & result , const matrix_data & matrix )
{
    platform_vector_insider :: x_unsafe_set ( result , matrix . _elements [ 8 ] ) ;
    platform_vector_insider :: y_unsafe_set ( result , matrix . _elements [ 9 ] ) ;
    platform_vector_insider :: z_unsafe_set ( result , matrix . _elements [ 10 ] ) ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: get_origin ( vector_data & result , const matrix_data & matrix )
{
    platform_vector_insider :: x_unsafe_set ( result , matrix . _elements [ 12 ] ) ;
    platform_vector_insider :: y_unsafe_set ( result , matrix . _elements [ 13 ] ) ;
    platform_vector_insider :: z_unsafe_set ( result , matrix . _elements [ 14 ] ) ;
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: identity ( matrix_data & matrix )
{
    for ( int i = 0 ; i < 16 ; i ++ )
    {
        if ( i == 0 || i == 5 || i == 10 || i == 15 )
            matrix . _elements [ i ] = 1 ;
        else
            matrix . _elements [ i ] = 0 ;
    }
}

template < typename platform_insider >
inline void shy_platform_matrix_float < platform_insider > :: inverse_rotation_translation ( matrix_data & matrix )
{
    vector_data axis_x ;
    vector_data axis_y ;
    vector_data axis_z ;
    vector_data origin ;
    get_axis_x ( axis_x , matrix ) ;
    get_axis_y ( axis_y , matrix ) ;
    get_axis_z ( axis_z , matrix ) ;
    get_origin ( origin , matrix ) ;
    
    num_fract dot_x ;
    num_fract dot_y ;
    num_fract dot_z ;
    platform_vector :: dot_product ( dot_x , origin , axis_x ) ;
    platform_vector :: dot_product ( dot_y , origin , axis_y ) ;
    platform_vector :: dot_product ( dot_z , origin , axis_z ) ;
    
    vector_data new_origin ;
    platform_vector_insider :: x_unsafe_set ( new_origin , - platform_math_insider :: num_fract_unsafe_value_get ( dot_x ) ) ;
    platform_vector_insider :: y_unsafe_set ( new_origin , - platform_math_insider :: num_fract_unsafe_value_get ( dot_y ) ) ;
    platform_vector_insider :: z_unsafe_set ( new_origin , - platform_math_insider :: num_fract_unsafe_value_get ( dot_z ) ) ;
    
    set_origin ( matrix , new_origin ) ;
    _swap_values ( matrix . _elements [ 1 ] , matrix . _elements [ 4 ] ) ;
    _swap_values ( matrix . _elements [ 2 ] , matrix . _elements [ 8 ] ) ;
    _swap_values ( matrix . _elements [ 6 ] , matrix . _elements [ 9 ] ) ;
}
