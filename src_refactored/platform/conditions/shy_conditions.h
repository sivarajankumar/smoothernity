#ifndef _shy_platform_conditions_included
#define _shy_platform_conditions_included

class shy_platform_conditions
{
public :
    static int fract_less_than_fract ( so_called_type_platform_math_num_fract , so_called_type_platform_math_num_fract ) ;
    static int whole_greater_or_equal_to_whole ( so_called_type_platform_math_num_whole , so_called_type_platform_math_num_whole ) ;
    static int fract_greater_than_fract ( so_called_type_platform_math_num_fract , so_called_type_platform_math_num_fract ) ;
    static int whole_greater_than_whole ( so_called_type_platform_math_num_whole , so_called_type_platform_math_num_whole ) ;
    static int whole_greater_than_zero ( so_called_type_platform_math_num_whole ) ;
    static int whole_is_even ( so_called_type_platform_math_num_whole ) ;
    static int whole_is_false ( so_called_type_platform_math_num_whole ) ;
    static int whole_is_true ( so_called_type_platform_math_num_whole ) ;
    static int whole_is_zero ( so_called_type_platform_math_num_whole ) ;
    static int whole_less_or_equal_to_whole ( so_called_type_platform_math_num_whole , so_called_type_platform_math_num_whole ) ;
    static int whole_less_or_equal_to_zero ( so_called_type_platform_math_num_whole ) ;
    static int whole_less_than_whole ( so_called_type_platform_math_num_whole , so_called_type_platform_math_num_whole ) ;
    static int whole_less_than_zero ( so_called_type_platform_math_num_whole ) ;
    static int wholes_are_equal ( so_called_type_platform_math_num_whole , so_called_type_platform_math_num_whole ) ;
} ;

#endif

