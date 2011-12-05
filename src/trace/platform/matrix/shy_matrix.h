class shy_trace_platform_matrix
{
public :
    static void check_args_set_axis_x 
        ( so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_set_axis_y 
        ( so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_set_axis_z
        ( so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_set_origin
        ( so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_set_axis_x ( so_called_platform_vector_data_type ) ;
    static void check_args_set_axis_y ( so_called_platform_vector_data_type ) ;
    static void check_args_set_axis_z ( so_called_platform_vector_data_type ) ;
    static void check_args_set_origin ( so_called_platform_vector_data_type ) ;
    static void check_args_get_axis_x ( so_called_platform_matrix_data_type ) ;
    static void check_args_get_axis_y ( so_called_platform_matrix_data_type ) ;
    static void check_args_get_axis_z ( so_called_platform_matrix_data_type ) ;
    static void check_args_get_origin ( so_called_platform_matrix_data_type ) ;
    static void check_args_inverse_rotation_translation ( so_called_platform_matrix_data_type ) ;

    static void check_data_uninitialized ( so_called_platform_matrix_data_type ) ;
} ;
