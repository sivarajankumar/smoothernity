namespace shy_guts
{
    namespace logic_main_menu_letters_meshes_storage_consts
    {
        static so_called_platform_math_const_int_32_type max_meshes 
            = so_called_common_logic_main_menu_consts :: max_rows 
            * so_called_common_logic_main_menu_consts :: max_cols
            ;
    }

    class mesh_state
    {
    public :
        so_called_common_engine_render_mesh_id_type mesh ;
        so_called_platform_math_num_whole_type row ;
        so_called_platform_math_num_whole_type col ;
    } ;

    static so_called_platform_static_array_data_type < shy_guts :: mesh_state , shy_guts :: logic_main_menu_letters_meshes_storage_consts :: max_meshes > meshes ;
    static so_called_platform_math_num_whole_type meshes_count ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_init_message )
{
    shy_guts :: meshes_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_logic_main_menu_letters_meshes_count_request_message )
{
    so_called_common_logic_main_menu_letters_meshes_count_reply_message reply_msg ;
    reply_msg . meshes = shy_guts :: meshes_count ;
    so_called_common_logic_main_menu_letters_meshes_count_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_logic_main_menu_letters_meshes_iterate_start_message )
{
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: meshes_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_pointer_data_type < shy_guts :: mesh_state > mesh_state ;
        so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , i ) ;
        
        so_called_common_logic_main_menu_letters_meshes_iteration_message iteration_msg ;
        iteration_msg . row = mesh_state . get ( ) . row ;
        iteration_msg . col = mesh_state . get ( ) . col ;
        iteration_msg . mesh = mesh_state . get ( ) . mesh ;
        so_called_common_logic_main_menu_letters_meshes_iteration_sender :: send ( iteration_msg ) ;
    }
    so_called_common_logic_main_menu_letters_meshes_iterate_finished_sender :: send ( so_called_common_logic_main_menu_letters_meshes_iterate_finished_message ( ) ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_logic_main_menu_letters_meshes_mesh_has_been_created_message msg )
{
    so_called_platform_pointer_data_type < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , shy_guts :: meshes_count ) ;
    mesh_state . get ( ) . mesh = msg . mesh ;
    mesh_state . get ( ) . row = msg . row ;
    mesh_state . get ( ) . col = msg . col ;
    so_called_platform_math :: inc_whole ( shy_guts :: meshes_count ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_logic_main_menu_letters_meshes_mesh_id_request_message msg )
{
    so_called_platform_pointer_data_type < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , msg . index ) ;
    
    so_called_common_logic_main_menu_letters_meshes_mesh_id_reply_message reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . mesh = mesh_state . get ( ) . mesh ;
    so_called_common_logic_main_menu_letters_meshes_mesh_id_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_common_logic_main_menu_letters_meshes_mesh_row_col_request_message msg )
{
    so_called_platform_pointer_data_type < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , msg . index ) ;

    so_called_common_logic_main_menu_letters_meshes_mesh_row_col_reply_message reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . row = mesh_state . get ( ) . row ;
    reply_msg . col = mesh_state . get ( ) . col ;
    so_called_common_logic_main_menu_letters_meshes_mesh_row_col_reply_sender :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

