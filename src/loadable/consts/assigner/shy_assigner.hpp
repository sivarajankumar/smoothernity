namespace shy_guts
{
    static so_called_lib_std_bool error = so_called_lib_std_false ;

    static void assign_module 
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        ) ;
    static void assign_module_value_fract 
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        ) ;
    static void assign_module_value_fract_clamped
        ( so_called_loadable_consts_content_module_container_type :: const_iterator
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        , so_called_lib_std_int32_t
        , so_called_lib_std_int32_t
        ) ;
    static void assign_module_value_fract_max
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        ) ;
    static void assign_module_value_fract_min
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        ) ;
    static void assign_module_value_whole 
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        ) ;
    static void assign_module_value_whole_clamped
        ( so_called_loadable_consts_content_module_container_type :: const_iterator
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        , so_called_lib_std_int32_t
        ) ;
    static void assign_module_value_whole_max
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        ) ;
    static void assign_module_value_whole_min
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        ) ;
    static void check_module_value_fract_max
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        ) ;
    static void check_module_value_fract_min
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_fract_container_type :: const_iterator
        ) ;
    static void check_module_value_whole_max
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        ) ;
    static void check_module_value_whole_min
        ( so_called_loadable_consts_content_module_container_type :: const_iterator 
        , so_called_loadable_consts_content_value_whole_container_type :: const_iterator
        ) ;
}

void shy_guts :: assign_module 
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    )
{
    const so_called_loadable_consts_content_module_type & module = module_i -> second ;
    for ( so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i = module . name_to_whole . begin ( )
        ; whole_i != module . name_to_whole . end ( )
        ; ++ whole_i
        )
    {
        shy_guts :: assign_module_value_whole ( module_i , whole_i ) ;
    }
    for ( so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i = module . name_to_fract . begin ( )
        ; fract_i != module . name_to_fract . end ( )
        ; ++ fract_i
        )
    {
        shy_guts :: assign_module_value_fract ( module_i , fract_i ) ;
    }
}

void shy_guts :: check_module_value_fract_min
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    )
{
    if ( ! fract_i -> second . min_set )
    {
        so_called_trace 
            ( so_called_trace_loadable_consts_assigner :: no_min_for_module_attribute_fract_error 
                ( module_i -> first . c_str ( ) 
                , fract_i -> first . c_str ( ) 
                ) 
            ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
}

void shy_guts :: check_module_value_fract_max
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    )
{
    if ( ! fract_i -> second . max_set )
    {
        so_called_trace 
            ( so_called_trace_loadable_consts_assigner :: no_max_for_module_attribute_fract_error 
                ( module_i -> first . c_str ( ) 
                , fract_i -> first . c_str ( ) 
                ) 
            ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
}

void shy_guts :: check_module_value_whole_min
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    )
{
    if ( ! whole_i -> second . min_set )
    {
        so_called_trace 
            ( so_called_trace_loadable_consts_assigner :: no_min_for_module_attribute_whole_error 
                ( module_i -> first . c_str ( ) 
                , whole_i -> first . c_str ( ) 
                ) 
            ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
}

void shy_guts :: check_module_value_whole_max
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    )
{
    if ( ! whole_i -> second . max_set )
    {
        so_called_trace 
            ( so_called_trace_loadable_consts_assigner :: no_max_for_module_attribute_whole_error 
                ( module_i -> first . c_str ( ) 
                , whole_i -> first . c_str ( ) 
                ) 
            ) ;
        shy_guts :: error = so_called_lib_std_true ;
    }
}

void shy_guts :: assign_module_value_fract_min
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    )
{
    so_called_trace 
        ( so_called_trace_loadable_consts_assigner :: min_limit_used_as_module_attribute_fract_value
            ( fract_i -> second . min_numerator
            , fract_i -> second . min_denominator
            , module_i -> first . c_str ( ) 
            , fract_i -> first . c_str ( ) 
            ) 
        ) ;
    so_called_platform_math :: make_num_fract ( * fract_i -> second . binding , fract_i -> second . min_numerator , fract_i -> second . min_denominator ) ;
}

void shy_guts :: assign_module_value_fract_max
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    )
{
    so_called_trace 
        ( so_called_trace_loadable_consts_assigner :: max_limit_used_as_module_attribute_fract_value
            ( fract_i -> second . max_numerator
            , fract_i -> second . max_denominator
            , module_i -> first . c_str ( ) 
            , fract_i -> first . c_str ( ) 
            ) 
        ) ;
    so_called_platform_math :: make_num_fract ( * fract_i -> second . binding , fract_i -> second . max_numerator , fract_i -> second . max_denominator ) ;
}

void shy_guts :: assign_module_value_whole_min
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    )
{
    so_called_trace 
        ( so_called_trace_loadable_consts_assigner :: min_limit_used_as_module_attribute_whole_value
            ( whole_i -> second . min_value
            , module_i -> first . c_str ( ) 
            , whole_i -> first . c_str ( ) 
            ) 
        ) ;
    so_called_platform_math :: make_num_whole ( * whole_i -> second . binding , whole_i -> second . min_value ) ;
}

void shy_guts :: assign_module_value_whole_max
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    )
{
    so_called_trace 
        ( so_called_trace_loadable_consts_assigner :: max_limit_used_as_module_attribute_whole_value
            ( whole_i -> second . max_value
            , module_i -> first . c_str ( ) 
            , whole_i -> first . c_str ( ) 
            ) 
        ) ;
    so_called_platform_math :: make_num_whole ( * whole_i -> second . binding , whole_i -> second . max_value ) ;
}

void shy_guts :: assign_module_value_fract 
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    )
{
    so_called_lib_std_string module_name = module_i -> first ;
    so_called_lib_std_string fract_name = fract_i -> first ;
    const so_called_loadable_consts_content_value_fract_type & fract = fract_i -> second ;

    shy_guts :: check_module_value_fract_min ( module_i , fract_i ) ;
    shy_guts :: check_module_value_fract_max ( module_i , fract_i ) ;

    so_called_lib_std_string string_numerator = fract . numerator_sign + fract . numerator_value ;
    so_called_lib_std_string string_denominator = fract . denominator_sign + fract . denominator_value ;
    if ( string_numerator . empty ( ) || string_denominator . empty ( ) )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace ( so_called_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_fract_error ( module_name . c_str ( ) , fract_name . c_str ( ) ) ) ;
        if ( fract . min_set )
            shy_guts :: assign_module_value_fract_min ( module_i , fract_i ) ;
    }
    else
    {
        so_called_lib_std_int32_t int_numerator = 0 ;
        so_called_lib_std_int32_t int_denominator = 0 ;
        so_called_lib_std_istringstream ( string_numerator ) >> int_numerator ;
        so_called_lib_std_istringstream ( string_denominator ) >> int_denominator ;
        if ( int_denominator == 0 )
        {
            shy_guts :: error = so_called_lib_std_true ;
            so_called_trace ( so_called_trace_loadable_consts_assigner :: zero_denominator_error ( module_name . c_str ( ) , fract_name . c_str ( ) ) ) ;
            if ( fract . min_set )
                shy_guts :: assign_module_value_fract_min ( module_i , fract_i ) ;
        }
        else
            shy_guts :: assign_module_value_fract_clamped ( module_i , fract_i , int_numerator , int_denominator ) ;
    }
}

void shy_guts :: assign_module_value_fract_clamped
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_fract_container_type :: const_iterator fract_i
    , so_called_lib_std_int32_t value_numerator
    , so_called_lib_std_int32_t value_denominator
    )
{
    so_called_lib_std_string module_name = module_i -> first ;
    so_called_lib_std_string fract_name = fract_i -> first ;
    const so_called_loadable_consts_content_value_fract_type & fract = fract_i -> second ;

    if ( fract . min_set && value_numerator * fract . min_denominator < fract . min_numerator * value_denominator )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace
            ( so_called_trace_loadable_consts_assigner :: module_attribute_fract_value_less_than_min_error
                ( module_name . c_str ( )
                , fract_name . c_str ( )
                , value_numerator
                , value_denominator
                , fract . min_numerator
                , fract . min_denominator
                )
            ) ;
        shy_guts :: assign_module_value_fract_min ( module_i , fract_i ) ;
    }
    else if ( fract . max_set && value_numerator * fract . max_denominator > fract . max_numerator * value_denominator )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace
            ( so_called_trace_loadable_consts_assigner :: module_attribute_fract_value_greater_than_max_error
                ( module_name . c_str ( )
                , fract_name . c_str ( )
                , value_numerator
                , value_denominator
                , fract . max_numerator
                , fract . max_denominator
                )
            ) ;
        shy_guts :: assign_module_value_fract_max ( module_i , fract_i ) ;
    }
    else
        so_called_platform_math :: make_num_fract ( * fract . binding , value_numerator , value_denominator ) ;
}

void shy_guts :: assign_module_value_whole_clamped
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    , so_called_lib_std_int32_t value
    )
{
    so_called_lib_std_string module_name = module_i -> first ;
    so_called_lib_std_string whole_name = whole_i -> first ;
    const so_called_loadable_consts_content_value_whole_type & whole = whole_i -> second ;

    if ( whole . min_set && value < whole . min_value )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace
            ( so_called_trace_loadable_consts_assigner :: module_attribute_whole_value_less_than_min_error
                ( module_name . c_str ( )
                , whole_name . c_str ( )
                , value
                , whole . min_value
                )
            ) ;
        shy_guts :: assign_module_value_whole_min ( module_i , whole_i ) ;
    }
    else if ( whole . max_set && value > whole . max_value )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace
            ( so_called_trace_loadable_consts_assigner :: module_attribute_whole_value_greater_than_max_error
                ( module_name . c_str ( )
                , whole_name . c_str ( )
                , value
                , whole . max_value
                )
            ) ;
        shy_guts :: assign_module_value_whole_max ( module_i , whole_i ) ;
    }
    else
        so_called_platform_math :: make_num_whole ( * whole . binding , value ) ;
}

void shy_guts :: assign_module_value_whole 
    ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i
    , so_called_loadable_consts_content_value_whole_container_type :: const_iterator whole_i
    )
{
    so_called_lib_std_string module_name = module_i -> first ;
    so_called_lib_std_string whole_name = whole_i -> first ;
    const so_called_loadable_consts_content_value_whole_type & whole = whole_i -> second ;
    
    shy_guts :: check_module_value_whole_min ( module_i , whole_i ) ;
    shy_guts :: check_module_value_whole_max ( module_i , whole_i ) ;

    so_called_lib_std_string string_value = whole . sign + whole . value ;
    if ( string_value . empty ( ) )
    {
        shy_guts :: error = so_called_lib_std_true ;
        so_called_trace ( so_called_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_whole_error ( module_name . c_str ( ) , whole_name . c_str ( ) ) ) ;
        if ( whole . min_set )
            shy_guts :: assign_module_value_whole_min ( module_i , whole_i ) ;
    }
    else
    {
        so_called_lib_std_int32_t int_value = 0 ;
        so_called_lib_std_istringstream ( string_value ) >> int_value ;
        shy_guts :: assign_module_value_whole_clamped ( module_i , whole_i , int_value ) ;
    }
}

void shy_loadable_consts_assigner :: prepare ( )
{
    shy_guts :: error = so_called_lib_std_false ;
}

void shy_loadable_consts_assigner :: assign ( )
{
    so_called_loadable_consts_content_module_container_type * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    for ( so_called_loadable_consts_content_module_container_type :: const_iterator module_i = module_container -> begin ( )
        ; module_i != module_container -> end ( )
        ; ++ module_i
        )
    {
        shy_guts :: assign_module ( module_i ) ;
    }
}

void shy_loadable_consts_assigner :: get_error ( so_called_lib_std_bool & arg_error )
{
    arg_error = shy_guts :: error ;
}
