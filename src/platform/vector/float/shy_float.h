class shy_platform_vector_float
{
public :
    static void xyz 
        ( so_called_platform_vector_float_data_type & 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        , so_called_platform_math_num_fract_type 
        ) ;
    static void dot_product ( so_called_platform_math_num_fract_type & , so_called_platform_vector_float_data_type , so_called_platform_vector_float_data_type ) ;
    static void cross_product ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type , so_called_platform_vector_float_data_type ) ;
    static void add ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type , so_called_platform_vector_float_data_type ) ;
    static void add_to ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type ) ;
    static void sub ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type , so_called_platform_vector_float_data_type ) ;
    static void mul ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type , so_called_platform_math_num_fract_type ) ;
    static void mul_by ( so_called_platform_vector_float_data_type & , so_called_platform_math_num_fract_type ) ;
    static void length ( so_called_platform_math_num_fract_type & , so_called_platform_vector_float_data_type ) ;
    static void normalize ( so_called_platform_vector_float_data_type & , so_called_platform_vector_float_data_type ) ;
} ;
