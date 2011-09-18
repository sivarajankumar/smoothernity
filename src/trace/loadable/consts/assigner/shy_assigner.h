class shy_trace_loadable_consts_assigner
{
public :
    static void max_limit_used_as_module_attribute_fract_value
        ( so_called_lib_std_int32_t max_numerator
        , so_called_lib_std_int32_t max_denominator
        , const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void max_limit_used_as_module_attribute_whole_value
        ( so_called_lib_std_int32_t max_value
        , const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void min_limit_used_as_module_attribute_fract_value
        ( so_called_lib_std_int32_t min_numerator
        , so_called_lib_std_int32_t min_denominator
        , const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void min_limit_used_as_module_attribute_whole_value
        ( so_called_lib_std_int32_t min_value
        , const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void module_attribute_fract_value_greater_than_max_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        , so_called_lib_std_int32_t value_numerator
        , so_called_lib_std_int32_t value_denominator
        , so_called_lib_std_int32_t max_numerator
        , so_called_lib_std_int32_t max_denominator
        ) ;
    static void module_attribute_fract_value_less_than_min_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        , so_called_lib_std_int32_t value_numerator
        , so_called_lib_std_int32_t value_denominator
        , so_called_lib_std_int32_t min_numerator
        , so_called_lib_std_int32_t min_denominator
        ) ;
    static void module_attribute_whole_value_greater_than_max_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        , so_called_lib_std_int32_t value
        , so_called_lib_std_int32_t max_value
        ) ;
    static void module_attribute_whole_value_less_than_min_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        , so_called_lib_std_int32_t value
        , so_called_lib_std_int32_t min_value
        ) ;
    static void no_max_for_module_attribute_fract_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void no_max_for_module_attribute_whole_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void no_min_for_module_attribute_fract_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void no_min_for_module_attribute_whole_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void no_value_assigned_to_module_attribute_fract_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute
        ) ;
    static void no_value_assigned_to_module_attribute_whole_error
        ( const so_called_lib_std_char * module
        , const so_called_lib_std_char * attribute 
        ) ;
    static void zero_denominator_error 
        ( const so_called_lib_std_char * module 
        , const so_called_lib_std_char * attribute 
        ) ;
} ;
