template < typename platform >
class shy_platform_math_consts
{
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: platform_math :: num_fract num_fract ;
    typedef typename platform :: platform_math :: num_whole num_whole ;
public :
    shy_platform_math_consts ( ) ;
public :
    num_fract fract_pi ;
    num_fract fract_2pi ;
    num_fract fract_0 ;
    num_fract fract_1 ;
    num_fract fract_2 ;
    num_fract fract_3 ;
    num_fract fract_4 ;
    num_fract fract_5 ;
    num_fract fract_6 ;
    num_fract fract_7 ;
    num_fract fract_8 ;
    num_fract fract_9 ;
    num_whole whole_0 ;
    num_whole whole_1 ;
    num_whole whole_2 ;
    num_whole whole_3 ;
    num_whole whole_4 ;
    num_whole whole_5 ;
    num_whole whole_6 ;
    num_whole whole_7 ;
    num_whole whole_8 ;
    num_whole whole_9 ;
    num_fract fract_minus_1 ;
    num_fract fract_minus_2 ;
    num_fract fract_minus_3 ;
    num_fract fract_minus_4 ;
    num_fract fract_minus_5 ;
    num_fract fract_minus_6 ;
    num_fract fract_minus_7 ;
    num_fract fract_minus_8 ;
    num_fract fract_minus_9 ;
    num_whole whole_minus_1 ;
    num_whole whole_minus_2 ;
    num_whole whole_minus_3 ;
    num_whole whole_minus_4 ;
    num_whole whole_minus_5 ;
    num_whole whole_minus_6 ;
    num_whole whole_minus_7 ;
    num_whole whole_minus_8 ;
    num_whole whole_minus_9 ;
} ;

template < typename platform >
shy_platform_math_consts < platform > :: shy_platform_math_consts ( )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_pi , 3.141592f ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_2pi , 6.283184f ) ;
    
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_0 , 0 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_1 , 1 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_2 , 2 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_3 , 3 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_4 , 4 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_5 , 5 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_6 , 6 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_7 , 7 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_8 , 8 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_9 , 9 ) ;
    
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_0 , 0 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_1 , 1 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_2 , 2 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_3 , 3 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_4 , 4 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_5 , 5 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_6 , 6 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_7 , 7 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_8 , 8 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_9 , 9 ) ;
    
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_1 , - 1 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_2 , - 2 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_3 , - 3 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_4 , - 4 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_5 , - 5 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_6 , - 6 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_7 , - 7 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_8 , - 8 ) ;
    _platform_math_insider :: num_fract_unsafe_value_set ( fract_minus_9 , - 9 ) ;
    
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_1 , - 1 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_2 , - 2 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_3 , - 3 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_4 , - 4 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_5 , - 5 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_6 , - 6 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_7 , - 7 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_8 , - 8 ) ;
    _platform_math_insider :: num_whole_unsafe_value_set ( whole_minus_9 , - 9 ) ;
}
