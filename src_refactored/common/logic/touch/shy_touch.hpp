namespace shy_guts
{
    namespace consts
    {
        static const so_called_type_platform_math_num_fract spot_r = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract spot_g = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract spot_b = so_called_platform_math :: init_num_fract ( 255 , 255 ) ;
        static const so_called_type_platform_math_num_fract spot_pos_z = so_called_platform_math :: init_num_fract ( - 3 , 1 ) ;
        static const so_called_type_platform_math_num_fract spot_size = so_called_platform_math :: init_num_fract ( 3 , 10 ) ;
        static const so_called_type_platform_math_num_whole spot_edges = so_called_platform_math :: init_num_whole ( 32 ) ;
        static const so_called_type_platform_math_num_whole spot_lifetime_in_frames = so_called_platform_math :: init_num_whole ( 60 ) ;
    }

    static void update_spot ( ) ;
	static void decrease_spot_lifetime ( ) ;
	static void poll_touchscreen ( ) ;
    static void poll_mouse ( ) ;
	static void place_new_spot ( ) ;
    static void render_spot_mesh ( ) ;
    static void create_spot_mesh ( ) ;

    static so_called_type_platform_math_num_whole spot_frames_left ;
    static so_called_type_platform_math_num_whole spot_mesh_created ;
    static so_called_type_platform_math_num_whole spot_prepare_permitted ;
	static so_called_type_platform_math_num_whole should_place_new_spot ;
    static so_called_type_platform_math_num_whole mesh_create_requested ;
	static so_called_type_platform_math_num_fract spot_x ;
	static so_called_type_platform_math_num_fract spot_y ;
    static so_called_type_common_engine_render_mesh_id spot_mesh_id ;
    static so_called_type_platform_vector_data spot_position ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_touch > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: update_spot ( )
{
}

void shy_guts :: decrease_spot_lifetime ( )
{
}

void shy_guts :: poll_touchscreen ( )
{
}

void shy_guts :: poll_mouse ( )
{
}

void shy_guts :: place_new_spot ( )
{
}

void shy_guts :: render_spot_mesh ( )
{
}

void shy_guts :: create_spot_mesh ( )
{
}

void _shy_common_logic_touch :: receive ( so_called_message_common_engine_render_mesh_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: mesh_create_requested ) )
    {
        shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: spot_mesh_id = msg . mesh ;
        shy_guts :: create_spot_mesh ( ) ;
        shy_guts :: spot_mesh_created = so_called_platform_math_consts :: whole_true ;
        so_called_sender_common_logic_touch_prepared :: send ( so_called_message_common_logic_touch_prepared ( ) ) ;
    }
}

void _shy_common_logic_touch :: receive ( so_called_message_common_init )
{
    shy_guts :: spot_frames_left = so_called_platform_math_consts :: whole_0 ;
    shy_guts :: spot_mesh_created = so_called_platform_math_consts :: whole_false ;
    shy_guts :: spot_prepare_permitted = so_called_platform_math_consts :: whole_false ;
    shy_guts :: should_place_new_spot = so_called_platform_math_consts :: whole_false ;
    shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_touch :: receive ( so_called_message_common_logic_touch_prepare_permit )
{
    shy_guts :: spot_prepare_permitted = so_called_platform_math_consts :: whole_true ;
}

void _shy_common_logic_touch :: receive ( so_called_message_common_logic_touch_render )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: spot_mesh_created ) && so_called_platform_conditions :: whole_greater_than_zero ( shy_guts :: spot_frames_left ) )
        shy_guts :: render_spot_mesh ( ) ;
}

void _shy_common_logic_touch :: receive ( so_called_message_common_logic_touch_update )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: spot_prepare_permitted ) )
    {
        if ( so_called_platform_conditions :: whole_is_false ( shy_guts :: spot_mesh_created ) )
        {
            shy_guts :: mesh_create_requested = so_called_platform_math_consts :: whole_true ;
            
            so_called_message_common_engine_render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = shy_guts :: consts :: spot_edges ;
            mesh_create_msg . triangle_fan_indices = shy_guts :: consts :: spot_edges ;
            mesh_create_msg . triangle_strip_indices = so_called_platform_math_consts :: whole_0 ;
            so_called_sender_common_engine_render_mesh_create_request :: send ( mesh_create_msg ) ;
        }
        else
            shy_guts :: update_spot ( ) ;
    }
}
