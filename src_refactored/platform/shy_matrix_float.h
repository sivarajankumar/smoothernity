#ifndef _shy_platform_matrix_float_included
#define _shy_platform_matrix_float_included

class shy_platform_matrix_float_insider ;

class shy_platform_matrix_float
{
    typedef so_called_platform_math :: num_fract num_fract ;
    typedef so_called_platform_vector :: vector_data vector_data ;
public :
    class matrix_data
    {
        friend class shy_platform_matrix_float ;
        friend class shy_platform_matrix_float_insider ;
    public :
        matrix_data ( ) ;
    private :
        float _elements [ 16 ] ;
    } ;
public :
    static void set_axis_x ( matrix_data & , num_fract , num_fract , num_fract ) ;
    static void set_axis_y ( matrix_data & , num_fract , num_fract , num_fract ) ;
    static void set_axis_z ( matrix_data & , num_fract , num_fract , num_fract ) ;
    static void set_origin ( matrix_data & , num_fract , num_fract , num_fract ) ;
    static void set_axis_x ( matrix_data & , vector_data ) ;
    static void set_axis_y ( matrix_data & , vector_data ) ;
    static void set_axis_z ( matrix_data & , vector_data ) ;
    static void set_origin ( matrix_data & , vector_data ) ;
    static void get_axis_x ( vector_data & , const matrix_data & ) ;
    static void get_axis_y ( vector_data & , const matrix_data & ) ;
    static void get_axis_z ( vector_data & , const matrix_data & ) ;
    static void get_origin ( vector_data & , const matrix_data & ) ;
    static void identity ( matrix_data & ) ;
    static void inverse_rotation_translation ( matrix_data & ) ;
private :
    static void _swap_values ( float & , float & ) ;
} ;

#endif
