namespace shy_guts
{
    namespace logic_room_update_state
    {
        static so_called_platform_math_num_whole_type launch_permitted ;
        static so_called_platform_math_num_fract_type time ;
    }

    namespace logic_room_creation_permit_state
    {
        static so_called_platform_math_num_whole_type creation_permitted ;
    }

    namespace logic_room_mesh_create_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
    }

    namespace logic_room_texture_create_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
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
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_creation_permit_state :: creation_permitted ) )
    {
        shy_guts :: logic_room_creation_permit_state :: creation_permitted = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_mesh_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_create_state :: replied ) )
    {
        shy_guts :: logic_room_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_texture_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_create_state :: replied ) )
    {
        shy_guts :: logic_room_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_created ( ) ;
    }
}

void shy_guts :: request_mesh_create ( )
{
    shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_room_mesh_create_sender :: send ( so_called_common_logic_room_mesh_create_message ( ) ) ;
}

void shy_guts :: request_texture_create ( )
{
    shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_logic_room_texture_create_sender :: send ( so_called_common_logic_room_texture_create_message ( ) ) ;
}

void shy_guts :: texture_created ( )
{
    so_called_common_logic_room_creation_finished_sender :: send ( so_called_common_logic_room_creation_finished_message ( ) ) ;
    so_called_common_logic_room_render_permit_sender :: send ( so_called_common_logic_room_render_permit_message ( ) ) ;
}

void _shy_common_logic_room :: receive ( so_called_common_init_message )
{
    shy_guts :: logic_room_creation_permit_state :: creation_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_mesh_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_room :: receive ( so_called_common_logic_room_creation_permit_message )
{
    shy_guts :: logic_room_creation_permit_state :: creation_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_room :: receive ( so_called_common_logic_room_launch_permit_message )
{
    shy_guts :: logic_room_update_state :: launch_permitted = so_called_platform_math_consts :: whole_true ;
    shy_guts :: logic_room_update_state :: time = so_called_platform_math_consts :: fract_0 ;
}

void _shy_common_logic_room :: receive ( so_called_common_logic_room_mesh_creation_finished_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_mesh_create_state :: requested ) )
    {
        shy_guts :: logic_room_mesh_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_mesh_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room :: receive ( so_called_common_logic_room_texture_creation_finished_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_create_state :: requested ) )
    {
        shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: logic_room_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room :: receive ( so_called_common_logic_room_update_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_update_state :: launch_permitted ) )
    {
        so_called_platform_math_num_fract_type time ;
        so_called_platform_math_num_fract_type time_step ;
        so_called_platform_math_num_fract_type show_time ;

        time = shy_guts :: logic_room_update_state :: time ;
        show_time = so_called_common_logic_room_consts :: room_show_time ;
        so_called_platform_math :: make_num_fract ( time_step , 1 , so_called_platform_consts :: frames_per_second ) ;

        so_called_platform_math :: add_to_fract ( time , time_step ) ;
        if ( so_called_platform_conditions :: fract_greater_than_fract ( time , show_time ) )
        {
            shy_guts :: logic_room_update_state :: launch_permitted = so_called_platform_math_consts :: whole_false ;
            so_called_common_logic_room_finished_sender :: send ( so_called_common_logic_room_finished_message ( ) ) ;
        }

        shy_guts :: logic_room_update_state :: time = time ;
    }
}

void _shy_common_logic_room :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

