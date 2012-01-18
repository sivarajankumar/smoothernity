namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_buttons ;
    static so_called_platform_math_num_whole_type id_coords ;
    static so_called_platform_math_num_whole_type id_enabled ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_mouse :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_mouse_" #x )
    make_name_id_helper ( buttons ) ;
    make_name_id_helper ( coords ) ;
    make_name_id_helper ( enabled ) ;
#undef make_name_id_helper
}

void shy_profile_platform_mouse :: buttons ( )
{
    shy_guts :: profile ( shy_guts :: id_buttons ) ;
}

void shy_profile_platform_mouse :: coords ( )
{
    shy_guts :: profile ( shy_guts :: id_coords ) ;
}

void shy_profile_platform_mouse :: enabled ( )
{
    shy_guts :: profile ( shy_guts :: id_enabled ) ;
}
