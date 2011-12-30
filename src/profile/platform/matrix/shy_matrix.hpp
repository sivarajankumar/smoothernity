namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_identity ;
    static so_called_platform_math_num_whole_type id_inverse ;
    static so_called_platform_math_num_whole_type id_row_get ;
    static so_called_platform_math_num_whole_type id_row_set ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_matrix :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_matrix_" #x )
    make_name_id_helper ( identity ) ;
    make_name_id_helper ( inverse ) ;
    make_name_id_helper ( row_get ) ;
    make_name_id_helper ( row_set ) ;
#undef make_name_id_helper
}

void shy_profile_platform_matrix :: identity ( )
{
    shy_guts :: profile ( shy_guts :: id_identity ) ;
}

void shy_profile_platform_matrix :: inverse ( )
{
    shy_guts :: profile ( shy_guts :: id_inverse ) ;
}

void shy_profile_platform_matrix :: row_get ( )
{
    shy_guts :: profile ( shy_guts :: id_row_get ) ;
}

void shy_profile_platform_matrix :: row_set ( )
{
    shy_guts :: profile ( shy_guts :: id_row_set ) ;
}
