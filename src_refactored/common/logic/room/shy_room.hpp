namespace shy_guts
{
    namespace logic_room_update_state
    {
        static so_called_type_platform_math_num_whole launch_permitted ;
        static so_called_type_platform_math_num_fract time ;
    }

    namespace logic_room_creation_permit_state
    {
        static so_called_type_platform_math_num_whole creation_permitted ;
    }

    namespace logic_room_mesh_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    namespace logic_room_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
    }

    static void proceed_with_creation ( ) ;
    static void request_mesh_create ( ) ;
    static void request_texture_create ( ) ;
    static void texture_created ( ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
}

void shy_guts :: request_mesh_create ( )
{
}

void shy_guts :: request_texture_create ( )
{
}

void shy_guts :: texture_created ( )
{
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_creation_permit )
{
    shy_guts :: logic_room_creation_permit_state :: creation_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_launch_permit )
{
    shy_guts :: logic_room_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_room_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_mesh_creation_finished )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_create_state :: requested ) )
    {
        shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_texture_creation_finished )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_create_state :: requested ) )
    {
        shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room :: receive ( so_called_message_common_logic_room_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_update_state :: launch_permitted ) )
    {
        so_called_type_platform_math_num_fract time ;
        so_called_type_platform_math_num_fract time_step ;
        so_called_type_platform_math_num_fract show_time ;

        time = shy_guts :: logic_room_update_state :: time ;
        show_time = so_called_common_logic_room_consts :: room_show_time ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;

        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , show_time ) )
        {
            shy_guts :: logic_room_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
            so_called_sender_common_logic_room_finished :: send ( so_called_message_common_logic_room_finished ( ) ) ;
        }

        shy_guts :: logic_room_update_state :: time = time ;
    }
}
