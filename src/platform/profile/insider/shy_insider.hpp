namespace shy_guts
{
    typedef so_called_lib_std_map < so_called_lib_std_int32_t , so_called_lib_std_string > id_to_name_type ;
    typedef so_called_lib_std_map < so_called_lib_std_int32_t , so_called_lib_std_int32_t > frame_type ;
    typedef so_called_lib_std_vector < shy_guts :: frame_type > history_type ;

    static so_called_lib_std_int32_t last_id = 0 ;
    static id_to_name_type id_to_name ;
    static history_type history ;
}

void shy_platform_profile_insider :: flush ( )
{
}

void shy_platform_profile_insider :: id_value_add ( so_called_platform_math_num_whole_type id_whole , so_called_platform_math_num_whole_type value_whole )
{
    if ( ! shy_guts :: history . empty ( ) )
    {
        so_called_lib_std_int32_t id ;
        so_called_lib_std_int32_t value ;
        so_called_platform_math_insider :: num_whole_value_set ( id_whole , id ) ;
        so_called_platform_math_insider :: num_whole_value_set ( value_whole , value ) ;
        shy_guts :: frame_type & last_frame = shy_guts :: history . back ( ) ;
        if ( last_frame . find ( id ) == last_frame . end ( ) )
            last_frame [ id ] = value ;
        else
            last_frame [ id ] += value ;
    }
}

void shy_platform_profile_insider :: id_value_max ( so_called_platform_math_num_whole_type id_whole , so_called_platform_math_num_whole_type value_whole )
{
    if ( ! shy_guts :: history . empty ( ) )
    {
        so_called_lib_std_int32_t id ;
        so_called_lib_std_int32_t value ;
        so_called_platform_math_insider :: num_whole_value_set ( id_whole , id ) ;
        so_called_platform_math_insider :: num_whole_value_set ( value_whole , value ) ;
        shy_guts :: frame_type & last_frame = shy_guts :: history . back ( ) ;
        if ( last_frame . find ( id ) == last_frame . end ( ) )
            last_frame [ id ] = value ;
        else if ( last_frame [ id ] < value )
            last_frame [ id ] = value ;
    }
}

void shy_platform_profile_insider :: init ( )
{
    shy_guts :: last_id = 0 ;
    shy_guts :: id_to_name . clear ( ) ;
    shy_guts :: history . clear ( ) ;
}

void shy_platform_profile_insider :: next_frame ( )
{
    shy_guts :: history . push_back ( shy_guts :: frame_type ( ) ) ;
}

void shy_platform_profile_insider :: make_name_id ( so_called_platform_math_num_whole_type & id , const so_called_lib_std_char * name )
{
    so_called_platform_math_insider :: num_whole_value_set ( id , shy_guts :: last_id ) ;
    shy_guts :: id_to_name [ shy_guts :: last_id ] = so_called_lib_std_string ( name ) ;
    ++ shy_guts :: last_id ;
}
