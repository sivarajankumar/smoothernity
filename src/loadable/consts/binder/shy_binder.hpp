namespace shy_guts
{
    static so_called_loadable_consts_content_module_type * current_module = 0 ;
    static so_called_lib_std_string current_name_fract ;
    static so_called_lib_std_string current_name_whole ;
}

void shy_loadable_consts_binder :: bind_module ( const so_called_lib_std_char * name , so_called_loadable_consts_content_module_binding_type )
{
    so_called_loadable_consts_content_module_container_type * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    ( * module_container ) [ name ] = so_called_loadable_consts_content_module_type ( ) ;
    shy_guts :: current_module = & ( ( * module_container ) [ name ] ) ;
}

void shy_loadable_consts_binder :: bind_value ( const so_called_lib_std_char * name , so_called_loadable_consts_content_value_fract_binding_type value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_fract [ name ] = so_called_loadable_consts_content_value_fract_type ( ) ;
        shy_guts :: current_module -> name_to_fract [ name ] . binding = const_cast < so_called_platform_math_num_fract_type * > ( & value ) ;
        shy_guts :: current_name_fract = name ;
    }
}

void shy_loadable_consts_binder :: bind_value ( const so_called_lib_std_char * name , so_called_loadable_consts_content_value_whole_binding_type value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_whole [ name ] = so_called_loadable_consts_content_value_whole_type ( ) ;
        shy_guts :: current_module -> name_to_whole [ name ] . binding = const_cast < so_called_platform_math_num_whole_type * > ( & value ) ;
        shy_guts :: current_name_whole = name ;
    }
}

void shy_loadable_consts_binder :: bind_value_min ( so_called_lib_std_int32_t value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_whole [ shy_guts :: current_name_whole ] . min_value = value ;
        shy_guts :: current_module -> name_to_whole [ shy_guts :: current_name_whole ] . min_set = so_called_lib_std_true ;
    }
}

void shy_loadable_consts_binder :: bind_value_max ( so_called_lib_std_int32_t value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_whole [ shy_guts :: current_name_whole ] . max_value = value ;
        shy_guts :: current_module -> name_to_whole [ shy_guts :: current_name_whole ] . max_set = so_called_lib_std_true ;
    }
}

void shy_loadable_consts_binder :: bind_value_min ( so_called_lib_std_int32_t numerator , so_called_lib_std_int32_t denominator )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . min_numerator = numerator ;
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . min_denominator = denominator ;
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . min_set = so_called_lib_std_true ;
    }
}

void shy_loadable_consts_binder :: bind_value_max ( so_called_lib_std_int32_t numerator , so_called_lib_std_int32_t denominator )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . max_numerator = numerator ;
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . max_denominator = denominator ;
        shy_guts :: current_module -> name_to_fract [ shy_guts :: current_name_fract ] . max_set = so_called_lib_std_true ;
    }
}
