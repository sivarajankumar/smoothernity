#include "shy_vector_float.h"
#include <math.h>

shy_platform_vector_float :: vector_data :: vector_data ( )
: _x ( ( float ) so_called_platform_consts_insider :: uninitialized_value )
, _y ( ( float ) so_called_platform_consts_insider :: uninitialized_value )
, _z ( ( float ) so_called_platform_consts_insider :: uninitialized_value )
{
}

void shy_platform_vector_float :: xyz ( vector_data & result , num_fract x , num_fract y , num_fract z )
{
    so_called_platform_math_insider :: num_fract_value_get ( result . _x , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( result . _y , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( result . _z , z ) ;
}

void shy_platform_vector_float :: dot_product ( num_fract & result , vector_data v1 , vector_data v2 )
{
    so_called_platform_math_insider :: num_fract_value_set 
        ( result
        , v1 . _x * v2 . _x
        + v1 . _y * v2 . _y
        + v1 . _z * v2 . _z
        ) ;
}

void shy_platform_vector_float :: cross_product ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
}

void shy_platform_vector_float :: add ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
}

void shy_platform_vector_float :: add_to ( vector_data & result , vector_data v )
{
    result . _x += v . _x ;
    result . _y += v . _y ;
    result . _z += v . _z ;
}

void shy_platform_vector_float :: sub ( vector_data & result , vector_data v1 , vector_data v2 )
{
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
}

void shy_platform_vector_float :: mul ( vector_data & result , vector_data v , num_fract f )
{
    float f_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    result . _x = f_float * v . _x ;
    result . _y = f_float * v . _y ;
    result . _z = f_float * v . _z ;
}

void shy_platform_vector_float :: mul_by ( vector_data & v , num_fract f )
{
    float f_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    v . _x *= f_float ;
    v . _y *= f_float ;
    v . _z *= f_float ;
}

void shy_platform_vector_float :: length ( num_fract & result , vector_data v )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

void shy_platform_vector_float :: normalize ( vector_data & result , vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}

