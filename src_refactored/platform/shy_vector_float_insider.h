#ifndef _shy_platform_vector_float_insider_included
#define _shy_platform_vector_float_insider_included

class shy_platform_vector_float_insider
{
    typedef so_called_platform_vector :: vector_data vector_data ;
public :
    static void x_get ( float & , vector_data ) ;
    static void y_get ( float & , vector_data ) ;
    static void z_get ( float & , vector_data ) ;
    static void x_set ( vector_data & , float ) ;
    static void y_set ( vector_data & , float ) ;
    static void z_set ( vector_data & , float ) ;
} ;

#endif
