#ifndef _shy_platform_math_int_float_insider_included
#define _shy_platform_math_int_float_insider_included

class shy_platform_math_int_float_insider
{
    typedef so_called_platform_math :: num_fract num_fract ;
    typedef so_called_platform_math :: num_whole num_whole ;
public :
    static void num_whole_value_get ( int & , num_whole ) ;
    static void num_whole_value_set ( num_whole & , int ) ;
    static void num_fract_value_get ( float & , num_fract ) ;
    static void num_fract_value_set ( num_fract & , float ) ;
} ;

#endif
