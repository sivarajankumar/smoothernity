#include "shy_conditions.h"

int shy_platform_conditions :: wholes_are_equal ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int == b_int ;
}

int shy_platform_conditions :: whole_is_true ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == int ( true ) ;
}

int shy_platform_conditions :: whole_is_false ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == false ;
}

int shy_platform_conditions :: whole_greater_than_zero ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int > 0 ;
}

int shy_platform_conditions :: whole_less_than_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int < b_int ;
}

int shy_platform_conditions :: whole_less_or_equal_to_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int <= b_int ;
}

int shy_platform_conditions :: whole_is_zero ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int == 0 ;
}

int shy_platform_conditions :: whole_is_even ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int % 2 == 0 ;
}

int shy_platform_conditions :: whole_less_or_equal_to_zero ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int <= 0 ;
}

int shy_platform_conditions :: whole_greater_or_equal_to_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int >= b_int ;
}

int shy_platform_conditions :: whole_less_than_zero ( num_whole num )
{
    int num_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( num_int , num ) ;
    return num_int < 0 ;
}

int shy_platform_conditions :: whole_greater_than_whole ( num_whole a , num_whole b )
{
    int a_int = 0 ;
    int b_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( a_int , a ) ;
    so_called_platform_math_insider :: num_whole_value_get ( b_int , b ) ;
    return a_int > b_int ;
}

int shy_platform_conditions :: fract_less_than_fract ( num_fract a , num_fract b )
{
    float a_float = 0 ;
    float b_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float < b_float ;
}

int shy_platform_conditions :: fract_greater_than_fract ( num_fract a , num_fract b )
{
    float a_float = 0 ;
    float b_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    return a_float > b_float ;
}
