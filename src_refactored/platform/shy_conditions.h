#ifndef _shy_platform_conditions_included
#define _shy_platform_conditions_included

class shy_platform_conditions
{
    typedef so_called_platform_math :: num_fract num_fract ;
    typedef so_called_platform_math :: num_whole num_whole ;
    
public :
    static int fract_less_than_fract ( num_fract , num_fract ) ;
    static int whole_greater_or_equal_to_whole ( num_whole , num_whole ) ;
    static int fract_greater_than_fract ( num_fract , num_fract ) ;
    static int whole_greater_than_whole ( num_whole , num_whole ) ;
    static int whole_greater_than_zero ( num_whole ) ;
    static int whole_is_even ( num_whole ) ;
    static int whole_is_false ( num_whole ) ;
    static int whole_is_true ( num_whole ) ;
    static int whole_is_zero ( num_whole ) ;
    static int whole_less_or_equal_to_whole ( num_whole , num_whole ) ;
    static int whole_less_or_equal_to_zero ( num_whole ) ;
    static int whole_less_than_whole ( num_whole , num_whole ) ;
    static int whole_less_than_zero ( num_whole ) ;
    static int wholes_are_equal ( num_whole , num_whole ) ;
} ;

#endif

