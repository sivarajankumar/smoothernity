#ifndef _shy_platform_math_int_float_included
#define _shy_platform_math_int_float_included

class shy_platform_math_int_float
{
public :
    static void add_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void sub_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole from 
        , so_called_type_platform_math_num_whole what 
        ) ;
    static void mul_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void mod_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole value 
        , so_called_type_platform_math_num_whole modulator 
        ) ;
    static void div_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void xor_wholes 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void div_whole_by ( so_called_type_platform_math_num_whole & a , so_called_type_platform_math_num_whole b ) ;
    static void mod_whole_by ( so_called_type_platform_math_num_whole & a , so_called_type_platform_math_num_whole b ) ;
    static void mul_whole_by ( so_called_type_platform_math_num_whole & a , so_called_type_platform_math_num_whole b ) ;
    static void sub_from_whole ( so_called_type_platform_math_num_whole & a , so_called_type_platform_math_num_whole b ) ;
    static void add_to_whole ( so_called_type_platform_math_num_whole & a , so_called_type_platform_math_num_whole b ) ;
    static void neg_whole ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole a ) ;
    static void inc_whole ( so_called_type_platform_math_num_whole & a ) ;
    static void dec_whole ( so_called_type_platform_math_num_whole & a ) ;

    static void sub_fracts 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract from 
        , so_called_type_platform_math_num_fract what 
        ) ;
    static void add_fracts 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract a 
        , so_called_type_platform_math_num_fract b 
        ) ;
    static void mul_fracts 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract a 
        , so_called_type_platform_math_num_fract b 
        ) ;
    static void div_fracts 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract a 
        , so_called_type_platform_math_num_fract b 
        ) ;
    static void add_to_fract ( so_called_type_platform_math_num_fract & a , so_called_type_platform_math_num_fract b ) ;
    static void sub_from_fract ( so_called_type_platform_math_num_fract & from , so_called_type_platform_math_num_fract what ) ;
    static void mul_fract_by ( so_called_type_platform_math_num_fract & a , so_called_type_platform_math_num_fract b ) ;
    static void div_fract_by ( so_called_type_platform_math_num_fract & a , so_called_type_platform_math_num_fract b ) ;
    static void neg_fract ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_fract a ) ;
    static void sin ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_fract a ) ;
    static void cos ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_fract a ) ;    
    static void neg_fract ( so_called_type_platform_math_num_fract & a ) ;
    
    static void make_whole_from_fract ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_fract fract ) ;
    static void make_fract_from_whole ( so_called_type_platform_math_num_fract & result , so_called_type_platform_math_num_whole whole ) ;
    
    static void make_num_whole 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_const_int_32 value 
        ) ;
    static void make_num_fract 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_const_int_32 numerator 
        , so_called_type_platform_math_const_int_32 denominator 
        ) ;
} ;

#endif
