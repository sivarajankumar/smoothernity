namespace shy_guts
{
    class type_entry
    {
    public :
        so_called_type_common_engine_render_mesh_id mesh ;
    } ;

    static so_called_type_platform_static_array_data < type_entry , so_called_common_logic_salutation_letters_consts :: max_letters > entries_data ;
    static so_called_type_platform_math_num_whole entries_count ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_salutation_letters_meshes_storage > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_init )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_add_mesh msg )
{
    so_called_type_platform_math_num_whole whole_max_entries ;
    so_called_platform_math :: make_num_whole ( whole_max_entries , so_called_common_logic_salutation_letters_consts :: max_letters ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( shy_guts :: entries_count , whole_max_entries ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: type_entry > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , shy_guts :: entries_count ) ;
        entry . get ( ) . mesh = msg . mesh ;
        so_called_platform_math :: inc_whole ( shy_guts :: entries_count ) ;
    }
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_clean )
{
    shy_guts :: entries_count = so_called_platform_math_consts :: whole_0 ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_mesh_request msg )
{
    so_called_type_common_engine_render_mesh_id mesh ;
    so_called_type_platform_math_num_whole whole_max_entries ;
    so_called_platform_math :: make_num_whole ( whole_max_entries , so_called_common_logic_salutation_letters_consts :: max_letters ) ;
    if ( so_called_platform_conditions :: whole_less_than_whole ( msg . index , whole_max_entries ) )
    {
        so_called_type_platform_pointer_data < shy_guts :: type_entry > entry ;
        so_called_platform_static_array :: element_ptr ( entry , shy_guts :: entries_data , msg . index ) ;
        mesh = entry . get ( ) . mesh ;
    }
    else
        mesh = so_called_common_engine_render_consts :: null_mesh ;

    so_called_message_common_logic_salutation_letters_meshes_storage_mesh_reply reply_msg ;
    reply_msg . index = msg . index ;
    reply_msg . mesh = mesh ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_mesh_reply :: send ( reply_msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: receive ( so_called_message_common_logic_salutation_letters_meshes_storage_size_request )
{
    so_called_message_common_logic_salutation_letters_meshes_storage_size_reply msg ;
    msg . size = shy_guts :: entries_count ;
    so_called_sender_common_logic_salutation_letters_meshes_storage_size_reply :: send ( msg ) ;
}

void _shy_common_logic_salutation_letters_meshes_storage :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}
