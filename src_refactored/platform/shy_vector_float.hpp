#include "shy_vector_float.h"
#include <math.h>

void shy_platform_vector_float :: xyz 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( result . _x , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( result . _y , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( result . _z , z ) ;
}

void shy_platform_vector_float :: dot_product 
    ( so_called_type_platform_math_num_fract & result 
    , so_called_type_platform_vector_data v1 
    , so_called_type_platform_vector_data v2 
    )
{
    so_called_platform_math_insider :: num_fract_value_set 
        ( result
        , v1 . _x * v2 . _x
        + v1 . _y * v2 . _y
        + v1 . _z * v2 . _z
        ) ;
}

void shy_platform_vector_float :: cross_product 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_vector_data v1 
    , so_called_type_platform_vector_data v2 
    )
{
    result . _x = v1 . _y * v2 . _z - v2 . _y * v1 . _z ;
    result . _y = v1 . _z * v2 . _x - v2 . _z * v1 . _x ;
    result . _z = v1 . _x * v2 . _y - v2 . _x * v1 . _y ;
}

void shy_platform_vector_float :: add 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_vector_data v1 
    , so_called_type_platform_vector_data v2 
    )
{
    result . _x = v1 . _x + v2 . _x ;
    result . _y = v1 . _y + v2 . _y ;
    result . _z = v1 . _z + v2 . _z ;
}

void shy_platform_vector_float :: add_to 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_vector_data v 
    )
{
    result . _x += v . _x ;
    result . _y += v . _y ;
    result . _z += v . _z ;
}

void shy_platform_vector_float :: sub 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_vector_data v1 
    , so_called_type_platform_vector_data v2 
    )
{
    result . _x = v1 . _x - v2 . _x ;
    result . _y = v1 . _y - v2 . _y ;
    result . _z = v1 . _z - v2 . _z ;
}

void shy_platform_vector_float :: mul 
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_vector_data v 
    , so_called_type_platform_math_num_fract f 
    )
{
    float f_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    result . _x = f_float * v . _x ;
    result . _y = f_float * v . _y ;
    result . _z = f_float * v . _z ;
}

void shy_platform_vector_float :: mul_by ( so_called_type_platform_vector_data & v , so_called_type_platform_math_num_fract f )
{
    float f_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( f_float , f ) ;
    v . _x *= f_float ;
    v . _y *= f_float ;
    v . _z *= f_float ;
}

void shy_platform_vector_float :: length ( so_called_type_platform_math_num_fract & result , so_called_type_platform_vector_data v )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ) ;
}

void shy_platform_vector_float :: normalize ( so_called_type_platform_vector_data & result , so_called_type_platform_vector_data v )
{
    float inv_length = 1.0f / float ( sqrt ( v . _x * v . _x + v . _y * v . _y + v . _z * v . _z ) ) ;
    result . _x = inv_length * v . _x ;
    result . _y = inv_length * v . _y ;
    result . _z = inv_length * v . _z ;
}

