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

void _shy_common_logic_touch :: receive ( so_called_message_common_engine_render_mesh_create_reply )
{
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
}

void _shy_common_logic_touch :: receive ( so_called_message_common_logic_touch_render )
{
}

void _shy_common_logic_touch :: receive ( so_called_message_common_logic_touch_update )
{
}
