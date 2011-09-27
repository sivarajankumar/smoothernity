namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_add_sub ;
    static so_called_platform_math_num_whole_type id_cross ;
    static so_called_platform_math_num_whole_type id_dot ;
    static so_called_platform_math_num_whole_type id_length ;
    static so_called_platform_math_num_whole_type id_mul ;
    static so_called_platform_math_num_whole_type id_normalize ;
    static so_called_platform_math_num_whole_type id_set ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_vector :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_vector_" #x )
    make_name_id_helper ( add_sub ) ;
    make_name_id_helper ( cross ) ;
    make_name_id_helper ( dot ) ;
    make_name_id_helper ( length ) ;
    make_name_id_helper ( mul ) ;
    make_name_id_helper ( normalize ) ;
    make_name_id_helper ( set ) ;
#undef make_name_id_helper
}

void shy_profile_platform_vector :: add_sub ( )
{
    shy_guts :: profile ( shy_guts :: id_add_sub ) ;
}

void shy_profile_platform_vector :: cross ( )
{
    shy_guts :: profile ( shy_guts :: id_cross ) ;
}

void shy_profile_platform_vector :: dot ( )
{
    shy_guts :: profile ( shy_guts :: id_dot ) ;
}

void shy_profile_platform_vector :: length ( )
{
    shy_guts :: profile ( shy_guts :: id_length ) ;
}

void shy_profile_platform_vector :: mul ( )
{
    shy_guts :: profile ( shy_guts :: id_mul ) ;
}

void shy_profile_platform_vector :: normalize ( )
{
    shy_guts :: profile ( shy_guts :: id_normalize ) ;
}

void shy_profile_platform_vector :: set ( )
{
    shy_guts :: profile ( shy_guts :: id_set ) ;
}
