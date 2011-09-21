namespace shy_guts
{
    typedef so_called_lib_std_map < so_called_lib_std_int32_t , so_called_lib_std_string > id_to_name_type ;
    static so_called_lib_std_int32_t last_id = 0 ;
    static id_to_name_type id_to_name ;
}

void shy_platform_profile_insider :: flush ( )
{
}

void shy_platform_profile_insider :: id_value_add ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type )
{
}

void shy_platform_profile_insider :: id_value_max ( so_called_platform_math_num_whole_type , so_called_platform_math_num_whole_type )
{
}

void shy_platform_profile_insider :: init ( )
{
    shy_guts :: last_id = 0 ;
    shy_guts :: id_to_name . clear ( ) ;
}

void shy_platform_profile_insider :: next_frame ( )
{
}

void shy_platform_profile_insider :: make_name_id ( so_called_platform_math_num_whole_type & id , const so_called_lib_std_char * name )
{
    so_called_platform_math_insider :: num_whole_value_set ( id , shy_guts :: last_id ) ;
    shy_guts :: id_to_name [ shy_guts :: last_id ] = so_called_lib_std_string ( name ) ;
    ++ shy_guts :: last_id ;
}
