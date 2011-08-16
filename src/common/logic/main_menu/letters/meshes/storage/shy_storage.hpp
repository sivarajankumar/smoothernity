namespace shy_guts
{
    namespace logic_main_menu_letters_meshes_storage_consts
    {
        static so_called_type_platform_math_const_int_32 max_meshes 
            = so_called_common_logic_main_menu_consts :: max_rows 
            * so_called_common_logic_main_menu_consts :: max_cols
            ;
    }

    class mesh_state
    {
    public :
        so_called_type_common_engine_render_mesh_id mesh ;
        so_called_type_platform_math_num_whole row ;
        so_called_type_platform_math_num_whole col ;
    } ;

    static so_called_type_platform_static_array_data < shy_guts :: mesh_state , shy_guts :: logic_main_menu_letters_meshes_storage_consts :: max_meshes > meshes ;
    static so_called_type_platform_math_num_whole meshes_count ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_init )
{
    shy_guts :: meshes_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_count_request )
{
    so_called_message_common_logic_main_menu_letters_meshes_count_reply reply_msg ;
    reply_msg . meshes = shy_guts :: meshes_count ;
    so_called_sender_common_logic_main_menu_letters_meshes_count_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_iterate_start )
{
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , shy_guts :: meshes_count )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_pointer_data < shy_guts :: mesh_state > mesh_state ;
        so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , i ) ;
        
        so_called_message_common_logic_main_menu_letters_meshes_iteration iteration_msg ;
        iteration_msg . row = mesh_state . get ( ) . row ;
        iteration_msg . col = mesh_state . get ( ) . col ;
        iteration_msg . mesh = mesh_state . get ( ) . mesh ;
        so_called_sender_common_logic_main_menu_letters_meshes_iteration :: send ( iteration_msg ) ;
    }
    so_called_sender_common_logic_main_menu_letters_meshes_iterate_finished :: send ( so_called_message_common_logic_main_menu_letters_meshes_iterate_finished ( ) ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_has_been_created msg )
{
    so_called_type_platform_pointer_data < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , shy_guts :: meshes_count ) ;
    mesh_state . get ( ) . mesh = msg . mesh ;
    mesh_state . get ( ) . row = msg . row ;
    mesh_state . get ( ) . col = msg . col ;
    so_called_platform_math :: inc_whole ( shy_guts :: meshes_count ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_id_request msg )
{
    so_called_type_platform_pointer_data < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , msg . index ) ;
    
    so_called_message_common_logic_main_menu_letters_meshes_mesh_id_reply reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . mesh = mesh_state . get ( ) . mesh ;
    so_called_sender_common_logic_main_menu_letters_meshes_mesh_id_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: receive ( so_called_message_common_logic_main_menu_letters_meshes_mesh_row_col_request msg )
{
    so_called_type_platform_pointer_data < shy_guts :: mesh_state > mesh_state ;
    so_called_platform_static_array :: element_ptr ( mesh_state , shy_guts :: meshes , msg . index ) ;

    so_called_message_common_logic_main_menu_letters_meshes_mesh_row_col_reply reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . row = mesh_state . get ( ) . row ;
    reply_msg . col = mesh_state . get ( ) . col ;
    so_called_sender_common_logic_main_menu_letters_meshes_mesh_row_col_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_main_menu_letters_meshes_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

