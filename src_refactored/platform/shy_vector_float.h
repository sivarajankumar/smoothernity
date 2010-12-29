#ifndef _shy_platform_vector_float_included
#define _shy_platform_vector_float_included

class shy_platform_vector_float_insider ;

class shy_platform_vector_float
{
    typedef so_called_platform_math :: num_fract num_fract ;
public :
    class vector_data
    {
        friend class shy_platform_vector_float ;
        friend class shy_platform_vector_float_insider ;
    public :
        vector_data ( ) ;
    private :
        float _x ;
        float _y ;
        float _z ;
    } ;
public :
    static void xyz ( vector_data & , num_fract , num_fract , num_fract ) ;
    static void dot_product ( num_fract & , vector_data , vector_data ) ;
    static void cross_product ( vector_data & , vector_data , vector_data ) ;
    static void add ( vector_data & , vector_data , vector_data ) ;
    static void add_to ( vector_data & , vector_data ) ;
    static void sub ( vector_data & , vector_data , vector_data ) ;
    static void mul ( vector_data & , vector_data , num_fract ) ;
    static void mul_by ( vector_data & , num_fract ) ;
    static void length ( num_fract & , vector_data ) ;
    static void normalize ( vector_data & , vector_data ) ;
} ;

#endif

