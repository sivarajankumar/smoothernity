namespace shy_guts
{
    namespace logic_room_texture_create_state
    {
        static so_called_platform_math_num_whole_type requested ;
    }

    namespace engine_render_texture_create_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
        static so_called_common_engine_render_texture_id_type texture ;
    }

    namespace engine_rasterizer_finalize_state
    {
        static so_called_platform_math_num_whole_type requested ;
        static so_called_platform_math_num_whole_type replied ;
    }

    static void proceed_with_creation ( ) ;
    static void request_texture_create ( ) ;
    static void texture_received ( ) ;
    static void rasterizer_finalized ( ) ;
    static void use_texel 
        ( so_called_platform_render_texel_data_type 
        ) ;
    static void draw_cell 
        ( so_called_platform_math_num_whole_type x_left
        , so_called_platform_math_num_whole_type y_bottom
        , so_called_platform_math_num_whole_type x_right
        , so_called_platform_math_num_whole_type y_top
        ) ;
    static void draw_rect 
        ( so_called_platform_math_num_whole_type x1
        , so_called_platform_math_num_whole_type y1
        , so_called_platform_math_num_whole_type x2
        , so_called_platform_math_num_whole_type y2
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_room_texture > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_room_texture_create_state :: requested ) )
    {
        shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_texture_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: replied ) )
    {
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_received ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: replied ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: rasterizer_finalized ( ) ;
    }
}

void shy_guts :: request_texture_create ( )
{
    shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_render_texture_create_request_sender :: send ( so_called_common_engine_render_texture_create_request_message ( ) ) ;
}

void shy_guts :: texture_received ( )
{
    so_called_platform_math_num_whole_type texture_width ;
    so_called_platform_math_num_whole_type texture_height ;
    so_called_platform_math_num_whole_type grid_size ;
    so_called_common_engine_render_texture_id_type texture ;

    texture_width = so_called_common_engine_render_consts :: texture_width ;
    texture_height = so_called_common_engine_render_consts :: texture_height ;
    texture = shy_guts :: engine_render_texture_create_state :: texture ;
    grid_size = so_called_common_logic_room_consts :: texture_grid_size ;

    so_called_common_engine_rasterizer_use_texture_message texture_msg ;
    texture_msg . texture = texture ;
    texture_msg . origin_x = so_called_platform_math_consts :: whole_0 ;
    texture_msg . origin_y = so_called_platform_math_consts :: whole_0 ;
    so_called_common_engine_rasterizer_use_texture_sender :: send ( texture_msg ) ;

    for ( so_called_platform_math_num_whole_type grid_y = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( grid_y , grid_size )
        ; so_called_platform_math :: inc_whole ( grid_y )
        )
    {
        for ( so_called_platform_math_num_whole_type grid_x = so_called_platform_math_consts :: whole_0
            ; so_called_platform_conditions :: whole_less_than_whole ( grid_x , grid_size )
            ; so_called_platform_math :: inc_whole ( grid_x )
            )
        {
            so_called_platform_math_num_whole_type next_grid_x ;
            so_called_platform_math_num_whole_type next_grid_y ;
            so_called_platform_math_num_whole_type x_left ;
            so_called_platform_math_num_whole_type x_right ;
            so_called_platform_math_num_whole_type y_top ;
            so_called_platform_math_num_whole_type y_bottom ;

            so_called_platform_math :: add_wholes ( next_grid_x , grid_x , so_called_platform_math_consts :: whole_1 ) ;
            so_called_platform_math :: add_wholes ( next_grid_y , grid_y , so_called_platform_math_consts :: whole_1 ) ;

            so_called_platform_math :: mul_wholes ( x_left , texture_width , grid_x ) ;
            so_called_platform_math :: div_whole_by ( x_left , grid_size ) ;

            so_called_platform_math :: mul_wholes ( x_right , texture_width , next_grid_x ) ;
            so_called_platform_math :: div_whole_by ( x_right , grid_size ) ;

            so_called_platform_math :: mul_wholes ( y_bottom , texture_height , grid_y ) ;
            so_called_platform_math :: div_whole_by ( y_bottom , grid_size ) ;

            so_called_platform_math :: mul_wholes ( y_top , texture_height , next_grid_y ) ;
            so_called_platform_math :: div_whole_by ( y_top , grid_size ) ;

            so_called_platform_math :: dec_whole ( x_right ) ;
            so_called_platform_math :: dec_whole ( y_top ) ;

            shy_guts :: draw_cell ( x_left , y_bottom , x_right , y_top ) ;
        }
    }

    shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_rasterizer_finalize_request_sender :: send ( so_called_common_engine_rasterizer_finalize_request_message ( ) ) ;
}

void shy_guts :: rasterizer_finalized ( )
{
    so_called_common_engine_render_texture_finalize_message msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_common_engine_render_texture_finalize_sender :: send ( msg ) ;

    so_called_common_logic_room_texture_creation_finished_sender :: send ( so_called_common_logic_room_texture_creation_finished_message ( ) ) ;
}

void shy_guts :: use_texel ( so_called_platform_render_texel_data_type texel )
{
    so_called_common_engine_rasterizer_use_texel_message msg ;
    msg . texel = texel ;
    so_called_common_engine_rasterizer_use_texel_sender :: send ( msg ) ;
}

void shy_guts :: draw_cell 
    ( so_called_platform_math_num_whole_type x_left
    , so_called_platform_math_num_whole_type y_bottom
    , so_called_platform_math_num_whole_type x_right
    , so_called_platform_math_num_whole_type y_top
    )
{
    so_called_platform_math_num_whole_type x_center ;
    so_called_platform_math_num_whole_type y_center ;
    so_called_platform_math_num_fract_type pen_intensity ;
    so_called_platform_math_num_fract_type paper_intensity ;
    so_called_platform_math_num_fract_type alpha ;
    so_called_platform_render_texel_data_type pen ;
    so_called_platform_render_texel_data_type paper ;

    pen_intensity = so_called_common_logic_room_consts :: texture_pen_intensity ;
    paper_intensity = so_called_common_logic_room_consts :: texture_paper_intensity ;
    alpha = so_called_common_logic_room_consts :: texture_alpha ;

    so_called_common_engine_render_stateless :: set_texel_color ( pen , pen_intensity , pen_intensity , pen_intensity , alpha ) ;
    so_called_common_engine_render_stateless :: set_texel_color ( paper , paper_intensity , paper_intensity , paper_intensity , alpha ) ;

    so_called_platform_math :: add_wholes ( x_center , x_left , x_right ) ;
    so_called_platform_math :: add_wholes ( y_center , y_bottom , y_top ) ;
    so_called_platform_math :: div_whole_by ( x_center , so_called_platform_math_consts :: whole_2 ) ;
    so_called_platform_math :: div_whole_by ( y_center , so_called_platform_math_consts :: whole_2 ) ;

    shy_guts :: use_texel ( pen ) ;
    shy_guts :: draw_rect ( x_left , y_bottom , x_right , y_top ) ;
    shy_guts :: use_texel ( paper ) ;
    shy_guts :: draw_rect ( x_left , y_bottom , x_center , y_center ) ;
    shy_guts :: draw_rect ( x_center , y_center , x_right , y_top ) ;
}

void shy_guts :: draw_rect 
    ( so_called_platform_math_num_whole_type x1
    , so_called_platform_math_num_whole_type y1
    , so_called_platform_math_num_whole_type x2
    , so_called_platform_math_num_whole_type y2
    )
{
    so_called_common_engine_rasterizer_draw_rect_message msg ;
    msg . x1 = x1 ;
    msg . y1 = y1 ;
    msg . x2 = x2 ;
    msg . y2 = y2 ;
    so_called_common_engine_rasterizer_draw_rect_sender :: send ( msg ) ;
}

void _shy_common_logic_room_texture :: receive ( so_called_common_engine_rasterizer_finalize_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: requested ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room_texture :: receive ( so_called_common_engine_render_texture_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: requested ) )
    {
        shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_texture_create_state :: texture = msg . texture ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_room_texture :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_room_texture :: receive ( so_called_common_logic_room_texture_create_message )
{
    shy_guts :: logic_room_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_room_texture :: receive ( so_called_common_logic_room_texture_select_request_message )
{
    so_called_common_engine_render_texture_select_message msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_common_engine_render_texture_select_sender :: send ( msg ) ;

    so_called_common_logic_room_texture_select_reply_sender :: send ( so_called_common_logic_room_texture_select_reply_message ( ) ) ;
}

void _shy_common_logic_room_texture :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

