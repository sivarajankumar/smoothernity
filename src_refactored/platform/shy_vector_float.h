#ifndef _shy_platform_vector_float_included
#define _shy_platform_vector_float_included

class shy_platform_vector_float
{
public :
    static void xyz 
        ( so_called_type_platform_vector_data & 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        ) ;
    static void dot_product ( so_called_type_platform_math_num_fract & , so_called_type_platform_vector_data , so_called_type_platform_vector_data ) ;
    static void cross_product ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data , so_called_type_platform_vector_data ) ;
    static void add ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data , so_called_type_platform_vector_data ) ;
    static void add_to ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data ) ;
    static void sub ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data , so_called_type_platform_vector_data ) ;
    static void mul ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data , so_called_type_platform_math_num_fract ) ;
    static void mul_by ( so_called_type_platform_vector_data & , so_called_type_platform_math_num_fract ) ;
    static void length ( so_called_type_platform_math_num_fract & , so_called_type_platform_vector_data ) ;
    static void normalize ( so_called_type_platform_vector_data & , so_called_type_platform_vector_data ) ;
} ;

#endif

