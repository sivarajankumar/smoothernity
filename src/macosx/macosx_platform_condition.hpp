inline int shy_macosx_platform :: condition_wholes_are_equal ( num_whole a , num_whole b )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a ) 
        == _platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_true ( num_whole num )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( num ) == true ;
}

inline int shy_macosx_platform :: condition_false ( num_whole num )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( num ) == false ;
}

inline int shy_macosx_platform :: condition_whole_greater_than_zero ( num_whole num )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( num ) > 0 ;
}

inline int shy_macosx_platform :: condition_whole_less_than_whole ( num_whole a , num_whole b )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a )
         < _platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_whole_less_or_equal_to_whole ( num_whole a , num_whole b )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a ) 
        <= _platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_whole_is_zero ( num_whole num )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( num ) == 0 ;
}

inline int shy_macosx_platform :: condition_whole_is_even ( num_whole num )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( num ) % 2 == 0 ;
}

inline int shy_macosx_platform :: condition_whole_less_or_equal_to_zero ( num_whole a )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a ) <= 0 ;
}

inline int shy_macosx_platform :: condition_whole_greater_or_equal_to_whole ( num_whole a , num_whole b )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a )
        >= _platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_whole_less_than_zero ( num_whole a )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a ) < 0 ;
}

inline int shy_macosx_platform :: condition_whole_greater_than_whole ( num_whole a , num_whole b )
{
    return _platform_math_insider :: num_whole_unsafe_value_get ( a ) 
         > _platform_math_insider :: num_whole_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_fract_less_than_fract ( num_fract a , num_fract b )
{
    return _platform_math_insider :: num_fract_unsafe_value_get ( a )
         < _platform_math_insider :: num_fract_unsafe_value_get ( b ) ;
}

inline int shy_macosx_platform :: condition_fract_greater_than_fract ( num_fract a , num_fract b )
{
    return _platform_math_insider :: num_fract_unsafe_value_get ( a ) 
         > _platform_math_insider :: num_fract_unsafe_value_get ( b ) ;
}
