class shy_platform_matrix_float
{
public :
    static void set_axis_x 
        ( so_called_platform_matrix_float_data_type & 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        ) ;
    static void set_axis_y 
        ( so_called_platform_matrix_float_data_type & 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        ) ;
    static void set_axis_z 
        ( so_called_platform_matrix_float_data_type & 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        ) ;
    static void set_origin 
        ( so_called_platform_matrix_float_data_type & 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        ) ;
    static void set_axis_x ( so_called_platform_matrix_float_data_type & , so_called_platform_vector_data_type ) ;
    static void set_axis_y ( so_called_platform_matrix_float_data_type & , so_called_platform_vector_data_type ) ;
    static void set_axis_z ( so_called_platform_matrix_float_data_type & , so_called_platform_vector_data_type ) ;
    static void set_origin ( so_called_platform_matrix_float_data_type & , so_called_platform_vector_data_type ) ;
    static void get_axis_x ( so_called_platform_vector_data_type & , const so_called_platform_matrix_float_data_type & ) ;
    static void get_axis_y ( so_called_platform_vector_data_type & , const so_called_platform_matrix_float_data_type & ) ;
    static void get_axis_z ( so_called_platform_vector_data_type & , const so_called_platform_matrix_float_data_type & ) ;
    static void get_origin ( so_called_platform_vector_data_type & , const so_called_platform_matrix_float_data_type & ) ;
    static void identity ( so_called_platform_matrix_float_data_type & ) ;
    static void inverse_rotation_translation ( so_called_platform_matrix_float_data_type & ) ;
} ;
