inline int shy_win_platform :: condition_wholes_are_equal ( num_whole a , num_whole b )
{
    return a . _value == b . _value ;
}

inline int shy_win_platform :: condition_true ( num_whole num )
{
    return num . _value == true ;
}

inline int shy_win_platform :: condition_false ( num_whole num )
{
    return num . _value == false ;
}

inline int shy_win_platform :: condition_whole_greater_than_zero ( num_whole num )
{
    return num . _value > 0 ;
}

inline int shy_win_platform :: condition_whole_less_than_whole ( num_whole a , num_whole b )
{
    return a . _value < b . _value ;
}

inline int shy_win_platform :: condition_whole_less_or_equal_to_whole ( num_whole a , num_whole b )
{
    return a . _value <= b . _value ;
}

inline int shy_win_platform :: condition_whole_is_zero ( num_whole num )
{
    return num . _value == 0 ;
}

inline int shy_win_platform :: condition_whole_is_even ( num_whole num )
{
    return num . _value % 2 == 0 ;
}

inline int shy_win_platform :: condition_fract_less_than_fract ( num_fract a , num_fract b )
{
    return a . _value < b . _value ;
}

inline int shy_win_platform :: condition_whole_less_or_equal_to_zero ( num_whole a )
{
    return a . _value <= 0 ;
}

inline int shy_win_platform :: condition_fract_greater_than_fract ( num_fract a , num_fract b )
{
    return a . _value > b . _value ;
}

inline int shy_win_platform :: condition_whole_greater_or_equal_to_whole ( num_whole a , num_whole b )
{
    return a . _value >= b . _value ;
}

inline int shy_win_platform :: condition_whole_less_than_zero ( num_whole a )
{
    return a . _value < 0 ;
}

inline int shy_win_platform :: condition_whole_greater_than_whole ( num_whole a , num_whole b )
{
    return a . _value > b . _value ;
}
