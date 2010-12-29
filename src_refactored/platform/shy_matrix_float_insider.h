#ifndef _shy_platform_matrix_float_insider_included
#define _shy_platform_matrix_float_insider_included

class shy_platform_matrix_float_insider
{
    typedef so_called_platform_matrix :: matrix_data matrix_data ;
public :
    static void elements_ptr ( float * & , matrix_data & ) ;
    static void elements_ptr ( const float * & , const matrix_data & ) ;
} ;

#endif
