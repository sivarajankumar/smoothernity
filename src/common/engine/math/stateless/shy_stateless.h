class shy_common_engine_math_stateless
{
public :
    static void catmull_rom_spline 
        ( so_called_platform_vector_data_type & result 
        , so_called_platform_math_num_fract_type t 
        , so_called_platform_vector_data_type p0 
        , so_called_platform_vector_data_type p1 
        , so_called_platform_vector_data_type p2 
        , so_called_platform_vector_data_type p3 
        ) ;
    static void catmull_rom_spline 
        ( so_called_platform_math_num_fract_type & result 
        , so_called_platform_math_num_fract_type t 
        , so_called_platform_math_num_fract_type p0 
        , so_called_platform_math_num_fract_type p1 
        , so_called_platform_math_num_fract_type p2 
        , so_called_platform_math_num_fract_type p3 
        ) ;
    static void lerp 
        ( so_called_platform_math_num_fract_type & result_value 
        , so_called_platform_math_num_fract_type weight 
        , so_called_platform_math_num_fract_type from_value 
        , so_called_platform_math_num_fract_type from_weight 
        , so_called_platform_math_num_fract_type to_value 
        , so_called_platform_math_num_fract_type to_weight 
        ) ;
    static void easy_in_easy_out 
        ( so_called_platform_math_num_fract_type & result_value 
        , so_called_platform_math_num_fract_type weight 
        , so_called_platform_math_num_fract_type from_value 
        , so_called_platform_math_num_fract_type from_weight 
        , so_called_platform_math_num_fract_type to_value 
        , so_called_platform_math_num_fract_type to_weight 
        ) ;
    static void easy_in_hard_out 
        ( so_called_platform_math_num_fract_type & result_value 
        , so_called_platform_math_num_fract_type weight 
        , so_called_platform_math_num_fract_type from_value 
        , so_called_platform_math_num_fract_type from_weight 
        , so_called_platform_math_num_fract_type to_value 
        , so_called_platform_math_num_fract_type to_weight 
        ) ;
    static void hard_in_easy_out 
        ( so_called_platform_math_num_fract_type & result_value 
        , so_called_platform_math_num_fract_type weight 
        , so_called_platform_math_num_fract_type from_value 
        , so_called_platform_math_num_fract_type from_weight 
        , so_called_platform_math_num_fract_type to_value 
        , so_called_platform_math_num_fract_type to_weight 
        ) ;
    static void hard_attack_easy_decay 
        ( so_called_platform_math_num_fract_type & result_value 
        , so_called_platform_math_num_fract_type weight 
        , so_called_platform_math_num_fract_type from_value 
        , so_called_platform_math_num_fract_type from_weight 
        , so_called_platform_math_num_fract_type mid_value
        , so_called_platform_math_num_fract_type mid_weight
        , so_called_platform_math_num_fract_type to_value
        , so_called_platform_math_num_fract_type to_weight
        ) ;
    static void clamp_fract 
        ( so_called_platform_math_num_fract_type & result 
        , so_called_platform_math_num_fract_type num 
        , so_called_platform_math_num_fract_type from 
        , so_called_platform_math_num_fract_type to 
        ) ;
    static void clamp_fract 
        ( so_called_platform_math_num_fract_type & num 
        , so_called_platform_math_num_fract_type from 
        , so_called_platform_math_num_fract_type to 
        ) ;
    static void clamp_whole
        ( so_called_platform_math_num_whole_type & result 
        , so_called_platform_math_num_whole_type num 
        , so_called_platform_math_num_whole_type from 
        , so_called_platform_math_num_whole_type to 
        ) ;
    static void min_fract
        ( so_called_platform_math_num_fract_type & result 
        , so_called_platform_math_num_fract_type a 
        , so_called_platform_math_num_fract_type b 
        ) ;
    static void min_whole 
        ( so_called_platform_math_num_whole_type & result 
        , so_called_platform_math_num_whole_type a 
        , so_called_platform_math_num_whole_type b 
        ) ;
    static void max_fract
        ( so_called_platform_math_num_fract_type & result 
        , so_called_platform_math_num_fract_type a 
        , so_called_platform_math_num_fract_type b 
        ) ;
    static void max_whole 
        ( so_called_platform_math_num_whole_type & result 
        , so_called_platform_math_num_whole_type a 
        , so_called_platform_math_num_whole_type b 
        ) ;
    static void rotation_z 
        ( so_called_platform_vector_data_type & axis_x 
        , so_called_platform_vector_data_type & axis_y 
        , so_called_platform_math_num_fract_type angle 
        ) ;
    static void abs_whole ( so_called_platform_math_num_whole_type & result , so_called_platform_math_num_whole_type a ) ;
    static void scale ( so_called_platform_matrix_data_type & matrix , so_called_platform_math_num_fract_type scale ) ;
    static void scale_rotation_z
        ( so_called_platform_matrix_data_type & matrix
        , so_called_platform_math_num_fract_type scale
        , so_called_platform_math_num_fract_type angle
        ) ;
    static void add_frame_to_time ( so_called_platform_math_num_fract_type & ) ;
    static void make_radians_from_periods ( so_called_platform_math_num_fract_type & , so_called_platform_math_num_fract_type ) ;
    static void make_cartesian_from_polar 
        ( so_called_platform_vector_data_type & result
        , so_called_platform_math_num_fract_type radius
        , so_called_platform_math_num_fract_type angle
        ) ;
    static void shift
        ( so_called_platform_math_num_fract_type & result
        , so_called_platform_math_num_fract_type value
        , so_called_platform_math_num_fract_type shifter
        , so_called_platform_math_num_whole_type times
        ) ;
} ;
