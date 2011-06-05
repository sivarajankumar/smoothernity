class shy_platform_matrix_float
{
public :
    static void set_axis_x 
        ( so_called_type_platform_matrix_float_data & 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        ) ;
    static void set_axis_y 
        ( so_called_type_platform_matrix_float_data & 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        ) ;
    static void set_axis_z 
        ( so_called_type_platform_matrix_float_data & 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        ) ;
    static void set_origin 
        ( so_called_type_platform_matrix_float_data & 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        , so_called_type_platform_math_num_fract 
        ) ;
    static void set_axis_x ( so_called_type_platform_matrix_float_data & , so_called_type_platform_vector_data ) ;
    static void set_axis_y ( so_called_type_platform_matrix_float_data & , so_called_type_platform_vector_data ) ;
    static void set_axis_z ( so_called_type_platform_matrix_float_data & , so_called_type_platform_vector_data ) ;
    static void set_origin ( so_called_type_platform_matrix_float_data & , so_called_type_platform_vector_data ) ;
    static void get_axis_x ( so_called_type_platform_vector_data & , const so_called_type_platform_matrix_float_data & ) ;
    static void get_axis_y ( so_called_type_platform_vector_data & , const so_called_type_platform_matrix_float_data & ) ;
    static void get_axis_z ( so_called_type_platform_vector_data & , const so_called_type_platform_matrix_float_data & ) ;
    static void get_origin ( so_called_type_platform_vector_data & , const so_called_type_platform_matrix_float_data & ) ;
    static void identity ( so_called_type_platform_matrix_float_data & ) ;
    static void inverse_rotation_translation ( so_called_type_platform_matrix_float_data & ) ;
} ;
