#ifndef _shy_platform_math_int_float_included
#define _shy_platform_math_int_float_included

class shy_platform_math_int_float_insider ;

class shy_platform_math_int_float
{
public :
    typedef const int const_int_32 ;
    
    class num_whole
    {
        friend class shy_platform_math_int_float ;
        friend class shy_platform_math_int_float_insider ;
    public :
        num_whole ( ) ;
    private :
        num_whole ( int arg_value ) ;
    private :
        int _value ;
    } ;
    
    class num_fract
    {
        friend class shy_platform_math_int_float ;
        friend class shy_platform_math_int_float_insider ;
    public :
        num_fract ( ) ;
    private :
        num_fract ( float arg_value ) ;
    private :
        float _value ;
    } ;
    
public :
    static void add_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void add_to_whole ( num_whole & a , num_whole b ) ;
    static void sub_wholes ( num_whole & result , num_whole from , num_whole what ) ;
    static void sub_from_whole ( num_whole & a , num_whole b ) ;
    static void mul_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void mul_whole_by ( num_whole & a , num_whole b ) ;
    static void mod_wholes ( num_whole & result , num_whole value , num_whole modulator ) ;
    static void mod_whole_by ( num_whole & a , num_whole b ) ;
    static void div_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void div_whole_by ( num_whole & a , num_whole b ) ;
    static void inc_whole ( num_whole & a ) ;
    static void dec_whole ( num_whole & a ) ;
    static void xor_wholes ( num_whole & result , num_whole a , num_whole b ) ;
    static void neg_whole ( num_whole & result , num_whole a ) ;

    static void sin ( num_fract & result , num_fract a ) ;
    static void cos ( num_fract & result , num_fract a ) ;    
    static void sub_fracts ( num_fract & result , num_fract from , num_fract what ) ;
    static void sub_from_fract ( num_fract & from , num_fract what ) ;
    static void add_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void add_to_fract ( num_fract & a , num_fract b ) ;
    static void mul_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void mul_fract_by ( num_fract & a , num_fract b ) ;
    static void div_fracts ( num_fract & result , num_fract a , num_fract b ) ;
    static void div_fract_by ( num_fract & a , num_fract b ) ;
    static void neg_fract ( num_fract & a ) ;
    static void neg_fract ( num_fract & result , num_fract a ) ;
    
    static void make_whole_from_fract ( num_whole & result , num_fract fract ) ;
    static void make_fract_from_whole ( num_fract & result , num_whole whole ) ;
    
    static void make_num_whole ( num_whole & result , const_int_32 value ) ;
    static void make_num_fract ( num_fract & result , const_int_32 numerator , const_int_32 denominator ) ;
} ;

#endif
