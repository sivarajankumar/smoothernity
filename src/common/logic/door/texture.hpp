template < typename mediator >
class shy_logic_door_texture
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: engine_render_stateless :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator :: engine_render_stateless :: engine_render_texture_id engine_render_texture_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;

    class _logic_door_texture_consts_type
    {
    public :
        _logic_door_texture_consts_type ( ) ;
    public :
        num_fract pen_r ;
        num_fract pen_g ;
        num_fract pen_b ;
        num_fract pen_a ;
        num_fract paper_r ;
        num_fract paper_g ;
        num_fract paper_b ;
        num_fract paper_a ;
        num_whole stripes ;
    } ;

    class _logic_door_texture_create_state_type
    {
    public :
        num_whole requested ;
    } ;

    class _engine_render_texture_create_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
        engine_render_texture_id texture ;
    } ;

    class _engine_rasterizer_finalize_state_type
    {
    public :
        num_whole requested ;
        num_whole replied ;
    } ;

public :
    shy_logic_door_texture ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_door_texture_create ) ;
    void receive ( typename messages :: logic_door_texture_select_request ) ;
    void receive ( typename messages :: engine_render_texture_create_reply ) ;
    void receive ( typename messages :: engine_rasterizer_finalize_reply ) ;
private :
    shy_logic_door_texture < mediator > & operator= ( const shy_logic_door_texture < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _request_texture_create ( ) ;
    void _texture_created ( ) ;
    void _fill_texture_contents ( ) ;
    void _finalize_texture ( ) ;
    void _reply_door_texture_created ( ) ;
    void _request_rasterizer_finalize ( ) ;
    void _rasterizer_finalized ( ) ;
    void _use_texel ( texel_data ) ;
    void _draw_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > _engine_render_stateless_consts ;
    const _logic_door_texture_consts_type _logic_door_texture_consts ;

    _logic_door_texture_create_state_type _logic_door_texture_create_state ;
    _engine_render_texture_create_state_type _engine_render_texture_create_state ;
    _engine_rasterizer_finalize_state_type _engine_rasterizer_finalize_state ;
} ;

template < typename mediator >
shy_logic_door_texture < mediator > :: _logic_door_texture_consts_type :: _logic_door_texture_consts_type ( )
{
    platform_math :: make_num_fract ( pen_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( pen_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( pen_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( pen_a , 1 , 1 ) ;
    platform_math :: make_num_fract ( paper_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( paper_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( paper_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( paper_a , 1 , 1 ) ;
    platform_math :: make_num_whole ( stripes , 9 ) ;
}

template < typename mediator >
shy_logic_door_texture < mediator > :: shy_logic_door_texture ( )
{
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . engine_render_stateless_consts ( _engine_render_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: receive ( typename messages :: logic_door_texture_create )
{
    _logic_door_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: receive ( typename messages :: logic_door_texture_select_request )
{
    typename messages :: engine_render_texture_select msg ;
    msg . texture = _engine_render_texture_create_state . texture ;
    _mediator . get ( ) . send ( msg ) ;
    _mediator . get ( ) . send ( typename messages :: logic_door_texture_select_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: receive ( typename messages :: engine_render_texture_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _engine_render_texture_create_state . requested ) )
    {
        _engine_render_texture_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_render_texture_create_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _engine_render_texture_create_state . texture = msg . texture ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: receive ( typename messages :: engine_rasterizer_finalize_reply )
{
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . requested ) )
    {
        _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_door_texture_create_state . requested ) )
    {
        _logic_door_texture_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_texture_create ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_texture_create_state . replied ) )
    {
        _engine_render_texture_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _texture_created ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . replied ) )
    {
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _rasterizer_finalized ( ) ;
    }
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _request_texture_create ( )
{
    _engine_render_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_texture_create_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _texture_created ( )
{
    _fill_texture_contents ( ) ;
    _request_rasterizer_finalize ( ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _rasterizer_finalized ( )
{
    _finalize_texture ( ) ;
    _reply_door_texture_created ( ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _fill_texture_contents ( )
{
    num_fract pen_r ;
    num_fract pen_g ;
    num_fract pen_b ;
    num_fract pen_a ;
    num_fract paper_r ;
    num_fract paper_g ;
    num_fract paper_b ;
    num_fract paper_a ;
    num_whole x_left ;
    num_whole x_right ;
    num_whole y_bottom ;
    num_whole y_top ;
    num_whole texture_width ;
    num_whole texture_height ;
    num_whole stripes ;
    num_whole colored_stripe ;
    engine_render_texture_id texture ;
    texel_data pen ;
    texel_data paper ;

    pen_r = _logic_door_texture_consts . pen_r ;
    pen_g = _logic_door_texture_consts . pen_g ;
    pen_b = _logic_door_texture_consts . pen_b ;
    pen_a = _logic_door_texture_consts . pen_a ;
    paper_r = _logic_door_texture_consts . paper_r ;
    paper_g = _logic_door_texture_consts . paper_g ;
    paper_b = _logic_door_texture_consts . paper_b ;
    stripes = _logic_door_texture_consts . stripes ;
    texture_width = _engine_render_stateless_consts . get ( ) . texture_width ;
    texture_height = _engine_render_stateless_consts . get ( ) . texture_height ;
    texture = _engine_render_texture_create_state . texture ;

    typename messages :: engine_rasterizer_use_texture texture_msg ;
    texture_msg . texture = texture ;
    texture_msg . origin_x = _platform_math_consts . get ( ) . whole_0 ;
    texture_msg . origin_y = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( texture_msg ) ;

    x_left = _platform_math_consts . get ( ) . whole_0 ;
    y_bottom = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: sub_wholes ( x_right , texture_width , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( y_top , texture_height , _platform_math_consts . get ( ) . whole_1 ) ;

    engine_render_stateless :: set_texel_color ( pen , pen_r , pen_g , pen_b , pen_a ) ;
    engine_render_stateless :: set_texel_color ( paper , paper_r , paper_g , paper_b , paper_a ) ;

    _use_texel ( paper ) ;
    _draw_rect ( x_left , y_bottom , x_right , y_top ) ;

    _use_texel ( pen ) ;
    colored_stripe = _platform_math_consts . get ( ) . whole_false ;
    for ( num_whole i = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( i , stripes )
        ; platform_math :: inc_whole ( i )
        )
    {
        num_whole next_i ;
        num_whole stripe_y_top ;
        num_whole stripe_y_bottom ;

        platform_math :: add_wholes ( next_i , i , _platform_math_consts . get ( ) . whole_1 ) ;

        platform_math :: mul_wholes ( stripe_y_top , next_i , y_top ) ;
        platform_math :: mul_wholes ( stripe_y_bottom , i , y_top ) ;

        platform_math :: div_whole_by ( stripe_y_top , stripes ) ;
        platform_math :: div_whole_by ( stripe_y_bottom , stripes ) ;

        if ( platform_conditions :: whole_is_true ( colored_stripe ) )
        {
            colored_stripe = _platform_math_consts . get ( ) . whole_false ;
            _draw_rect ( x_left , stripe_y_bottom , x_right , stripe_y_top ) ;
        }
        else
            colored_stripe = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _use_texel ( texel_data texel )
{
    typename messages :: engine_rasterizer_use_texel msg ;
    msg . texel = texel ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _draw_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    typename messages :: engine_rasterizer_draw_rect msg ;
    msg . x1 = x1 ;
    msg . y1 = y1 ;
    msg . x2 = x2 ;
    msg . y2 = y2 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _request_rasterizer_finalize ( )
{
    _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_rasterizer_finalize_request ( ) ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _finalize_texture ( )
{
    typename messages :: engine_render_texture_finalize msg ;
    msg . texture = _engine_render_texture_create_state . texture ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_door_texture < mediator > :: _reply_door_texture_created ( )
{
    _mediator . get ( ) . send ( typename messages :: logic_door_texture_creation_finished ( ) ) ;
}

