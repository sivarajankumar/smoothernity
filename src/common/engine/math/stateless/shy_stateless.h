class shy_common_engine_math_stateless
{
public :
    static void catmull_rom_spline 
        ( so_called_type_platform_vector_data & result 
        , so_called_type_platform_math_num_fract t 
        , so_called_type_platform_vector_data p0 
        , so_called_type_platform_vector_data p1 
        , so_called_type_platform_vector_data p2 
        , so_called_type_platform_vector_data p3 
        ) ;
    static void catmull_rom_spline 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract t 
        , so_called_type_platform_math_num_fract p0 
        , so_called_type_platform_math_num_fract p1 
        , so_called_type_platform_math_num_fract p2 
        , so_called_type_platform_math_num_fract p3 
        ) ;
    static void lerp 
        ( so_called_type_platform_math_num_fract & result_value 
        , so_called_type_platform_math_num_fract weight 
        , so_called_type_platform_math_num_fract from_value 
        , so_called_type_platform_math_num_fract from_weight 
        , so_called_type_platform_math_num_fract to_value 
        , so_called_type_platform_math_num_fract to_weight 
        ) ;
    static void easy_in_easy_out 
        ( so_called_type_platform_math_num_fract & result_value 
        , so_called_type_platform_math_num_fract weight 
        , so_called_type_platform_math_num_fract from_value 
        , so_called_type_platform_math_num_fract from_weight 
        , so_called_type_platform_math_num_fract to_value 
        , so_called_type_platform_math_num_fract to_weight 
        ) ;
    static void easy_in_hard_out 
        ( so_called_type_platform_math_num_fract & result_value 
        , so_called_type_platform_math_num_fract weight 
        , so_called_type_platform_math_num_fract from_value 
        , so_called_type_platform_math_num_fract from_weight 
        , so_called_type_platform_math_num_fract to_value 
        , so_called_type_platform_math_num_fract to_weight 
        ) ;
    static void hard_in_easy_out 
        ( so_called_type_platform_math_num_fract & result_value 
        , so_called_type_platform_math_num_fract weight 
        , so_called_type_platform_math_num_fract from_value 
        , so_called_type_platform_math_num_fract from_weight 
        , so_called_type_platform_math_num_fract to_value 
        , so_called_type_platform_math_num_fract to_weight 
        ) ;
    static void hard_attack_easy_decay 
        ( so_called_type_platform_math_num_fract & result_value 
        , so_called_type_platform_math_num_fract weight 
        , so_called_type_platform_math_num_fract from_value 
        , so_called_type_platform_math_num_fract from_weight 
        , so_called_type_platform_math_num_fract mid_value
        , so_called_type_platform_math_num_fract mid_weight
        , so_called_type_platform_math_num_fract to_value
        , so_called_type_platform_math_num_fract to_weight
        ) ;
    static void clamp_fract 
        ( so_called_type_platform_math_num_fract & result 
        , so_called_type_platform_math_num_fract num 
        , so_called_type_platform_math_num_fract from 
        , so_called_type_platform_math_num_fract to 
        ) ;
    static void clamp_fract 
        ( so_called_type_platform_math_num_fract & num 
        , so_called_type_platform_math_num_fract from 
        , so_called_type_platform_math_num_fract to 
        ) ;
    static void clamp_whole
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole num 
        , so_called_type_platform_math_num_whole from 
        , so_called_type_platform_math_num_whole to 
        ) ;
    static void min_whole 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void max_whole 
        ( so_called_type_platform_math_num_whole & result 
        , so_called_type_platform_math_num_whole a 
        , so_called_type_platform_math_num_whole b 
        ) ;
    static void rotation_z 
        ( so_called_type_platform_vector_data & axis_x 
        , so_called_type_platform_vector_data & axis_y 
        , so_called_type_platform_math_num_fract angle 
        ) ;
    static void abs_whole ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole a ) ;
    static void scale ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_math_num_fract scale ) ;
} ;
