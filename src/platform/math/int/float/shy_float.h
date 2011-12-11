class shy_platform_math_int_float
{
public :
    static void add_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type a 
        , so_called_platform_math_int_float_num_whole_type b 
        ) ;
    static void sub_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type from 
        , so_called_platform_math_int_float_num_whole_type what 
        ) ;
    static void mul_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type a 
        , so_called_platform_math_int_float_num_whole_type b 
        ) ;
    static void mod_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type value 
        , so_called_platform_math_int_float_num_whole_type modulator 
        ) ;
    static void div_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type a 
        , so_called_platform_math_int_float_num_whole_type b 
        ) ;
    static void xor_wholes 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_num_whole_type a 
        , so_called_platform_math_int_float_num_whole_type b 
        ) ;
    static void div_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b ) ;
    static void mod_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b ) ;
    static void mul_whole_by ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b ) ;
    static void sub_from_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b ) ;
    static void add_to_whole ( so_called_platform_math_int_float_num_whole_type & a , so_called_platform_math_int_float_num_whole_type b ) ;
    static void neg_whole ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_num_whole_type a ) ;
    static void inc_whole ( so_called_platform_math_int_float_num_whole_type & a ) ;
    static void dec_whole ( so_called_platform_math_int_float_num_whole_type & a ) ;

    static void sub_fracts 
        ( so_called_platform_math_int_float_num_fract_type & result 
        , so_called_platform_math_int_float_num_fract_type from 
        , so_called_platform_math_int_float_num_fract_type what 
        ) ;
    static void add_fracts 
        ( so_called_platform_math_int_float_num_fract_type & result 
        , so_called_platform_math_int_float_num_fract_type a 
        , so_called_platform_math_int_float_num_fract_type b 
        ) ;
    static void mul_fracts 
        ( so_called_platform_math_int_float_num_fract_type & result 
        , so_called_platform_math_int_float_num_fract_type a 
        , so_called_platform_math_int_float_num_fract_type b 
        ) ;
    static void div_fracts 
        ( so_called_platform_math_int_float_num_fract_type & result 
        , so_called_platform_math_int_float_num_fract_type a 
        , so_called_platform_math_int_float_num_fract_type b 
        ) ;
    static void add_to_fract ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b ) ;
    static void sub_from_fract ( so_called_platform_math_int_float_num_fract_type & from , so_called_platform_math_int_float_num_fract_type what ) ;
    static void mul_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b ) ;
    static void div_fract_by ( so_called_platform_math_int_float_num_fract_type & a , so_called_platform_math_int_float_num_fract_type b ) ;
    static void neg_fract ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a ) ;
    static void sin ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a ) ;
    static void cos ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_fract_type a ) ;    
    static void neg_fract ( so_called_platform_math_int_float_num_fract_type & a ) ;
    
    static void make_whole_from_fract ( so_called_platform_math_int_float_num_whole_type & result , so_called_platform_math_int_float_num_fract_type fract ) ;
    static void make_fract_from_whole ( so_called_platform_math_int_float_num_fract_type & result , so_called_platform_math_int_float_num_whole_type whole ) ;
    
    static void make_num_whole 
        ( so_called_platform_math_int_float_num_whole_type & result 
        , so_called_platform_math_int_float_const_int_32_type value 
        ) ;
    static void make_num_fract 
        ( so_called_platform_math_int_float_num_fract_type & result 
        , so_called_platform_math_int_float_const_int_32_type numerator 
        , so_called_platform_math_int_float_const_int_32_type denominator 
        ) ;

    static so_called_platform_math_int_float_num_whole_type init_num_whole 
        ( so_called_platform_math_int_float_const_int_32_type value 
        ) ;
    static so_called_platform_math_int_float_num_fract_type init_num_fract 
        ( so_called_platform_math_int_float_const_int_32_type numerator
        , so_called_platform_math_int_float_const_int_32_type denominator
        ) ;
} ;
