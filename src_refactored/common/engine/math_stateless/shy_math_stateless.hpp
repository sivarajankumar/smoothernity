void shy_common_engine_math_stateless :: catmull_rom_spline
    ( so_called_type_platform_vector_data & result 
    , so_called_type_platform_math_num_fract t 
    , so_called_type_platform_vector_data p0 
    , so_called_type_platform_vector_data p1 
    , so_called_type_platform_vector_data p2 
    , so_called_type_platform_vector_data p3 
    )
{
    so_called_type_platform_math_num_fract t2 ;
    so_called_type_platform_math_num_fract t3 ;
    so_called_type_platform_math_num_fract t2_mul_2 ;
    so_called_type_platform_math_num_fract t2_mul_4 ;
    so_called_type_platform_math_num_fract t2_mul_5 ;
    so_called_type_platform_math_num_fract t3_mul_3 ;
    so_called_type_platform_math_num_fract p0_coeff ;
    so_called_type_platform_math_num_fract p1_coeff ;
    so_called_type_platform_math_num_fract p2_coeff ;
    so_called_type_platform_math_num_fract p3_coeff ;
    so_called_type_platform_math_num_fract half ;
    so_called_type_platform_math_num_fract fract_2 ;
    so_called_type_platform_math_num_fract fract_3 ;
    so_called_type_platform_math_num_fract fract_4 ;
    so_called_type_platform_math_num_fract fract_5 ;
    so_called_type_platform_vector_data p0_scaled ;
    so_called_type_platform_vector_data p1_scaled ;
    so_called_type_platform_vector_data p2_scaled ;
    so_called_type_platform_vector_data p3_scaled ;
    so_called_type_platform_vector_data result_p0_p1 ;
    so_called_type_platform_vector_data result_p2_p3 ;
    so_called_type_platform_vector_data result_p0_p1_p2_p3 ;
    so_called_platform_math :: make_num_fract ( half , 1 , 2 ) ;    
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_3 , 3 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_4 , 4 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_5 , 5 , 1 ) ;
    so_called_platform_math :: mul_fracts ( t2 , t , t ) ;
    so_called_platform_math :: mul_fracts ( t3 , t2 , t ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_2 , t2 , fract_2 ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_4 , t2 , fract_4 ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_5 , t2 , fract_5 ) ;
    so_called_platform_math :: mul_fracts ( t3_mul_3 , t3 , fract_3 ) ;
    so_called_platform_math :: sub_fracts ( p0_coeff , t2_mul_2 , t ) ;
    so_called_platform_math :: sub_from_fract ( p0_coeff , t3 ) ;
    so_called_platform_math :: sub_fracts ( p1_coeff , t3_mul_3 , t2_mul_5 ) ;
    so_called_platform_math :: add_to_fract ( p1_coeff , fract_2 ) ;
    so_called_platform_math :: sub_fracts ( p2_coeff , t2_mul_4 , t3_mul_3 ) ;
    so_called_platform_math :: add_to_fract ( p2_coeff , t ) ;
    so_called_platform_math :: sub_fracts ( p3_coeff , t3 , t2 ) ;
    so_called_platform_vector :: mul ( p0_scaled , p0 , p0_coeff ) ;
    so_called_platform_vector :: mul ( p1_scaled , p1 , p1_coeff ) ;
    so_called_platform_vector :: mul ( p2_scaled , p2 , p2_coeff ) ;
    so_called_platform_vector :: mul ( p3_scaled , p3 , p3_coeff ) ;
    so_called_platform_vector :: add ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    so_called_platform_vector :: add ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    so_called_platform_vector :: add ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    so_called_platform_vector :: mul ( result , result_p0_p1_p2_p3 , half ) ;
}

void shy_common_engine_math_stateless :: catmull_rom_spline
    ( so_called_type_platform_math_num_fract & result 
    , so_called_type_platform_math_num_fract t 
    , so_called_type_platform_math_num_fract p0 
    , so_called_type_platform_math_num_fract p1 
    , so_called_type_platform_math_num_fract p2 
    , so_called_type_platform_math_num_fract p3 
    )
{
    so_called_type_platform_math_num_fract t2 ;
    so_called_type_platform_math_num_fract t3 ;
    so_called_type_platform_math_num_fract t2_mul_2 ;
    so_called_type_platform_math_num_fract t2_mul_4 ;
    so_called_type_platform_math_num_fract t2_mul_5 ;
    so_called_type_platform_math_num_fract t3_mul_3 ;
    so_called_type_platform_math_num_fract p0_coeff ;
    so_called_type_platform_math_num_fract p1_coeff ;
    so_called_type_platform_math_num_fract p2_coeff ;
    so_called_type_platform_math_num_fract p3_coeff ;
    so_called_type_platform_math_num_fract half ;
    so_called_type_platform_math_num_fract fract_2 ;
    so_called_type_platform_math_num_fract fract_3 ;
    so_called_type_platform_math_num_fract fract_4 ;
    so_called_type_platform_math_num_fract fract_5 ;
    so_called_type_platform_math_num_fract p0_scaled ;
    so_called_type_platform_math_num_fract p1_scaled ;
    so_called_type_platform_math_num_fract p2_scaled ;
    so_called_type_platform_math_num_fract p3_scaled ;
    so_called_type_platform_math_num_fract result_p0_p1 ;
    so_called_type_platform_math_num_fract result_p2_p3 ;
    so_called_type_platform_math_num_fract result_p0_p1_p2_p3 ;
    so_called_platform_math :: make_num_fract ( half , 1 , 2 ) ;    
    so_called_platform_math :: make_num_fract ( fract_2 , 2 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_3 , 3 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_4 , 4 , 1 ) ;
    so_called_platform_math :: make_num_fract ( fract_5 , 5 , 1 ) ;
    so_called_platform_math :: mul_fracts ( t2 , t , t ) ;
    so_called_platform_math :: mul_fracts ( t3 , t2 , t ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_2 , t2 , fract_2 ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_4 , t2 , fract_4 ) ;
    so_called_platform_math :: mul_fracts ( t2_mul_5 , t2 , fract_5 ) ;
    so_called_platform_math :: mul_fracts ( t3_mul_3 , t3 , fract_3 ) ;
    so_called_platform_math :: sub_fracts ( p0_coeff , t2_mul_2 , t ) ;
    so_called_platform_math :: sub_from_fract ( p0_coeff , t3 ) ;
    so_called_platform_math :: sub_fracts ( p1_coeff , t3_mul_3 , t2_mul_5 ) ;
    so_called_platform_math :: add_to_fract ( p1_coeff , fract_2 ) ;
    so_called_platform_math :: sub_fracts ( p2_coeff , t2_mul_4 , t3_mul_3 ) ;
    so_called_platform_math :: add_to_fract ( p2_coeff , t ) ;
    so_called_platform_math :: sub_fracts ( p3_coeff , t3 , t2 ) ;
    so_called_platform_math :: mul_fracts ( p0_scaled , p0 , p0_coeff ) ;
    so_called_platform_math :: mul_fracts ( p1_scaled , p1 , p1_coeff ) ;
    so_called_platform_math :: mul_fracts ( p2_scaled , p2 , p2_coeff ) ;
    so_called_platform_math :: mul_fracts ( p3_scaled , p3 , p3_coeff ) ;
    so_called_platform_math :: add_fracts ( result_p0_p1 , p0_scaled , p1_scaled ) ;
    so_called_platform_math :: add_fracts ( result_p2_p3 , p2_scaled , p3_scaled ) ;
    so_called_platform_math :: add_fracts ( result_p0_p1_p2_p3 , result_p0_p1 , result_p2_p3 ) ;
    so_called_platform_math :: mul_fracts ( result , result_p0_p1_p2_p3 , half ) ;
}

void shy_common_engine_math_stateless :: lerp
    ( so_called_type_platform_math_num_fract & result_value
    , so_called_type_platform_math_num_fract weight
    , so_called_type_platform_math_num_fract from_value 
    , so_called_type_platform_math_num_fract from_weight 
    , so_called_type_platform_math_num_fract to_value 
    , so_called_type_platform_math_num_fract to_weight 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( weight , from_weight ) )
        result_value = from_value ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , to_weight ) )
    {
        so_called_type_platform_math_num_fract value_diff ;
        so_called_type_platform_math_num_fract weight_diff ;
        so_called_type_platform_math_num_fract current_diff ;
        so_called_platform_math :: sub_fracts ( value_diff , to_value , from_value ) ;
        so_called_platform_math :: sub_fracts ( weight_diff , to_weight , from_weight ) ;
        so_called_platform_math :: sub_fracts ( current_diff , weight , from_weight ) ;
        so_called_platform_math :: mul_fracts ( result_value , value_diff , current_diff ) ;
        so_called_platform_math :: div_fract_by ( result_value , weight_diff ) ;
        so_called_platform_math :: add_to_fract ( result_value , from_value ) ;
    }
    else
        result_value = to_value ;
}

void shy_common_engine_math_stateless :: hard_in_easy_out 
    ( so_called_type_platform_math_num_fract & result_value 
    , so_called_type_platform_math_num_fract weight 
    , so_called_type_platform_math_num_fract from_value 
    , so_called_type_platform_math_num_fract from_weight 
    , so_called_type_platform_math_num_fract to_value 
    , so_called_type_platform_math_num_fract to_weight 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( weight , from_weight ) )
        result_value = from_value ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , to_weight ) )
    {
        so_called_type_platform_math_num_fract p0 ;
        so_called_type_platform_math_num_fract p1 ;
        so_called_type_platform_math_num_fract p2 ;
        so_called_type_platform_math_num_fract p3 ;
        so_called_type_platform_math_num_fract delta_value ;
        so_called_type_platform_math_num_fract t ;
        so_called_type_platform_math_num_fract t0 ;
        so_called_type_platform_math_num_fract t1 ;
        so_called_platform_math :: make_num_fract ( t0 , 0 , 1 ) ;
        so_called_platform_math :: make_num_fract ( t1 , 1 , 1 ) ;
        so_called_platform_math :: sub_fracts ( delta_value , from_value , to_value ) ;
        lerp ( t , weight , t0 , from_weight , t1 , to_weight ) ;
        so_called_platform_math :: add_fracts ( p0 , from_value , delta_value ) ;
        p1 = from_value ;
        p2 = to_value ;
        p3 = p1 ;
        catmull_rom_spline ( result_value , t , p0 , p1 , p2 , p3 ) ;
    }
    else
        result_value = to_value ;
}

void shy_common_engine_math_stateless :: easy_in_easy_out 
    ( so_called_type_platform_math_num_fract & result_value 
    , so_called_type_platform_math_num_fract weight 
    , so_called_type_platform_math_num_fract from_value 
    , so_called_type_platform_math_num_fract from_weight 
    , so_called_type_platform_math_num_fract to_value 
    , so_called_type_platform_math_num_fract to_weight 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( weight , from_weight ) )
        result_value = from_value ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , to_weight ) )
    {
        so_called_type_platform_math_num_fract p0 ;
        so_called_type_platform_math_num_fract p1 ;
        so_called_type_platform_math_num_fract p2 ;
        so_called_type_platform_math_num_fract p3 ;
        so_called_type_platform_math_num_fract t ;
        so_called_type_platform_math_num_fract t0 ;
        so_called_type_platform_math_num_fract t1 ;
        so_called_platform_math :: make_num_fract ( t0 , 0 , 1 ) ;
        so_called_platform_math :: make_num_fract ( t1 , 1 , 1 ) ;
        lerp ( t , weight , t0 , from_weight , t1 , to_weight ) ;
        p1 = from_value ;
        p2 = to_value ;
        p0 = p2 ;
        p3 = p1 ;
        catmull_rom_spline ( result_value , t , p0 , p1 , p2 , p3 ) ;
    }
    else
        result_value = to_value ;
}

void shy_common_engine_math_stateless :: easy_in_hard_out
    ( so_called_type_platform_math_num_fract & result_value 
    , so_called_type_platform_math_num_fract weight 
    , so_called_type_platform_math_num_fract from_value 
    , so_called_type_platform_math_num_fract from_weight 
    , so_called_type_platform_math_num_fract to_value 
    , so_called_type_platform_math_num_fract to_weight 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( weight , from_weight ) )
        result_value = from_value ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , to_weight ) )
    {
        so_called_type_platform_math_num_fract p0 ;
        so_called_type_platform_math_num_fract p1 ;
        so_called_type_platform_math_num_fract p2 ;
        so_called_type_platform_math_num_fract p3 ;
        so_called_type_platform_math_num_fract delta_value ;
        so_called_type_platform_math_num_fract t ;
        so_called_type_platform_math_num_fract t0 ;
        so_called_type_platform_math_num_fract t1 ;
        so_called_platform_math :: make_num_fract ( t0 , 0 , 1 ) ;
        so_called_platform_math :: make_num_fract ( t1 , 1 , 1 ) ;
        so_called_platform_math :: sub_fracts ( delta_value , from_value , to_value ) ;
        lerp ( t , weight , t0 , from_weight , t1 , to_weight ) ;
        p1 = from_value ;
        p2 = to_value ;
        p0 = p2 ;
        so_called_platform_math :: sub_fracts ( p3 , to_value , delta_value ) ;
        catmull_rom_spline ( result_value , t , p0 , p1 , p2 , p3 ) ;
    }
    else
        result_value = to_value ;
}

void shy_common_engine_math_stateless :: hard_attack_easy_decay 
    ( so_called_type_platform_math_num_fract & result_value 
    , so_called_type_platform_math_num_fract weight 
    , so_called_type_platform_math_num_fract from_value 
    , so_called_type_platform_math_num_fract from_weight 
    , so_called_type_platform_math_num_fract mid_value
    , so_called_type_platform_math_num_fract mid_weight
    , so_called_type_platform_math_num_fract to_value
    , so_called_type_platform_math_num_fract to_weight
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( weight , from_weight ) )
        result_value = from_value ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , mid_weight ) )
        hard_in_easy_out ( result_value , weight , from_value , from_weight , mid_value , mid_weight ) ;
    else if ( so_called_platform_conditions :: fract_less_than_fract ( weight , to_weight ) )
        easy_in_easy_out ( result_value , weight , mid_value , mid_weight , to_value , to_weight ) ;
    else
        result_value = to_value ;
}

void shy_common_engine_math_stateless :: clamp_fract 
    ( so_called_type_platform_math_num_fract & result 
    , so_called_type_platform_math_num_fract num 
    , so_called_type_platform_math_num_fract from 
    , so_called_type_platform_math_num_fract to 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( num , from ) )
        result = from ;
    else if ( so_called_platform_conditions :: fract_greater_than_fract ( num , to ) )
        result = to ;
    else
        result = num ;
}

void shy_common_engine_math_stateless :: clamp_fract 
    ( so_called_type_platform_math_num_fract & num 
    , so_called_type_platform_math_num_fract from 
    , so_called_type_platform_math_num_fract to 
    )
{
    if ( so_called_platform_conditions :: fract_less_than_fract ( num , from ) )
        num = from ;
    else if ( so_called_platform_conditions :: fract_greater_than_fract ( num , to ) )
        num = to ;
}

void shy_common_engine_math_stateless :: min_whole 
    ( so_called_type_platform_math_num_whole & result 
    , so_called_type_platform_math_num_whole a 
    , so_called_type_platform_math_num_whole b 
    )
{
    if ( so_called_platform_conditions :: whole_less_than_whole ( a , b ) )
        result = a ;
    else
        result = b ;
}

void shy_common_engine_math_stateless :: max_whole 
    ( so_called_type_platform_math_num_whole & result 
    , so_called_type_platform_math_num_whole a 
    , so_called_type_platform_math_num_whole b 
    )
{
    if ( so_called_platform_conditions :: whole_greater_than_whole ( a , b ) )
        result = a ;
    else
        result = b ;
}
    
void shy_common_engine_math_stateless :: abs_whole ( so_called_type_platform_math_num_whole & result , so_called_type_platform_math_num_whole a )
{
    if ( so_called_platform_conditions :: whole_less_than_zero ( a ) )
        so_called_platform_math :: neg_whole ( result , a ) ;
    else
        result = a ;
}

void shy_common_engine_math_stateless :: rotation_z 
    ( so_called_type_platform_vector_data & axis_x 
    , so_called_type_platform_vector_data & axis_y 
    , so_called_type_platform_math_num_fract angle 
    )
{
    so_called_type_platform_math_num_fract rot_sin ;
    so_called_type_platform_math_num_fract rot_cos ;
    so_called_type_platform_math_num_fract axis_x_x ;
    so_called_type_platform_math_num_fract axis_x_y ;
    so_called_type_platform_math_num_fract axis_x_z ;
    so_called_type_platform_math_num_fract axis_y_x ;
    so_called_type_platform_math_num_fract axis_y_y ;
    so_called_type_platform_math_num_fract axis_y_z ;

    so_called_platform_math :: sin ( rot_sin , angle ) ;
    so_called_platform_math :: cos ( rot_cos , angle ) ;

    axis_x_x = rot_cos ;
    axis_x_y = rot_sin ;
    so_called_platform_math :: make_num_fract ( axis_x_z , 0 , 1 ) ;

    so_called_platform_math :: neg_fract ( axis_y_x , rot_sin ) ;
    axis_y_y = rot_cos ;
    so_called_platform_math :: make_num_fract ( axis_y_z , 0 , 1 ) ;

    so_called_platform_vector :: xyz ( axis_x , axis_x_x , axis_x_y , axis_x_z ) ;
    so_called_platform_vector :: xyz ( axis_y , axis_y_x , axis_y_y , axis_y_z ) ;
}

void shy_common_engine_math_stateless :: scale ( so_called_type_platform_matrix_data & matrix , so_called_type_platform_math_num_fract scale )
{
    so_called_type_platform_math_num_fract zero ;
    so_called_platform_math :: make_num_fract ( zero , 0 , 1 ) ;
    so_called_platform_matrix :: identity ( matrix ) ;
    so_called_platform_matrix :: set_axis_x ( matrix , scale , zero , zero ) ;
    so_called_platform_matrix :: set_axis_y ( matrix , zero , scale , zero ) ;
    so_called_platform_matrix :: set_axis_z ( matrix , zero , zero , scale ) ;
}

