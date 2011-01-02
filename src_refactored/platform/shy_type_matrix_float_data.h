#ifndef _shy_type_platform_matrix_float_data_included
#define _shy_type_platform_matrix_float_data_included

class shy_type_platform_matrix_float_data
{
    friend class shy_platform_matrix_float ;
    friend class shy_platform_matrix_float_insider ;
public :
    shy_type_platform_matrix_float_data ( ) ;
private :
    float _elements [ 16 ] ;
} ;

#endif
