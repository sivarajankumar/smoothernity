#include "shy_vector_float_insider.h"

void shy_platform_vector_float_insider :: x_get ( float & x , vector_data v )
{
    x = v . _x ;
}

void shy_platform_vector_float_insider :: y_get ( float & y , vector_data v )
{
    y = v . _y ;
}

void shy_platform_vector_float_insider :: z_get ( float & z , vector_data v )
{
    z = v . _z ;
}

void shy_platform_vector_float_insider :: x_set ( vector_data & v , float x )
{
    v . _x = x ;
}

void shy_platform_vector_float_insider :: y_set ( vector_data & v , float y )
{
    v . _y = y ;
}

void shy_platform_vector_float_insider :: z_set ( vector_data & v , float z )
{
    v . _z = z ;
}

