#ifndef _shy_platform_math_consts_included
#define _shy_platform_math_consts_included

class shy_platform_math_consts
{
    typedef so_called_platform_math :: num_fract num_fract ;
    typedef so_called_platform_math :: num_whole num_whole ;
public :
    static void assign_consts_values ( ) ;
private :
    static void _assign_const_num_fract ( const num_fract & , float ) ;
    static void _assign_const_num_whole ( const num_whole & , int ) ;
public :
    static const num_fract fract_pi ;
    static const num_fract fract_pi2 ;
    static const num_fract fract_2pi ;
    static const num_fract fract_0 ;
    static const num_fract fract_1 ;
    static const num_fract fract_2 ;
    static const num_fract fract_3 ;
    static const num_fract fract_4 ;
    static const num_fract fract_5 ;
    static const num_fract fract_6 ;
    static const num_fract fract_7 ;
    static const num_fract fract_8 ;
    static const num_fract fract_9 ;
    static const num_fract fract_minus_1 ;
    static const num_fract fract_minus_2 ;
    static const num_fract fract_minus_3 ;
    static const num_fract fract_minus_4 ;
    static const num_fract fract_minus_5 ;
    static const num_fract fract_minus_6 ;
    static const num_fract fract_minus_7 ;
    static const num_fract fract_minus_8 ;
    static const num_fract fract_minus_9 ;

    static const num_whole whole_true ;
    static const num_whole whole_false ;
    static const num_whole whole_0 ;
    static const num_whole whole_1 ;
    static const num_whole whole_2 ;
    static const num_whole whole_3 ;
    static const num_whole whole_4 ;
    static const num_whole whole_5 ;
    static const num_whole whole_6 ;
    static const num_whole whole_7 ;
    static const num_whole whole_8 ;
    static const num_whole whole_9 ;
    static const num_whole whole_minus_1 ;
    static const num_whole whole_minus_2 ;
    static const num_whole whole_minus_3 ;
    static const num_whole whole_minus_4 ;
    static const num_whole whole_minus_5 ;
    static const num_whole whole_minus_6 ;
    static const num_whole whole_minus_7 ;
    static const num_whole whole_minus_8 ;
    static const num_whole whole_minus_9 ;
} ;

#endif

