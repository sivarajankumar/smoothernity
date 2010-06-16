template < typename platform >
class shy_platform_math_consts
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    shy_platform_math_consts ( ) ;
public :
    const num_fract fract_pi ;
    const num_fract fract_2pi ;
    const num_fract fract_0 ;
    const num_fract fract_1 ;
    const num_fract fract_2 ;
    const num_fract fract_3 ;
    const num_fract fract_4 ;
    const num_fract fract_5 ;
    const num_fract fract_6 ;
    const num_fract fract_7 ;
    const num_fract fract_8 ;
    const num_fract fract_9 ;
    const num_whole whole_0 ;
    const num_whole whole_1 ;
    const num_whole whole_2 ;
    const num_whole whole_3 ;
    const num_whole whole_4 ;
    const num_whole whole_5 ;
    const num_whole whole_6 ;
    const num_whole whole_7 ;
    const num_whole whole_8 ;
    const num_whole whole_9 ;
    const num_fract fract_minus_1 ;
    const num_fract fract_minus_2 ;
    const num_fract fract_minus_3 ;
    const num_fract fract_minus_4 ;
    const num_fract fract_minus_5 ;
    const num_fract fract_minus_6 ;
    const num_fract fract_minus_7 ;
    const num_fract fract_minus_8 ;
    const num_fract fract_minus_9 ;
    const num_whole whole_minus_1 ;
    const num_whole whole_minus_2 ;
    const num_whole whole_minus_3 ;
    const num_whole whole_minus_4 ;
    const num_whole whole_minus_5 ;
    const num_whole whole_minus_6 ;
    const num_whole whole_minus_7 ;
    const num_whole whole_minus_8 ;
    const num_whole whole_minus_9 ;
} ;

template < typename platform >
shy_platform_math_consts < platform > :: shy_platform_math_consts ( )
{
    _platform_math_insider :: num_fract_unsafe_value ( fract_pi ) = 3.141592f ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_2pi ) = 6.283184f ;
    
    _platform_math_insider :: num_fract_unsafe_value ( fract_0 ) = 0 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_1 ) = 1 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_2 ) = 2 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_3 ) = 3 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_4 ) = 4 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_5 ) = 5 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_6 ) = 6 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_7 ) = 7 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_8 ) = 8 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_9 ) = 9 ;
    
    _platform_math_insider :: num_whole_unsafe_value ( whole_0 ) = 0 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_1 ) = 1 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_2 ) = 2 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_3 ) = 3 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_4 ) = 4 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_5 ) = 5 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_6 ) = 6 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_7 ) = 7 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_8 ) = 8 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_9 ) = 9 ;
    
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_1 ) = - 1 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_2 ) = - 2 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_3 ) = - 3 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_4 ) = - 4 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_5 ) = - 5 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_6 ) = - 6 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_7 ) = - 7 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_8 ) = - 8 ;
    _platform_math_insider :: num_fract_unsafe_value ( fract_minus_9 ) = - 9 ;
    
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_1 ) = - 1 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_2 ) = - 2 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_3 ) = - 3 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_4 ) = - 4 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_5 ) = - 5 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_6 ) = - 6 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_7 ) = - 7 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_8 ) = - 8 ;
    _platform_math_insider :: num_whole_unsafe_value ( whole_minus_9 ) = - 9 ;
}
