namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_fract_add_sub ;
    static so_called_platform_math_num_whole_type id_fract_div ;
    static so_called_platform_math_num_whole_type id_fract_make ;
    static so_called_platform_math_num_whole_type id_fract_make_from_whole ;
    static so_called_platform_math_num_whole_type id_fract_mul ;
    static so_called_platform_math_num_whole_type id_fract_sin_cos ;
    static so_called_platform_math_num_whole_type id_whole_add_sub ;
    static so_called_platform_math_num_whole_type id_whole_bitwise ;
    static so_called_platform_math_num_whole_type id_whole_div_mod ;
    static so_called_platform_math_num_whole_type id_whole_make ;
    static so_called_platform_math_num_whole_type id_whole_make_from_fract ;
    static so_called_platform_math_num_whole_type id_whole_mul ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_math :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_math_" #x )
    make_name_id_helper ( fract_add_sub ) ;
    make_name_id_helper ( fract_div ) ;
    make_name_id_helper ( fract_make ) ;
    make_name_id_helper ( fract_make_from_whole ) ;
    make_name_id_helper ( fract_mul ) ;
    make_name_id_helper ( fract_sin_cos ) ;
    make_name_id_helper ( whole_add_sub ) ;
    make_name_id_helper ( whole_bitwise ) ;
    make_name_id_helper ( whole_div_mod ) ;
    make_name_id_helper ( whole_make ) ;
    make_name_id_helper ( whole_make_from_fract ) ;
    make_name_id_helper ( whole_mul ) ;
#undef make_name_id_helper
}

void shy_profile_platform_math :: fract_add_sub ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_add_sub ) ;
}

void shy_profile_platform_math :: fract_div ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_div ) ;
}

void shy_profile_platform_math :: fract_make ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_make ) ;
}

void shy_profile_platform_math :: fract_make_from_whole ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_make_from_whole ) ;
}

void shy_profile_platform_math :: fract_mul ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_mul ) ;
}

void shy_profile_platform_math :: fract_sin_cos ( )
{
    shy_guts :: profile ( shy_guts :: id_fract_sin_cos ) ;
}

void shy_profile_platform_math :: whole_add_sub ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_add_sub ) ;
}

void shy_profile_platform_math :: whole_bitwise ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_bitwise ) ;
}

void shy_profile_platform_math :: whole_div_mod ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_div_mod ) ;
}

void shy_profile_platform_math :: whole_make ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_make ) ;
}

void shy_profile_platform_math :: whole_make_from_fract ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_make_from_fract ) ;
}

void shy_profile_platform_math :: whole_mul ( )
{
    shy_guts :: profile ( shy_guts :: id_whole_mul ) ;
}

