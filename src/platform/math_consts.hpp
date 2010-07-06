template < typename platform_insider >
class shy_platform_math_consts
{
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
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
    num_whole whole_true ;
    num_whole whole_false ;
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

template < typename platform_insider >
shy_platform_math_consts < platform_insider > :: shy_platform_math_consts ( )
{
    platform_math_insider :: num_fract_value_set ( fract_pi , 3.141592f ) ;
    platform_math_insider :: num_fract_value_set ( fract_2pi , 6.283184f ) ;
    
    platform_math_insider :: num_fract_value_set ( fract_0 , 0 ) ;
    platform_math_insider :: num_fract_value_set ( fract_1 , 1 ) ;
    platform_math_insider :: num_fract_value_set ( fract_2 , 2 ) ;
    platform_math_insider :: num_fract_value_set ( fract_3 , 3 ) ;
    platform_math_insider :: num_fract_value_set ( fract_4 , 4 ) ;
    platform_math_insider :: num_fract_value_set ( fract_5 , 5 ) ;
    platform_math_insider :: num_fract_value_set ( fract_6 , 6 ) ;
    platform_math_insider :: num_fract_value_set ( fract_7 , 7 ) ;
    platform_math_insider :: num_fract_value_set ( fract_8 , 8 ) ;
    platform_math_insider :: num_fract_value_set ( fract_9 , 9 ) ;

    platform_math_insider :: num_fract_value_set ( fract_minus_1 , - 1 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_2 , - 2 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_3 , - 3 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_4 , - 4 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_5 , - 5 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_6 , - 6 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_7 , - 7 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_8 , - 8 ) ;
    platform_math_insider :: num_fract_value_set ( fract_minus_9 , - 9 ) ;
    
    int * whole_true_int = 0 ;
    int * whole_false_int = 0 ;
    int * whole_0_int = 0 ;
    int * whole_1_int = 0 ;
    int * whole_2_int = 0 ;
    int * whole_3_int = 0 ;
    int * whole_4_int = 0 ;
    int * whole_5_int = 0 ;
    int * whole_6_int = 0 ;
    int * whole_7_int = 0 ;
    int * whole_8_int = 0 ;
    int * whole_9_int = 0 ;
    int * whole_minus_1_int = 0 ;
    int * whole_minus_2_int = 0 ;
    int * whole_minus_3_int = 0 ;
    int * whole_minus_4_int = 0 ;
    int * whole_minus_5_int = 0 ;
    int * whole_minus_6_int = 0 ;
    int * whole_minus_7_int = 0 ;
    int * whole_minus_8_int = 0 ;
    int * whole_minus_9_int = 0 ;
    
    platform_math_insider :: num_whole_value_ptr ( whole_true_int , whole_true ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_false_int , whole_false ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_0_int , whole_0 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_1_int , whole_1 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_2_int , whole_2 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_3_int , whole_3 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_4_int , whole_4 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_5_int , whole_5 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_6_int , whole_6 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_7_int , whole_7 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_8_int , whole_8 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_9_int , whole_9 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_1_int , whole_minus_1 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_2_int , whole_minus_2 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_3_int , whole_minus_3 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_4_int , whole_minus_4 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_5_int , whole_minus_5 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_6_int , whole_minus_6 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_7_int , whole_minus_7 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_8_int , whole_minus_8 ) ;
    platform_math_insider :: num_whole_value_ptr ( whole_minus_9_int , whole_minus_9 ) ;
    
    * whole_true_int = true ;
    * whole_false_int = false ;    
    * whole_0_int = 0 ;
    * whole_1_int = 1 ;
    * whole_2_int = 2 ;
    * whole_3_int = 3 ;
    * whole_4_int = 4 ;
    * whole_5_int = 5 ;
    * whole_6_int = 6 ;
    * whole_7_int = 7 ;
    * whole_8_int = 8 ;
    * whole_9_int = 9 ;
    * whole_minus_1_int = - 1 ;
    * whole_minus_2_int = - 2 ;
    * whole_minus_3_int = - 3 ;
    * whole_minus_4_int = - 4 ;
    * whole_minus_5_int = - 5 ;
    * whole_minus_6_int = - 6 ;
    * whole_minus_7_int = - 7 ;
    * whole_minus_8_int = - 8 ;
    * whole_minus_9_int = - 9 ;    
}
