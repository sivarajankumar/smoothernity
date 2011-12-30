namespace shy_guts
{
    namespace consts
    {
        static const so_called_lib_std_char module_name [ ] = "loadable_consts_assigner" ;
        static const so_called_lib_std_bool trace_enabled = so_called_lib_std_true ;
    }
}

void shy_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_fract_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. No value has been assigned to fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: no_value_assigned_to_module_attribute_whole_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. No value has been assigned to whole attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: zero_denominator_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute 
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Error. Zero denominator has been assigned to fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: max_limit_used_as_module_attribute_fract_value
    ( so_called_lib_std_int32_t max_numerator
    , so_called_lib_std_int32_t max_denominator
    , const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Max limit of " ) ;
        so_called_platform_trace :: trace_num_fract ( max_numerator , max_denominator ) ;
        so_called_platform_trace :: trace_string ( " has been assigned to the value of fract attribute " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( attribute ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( " of module " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( module ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: min_limit_used_as_module_attribute_fract_value
    ( so_called_lib_std_int32_t min_numerator
    , so_called_lib_std_int32_t min_denominator
    , const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Min limit of " ) ;
        so_called_platform_trace :: trace_num_fract ( min_numerator , min_denominator ) ;
        so_called_platform_trace :: trace_string ( " has been assigned to the value of fract attribute " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( attribute ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( " of module " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( module ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: max_limit_used_as_module_attribute_whole_value
    ( so_called_lib_std_int32_t max_value
    , const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Max limit of " ) ;
        so_called_platform_trace :: trace_const_int_32 ( max_value ) ;
        so_called_platform_trace :: trace_string ( " has been assigned to the value of whole attribute " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( attribute ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( " of module " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( module ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: min_limit_used_as_module_attribute_whole_value
    ( so_called_lib_std_int32_t min_value
    , const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string ( "Min limit of " ) ;
        so_called_platform_trace :: trace_const_int_32 ( min_value ) ;
        so_called_platform_trace :: trace_string ( " has been assigned to the value of whole attribute " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( attribute ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( " of module " ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string_name ( module ) ;
        so_called_platform_trace :: trace_string_name ( "\"" ) ;
        so_called_platform_trace :: trace_string ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: module_attribute_fract_value_greater_than_max_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    , so_called_lib_std_int32_t value_numerator
    , so_called_lib_std_int32_t value_denominator
    , so_called_lib_std_int32_t max_numerator
    , so_called_lib_std_int32_t max_denominator
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Value " ) ;
        so_called_platform_trace :: trace_num_fract_error ( value_numerator , value_denominator ) ;
        so_called_platform_trace :: trace_string_error ( " of fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " is greater than maximum acceptable value of " ) ;
        so_called_platform_trace :: trace_num_fract_error ( max_numerator , max_denominator ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: module_attribute_fract_value_less_than_min_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    , so_called_lib_std_int32_t value_numerator
    , so_called_lib_std_int32_t value_denominator
    , so_called_lib_std_int32_t min_numerator
    , so_called_lib_std_int32_t min_denominator
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Value " ) ;
        so_called_platform_trace :: trace_num_fract_error ( value_numerator , value_denominator ) ;
        so_called_platform_trace :: trace_string_error ( " of fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " is lesser than minimum acceptable value of " ) ;
        so_called_platform_trace :: trace_num_fract_error ( min_numerator , min_denominator ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: module_attribute_whole_value_greater_than_max_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    , so_called_lib_std_int32_t value
    , so_called_lib_std_int32_t max_value
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Value " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( value ) ;
        so_called_platform_trace :: trace_string_error ( " of whole attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " is greater than maximum acceptable value of " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( max_value ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: module_attribute_whole_value_less_than_min_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    , so_called_lib_std_int32_t value
    , so_called_lib_std_int32_t min_value
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "Value " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( value ) ;
        so_called_platform_trace :: trace_string_error ( " of whole attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " is lesser than minimum acceptable value of " ) ;
        so_called_platform_trace :: trace_const_int_32_error ( min_value ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: no_max_for_module_attribute_fract_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "No acceptable maximum value has been specified for fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: no_max_for_module_attribute_whole_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "No acceptable maximum value has been specified for whole attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: no_min_for_module_attribute_fract_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "No acceptable minimum value has been specified for fract attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

void shy_trace_loadable_consts_assigner :: no_min_for_module_attribute_whole_error
    ( const so_called_lib_std_char * module
    , const so_called_lib_std_char * attribute
    )
{
    if ( shy_guts :: consts :: trace_enabled )
    {
        so_called_platform_trace :: trace_begin ( shy_guts :: consts :: module_name ) ;
        so_called_platform_trace :: trace_string_error ( "No acceptable minimum value has been specified for whole attribute " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( attribute ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( " of module " ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_name_error ( module ) ;
        so_called_platform_trace :: trace_string_name_error ( "\"" ) ;
        so_called_platform_trace :: trace_string_error ( "." ) ;
        so_called_platform_trace :: trace_end ( ) ;
    }
}

