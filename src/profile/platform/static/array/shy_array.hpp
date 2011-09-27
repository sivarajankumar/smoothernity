namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_element ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_static_array :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_static_array_" #x )
    make_name_id_helper ( element ) ;
#undef make_name_id_helper
}

void shy_profile_platform_static_array :: element ( )
{
    shy_guts :: profile ( shy_guts :: id_element ) ;
}
