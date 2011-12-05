namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "platform_vector" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_platform_vector :: check_data_uninitialized ( so_called_platform_vector_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_bool uninitialized = so_called_lib_std_false ;
        so_called_platform_vector_insider :: data_uninitialized ( uninitialized , value ) ;
        if ( uninitialized )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Uninitialized vector value." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_vector :: check_zero_length ( so_called_platform_vector_data_type value )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_lib_std_float x = 0 ;
        so_called_lib_std_float y = 0 ;
        so_called_lib_std_float z = 0 ;
        so_called_platform_vector_insider :: x_get ( x , value ) ;
        so_called_platform_vector_insider :: y_get ( y , value ) ;
        so_called_platform_vector_insider :: z_get ( z , value ) ;
        if ( x == so_called_lib_std_float ( 0 ) && y == so_called_lib_std_float ( 0 ) && z == so_called_lib_std_float ( 0 ) )
        {
            so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
            so_called_platform_trace :: trace_string_error ( "Error. Zero length vector." ) ;
            so_called_platform_trace :: trace_end ( ) ;
        }
    }
}

void shy_trace_platform_vector :: check_args_xyz 
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

void shy_trace_platform_vector :: check_args_dot_product 
    ( so_called_platform_vector_data_type v1
    , so_called_platform_vector_data_type v2
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v1 ) ;
        check_data_uninitialized ( v2 ) ;
    }
}

void shy_trace_platform_vector :: check_args_cross_product 
    ( so_called_platform_vector_data_type v1
    , so_called_platform_vector_data_type v2
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v1 ) ;
        check_data_uninitialized ( v2 ) ;
    }
}

void shy_trace_platform_vector :: check_args_add 
    ( so_called_platform_vector_data_type v1
    , so_called_platform_vector_data_type v2
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v1 ) ;
        check_data_uninitialized ( v2 ) ;
    }
}

void shy_trace_platform_vector :: check_args_add_to
    ( so_called_platform_vector_data_type v1
    , so_called_platform_vector_data_type v2
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v1 ) ;
        check_data_uninitialized ( v2 ) ;
    }
}

void shy_trace_platform_vector :: check_args_sub
    ( so_called_platform_vector_data_type v1
    , so_called_platform_vector_data_type v2
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v1 ) ;
        check_data_uninitialized ( v2 ) ;
    }
}

void shy_trace_platform_vector :: check_args_mul 
    ( so_called_platform_vector_data_type v
    , so_called_platform_math_num_fract_type f
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( f ) ;
    }
}

void shy_trace_platform_vector :: check_args_mul_by
    ( so_called_platform_vector_data_type v
    , so_called_platform_math_num_fract_type f
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v ) ;
        so_called_trace_platform_math :: check_num_fract_uninitialized ( f ) ;
    }
}

void shy_trace_platform_vector :: check_args_length ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
        check_data_uninitialized ( v ) ;
}

void shy_trace_platform_vector :: check_args_normalize ( so_called_platform_vector_data_type v )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        check_data_uninitialized ( v ) ;
        check_zero_length ( v ) ;
    }
}
