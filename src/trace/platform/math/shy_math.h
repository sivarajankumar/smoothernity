class shy_trace_platform_math
{
public :
    static void check_args_sin ( so_called_platform_math_num_fract_type ) ;
    static void check_args_cos ( so_called_platform_math_num_fract_type ) ;
    static void check_args_add_to_whole ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type ) ;
    static void check_args_sub_from_whole ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type ) ;
    static void check_args_sub_wholes ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type ) ;
    static void check_args_add_fracts ( so_called_platform_math_num_fract_type , so_called_platform_math_num_fract_type ) ;
    static void check_args_mul_fracts ( so_called_platform_math_num_fract_type , so_called_platform_math_num_fract_type ) ;
    static void check_args_mul_fract_by ( so_called_platform_math_num_fract_type , so_called_platform_math_num_fract_type ) ;
    static void check_args_make_num_fract
        ( so_called_platform_math_const_int_32_type numerator 
        , so_called_platform_math_const_int_32_type denominator 
        ) ;
    static void check_args_make_whole_from_fract ( so_called_platform_math_num_fract_type ) ;
    static void check_args_mod_wholes ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type ) ;
    static void check_num_fract_exceeds_range_int ( so_called_platform_math_num_fract_type , so_called_platform_math_const_int_32_type , so_called_platform_math_const_int_32_type ) ;
    static void check_num_fract_non_positive ( so_called_platform_math_num_fract_type ) ;
    static void check_num_fract_not_less_than_fract ( so_called_platform_math_num_fract_type , so_called_platform_math_num_fract_type ) ;
    static void check_num_fract_uninitialized ( so_called_platform_math_num_fract_type ) ;
    static void check_num_whole_exceeds_range_int ( so_called_platform_math_num_whole_type , so_called_platform_math_const_int_32_type , so_called_platform_math_const_int_32_type ) ;
    static void check_num_whole_negative ( so_called_platform_math_num_whole_type ) ;
    static void check_num_whole_non_positive ( so_called_platform_math_num_whole_type ) ;
    static void check_num_whole_uninitialized ( so_called_platform_math_num_whole_type ) ;
    static void check_division_num_fract_by_zero ( so_called_platform_math_num_fract_type , so_called_platform_math_num_fract_type ) ;
    static void check_division_num_whole_by_zero ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type ) ;
    static void check_division_const_int_32_by_zero ( so_called_platform_math_const_int_32_type , so_called_platform_math_const_int_32_type ) ;
} ;
