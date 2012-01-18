namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_coords ;
    static so_called_platform_math_num_whole_type id_enabled ;
    static so_called_platform_math_num_whole_type id_occured ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_touch :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_touch_" #x )
    make_name_id_helper ( coords ) ;
    make_name_id_helper ( enabled ) ;
    make_name_id_helper ( occured ) ;
#undef make_name_id_helper
}

void shy_profile_platform_touch :: coords ( )
{
    shy_guts :: profile ( shy_guts :: id_coords ) ;
}

void shy_profile_platform_touch :: enabled ( )
{
    shy_guts :: profile ( shy_guts :: id_enabled ) ;
}

void shy_profile_platform_touch :: occured ( )
{
    shy_guts :: profile ( shy_guts :: id_occured ) ;
}
