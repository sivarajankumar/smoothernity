namespace shy_guts
{
    static so_called_platform_math_num_whole_type id_buffer_create ;
    static so_called_platform_math_num_whole_type id_buffer_set ;
    static so_called_platform_math_num_whole_type id_listener_state ;
    static so_called_platform_math_num_whole_type id_source_create ;
    static so_called_platform_math_num_whole_type id_source_play ;
    static so_called_platform_math_num_whole_type id_source_state ;
    static so_called_platform_math_num_whole_type id_source_stop ;

    static void profile ( so_called_platform_math_num_whole_type ) ;
}

void shy_guts :: profile ( so_called_platform_math_num_whole_type id )
{
    so_called_platform_profile :: id_value_add ( id , so_called_platform_math_consts :: whole_1 ) ;
}

void shy_profile_platform_sound :: init ( )
{
#define make_name_id_helper(x) so_called_platform_profile :: make_name_id ( shy_guts :: id_##x , "platform_sound_" #x )
    make_name_id_helper ( buffer_create ) ;
    make_name_id_helper ( buffer_set ) ;
    make_name_id_helper ( listener_state ) ;
    make_name_id_helper ( source_create ) ;
    make_name_id_helper ( source_play ) ;
    make_name_id_helper ( source_state ) ;
    make_name_id_helper ( source_stop ) ;
#undef make_name_id_helper
}

void shy_profile_platform_sound :: buffer_create ( )
{
    shy_guts :: profile ( shy_guts :: id_buffer_create ) ;
}

void shy_profile_platform_sound :: buffer_set ( )
{
    shy_guts :: profile ( shy_guts :: id_buffer_set ) ;
}

void shy_profile_platform_sound :: listener_state ( )
{
    shy_guts :: profile ( shy_guts :: id_listener_state ) ;
}

void shy_profile_platform_sound :: source_create ( )
{
    shy_guts :: profile ( shy_guts :: id_source_create ) ;
}

void shy_profile_platform_sound :: source_play ( )
{
    shy_guts :: profile ( shy_guts :: id_source_play ) ;
}

void shy_profile_platform_sound :: source_state ( )
{
    shy_guts :: profile ( shy_guts :: id_source_state ) ;
}

void shy_profile_platform_sound :: source_stop ( )
{
    shy_guts :: profile ( shy_guts :: id_source_stop ) ;
}
