namespace shy_guts
{
    namespace consts
    {
        static void error_no_value_assigned_to_module_attribute ( so_called_std_string & error , so_called_std_string module , so_called_std_string attribute ) ;
    }

    static so_called_std_string error ;
}

void shy_guts :: consts :: error_no_value_assigned_to_module_attribute ( so_called_std_string & error , so_called_std_string module , so_called_std_string attribute )
{
    error = so_called_std_string ( "no value assigned to module '" ) + module + so_called_std_string ( "' attribute '" ) + attribute + so_called_std_string ( "'" ) ;
}

void shy_loadable_consts_assigner :: assign ( )
{
    so_called_type_loadable_consts_content_module_container * module_container = 0 ;
    so_called_loadable_consts_content :: get_module_container ( module_container ) ;
    for ( so_called_type_loadable_consts_content_module_container :: const_iterator module_i = module_container -> begin ( )
        ; module_i != module_container -> end ( )
        ; ++ module_i
        )
    {
        so_called_std_string module_name = module_i -> first ;
        const so_called_type_loadable_consts_content_module & module = module_i -> second ;
        for ( so_called_type_loadable_consts_content_value_whole_container :: const_iterator whole_i = module . name_to_whole . begin ( )
            ; whole_i != module . name_to_whole . end ( )
            ; ++ whole_i
            )
        {
            so_called_std_string whole_name = whole_i -> first ;
            const so_called_type_loadable_consts_content_value_whole & whole = whole_i -> second ;
            
            so_called_std_string string_value = whole . sign + whole . value ;
            if ( string_value . empty ( ) )
                shy_guts :: consts :: error_no_value_assigned_to_module_attribute ( shy_guts :: error , module_name , whole_name ) ;
            else
            {
                so_called_lib_std_int32_t int_value = 0 ;
                so_called_lib_std_istringstream ( string_value ) >> int_value ;
                so_called_platform_math :: make_num_whole ( * whole . binding , int_value ) ;
            }
        }
        for ( so_called_type_loadable_consts_content_value_fract_container :: const_iterator fract_i = module . name_to_fract . begin ( )
            ; fract_i != module . name_to_fract . end ( )
            ; ++ fract_i
            )
        {
            so_called_std_string fract_name = fract_i -> first ;
            const so_called_type_loadable_consts_content_value_fract & fract = fract_i -> second ;
            
            so_called_std_string string_numerator = fract . numerator_sign + fract . numerator_value ;
            so_called_std_string string_denominator = fract . denominator_sign + fract . denominator_value ;
            if ( string_numerator . empty ( ) || string_denominator . empty ( ) )
                shy_guts :: consts :: error_no_value_assigned_to_module_attribute ( shy_guts :: error , module_name , fract_name ) ;
            else
            {
                so_called_lib_std_int32_t int_numerator = 0 ;
                so_called_lib_std_int32_t int_denominator = 0 ;
                so_called_lib_std_istringstream ( string_numerator ) >> int_numerator ;
                so_called_lib_std_istringstream ( string_denominator ) >> int_denominator ;
                so_called_platform_math :: make_num_fract ( * fract . binding , int_numerator , int_denominator ) ;
            }
        }
    }
}

void shy_loadable_consts_assigner :: get_error ( so_called_std_string & arg_error )
{
    arg_error = shy_guts :: error ;
}
