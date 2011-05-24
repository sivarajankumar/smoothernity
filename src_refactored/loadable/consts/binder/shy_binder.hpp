namespace shy_guts
{
    static so_called_type_loadable_consts_content_module * current_module = 0 ;
}

void shy_loadable_consts_binder :: module ( const so_called_lib_std_char * name )
{
    so_called_type_loadable_consts_content_module_container * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    ( * module_container ) [ name ] = so_called_type_loadable_consts_content_module ( ) ;
    shy_guts :: current_module = & ( ( * module_container ) [ name ] ) ;
}

void shy_loadable_consts_binder :: bind ( const so_called_lib_std_char * name , const so_called_type_platform_math_num_fract & value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_fract [ name ] = so_called_type_loadable_consts_content_value_fract ( ) ;
        shy_guts :: current_module -> name_to_fract [ name ] . binding = const_cast < so_called_type_platform_math_num_fract * > ( & value ) ;
    }
}

void shy_loadable_consts_binder :: bind ( const so_called_lib_std_char * name , const so_called_type_platform_math_num_whole & value )
{
    if ( shy_guts :: current_module )
    {
        shy_guts :: current_module -> name_to_whole [ name ] = so_called_type_loadable_consts_content_value_whole ( ) ;
        shy_guts :: current_module -> name_to_whole [ name ] . binding = const_cast < so_called_type_platform_math_num_whole * > ( & value ) ;
    }
}

