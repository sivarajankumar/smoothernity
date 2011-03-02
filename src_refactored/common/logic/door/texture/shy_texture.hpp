namespace shy_guts
{
    namespace logic_door_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
    }

    namespace engine_render_texture_create_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
        static so_called_type_common_engine_render_texture_id texture ;
    }

    namespace engine_rasterizer_finalize_state
    {
        static so_called_type_platform_math_num_whole requested ;
        static so_called_type_platform_math_num_whole replied ;
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
        ( so_called_type_platform_render_texel_data 
        ) ;
    static void draw_rect 
        ( so_called_type_platform_math_num_whole x1 
        , so_called_type_platform_math_num_whole y1 
        , so_called_type_platform_math_num_whole x2 
        , so_called_type_platform_math_num_whole y2 
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
    so_called_sender_common_engine_render_texture_create_request :: send ( so_called_message_common_engine_render_texture_create_request ( ) ) ;
}

void shy_guts :: texture_created ( )
{
    shy_guts :: fill_texture_contents ( ) ;
    shy_guts :: request_rasterizer_finalize ( ) ;
}

void shy_guts :: fill_texture_contents ( )
{
    so_called_type_platform_math_num_fract pen_r ;
    so_called_type_platform_math_num_fract pen_g ;
    so_called_type_platform_math_num_fract pen_b ;
    so_called_type_platform_math_num_fract pen_a ;
    so_called_type_platform_math_num_fract paper_r ;
    so_called_type_platform_math_num_fract paper_g ;
    so_called_type_platform_math_num_fract paper_b ;
    so_called_type_platform_math_num_fract paper_a ;
    so_called_type_platform_math_num_whole x_left ;
    so_called_type_platform_math_num_whole x_right ;
    so_called_type_platform_math_num_whole y_bottom ;
    so_called_type_platform_math_num_whole y_top ;
    so_called_type_platform_math_num_whole texture_width ;
    so_called_type_platform_math_num_whole texture_height ;
    so_called_type_platform_math_num_whole stripes ;
    so_called_type_platform_math_num_whole colored_stripe ;
    so_called_type_common_engine_render_texture_id texture ;
    so_called_type_platform_render_texel_data pen ;
    so_called_type_platform_render_texel_data paper ;

    pen_r = so_called_common_logic_door_consts :: texture_pen_r ;
    pen_g = so_called_common_logic_door_consts :: texture_pen_g ;
    pen_b = so_called_common_logic_door_consts :: texture_pen_b ;
    pen_a = so_called_common_logic_door_consts :: texture_pen_a ;
    paper_r = so_called_common_logic_door_consts :: texture_paper_r ;
    paper_g = so_called_common_logic_door_consts :: texture_paper_g ;
    paper_b = so_called_common_logic_door_consts :: texture_paper_b ;
    stripes = so_called_common_logic_door_consts :: texture_stripes ;
    texture_width = so_called_common_engine_render_consts :: texture_width ;
    texture_height = so_called_common_engine_render_consts :: texture_height ;
    texture = shy_guts :: engine_render_texture_create_state :: texture ;

    so_called_message_common_engine_rasterizer_use_texture texture_msg ;
    texture_msg . texture = texture ;
    texture_msg . origin_x = so_called_platform_math_consts :: whole_0 ;
    texture_msg . origin_y = so_called_platform_math_consts :: whole_0 ;
    so_called_sender_common_engine_rasterizer_use_texture :: send ( texture_msg ) ;

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
    for ( so_called_type_platform_math_num_whole i = so_called_platform_math_consts :: whole_0
        ; so_called_platform_conditions :: whole_less_than_whole ( i , stripes )
        ; so_called_platform_math :: inc_whole ( i )
        )
    {
        so_called_type_platform_math_num_whole next_i ;
        so_called_type_platform_math_num_whole stripe_y_top ;
        so_called_type_platform_math_num_whole stripe_y_bottom ;

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
}

void shy_guts :: reply_door_texture_created ( )
{
}

void shy_guts :: request_rasterizer_finalize ( )
{
}

void shy_guts :: rasterizer_finalized ( )
{
    shy_guts :: finalize_texture ( ) ;
    shy_guts :: reply_door_texture_created ( ) ;
}

void shy_guts :: use_texel ( so_called_type_platform_render_texel_data )
{
}

void shy_guts :: draw_rect 
    ( so_called_type_platform_math_num_whole x1 
    , so_called_type_platform_math_num_whole y1 
    , so_called_type_platform_math_num_whole x2 
    , so_called_type_platform_math_num_whole y2 
    )
{
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_engine_rasterizer_finalize_reply )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_rasterizer_finalize_state :: requested ) )
    {
        shy_guts :: engine_rasterizer_finalize_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_rasterizer_finalize_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_engine_render_texture_create_reply msg )
{
    if ( so_called_platform_conditions :: whole_is_true ( shy_guts :: engine_render_texture_create_state :: requested ) )
    {
        shy_guts :: engine_render_texture_create_state :: requested = so_called_platform_math_consts :: whole_false ;
        shy_guts :: engine_render_texture_create_state :: replied = so_called_platform_math_consts :: whole_true ;
        shy_guts :: engine_render_texture_create_state :: texture = msg . texture ;
        shy_guts :: proceed_with_creation ( ) ;
    }
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_logic_door_texture_create )
{
    shy_guts :: logic_door_texture_create_state :: requested = so_called_platform_math_consts :: whole_true ;
    shy_guts :: proceed_with_creation ( ) ;
}

void _shy_common_logic_door_texture :: receive ( so_called_message_common_logic_door_texture_select_request )
{
    so_called_message_common_engine_render_texture_select msg ;
    msg . texture = shy_guts :: engine_render_texture_create_state :: texture ;
    so_called_sender_common_engine_render_texture_select :: send ( msg ) ;
    so_called_sender_common_logic_door_texture_select_reply :: send ( so_called_message_common_logic_door_texture_select_reply ( ) ) ;
}
