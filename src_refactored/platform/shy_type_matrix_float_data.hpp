#include "shy_type_matrix_float_data.h"

shy_type_platform_matrix_float_data :: shy_type_platform_matrix_float_data ( )
{
    for ( int i = 0 ; i < 16 ; i ++ )
        _elements [ i ] = so_called_platform_consts_insider :: uninitialized_value ;
}

