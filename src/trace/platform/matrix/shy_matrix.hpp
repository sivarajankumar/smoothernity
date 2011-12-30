namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_matrix" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_matrix :: check_data_uninitialized ( so_called_platform_matrix_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_matrix_insider :: data_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized matrix value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_matrix :: check_args_set_axis_x 
    ( so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( x ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( y ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( z ) ;
    }
}

void shy_trace_platform_matrix :: check_args_set_axis_y
    ( so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( x ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( y ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( z ) ;
    }
}

void shy_trace_platform_matrix :: check_args_set_axis_z
    ( so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( x ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( y ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( z ) ;
    }
}

void shy_trace_platform_matrix :: check_args_set_origin 
    ( so_called_platform_math_num_fract_type x
    , so_called_platform_math_num_fract_type y
    , so_called_platform_math_num_fract_type z
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_trace_platform_math :: check_num_fract_uninitialized ( x ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( y ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( z ) ;
    }
}

void shy_trace_platform_matrix :: check_args_set_axis_x ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( v ) ;
}

void shy_trace_platform_matrix :: check_args_set_axis_y ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( v ) ;
}

void shy_trace_platform_matrix :: check_args_set_axis_z ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( v ) ;
}

void shy_trace_platform_matrix :: check_args_set_origin ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
        so_called_trace_platform_vector :: check_data_uninitialized ( v ) ;
}

void shy_trace_platform_matrix :: check_args_get_axis_x ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( m ) ;
}

void shy_trace_platform_matrix :: check_args_get_axis_y ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( m ) ;
}

void shy_trace_platform_matrix :: check_args_get_axis_z ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( m ) ;
}

void shy_trace_platform_matrix :: check_args_get_origin ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( m ) ;
}

void shy_trace_platform_matrix :: check_args_inverse_rotation_translation ( so_called_platform_matrix_data_type m )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( m ) ;
}
