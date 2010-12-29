#include "shy_matrix_float_insider.h"

void shy_platform_matrix_float_insider :: elements_ptr ( float * & result , matrix_data & matrix )
{
    result = matrix . _elements ;
}

void shy_platform_matrix_float_insider :: elements_ptr ( const float * & result , const matrix_data & matrix )
{
    result = matrix . _elements ;
}

