namespace shy_guts
{
    namespace logic_door_texture_create_state
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
    static void texture_created ( ) ;
    static void fill_texture_contents ( ) ;
    static void finalize_texture ( ) ;
    static void reply_door_texture_created ( ) ;
    static void request_rasterizer_finalize ( ) ;
    static void rasterizer_finalized ( ) ;
    static void use_texel 
        ( so_called_platform_render_texel_data_type 
        ) ;
    static void draw_rect 
        ( so_called_platform_math_num_whole_type x1 
        , so_called_platform_math_num_whole_type y1 
        , so_called_platform_math_num_whole_type x2 
        , so_called_platform_math_num_whole_type y2 
        ) ;
}

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_texture > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

void shy_guts :: proceed_with_creation ( )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: logic_door_texture_create_state :: requested ) )
    {
        shy_guts :: logic_door_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: request_texture_create ( ) ;
    }
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: replied ) )
    {
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
        shy_guts :: texture_created ( ) ;
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

void shy_guts :: texture_created ( )
{
    shy_guts :: fill_texture_contents ( ) ;
    shy_guts :: request_rasterizer_finalize ( ) ;
}

void shy_guts :: fill_texture_contents ( )
{
    so_called_platform_math_num_fract_type pen_r ;
    so_called_platform_math_num_fract_type pen_g ;
    so_called_platform_math_num_fract_type pen_b ;
    so_called_platform_math_num_fract_type pen_a ;
    so_called_platform_math_num_fract_type paper_r ;
    so_called_platform_math_num_fract_type paper_g ;
    so_called_platform_math_num_fract_type paper_b ;
    so_called_platform_math_num_fract_type paper_a ;
    so_called_platform_math_num_whole_type x_left ;
    so_called_platform_math_num_whole_type x_right ;
    so_called_platform_math_num_whole_type y_bottom ;
    so_called_platform_math_num_whole_type y_top ;
    so_called_platform_math_num_whole_type texture_width ;
    so_called_platform_math_num_whole_type texture_height ;
    so_called_platform_math_num_whole_type stripes ;
    so_called_platform_math_num_whole_type colored_stripe ;
    so_called_common_engine_render_texture_id_type texture ;
    so_called_platform_render_texel_data_type pen ;
    so_called_platform_render_texel_data_type paper ;

    pen_r = so_called_common_logic_door_consts :: texture_pen_r ;
    pen_g = so_called_common_logic_door_consts :: texture_pen_g ;
    pen_b = so_called_common_logic_door_consts :: texture_pen_b ;
    pen_a = so_called_common_logic_door_consts :: texture_pen_a ;
    paper_r = so_called_common_logic_door_consts :: texture_paper_r ;
    paper_g = so_called_common_logic_door_consts :: texture_paper_g ;
    paper_b = so_called_common_logic_door_consts :: texture_paper_b ;
    paper_a = so_called_common_logic_door_consts :: texture_paper_a ;
    stripes = so_called_common_logic_door_consts :: texture_stripes ;
    texture_width = so_called_common_engine_render_consts :: texture_width ;
    texture_height = so_called_common_engine_render_consts :: texture_height ;
    texture = shy_guts :: engine_render_texture_create_state :: texture ;

    so_called_common_engine_rasterizer_use_texture_message texture_msg ;
    texture_msg . texture = texture ;
    texture_msg . origin_x = so_called_platform_math_consts :: whole_0 ;
    texture_msg . origin_y = so_called_platform_math_consts :: whole_0 ;
    so_called_common_engine_rasterizer_use_texture_sender :: send ( texture_msg ) ;

    x_left = so_called_platform_math_consts :: whole_0 ;
    y_bottom = so_called_platform_math_consts :: whole_0 ;
    so_called_platform_math :: sub_wholes ( x_right , texture_width , so_called_platform_math_consts :: whole_1 ) ;
    so_called_platform_math :: sub_wholes ( y_top , texture_height , so_called_platform_math_consts :: whole_1 ) ;

    so_called_common_engine_render_stateless :: set_texel_color ( pen , pen_r , pen_g , pen_b , pen_a ) ;
    so_called_common_engine_render_stateless :: set_texel_color ( paper , paper_r , paper_g , paper_b , paper_a ) ;

    shy_guts :: use_texel ( paper ) ;
    shy_guts :: draw_rect ( x_left , y_bottom , x_right , y_top ) ;

    shy_guts :: use_texel ( pen ) ;
    colored_stripe = so_called_platform_math_consts :: whole_false ;
    for ( so_called_platform_math_num_whole_type i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , stripes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_platform_math_num_whole_type next_i ;
        so_called_platform_math_num_whole_type stripe_y_top ;
        so_called_platform_math_num_whole_type stripe_y_bottom ;

        so_called_platform_math :: add_wholes ( next_i , i , so_called_platform_math_consts :: whole_1 ) ;

        so_called_platform_math :: mul_wholes ( stripe_y_top , next_i , y_top ) ;
        so_called_platform_math :: mul_wholes ( stripe_y_bottom , i , y_top ) ;

        so_called_platform_math :: div_whole_by ( stripe_y_top , stripes ) ;
        so_called_platform_math :: div_whole_by ( stripe_y_bottom , stripes ) ;

        if ( so_called_platform_conditions :: whole_is_true ( colored_stripe ) )
        {
            colored_stripe = so_called_platform_math_consts :: whole_false ;
            shy_guts :: draw_rect ( x_left , stripe_y_bottom , x_right , stripe_y_top ) ;
        }
        else
            colored_stripe = so_called_platform_math_consts :: whole_true ;
    }
}

void shy_guts :: finalize_texture ( )
{
    so_called_common_engine_render_texture_finalize_message msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_common_engine_render_texture_finalize_sender :: send ( msg ) ;
}

void shy_guts :: reply_door_texture_created ( )
{
    so_called_common_logic_door_texture_creation_finished_sender :: send ( so_called_common_logic_door_texture_creation_finished_message ( ) ) ;
}

void shy_guts :: request_rasterizer_finalize ( )
{
    shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_true ;
    so_called_common_engine_rasterizer_finalize_request_sender :: send ( so_called_common_engine_rasterizer_finalize_request_message ( ) ) ;
}

void shy_guts :: rasterizer_finalized ( )
{
    shy_guts :: finalize_texture ( ) ;
    shy_guts :: reply_door_texture_created ( ) ;
}

void shy_guts :: use_texel ( so_called_platform_render_texel_data_type texel )
{
    so_called_common_engine_rasterizer_use_texel_message msg ;
    msg . texel = texel ;
    so_called_common_engine_rasterizer_use_texel_sender :: send ( msg ) ;
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

void _shy_common_logic_door_texture :: receive ( so_called_common_engine_rasterizer_finalize_reply_message )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: requested ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_door_texture :: receive ( so_called_common_engine_render_texture_create_reply_message msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: requested ) )
    {
        shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_texture_create_state :: texture = msg . texture ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_door_texture :: receive ( so_called_common_init_message )
{
    shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_false ;
    shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
    shy_guts :: logic_door_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
}

void _shy_common_logic_door_texture :: receive ( so_called_common_logic_door_texture_create_message )
{
    shy_guts :: logic_door_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_door_texture :: receive ( so_called_common_logic_door_texture_select_request_message )
{
    so_called_common_engine_render_texture_select_message msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_common_engine_render_texture_select_sender :: send ( msg ) ;
    so_called_common_logic_door_texture_select_reply_sender :: send ( so_called_common_logic_door_texture_select_reply_message ( ) ) ;
}

void _shy_common_logic_door_texture :: register_in_scheduler ( )
{
    _scheduled_context_type :: register_in_scheduler ( ) ;
}

