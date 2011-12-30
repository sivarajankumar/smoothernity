namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_aspect ;
    static so_called_platform_math_num_whole_type id_clear_screen ;
    static so_called_platform_math_num_whole_type id_draw ;
    static so_called_platform_math_num_whole_type id_frame_loss ;
    static so_called_platform_math_num_whole_type id_index_create ;
    static so_called_platform_math_num_whole_type id_index_delete ;
    static so_called_platform_math_num_whole_type id_index_element ;
    static so_called_platform_math_num_whole_type id_index_map ;
    static so_called_platform_math_num_whole_type id_index_set ;
    static so_called_platform_math_num_whole_type id_index_unmap ;
    static so_called_platform_math_num_whole_type id_matrix_identity ;
    static so_called_platform_math_num_whole_type id_matrix_load ;
    static so_called_platform_math_num_whole_type id_matrix_mult ;
    static so_called_platform_math_num_whole_type id_matrix_pop ;
    static so_called_platform_math_num_whole_type id_matrix_push ;
    static so_called_platform_math_num_whole_type id_projection ;
    static so_called_platform_math_num_whole_type id_state ;
    static so_called_platform_math_num_whole_type id_texture_create ;
    static so_called_platform_math_num_whole_type id_texture_delete ;
    static so_called_platform_math_num_whole_type id_texture_set ;
    static so_called_platform_math_num_whole_type id_texture_subdata ;
    static so_called_platform_math_num_whole_type id_texture_use ;
    static so_called_platform_math_num_whole_type id_vertex_create ;
    static so_called_platform_math_num_whole_type id_vertex_delete ;
    static so_called_platform_math_num_whole_type id_vertex_element ;
    static so_called_platform_math_num_whole_type id_vertex_map ;
    static so_called_platform_math_num_whole_type id_vertex_set ;
    static so_called_platform_math_num_whole_type id_vertex_unmap ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_render :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_render_" #x )
    make_name_id_helper ( aspect ) ;
    make_name_id_helper ( clear_screen ) ;
    make_name_id_helper ( draw ) ;
    make_name_id_helper ( frame_loss ) ;
    make_name_id_helper ( index_create ) ;
    make_name_id_helper ( index_delete ) ;
    make_name_id_helper ( index_element ) ;
    make_name_id_helper ( index_map ) ;
    make_name_id_helper ( index_set ) ;
    make_name_id_helper ( index_unmap ) ;
    make_name_id_helper ( matrix_identity ) ;
    make_name_id_helper ( matrix_load ) ;
    make_name_id_helper ( matrix_mult ) ;
    make_name_id_helper ( matrix_pop ) ;
    make_name_id_helper ( matrix_push ) ;
    make_name_id_helper ( projection ) ;
    make_name_id_helper ( state ) ;
    make_name_id_helper ( texture_create ) ;
    make_name_id_helper ( texture_delete ) ;
    make_name_id_helper ( texture_set ) ;
    make_name_id_helper ( texture_subdata ) ;
    make_name_id_helper ( texture_use ) ;
    make_name_id_helper ( vertex_create ) ;
    make_name_id_helper ( vertex_delete ) ;
    make_name_id_helper ( vertex_element ) ;
    make_name_id_helper ( vertex_map ) ;
    make_name_id_helper ( vertex_set ) ;
    make_name_id_helper ( vertex_unmap ) ;
#undef make_name_id_helper
}

void shy_profile_platform_render :: aspect ( )
{
    shy_guts :: profile ( shy_guts :: id_aspect ) ;
}

void shy_profile_platform_render :: clear_screen ( )
{
    shy_guts :: profile ( shy_guts :: id_clear_screen ) ;
}

void shy_profile_platform_render :: draw ( )
{
    shy_guts :: profile ( shy_guts :: id_draw ) ;
}

void shy_profile_platform_render :: frame_loss ( )
{
    shy_guts :: profile ( shy_guts :: id_frame_loss ) ;
}

void shy_profile_platform_render :: index_create ( )
{
    shy_guts :: profile ( shy_guts :: id_index_create ) ;
}

void shy_profile_platform_render :: index_delete ( )
{
    shy_guts :: profile ( shy_guts :: id_index_delete ) ;
}

void shy_profile_platform_render :: index_element ( )
{
    shy_guts :: profile ( shy_guts :: id_index_element ) ;
}

void shy_profile_platform_render :: index_map ( )
{
    shy_guts :: profile ( shy_guts :: id_index_map ) ;
}

void shy_profile_platform_render :: index_set ( )
{
    shy_guts :: profile ( shy_guts :: id_index_set ) ;
}

void shy_profile_platform_render :: index_unmap ( )
{
    shy_guts :: profile ( shy_guts :: id_index_unmap ) ;
}

void shy_profile_platform_render :: matrix_identity ( )
{
    shy_guts :: profile ( shy_guts :: id_matrix_identity ) ;
}

void shy_profile_platform_render :: matrix_load ( )
{
    shy_guts :: profile ( shy_guts :: id_matrix_load ) ;
}

void shy_profile_platform_render :: matrix_mult ( )
{
    shy_guts :: profile ( shy_guts :: id_matrix_mult ) ;
}

void shy_profile_platform_render :: matrix_pop ( )
{
    shy_guts :: profile ( shy_guts :: id_matrix_pop ) ;
}

void shy_profile_platform_render :: matrix_push ( )
{
    shy_guts :: profile ( shy_guts :: id_matrix_push ) ;
}

void shy_profile_platform_render :: projection ( )
{
    shy_guts :: profile ( shy_guts :: id_projection ) ;
}

void shy_profile_platform_render :: state ( )
{
    shy_guts :: profile ( shy_guts :: id_state ) ;
}

void shy_profile_platform_render :: texture_create ( )
{
    shy_guts :: profile ( shy_guts :: id_texture_create ) ;
}

void shy_profile_platform_render :: texture_delete ( )
{
    shy_guts :: profile ( shy_guts :: id_texture_delete ) ;
}

void shy_profile_platform_render :: texture_set ( )
{
    shy_guts :: profile ( shy_guts :: id_texture_set ) ;
}

void shy_profile_platform_render :: texture_subdata ( )
{
    shy_guts :: profile ( shy_guts :: id_texture_subdata ) ;
}

void shy_profile_platform_render :: texture_use ( )
{
    shy_guts :: profile ( shy_guts :: id_texture_use ) ;
}

void shy_profile_platform_render :: vertex_create ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_create ) ;
}

void shy_profile_platform_render :: vertex_delete ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_delete ) ;
}

void shy_profile_platform_render :: vertex_element ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_element ) ;
}

void shy_profile_platform_render :: vertex_map ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_map ) ;
}

void shy_profile_platform_render :: vertex_set ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_set ) ;
}

void shy_profile_platform_render :: vertex_unmap ( )
{
    shy_guts :: profile ( shy_guts :: id_vertex_unmap ) ;
}
