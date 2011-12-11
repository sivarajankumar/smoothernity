class shy_trace_platform_vector
{
public :
    static void check_args_xyz 
        ( so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_dot_product 
        ( so_called_platform_vector_data_type
        , so_called_platform_vector_data_type
        ) ;
    static void check_args_cross_product 
        ( so_called_platform_vector_data_type
        , so_called_platform_vector_data_type
        ) ;
    static void check_args_add 
        ( so_called_platform_vector_data_type
        , so_called_platform_vector_data_type
        ) ;
    static void check_args_add_to
        ( so_called_platform_vector_data_type
        , so_called_platform_vector_data_type
        ) ;
    static void check_args_sub 
        ( so_called_platform_vector_data_type
        , so_called_platform_vector_data_type
        ) ;
    static void check_args_mul 
        ( so_called_platform_vector_data_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_mul_by
        ( so_called_platform_vector_data_type
        , so_called_platform_math_num_fract_type
        ) ;
    static void check_args_length ( so_called_platform_vector_data_type ) ;
    static void check_args_normalize ( so_called_platform_vector_data_type ) ;

    static void check_data_uninitialized ( so_called_platform_vector_data_type ) ;
    static void check_zero_length ( so_called_platform_vector_data_type ) ;
} ;
