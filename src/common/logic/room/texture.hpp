template < typename mediator >
class shy_logic_room_texture
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: engine_render_stateless :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator :: engine_render_stateless :: engine_render_texture_id engine_render_texture_id ;
    typedef typename mediator :: logic_room_stateless :: logic_room_stateless_consts_type logic_room_stateless_consts_type ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;

    class _logic_room_texture_create_state_type
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
    shy_logic_room_texture ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_room_texture_create ) ;
    void receive ( typename messages :: logic_room_texture_select_request ) ;
    void receive ( typename messages :: engine_render_texture_create_reply ) ;
    void receive ( typename messages :: engine_rasterizer_finalize_reply ) ;
private :
    shy_logic_room_texture < mediator > & operator= ( const shy_logic_room_texture < mediator > & ) ;
    void _proceed_with_creation ( ) ;
    void _request_texture_create ( ) ;
    void _texture_received ( ) ;
    void _rasterizer_finalized ( ) ;
    void _draw_cell ( num_whole x_left , num_whole y_bottom , num_whole x_right , num_whole y_top ) ;
    void _draw_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void _use_texel ( texel_data ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > _engine_render_stateless_consts ;
    typename platform_pointer :: template pointer < const logic_room_stateless_consts_type > _logic_room_stateless_consts ;

    _logic_room_texture_create_state_type _logic_room_texture_create_state ;
    _engine_render_texture_create_state_type _engine_render_texture_create_state ;
    _engine_rasterizer_finalize_state_type _engine_rasterizer_finalize_state ;
} ;

template < typename mediator >
shy_logic_room_texture < mediator > :: shy_logic_room_texture ( )
{
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . engine_render_stateless_consts ( _engine_render_stateless_consts ) ;
    _mediator . get ( ) . logic_room_stateless_consts ( _logic_room_stateless_consts ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: logic_room_texture_create )
{
    _logic_room_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _proceed_with_creation ( ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: logic_room_texture_select_request )
{
    typename messages :: engine_render_texture_select msg ;
    msg . texture = _engine_render_texture_create_state . texture ;
    _mediator . get ( ) . send ( msg ) ;

    _mediator . get ( ) . send ( typename messages :: logic_room_texture_select_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: receive ( typename messages :: engine_render_texture_create_reply msg )
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
void shy_logic_room_texture < mediator > :: receive ( typename messages :: engine_rasterizer_finalize_reply )
{
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . requested ) )
    {
        _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_true ;
        _proceed_with_creation ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _proceed_with_creation ( )
{
    if ( platform_conditions :: whole_is_true ( _logic_room_texture_create_state . requested ) )
    {
        _logic_room_texture_create_state . requested = _platform_math_consts . get ( ) . whole_false ;
        _request_texture_create ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_render_texture_create_state . replied ) )
    {
        _engine_render_texture_create_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _texture_received ( ) ;
    }
    if ( platform_conditions :: whole_is_true ( _engine_rasterizer_finalize_state . replied ) )
    {
        _engine_rasterizer_finalize_state . replied = _platform_math_consts . get ( ) . whole_false ;
        _rasterizer_finalized ( ) ;
    }
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _request_texture_create ( )
{
    _engine_render_texture_create_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_render_texture_create_request ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _texture_received ( )
{
    num_whole texture_width ;
    num_whole texture_height ;
    num_whole grid_size ;
    engine_render_texture_id texture ;

    texture_width = _engine_render_stateless_consts . get ( ) . texture_width ;
    texture_height = _engine_render_stateless_consts . get ( ) . texture_height ;
    texture = _engine_render_texture_create_state . texture ;
    grid_size = _logic_room_stateless_consts . get ( ) . texture_grid_size ;

    typename messages :: engine_rasterizer_use_texture texture_msg ;
    texture_msg . texture = texture ;
    texture_msg . origin_x = _platform_math_consts . get ( ) . whole_0 ;
    texture_msg . origin_y = _platform_math_consts . get ( ) . whole_0 ;
    _mediator . get ( ) . send ( texture_msg ) ;

    for ( num_whole grid_y = _platform_math_consts . get ( ) . whole_0
        ; platform_conditions :: whole_less_than_whole ( grid_y , grid_size )
        ; platform_math :: inc_whole ( grid_y )
        )
    {
        for ( num_whole grid_x = _platform_math_consts . get ( ) . whole_0
            ; platform_conditions :: whole_less_than_whole ( grid_x , grid_size )
            ; platform_math :: inc_whole ( grid_x )
            )
        {
            num_whole next_grid_x ;
            num_whole next_grid_y ;
            num_whole x_left ;
            num_whole x_right ;
            num_whole y_top ;
            num_whole y_bottom ;

            platform_math :: add_wholes ( next_grid_x , grid_x , _platform_math_consts . get ( ) . whole_1 ) ;
            platform_math :: add_wholes ( next_grid_y , grid_y , _platform_math_consts . get ( ) . whole_1 ) ;

            platform_math :: mul_wholes ( x_left , texture_width , grid_x ) ;
            platform_math :: div_whole_by ( x_left , grid_size ) ;

            platform_math :: mul_wholes ( x_right , texture_width , next_grid_x ) ;
            platform_math :: div_whole_by ( x_right , grid_size ) ;

            platform_math :: mul_wholes ( y_bottom , texture_height , grid_y ) ;
            platform_math :: div_whole_by ( y_bottom , grid_size ) ;

            platform_math :: mul_wholes ( y_top , texture_height , next_grid_y ) ;
            platform_math :: div_whole_by ( y_top , grid_size ) ;

            platform_math :: dec_whole ( x_right ) ;
            platform_math :: dec_whole ( y_top ) ;

            _draw_cell ( x_left , y_bottom , x_right , y_top ) ;
        }
    }

    _engine_rasterizer_finalize_state . requested = _platform_math_consts . get ( ) . whole_true ;
    _mediator . get ( ) . send ( typename messages :: engine_rasterizer_finalize_request ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _rasterizer_finalized ( )
{
    typename messages :: engine_render_texture_finalize msg ;
    msg . texture = _engine_render_texture_create_state . texture ;
    _mediator . get ( ) . send ( msg ) ;

    _mediator . get ( ) . send ( typename messages :: logic_room_texture_creation_finished ( ) ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _draw_cell ( num_whole x_left , num_whole y_bottom , num_whole x_right , num_whole y_top )
{
    num_whole x_center ;
    num_whole y_center ;
    num_fract pen_intensity ;
    num_fract paper_intensity ;
    num_fract alpha ;
    texel_data pen ;
    texel_data paper ;

    pen_intensity = _logic_room_stateless_consts . get ( ) . texture_pen_intensity ;
    paper_intensity = _logic_room_stateless_consts . get ( ) . texture_paper_intensity ;
    alpha = _logic_room_stateless_consts . get ( ) . texture_alpha ;

    engine_render_stateless :: set_texel_color ( pen , pen_intensity , pen_intensity , pen_intensity , alpha ) ;
    engine_render_stateless :: set_texel_color ( paper , paper_intensity , paper_intensity , paper_intensity , alpha ) ;

    platform_math :: add_wholes ( x_center , x_left , x_right ) ;
    platform_math :: add_wholes ( y_center , y_bottom , y_top ) ;
    platform_math :: div_whole_by ( x_center , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( y_center , _platform_math_consts . get ( ) . whole_2 ) ;

    _use_texel ( pen ) ;
    _draw_rect ( x_left , y_bottom , x_right , y_top ) ;
    _use_texel ( paper ) ;
    _draw_rect ( x_left , y_bottom , x_center , y_center ) ;
    _draw_rect ( x_center , y_center , x_right , y_top ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _draw_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    typename messages :: engine_rasterizer_draw_rect msg ;
    msg . x1 = x1 ;
    msg . y1 = y1 ;
    msg . x2 = x2 ;
    msg . y2 = y2 ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_room_texture < mediator > :: _use_texel ( texel_data texel )
{
    typename messages :: engine_rasterizer_use_texel msg ;
    msg . texel = texel ;
    _mediator . get ( ) . send ( msg ) ;
}

