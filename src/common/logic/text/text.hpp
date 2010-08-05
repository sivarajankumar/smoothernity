template < typename mediator >
class shy_logic_text
{
    typedef typename mediator :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: logic_text_letter_id logic_text_letter_id ;
    typedef typename mediator :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    typedef typename mediator :: engine_render_mesh_id engine_render_mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: engine_render_texture_id engine_render_texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_math_consts platform_math_consts ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;

    class _logic_text_consts_type
    {
    public :
        _logic_text_consts_type ( ) ;

        static const_int_32 max_letters_in_alphabet = 32 ;

        num_fract final_scale ;
        num_fract canvas_r ;
        num_fract canvas_g ;
        num_fract canvas_b ;
        num_fract canvas_a ;
        num_fract mesh_x ;
        num_fract mesh_y ;
        num_fract mesh_z ;
        num_whole scale_in_frames ;
        num_whole small_size ;
        num_whole big_size ;
    } ;
    
    class _tex_coords
    {
    public :
        num_fract left ;
        num_fract bottom ;
        num_fract right ;
        num_fract top ;
    } ;

    typedef typename platform_static_array :: template static_array < _tex_coords , _logic_text_consts_type :: max_letters_in_alphabet > _letters_tex_coords ;

public :
    shy_logic_text ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > ) ;
    void receive ( typename messages :: init ) ;
    void receive ( typename messages :: logic_text_prepare_permit ) ;
    void receive ( typename messages :: logic_text_render_request ) ;
    void receive ( typename messages :: logic_text_update ) ;
    void receive ( typename messages :: logic_text_use_text_texture_request ) ;
    void receive ( typename messages :: engine_render_texture_create_reply ) ;
    void receive ( typename messages :: engine_render_mesh_create_reply ) ;
    void receive ( typename messages :: logic_text_letter_big_tex_coords_request ) ;
    void receive ( typename messages :: logic_text_letter_small_tex_coords_request ) ;
    void receive ( typename messages :: engine_rasterizer_finalize_reply ) ;
private :
    shy_logic_text < mediator > & operator= ( const shy_logic_text < mediator > & ) ;
    void _render_text_mesh ( ) ;
    void _update_text_mesh ( ) ;
    void _create_text_mesh ( ) ;
    void _create_text_texture ( ) ;
    void _proceed_with_create_text ( ) ;
    void _next_letter_col ( ) ;
    void _next_letter_row ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
    void _prepare_rasterizer_for_drawing ( ) ;
    void _store_tex_coords ( logic_text_letter_id letter , _letters_tex_coords & letters_tex_coords ) ;
    void _rasterize_letter ( logic_text_letter_id letter , _letters_tex_coords & letters_tex_coords ) ;
    void _rasterize_use_texel ( texel_data texel ) ;
    void _rasterize_triangle ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 ) ;
    void _rasterize_ellipse_in_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void _rasterize_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 ) ;
    void _rasterize_english_alphabet ( num_whole letter_size_x , num_whole letter_size_y , _letters_tex_coords & letters_tex_coords ) ;
    void _rasterize_font_english_A ( ) ;
    void _rasterize_font_english_B ( ) ;
    void _rasterize_font_english_C ( ) ;
    void _rasterize_font_english_D ( ) ;
    void _rasterize_font_english_E ( ) ;
    void _rasterize_font_english_F ( ) ;
    void _rasterize_font_english_G ( ) ;
    void _rasterize_font_english_H ( ) ;
    void _rasterize_font_english_I ( ) ;
    void _rasterize_font_english_J ( ) ;
    void _rasterize_font_english_K ( ) ;
    void _rasterize_font_english_L ( ) ;
    void _rasterize_font_english_M ( ) ;
    void _rasterize_font_english_N ( ) ;
    void _rasterize_font_english_O ( ) ;
    void _rasterize_font_english_P ( ) ;
    void _rasterize_font_english_Q ( ) ;
    void _rasterize_font_english_R ( ) ;
    void _rasterize_font_english_S ( ) ;
    void _rasterize_font_english_T ( ) ;
    void _rasterize_font_english_U ( ) ;
    void _rasterize_font_english_V ( ) ;
    void _rasterize_font_english_W ( ) ;
    void _rasterize_font_english_X ( ) ;
    void _rasterize_font_english_Y ( ) ;
    void _rasterize_font_english_Z ( ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    const _logic_text_consts_type _logic_text_consts ;
    
    num_whole _texture_create_requested ;
    num_whole _texture_create_replied ;
    
    num_whole _mesh_create_requested ;
    num_whole _mesh_create_replied ;
    
    num_whole _rasterize_finalize_requested ;
    num_whole _rasterize_finalize_replied ;
    
    num_whole _empty_texture_created ;
    num_whole _small_letters_rasterized ;
    num_whole _big_letters_rasterized ;
        
    num_whole _text_mesh_created ;
    num_whole _text_prepare_permitted ;
    engine_render_mesh_id _text_mesh_id ;
    engine_render_texture_id _text_texture_id ;
    texel_data _filler ;
    texel_data _eraser ;
    num_whole _origin_x ;
    num_whole _origin_y ;
    num_whole _letter_size_x ;
    num_whole _letter_size_y ;
    num_whole _scale_frames ;
    _letters_tex_coords _letters_big ;
    _letters_tex_coords _letters_small ;
} ;

template < typename mediator >
shy_logic_text < mediator > :: shy_logic_text ( )
{
}

template < typename mediator >
shy_logic_text < mediator > & shy_logic_text < mediator > :: operator= ( const shy_logic_text < mediator > & )
{
    return * this ;
}

template < typename mediator >
shy_logic_text < mediator > :: _logic_text_consts_type :: _logic_text_consts_type ( )
{
    platform_math :: make_num_fract ( final_scale , 1 , 2 ) ;
    platform_math :: make_num_fract ( canvas_r , 255 , 255 ) ;
    platform_math :: make_num_fract ( canvas_g , 255 , 255 ) ;
    platform_math :: make_num_fract ( canvas_b , 255 , 255 ) ;
    platform_math :: make_num_fract ( canvas_a , 255 , 255 ) ;
    platform_math :: make_num_fract ( mesh_x , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_z , - 3 , 1 ) ;
    platform_math :: make_num_whole ( scale_in_frames , 60 ) ;
    platform_math :: make_num_whole ( small_size , 16 ) ;
    platform_math :: make_num_whole ( big_size , 32 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: init )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    
    _empty_texture_created = _platform_math_consts . get ( ) . whole_false ;
    _small_letters_rasterized = _platform_math_consts . get ( ) . whole_false ;
    _big_letters_rasterized = _platform_math_consts . get ( ) . whole_false ;
    _rasterize_finalize_requested = _platform_math_consts . get ( ) . whole_false ;
    _rasterize_finalize_replied = _platform_math_consts . get ( ) . whole_false ;
    _texture_create_requested = _platform_math_consts . get ( ) . whole_false ;
    _texture_create_replied = _platform_math_consts . get ( ) . whole_false ;
    _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
    _mesh_create_replied = _platform_math_consts . get ( ) . whole_false ;
    _text_mesh_created = _platform_math_consts . get ( ) . whole_false ;
    _text_prepare_permitted = _platform_math_consts . get ( ) . whole_false ;
    _scale_frames = _platform_math_consts . get ( ) . whole_0 ;
    _letter_size_x = _platform_math_consts . get ( ) . whole_0 ;
    _letter_size_y = _platform_math_consts . get ( ) . whole_0 ;
    _origin_x = _platform_math_consts . get ( ) . whole_0 ;
    _origin_y = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_use_text_texture_request )
{
    if ( platform_conditions :: whole_is_true ( _text_mesh_created ) )
    {
        typename messages :: engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = _text_texture_id ;
        _mediator . get ( ) . send ( texture_select_msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: logic_text_use_text_texture_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_letter_big_tex_coords_request msg )
{
    typename messages :: logic_text_letter_big_tex_coords_reply reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( platform_conditions :: whole_is_true ( _text_mesh_created ) )
    {
        typename platform_pointer :: template pointer < _tex_coords > coords ;
        platform_static_array :: element_ptr ( coords , _letters_big , msg . letter . _letter_id ) ;
        reply_msg . left = coords . get ( ) . left ;
        reply_msg . bottom = coords . get ( ) . bottom ;
        reply_msg . right = coords . get ( ) . right ;
        reply_msg . top = coords . get ( ) . top ;
    }
    else
    {
        reply_msg . left = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . bottom = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . right = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . top = _platform_math_consts . get ( ) . fract_0 ;
    }
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_letter_small_tex_coords_request msg )
{
    typename messages :: logic_text_letter_small_tex_coords_reply reply_msg ;
    reply_msg . letter = msg . letter ;
    if ( platform_conditions :: whole_is_true ( _text_mesh_created ) )
    {
        typename platform_pointer :: template pointer < _tex_coords > coords ;
        platform_static_array :: element_ptr ( coords , _letters_small , msg . letter . _letter_id ) ;
        reply_msg . left = coords . get ( ) . left ;
        reply_msg . bottom = coords . get ( ) . bottom ;
        reply_msg . right = coords . get ( ) . right ;
        reply_msg . top = coords . get ( ) . top ;
    }
    else
    {
        reply_msg . left = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . bottom = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . right = _platform_math_consts . get ( ) . fract_0 ;
        reply_msg . top = _platform_math_consts . get ( ) . fract_0 ;
    }
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_prepare_permit )
{
    _text_prepare_permitted = _platform_math_consts . get ( ) . whole_true ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_render_request )
{
    if ( platform_conditions :: whole_is_true ( _text_mesh_created ) )
        _render_text_mesh ( ) ;
    _mediator . get ( ) . send ( typename messages :: logic_text_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: logic_text_update )
{
    if ( platform_conditions :: whole_is_false ( _text_mesh_created ) )
        _proceed_with_create_text ( ) ;    
    if ( platform_conditions :: whole_is_true ( _text_mesh_created ) )
        _update_text_mesh ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: engine_render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_false ;
        _mesh_create_replied = _platform_math_consts . get ( ) . whole_true ;
        _text_mesh_id = msg . mesh ;
        _proceed_with_create_text ( ) ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: engine_render_texture_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _texture_create_requested ) )
    {
        _texture_create_requested = _platform_math_consts . get ( ) . whole_false ;
        _texture_create_replied = _platform_math_consts . get ( ) . whole_true ;
        _text_texture_id = msg . texture ;
        _proceed_with_create_text ( ) ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: receive ( typename messages :: engine_rasterizer_finalize_reply )
{
    if ( platform_conditions :: whole_is_true ( _rasterize_finalize_requested ) )
    {
        _rasterize_finalize_requested = _platform_math_consts . get ( ) . whole_false ;
        _rasterize_finalize_replied = _platform_math_consts . get ( ) . whole_true ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: _proceed_with_create_text ( )
{
    if ( platform_conditions :: whole_is_true ( _text_prepare_permitted ) )
    {
        _text_prepare_permitted = _platform_math_consts . get ( ) . whole_false ;
        
        _texture_create_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: engine_render_texture_create_request ( ) ) ;
        
        _mesh_create_requested = _platform_math_consts . get ( ) . whole_true ;
        typename messages :: engine_render_mesh_create_request mesh_create_msg ;
        mesh_create_msg . vertices = _platform_math_consts . get ( ) . whole_4 ;
        mesh_create_msg . triangle_strip_indices = _platform_math_consts . get ( ) . whole_4 ;
        mesh_create_msg . triangle_fan_indices = _platform_math_consts . get ( ) . whole_0 ;
        _mediator . get ( ) . send ( mesh_create_msg ) ;
    }
    else if ( platform_conditions :: whole_is_true ( _mesh_create_replied )
      && platform_conditions :: whole_is_true ( _texture_create_replied )
       )
    {
        _mesh_create_replied = _platform_math_consts . get ( ) . whole_false ;
        _texture_create_replied = _platform_math_consts . get ( ) . whole_false ;
        _create_text_mesh ( ) ;
        _create_text_texture ( ) ;
        _empty_texture_created = _platform_math_consts . get ( ) . whole_true ;
    }
    else if ( platform_conditions :: whole_is_true ( _empty_texture_created ) )
    {
        _empty_texture_created = _platform_math_consts . get ( ) . whole_false ;
        _small_letters_rasterized = _platform_math_consts . get ( ) . whole_true ;
        _rasterize_english_alphabet ( _logic_text_consts . small_size , _logic_text_consts . small_size , _letters_small ) ;
    }
    else if ( platform_conditions :: whole_is_true ( _small_letters_rasterized ) )
    {
        _small_letters_rasterized = _platform_math_consts . get ( ) . whole_false ;
        _big_letters_rasterized = _platform_math_consts . get ( ) . whole_true ;
        _rasterize_english_alphabet ( _logic_text_consts . big_size , _logic_text_consts . big_size , _letters_big ) ;
    }
    else if ( platform_conditions :: whole_is_true ( _big_letters_rasterized ) )
    {
        _big_letters_rasterized = _platform_math_consts . get ( ) . whole_false ;
        _rasterize_finalize_requested = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: engine_rasterizer_finalize_request ( ) ) ;
    }
    else if ( platform_conditions :: whole_is_true ( _rasterize_finalize_replied ) )
    {
        _rasterize_finalize_replied = _platform_math_consts . get ( ) . whole_false ;
        
        typename messages :: engine_render_texture_finalize texture_finalize_msg ;
        texture_finalize_msg . texture = _text_texture_id ;
        _mediator . get ( ) . send ( texture_finalize_msg ) ;
        
        _text_mesh_created = _platform_math_consts . get ( ) . whole_true ;
        _mediator . get ( ) . send ( typename messages :: logic_text_prepared ( ) ) ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: _update_text_mesh ( )
{
    matrix_data matrix ;
    num_fract fract_scale_frames ;    
    num_fract fract_scale_in_frames ;
    num_fract scale ;
    
    platform_math :: make_fract_from_whole ( fract_scale_frames , _scale_frames ) ;
    platform_math :: make_fract_from_whole ( fract_scale_in_frames , _logic_text_consts . scale_in_frames ) ;
    engine_math :: math_lerp 
        ( scale 
        , _platform_math_consts . get ( ) . fract_0 
        , _platform_math_consts . get ( ) . fract_0 
        , _logic_text_consts . final_scale 
        , fract_scale_in_frames 
        , fract_scale_frames 
        ) ;
    platform_matrix :: set_axis_x ( matrix , scale , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_y ( matrix , _platform_math_consts . get ( ) . fract_0 , scale , _platform_math_consts . get ( ) . fract_0 ) ;
    platform_matrix :: set_axis_z ( matrix , _platform_math_consts . get ( ) . fract_0 , _platform_math_consts . get ( ) . fract_0 , scale ) ;
    platform_matrix :: set_origin ( matrix , _logic_text_consts . mesh_x , _logic_text_consts . mesh_y , _logic_text_consts . mesh_z ) ;
    {
        typename messages :: engine_render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _text_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    }
    if ( platform_conditions :: whole_less_than_whole ( _scale_frames , _logic_text_consts . scale_in_frames ) )
        platform_math :: inc_whole ( _scale_frames ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _render_text_mesh ( )
{
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    {
        typename messages :: engine_render_texture_select texture_select_msg ;
        texture_select_msg . texture = _text_texture_id ;
        _mediator . get ( ) . send ( texture_select_msg ) ;
    }
    {
        typename messages :: engine_render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = _text_mesh_id ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: engine_render_blend_disable ( ) ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_mesh ( )
{
    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z ;
    num_fract color_r ;
    num_fract color_g ;
    num_fract color_b ;
    num_fract color_a ;
    x_left = _platform_math_consts . get ( ) . fract_minus_1 ;
    x_right = _platform_math_consts . get ( ) . fract_1 ;
    y_top = _platform_math_consts . get ( ) . fract_1 ;
    y_bottom = _platform_math_consts . get ( ) . fract_minus_1 ;
    u_left = _platform_math_consts . get ( ) . fract_0 ;
    u_right = _platform_math_consts . get ( ) . fract_1 ;
    v_top = _platform_math_consts . get ( ) . fract_1 ;
    v_bottom = _platform_math_consts . get ( ) . fract_0 ;
    z = _platform_math_consts . get ( ) . fract_0 ;
    color_r = _logic_text_consts . canvas_r ;
    color_g = _logic_text_consts . canvas_g ;
    color_b = _logic_text_consts . canvas_b ;
    color_a = _logic_text_consts . canvas_a ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_0 , x_left , y_top , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_0 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_0 , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_1 , x_left , y_bottom , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_1 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_1 , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_1 , _platform_math_consts . get ( ) . whole_1 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_2 , x_right , y_top , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_2 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_2 , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_2 , _platform_math_consts . get ( ) . whole_2 ) ;

    _mesh_set_vertex_position            ( _platform_math_consts . get ( ) . whole_3 , x_right , y_bottom , z ) ;
    _mesh_set_vertex_color               ( _platform_math_consts . get ( ) . whole_3 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( _platform_math_consts . get ( ) . whole_3 , u_right , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( _platform_math_consts . get ( ) . whole_3 , _platform_math_consts . get ( ) . whole_3 ) ;

    typename messages :: engine_render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _text_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: engine_render_mesh_set_vertex_position msg ;
    msg . mesh = _text_mesh_id ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v )
{
    typename messages :: engine_render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = _text_mesh_id ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    typename messages :: engine_render_mesh_set_vertex_color msg ;
    msg . mesh = _text_mesh_id ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: engine_render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _text_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_texture ( )
{
    num_whole texture_width ;
    num_whole texture_height ;
    num_fract filler_r ;
    num_fract filler_g ;
    num_fract filler_b ;
    num_fract filler_a ;
    num_fract eraser_r ;
    num_fract eraser_g ;
    num_fract eraser_b ;
    num_fract eraser_a ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > engine_render_stateless_consts ;
    _mediator . get ( ) . engine_render_stateless_consts ( engine_render_stateless_consts ) ;
    texture_width = engine_render_stateless_consts . get ( ) . texture_width ;
    texture_height = engine_render_stateless_consts . get ( ) . texture_height ;
    filler_r = _platform_math_consts . get ( ) . fract_1 ;
    filler_g = _platform_math_consts . get ( ) . fract_1 ;
    filler_b = _platform_math_consts . get ( ) . fract_1 ;
    filler_a = _platform_math_consts . get ( ) . fract_1 ;
    eraser_r = _platform_math_consts . get ( ) . fract_0 ;
    eraser_g = _platform_math_consts . get ( ) . fract_0 ;
    eraser_b = _platform_math_consts . get ( ) . fract_0 ;
    eraser_a = _platform_math_consts . get ( ) . fract_0 ;
    engine_render_stateless :: set_texel_color ( _filler , filler_r , filler_g , filler_b , filler_a ) ;
    engine_render_stateless :: set_texel_color ( _eraser , eraser_r , eraser_g , eraser_b , eraser_a ) ;
    
    typename messages :: engine_render_texture_set_texels_rect set_texels_msg ;
    set_texels_msg . texel = _eraser ;
    set_texels_msg . texture = _text_texture_id ;
    set_texels_msg . left = _platform_math_consts . get ( ) . whole_0 ;
    set_texels_msg . bottom = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: sub_wholes ( set_texels_msg . right , texture_width , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( set_texels_msg . top , texture_height , _platform_math_consts . get ( ) . whole_1 ) ;
    _mediator . get ( ) . send ( set_texels_msg ) ;
    
    _origin_y = texture_height ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_english_alphabet 
    ( num_whole letter_size_x , num_whole letter_size_y , _letters_tex_coords & letters_tex_coords )
{
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    const alphabet_english_type & eng = logic_text_stateless_consts . get ( ) . alphabet_english ;
    _letter_size_x = letter_size_x ;
    _letter_size_y = letter_size_y ;
    _next_letter_row ( ) ;
    _rasterize_letter ( eng . A , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . B , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . C , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . D , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . E , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . F , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . G , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . H , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . I , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . J , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . K , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . L , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . M , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . N , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . O , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . P , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . Q , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . R , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . S , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . T , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . U , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . V , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . W , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . X , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . Y , letters_tex_coords ) ; _next_letter_col ( ) ;
    _rasterize_letter ( eng . Z , letters_tex_coords ) ; _next_letter_col ( ) ;
    _next_letter_row ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_col ( )
{
    num_whole delta_x ;
    num_whole texture_width ;
    num_whole right_limit ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > engine_render_stateless_consts ;
    _mediator . get ( ) . engine_render_stateless_consts ( engine_render_stateless_consts ) ;
    texture_width = engine_render_stateless_consts . get ( ) . texture_width ;
    platform_math :: div_wholes ( delta_x , _letter_size_x , _platform_math_consts . get ( ) . whole_8 ) ;
    platform_math :: add_to_whole ( _origin_x , _letter_size_x ) ;
    platform_math :: add_to_whole ( _origin_x , delta_x ) ;
    platform_math :: sub_wholes ( right_limit , texture_width , _letter_size_x ) ;
    if ( platform_conditions :: whole_greater_or_equal_to_whole ( _origin_x , right_limit ) )
    {
        num_whole delta_y ;
        platform_math :: div_wholes ( delta_y , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
        platform_math :: sub_from_whole ( _origin_y , delta_y ) ;
        _next_letter_row ( ) ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_row ( )
{
    platform_math :: sub_from_whole ( _origin_y , _letter_size_y ) ;
    _origin_x = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _store_tex_coords ( logic_text_letter_id letter , _letters_tex_coords & letters_tex_coords )
{
    num_whole whole_left ;
    num_whole whole_bottom ;
    num_whole whole_right ;
    num_whole whole_top ;
    num_whole whole_texture_width ;
    num_whole whole_texture_height ;
    num_fract fract_texture_width ;
    num_fract fract_texture_height ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > engine_render_stateless_consts ;
    typename platform_pointer :: template pointer < _tex_coords > coords ;

    _mediator . get ( ) . engine_render_stateless_consts ( engine_render_stateless_consts ) ;
    platform_static_array :: element_ptr ( coords , letters_tex_coords , letter . _letter_id ) ;    
    
    whole_left = _origin_x ;
    whole_bottom = _origin_y ;
    platform_math :: add_wholes ( whole_right , _origin_x , _letter_size_x ) ;
    platform_math :: add_wholes ( whole_top , _origin_y , _letter_size_y ) ;
    whole_texture_width = engine_render_stateless_consts . get ( ) . texture_width ;
    whole_texture_height = engine_render_stateless_consts . get ( ) . texture_height ;
    platform_math :: make_fract_from_whole ( fract_texture_width , whole_texture_width ) ;
    platform_math :: make_fract_from_whole ( fract_texture_height , whole_texture_height ) ;
    platform_math :: make_fract_from_whole ( coords . get ( ) . left , whole_left ) ;
    platform_math :: make_fract_from_whole ( coords . get ( ) . bottom , whole_bottom ) ;
    platform_math :: make_fract_from_whole ( coords . get ( ) . right , whole_right ) ;
    platform_math :: make_fract_from_whole ( coords . get ( ) . top , whole_top ) ;
    platform_math :: div_fract_by ( coords . get ( ) . left , fract_texture_width ) ;
    platform_math :: div_fract_by ( coords . get ( ) . bottom , fract_texture_height ) ;
    platform_math :: div_fract_by ( coords . get ( ) . right , fract_texture_width ) ;
    platform_math :: div_fract_by ( coords . get ( ) . top , fract_texture_height ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _prepare_rasterizer_for_drawing ( )
{
    typename messages :: engine_rasterizer_use_texture rasterize_use_texture_msg ;
    rasterize_use_texture_msg . texture = _text_texture_id ;
    rasterize_use_texture_msg . origin_x = _origin_x ;
    rasterize_use_texture_msg . origin_y = _origin_y ;
    _mediator . get ( ) . send ( rasterize_use_texture_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_letter ( logic_text_letter_id letter , _letters_tex_coords & letters_tex_coords )
{
    typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > logic_text_stateless_consts ;
    _mediator . get ( ) . logic_text_stateless_consts ( logic_text_stateless_consts ) ;
    const alphabet_english_type & eng = logic_text_stateless_consts . get ( ) . alphabet_english ;
    
    _store_tex_coords ( letter , letters_tex_coords ) ;
    if      ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . A . _letter_id ) ) _rasterize_font_english_A ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . B . _letter_id ) ) _rasterize_font_english_B ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . C . _letter_id ) ) _rasterize_font_english_C ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . D . _letter_id ) ) _rasterize_font_english_D ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . E . _letter_id ) ) _rasterize_font_english_E ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . F . _letter_id ) ) _rasterize_font_english_F ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . G . _letter_id ) ) _rasterize_font_english_G ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . H . _letter_id ) ) _rasterize_font_english_H ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . I . _letter_id ) ) _rasterize_font_english_I ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . J . _letter_id ) ) _rasterize_font_english_J ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . K . _letter_id ) ) _rasterize_font_english_K ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . L . _letter_id ) ) _rasterize_font_english_L ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . M . _letter_id ) ) _rasterize_font_english_M ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . N . _letter_id ) ) _rasterize_font_english_N ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . O . _letter_id ) ) _rasterize_font_english_O ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . P . _letter_id ) ) _rasterize_font_english_P ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . Q . _letter_id ) ) _rasterize_font_english_Q ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . R . _letter_id ) ) _rasterize_font_english_R ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . S . _letter_id ) ) _rasterize_font_english_S ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . T . _letter_id ) ) _rasterize_font_english_T ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . U . _letter_id ) ) _rasterize_font_english_U ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . V . _letter_id ) ) _rasterize_font_english_V ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . W . _letter_id ) ) _rasterize_font_english_W ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . X . _letter_id ) ) _rasterize_font_english_X ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . Y . _letter_id ) ) _rasterize_font_english_Y ( ) ;
    else if ( platform_conditions :: wholes_are_equal ( letter . _letter_id , eng . Z . _letter_id ) ) _rasterize_font_english_Z ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_use_texel ( texel_data texel )
{
    typename messages :: engine_rasterizer_use_texel rasterize_use_texel_msg ;
    rasterize_use_texel_msg . texel = texel ;
    _mediator . get ( ) . send ( rasterize_use_texel_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_triangle ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 , num_whole x3 , num_whole y3 )
{
    typename messages :: engine_rasterizer_draw_triangle rasterize_triangle_msg ;
    rasterize_triangle_msg . x1 = x1 ;
    rasterize_triangle_msg . y1 = y1 ;
    rasterize_triangle_msg . x2 = x2 ;
    rasterize_triangle_msg . y2 = y2 ;
    rasterize_triangle_msg . x3 = x3 ;
    rasterize_triangle_msg . y3 = y3 ;
    _mediator . get ( ) . send ( rasterize_triangle_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_ellipse_in_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    typename messages :: engine_rasterizer_draw_ellipse_in_rect rasterize_ellipse_in_rect_msg ;
    rasterize_ellipse_in_rect_msg . x1 = x1 ;
    rasterize_ellipse_in_rect_msg . y1 = y1 ;
    rasterize_ellipse_in_rect_msg . x2 = x2 ;
    rasterize_ellipse_in_rect_msg . y2 = y2 ;
    _mediator . get ( ) . send ( rasterize_ellipse_in_rect_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_rect ( num_whole x1 , num_whole y1 , num_whole x2 , num_whole y2 )
{
    typename messages :: engine_rasterizer_draw_rect rasterize_rect_msg ;
    rasterize_rect_msg . x1 = x1 ;
    rasterize_rect_msg . y1 = y1 ;
    rasterize_rect_msg . x2 = x2 ;
    rasterize_rect_msg . y2 = y2 ;
    _mediator . get ( ) . send ( rasterize_rect_msg ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_A ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole outer_top ;
    num_whole outer_bottom = _platform_math_consts . get ( ) . whole_0 ;
    num_whole outer_center ;
    num_whole outer_left = _platform_math_consts . get ( ) . whole_0 ;
    num_whole outer_right ;
    platform_math :: sub_wholes ( outer_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: div_wholes ( outer_center , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: sub_wholes ( outer_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( outer_center , outer_top , outer_left , outer_bottom , outer_right , outer_bottom ) ;

    num_whole inner_top ;
    num_whole inner_bottom = _platform_math_consts . get ( ) . whole_0 ;
    num_whole inner_center ;
    num_whole inner_left ;
    num_whole inner_right ;
    platform_math :: mul_wholes ( inner_top , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( inner_top , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_wholes ( inner_center , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_wholes ( inner_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( inner_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( inner_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_triangle ( inner_center , inner_top , inner_left , inner_bottom , inner_right , inner_bottom ) ;

    num_whole board_top ;
    num_whole board_bottom ;    
    num_whole outer_left_minus_center ;
    num_whole outer_right_minus_center ;
    num_whole outer_top_minus_board_top ;
    num_whole outer_top_minus_board_bottom ;
    num_whole outer_top_minus_bottom ;
    num_whole board_top_left ;
    num_whole board_bottom_left ;
    num_whole board_top_right ;
    num_whole board_bottom_right ;
    platform_math :: mul_wholes ( board_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( board_top , _platform_math_consts . get ( ) . whole_7 ) ;
    platform_math :: mul_wholes ( board_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( board_bottom , _platform_math_consts . get ( ) . whole_7 ) ;
    platform_math :: sub_wholes ( outer_left_minus_center , outer_left , outer_center ) ;
    platform_math :: sub_wholes ( outer_right_minus_center , outer_right , outer_center ) ;
    platform_math :: sub_wholes ( outer_top_minus_board_top , outer_top , board_top ) ;
    platform_math :: sub_wholes ( outer_top_minus_board_bottom , outer_top , board_bottom ) ;
    platform_math :: sub_wholes ( outer_top_minus_bottom , outer_top , outer_bottom ) ;    
    platform_math :: mul_wholes ( board_top_left , outer_left_minus_center , outer_top_minus_board_top ) ;
    platform_math :: div_whole_by ( board_top_left , outer_top_minus_bottom ) ;
    platform_math :: add_to_whole ( board_top_left , outer_center ) ;
    platform_math :: mul_wholes ( board_bottom_left , outer_left_minus_center , outer_top_minus_board_bottom ) ;
    platform_math :: div_whole_by ( board_bottom_left , outer_top_minus_bottom ) ;
    platform_math :: add_to_whole ( board_bottom_left , outer_center ) ;
    platform_math :: mul_wholes ( board_top_right , outer_right_minus_center , outer_top_minus_board_top ) ;
    platform_math :: div_whole_by ( board_top_right , outer_top_minus_bottom ) ;
    platform_math :: add_to_whole ( board_top_right , outer_center ) ;
    platform_math :: mul_wholes ( board_bottom_right , outer_right_minus_center , outer_top_minus_board_bottom ) ;
    platform_math :: div_whole_by ( board_bottom_right , outer_top_minus_bottom ) ;
    platform_math :: add_to_whole ( board_bottom_right , outer_center ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( board_top_left , board_top , board_bottom_left , board_bottom , board_bottom_right , board_bottom ) ;
    _rasterize_triangle ( board_top_left , board_top , board_top_right , board_top , board_bottom_right , board_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_B ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole ellipse_y_top ;
    num_whole ellipse_y_mid ;
    num_whole ellipse_x_right ;
    platform_math :: sub_wholes ( ellipse_y_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: div_wholes ( ellipse_y_mid , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: sub_wholes ( ellipse_x_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , ellipse_x_right , ellipse_y_mid ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , ellipse_y_mid , ellipse_x_right , ellipse_y_top ) ;

    num_whole spine_right ;
    num_whole spine_top ;
    platform_math :: div_wholes ( spine_right , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: sub_wholes ( spine_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , spine_top , spine_right , _platform_math_consts . get ( ) . whole_0 ) ;
    
    num_whole hole_divider ;
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_height ;
    num_whole hole_top_minus_height ;
    num_whole hole_bottom_plus_height ;
    platform_math :: make_num_whole ( hole_divider , 16 ) ;
    platform_math :: mul_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_left , hole_divider ) ;
    platform_math :: make_num_whole ( hole_right , 12 ) ;
    platform_math :: mul_whole_by ( hole_right , _letter_size_x ) ;
    platform_math :: div_whole_by ( hole_right , hole_divider ) ;
    platform_math :: make_num_whole ( hole_top , 13 ) ;
    platform_math :: mul_whole_by ( hole_top , _letter_size_y ) ;
    platform_math :: div_whole_by ( hole_top , hole_divider ) ;
    platform_math :: mul_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_bottom , hole_divider ) ;
    platform_math :: mul_wholes ( hole_height , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_height , hole_divider ) ;
    platform_math :: sub_wholes ( hole_top_minus_height , hole_top , hole_height ) ;
    platform_math :: add_wholes ( hole_bottom_plus_height , hole_bottom , hole_height ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_top_minus_height ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_bottom , hole_right , hole_bottom_plus_height ) ;
    
    num_whole hole_center_x ;
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , hole_top , hole_center_x , hole_top_minus_height ) ;
    _rasterize_rect ( hole_left , hole_bottom , hole_center_x , hole_bottom_plus_height ) ;    
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_C ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    num_whole hole_center_x ;
    num_whole hole_center_top ;
    num_whole hole_center_bottom ;
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: mul_wholes ( hole_center_top , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_whole_by ( hole_center_top , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_center_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_center_bottom , _platform_math_consts . get ( ) . whole_7 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_D ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;

    num_whole half_size_x ;
    platform_math :: div_wholes ( half_size_x , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , half_size_x , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole hole_center_x ;
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , hole_top , hole_center_x , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_E ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole right ;
    num_whole top_limit ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    num_whole hole_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( hole_mid_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_mid_top , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( hole_mid_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_mid_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_F ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: sub_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_mid_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_mid_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_mid_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_mid_bottom , _platform_math_consts . get ( ) . whole_5 ) ;        
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _rasterize_rect ( hole_left , hole_mid_bottom , hole_right , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_G ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    num_whole hole_center_x ;
    num_whole hole_center_top ;
    num_whole hole_center_bottom ;
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: mul_wholes ( hole_center_top , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_whole_by ( hole_center_top , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_center_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_center_bottom , _platform_math_consts . get ( ) . whole_7 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
    
    num_whole brick_top ;
    num_whole brick_bottom ;
    num_whole brick_left ;
    num_whole brick_right ;
    platform_math :: mul_wholes ( brick_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( brick_top , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( brick_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( brick_bottom , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( brick_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( brick_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( brick_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( brick_left , brick_top , brick_right , brick_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_H ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;        
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_mid_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_mid_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_mid_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_mid_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , top_limit , hole_right , hole_mid_top ) ;
    _rasterize_rect ( hole_left , hole_mid_bottom , hole_right , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_I ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_6 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_7 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_mid_left ;
    num_whole hole_mid_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform_math :: mul_wholes ( hole_mid_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_mid_left , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_mid_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_mid_right , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , hole_top , hole_mid_left , hole_bottom ) ;
    _rasterize_rect ( hole_mid_right , hole_top , right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_J ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    num_whole circle_top ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( circle_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( circle_top , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , circle_top ) ;

    num_whole circle_center_y ;
    platform_math :: div_wholes ( circle_center_y , circle_top , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , circle_center_y , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole hole_center_y ;
    platform_math :: add_wholes ( hole_center_y , hole_top , hole_bottom ) ;
    platform_math :: div_whole_by ( hole_center_y , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , circle_top , hole_right , hole_center_y ) ;
    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , top_limit , hole_left , hole_center_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_K ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right_limit ;
    num_whole half_size_y ;    
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: div_wholes ( half_size_y , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;

    num_whole hole_1_left ;
    platform_math :: mul_wholes ( hole_1_left , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_1_left , _platform_math_consts . get ( ) . whole_9 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_triangle ( hole_1_left , half_size_y , right_limit , top_limit , right_limit , _platform_math_consts . get ( ) . whole_0 ) ;

    num_whole hole_2_right ;
    platform_math :: mul_wholes ( hole_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_6 ) ;
    platform_math :: div_whole_by ( hole_2_right , _platform_math_consts . get ( ) . whole_9 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_triangle ( _platform_math_consts . get ( ) . whole_0 , top_limit , hole_2_right , top_limit , _platform_math_consts . get ( ) . whole_0 , half_size_y ) ;

    _rasterize_use_texel ( _eraser ) ;
    _rasterize_triangle ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , hole_2_right , _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , half_size_y ) ;

    num_whole spine_right ;
    platform_math :: div_wholes ( spine_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , spine_right , top_limit ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_L ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , top_limit , right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_M ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole spine_1_right ;
    num_whole spine_2_left ;
    num_whole spine_2_right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( spine_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( spine_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( spine_2_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( spine_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( spine_2_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , spine_1_right , top_limit ) ;
    _rasterize_rect ( spine_2_left , _platform_math_consts . get ( ) . whole_0 , spine_2_right , top_limit ) ;

    num_whole board_height ;
    num_whole board_center_x ;
    num_whole top_minus_board_height ;
    platform_math :: mul_wholes ( board_height , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( board_height , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( board_center_x , spine_2_right , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: sub_wholes ( top_minus_board_height , _letter_size_y , board_height ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( spine_1_right , top_limit , board_center_x , board_height , board_center_x , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , board_center_x , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( board_center_x , board_height , spine_2_left , top_limit , spine_2_left , top_minus_board_height ) ;
    _rasterize_triangle ( board_center_x , board_height , board_center_x , _platform_math_consts . get ( ) . whole_0 , spine_2_left , top_minus_board_height ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_N ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole spine_1_right ;
    num_whole spine_2_left ;
    num_whole spine_2_right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( spine_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( spine_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( spine_2_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( spine_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( spine_2_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , spine_1_right , top_limit ) ;
    _rasterize_rect ( spine_2_left , _platform_math_consts . get ( ) . whole_0 , spine_2_right , top_limit ) ;
    
    num_whole board_height ;
    num_whole top_minus_board_height ;
    platform_math :: div_wholes ( board_height , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;    
    platform_math :: sub_wholes ( top_minus_board_height , _letter_size_y , board_height ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( spine_1_right , top_limit , spine_2_left , board_height , spine_2_left , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , spine_2_left , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_O ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_P ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole spine_right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( spine_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , spine_right , top_limit ) ;
    
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_bottom ;
    platform_math :: div_wholes ( ellipse_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: sub_wholes ( ellipse_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( ellipse_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( ellipse_bottom , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( ellipse_left , top_limit , ellipse_right , ellipse_bottom ) ;
    
    num_whole ellipse_center_x ;
    platform_math :: add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    platform_math :: div_whole_by ( ellipse_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( spine_right , top_limit , ellipse_center_x , ellipse_bottom ) ;

    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_center_x ;
    platform_math :: mul_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_left , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Q ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right_limit ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: sub_wholes ( right_limit , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole board_width ;
    num_whole board_left ;
    num_whole board_top ;
    num_whole right_minus_board_width ;
    num_whole left_plus_board_width ;
    platform_math :: div_wholes ( board_width , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( board_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: mul_wholes ( board_top , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( board_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( right_minus_board_width , _letter_size_x , board_width ) ;
    platform_math :: add_wholes ( left_plus_board_width , board_left , board_width ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( board_left , board_top , right_minus_board_width , _platform_math_consts . get ( ) . whole_0 , _letter_size_x , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( board_left , board_top , left_plus_board_width , board_top , _letter_size_x , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_R ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole top_limit ;
    num_whole spine_right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( spine_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , spine_right , top_limit ) ;
    
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_top ;
    num_whole ellipse_bottom ;
    platform_math :: div_wholes ( ellipse_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: sub_wholes ( ellipse_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: sub_wholes ( ellipse_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( ellipse_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( ellipse_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;
    
    num_whole ellipse_center_x ;
    platform_math :: add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    platform_math :: div_whole_by ( ellipse_center_x , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( spine_right , ellipse_top , ellipse_center_x , ellipse_bottom ) ;

    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_center_x ;
    platform_math :: mul_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_left , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform_math :: div_whole_by ( hole_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;

    num_whole board_width ;
    num_whole right_minus_board_width ;
    num_whole spine_plus_board_width ;
    platform_math :: mul_wholes ( board_width , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( board_width , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: sub_wholes ( right_minus_board_width , _letter_size_x , board_width ) ;    
    platform_math :: add_wholes ( spine_plus_board_width , spine_right , board_width ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( spine_right , ellipse_bottom , right_minus_board_width , _platform_math_consts . get ( ) . whole_0 , _letter_size_x , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( spine_right , ellipse_bottom , spine_plus_board_width , ellipse_bottom , _letter_size_x , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_S ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole circle_high_left ;
    num_whole circle_high_right ;
    num_whole circle_high_top ;
    num_whole circle_high_bottom ;
    circle_high_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( circle_high_right , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: sub_wholes ( circle_high_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( circle_high_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( circle_high_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( circle_high_left , circle_high_top , circle_high_right , circle_high_bottom ) ;
    
    num_whole circle_low_left ;
    num_whole circle_low_right ;
    num_whole circle_low_top ;
    num_whole circle_low_bottom ;
    platform_math :: div_wholes ( circle_low_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    platform_math :: sub_wholes ( circle_low_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( circle_low_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( circle_low_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    circle_low_bottom = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_ellipse_in_rect ( circle_low_left , circle_low_top , circle_low_right , circle_low_bottom ) ;

    num_whole board_mid_left ;
    num_whole board_mid_right ;
    num_whole board_mid_top ;
    num_whole board_mid_bottom ;
    platform_math :: div_wholes ( board_mid_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: mul_wholes ( board_mid_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( board_mid_right , _platform_math_consts . get ( ) . whole_4 ) ;    
    board_mid_top = circle_low_top ;
    board_mid_bottom = circle_high_bottom ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( board_mid_left , board_mid_top , board_mid_right , board_mid_bottom ) ;
    
    num_whole board_high_left ;
    num_whole board_high_right ;
    num_whole board_high_top ;
    num_whole board_high_bottom ;
    board_high_left = board_mid_left ;    
    platform_math :: mul_wholes ( board_high_right , _letter_size_x , _platform_math_consts . get ( ) . whole_8 ) ;
    platform_math :: div_whole_by ( board_high_right , _platform_math_consts . get ( ) . whole_9 ) ;
    platform_math :: sub_wholes ( board_high_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( board_high_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( board_high_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( board_high_left , board_high_top , board_high_right , board_high_bottom ) ;
    
    num_whole board_low_left ;
    num_whole board_low_right ;
    num_whole board_low_top ;
    num_whole board_low_bottom ;
    platform_math :: div_wholes ( board_low_left , _letter_size_x , _platform_math_consts . get ( ) . whole_9 ) ;    
    board_low_right = board_mid_right ;
    platform_math :: div_wholes ( board_low_top , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    board_low_bottom = _platform_math_consts . get ( ) . whole_0 ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( board_low_left , board_low_top , board_low_right , board_low_bottom ) ;
        
    num_whole hole_high_left ;
    num_whole hole_high_right ;
    num_whole hole_high_top ;
    num_whole hole_high_bottom ;
    platform_math :: div_wholes ( hole_high_left , _letter_size_x , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: div_wholes ( hole_high_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;    
    platform_math :: sub_wholes ( hole_high_top , board_high_bottom , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: add_wholes ( hole_high_bottom , board_mid_top , _platform_math_consts . get ( ) . whole_1 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_high_left , hole_high_top , hole_high_right , hole_high_bottom ) ;

    num_whole hole_low_left ;
    num_whole hole_low_right ;
    num_whole hole_low_top ;
    num_whole hole_low_bottom ;
    platform_math :: mul_wholes ( hole_low_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_low_left , _platform_math_consts . get ( ) . whole_3 ) ;    
    platform_math :: mul_wholes ( hole_low_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: div_whole_by ( hole_low_right , _platform_math_consts . get ( ) . whole_6 ) ;    
    platform_math :: sub_wholes ( hole_low_top , board_mid_bottom , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: add_wholes ( hole_low_bottom , board_low_top , _platform_math_consts . get ( ) . whole_1 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_low_left , hole_low_top , hole_low_right , hole_low_bottom ) ;
    
    num_whole hole_high_center_x ;
    platform_math :: add_wholes ( hole_high_center_x , hole_high_left , hole_high_right ) ;
    platform_math :: div_whole_by ( hole_high_center_x , _platform_math_consts . get ( ) . whole_2 ) ;    
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_high_center_x , hole_high_top , circle_high_right , hole_high_bottom ) ;
    
    num_whole hole_low_center_x ;
    platform_math :: add_wholes ( hole_low_center_x , hole_low_left , hole_low_right ) ;
    platform_math :: div_whole_by ( hole_low_center_x , _platform_math_consts . get ( ) . whole_2 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( circle_low_left , hole_low_top , hole_low_center_x , hole_low_bottom ) ;    
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_T ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    platform_math :: mul_wholes ( right , _letter_size_x , _platform_math_consts . get ( ) . whole_6 ) ;
    platform_math :: div_whole_by ( right , _platform_math_consts . get ( ) . whole_7 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( _platform_math_consts . get ( ) . whole_0 , _platform_math_consts . get ( ) . whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_mid_left ;
    num_whole hole_mid_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    hole_left = _platform_math_consts . get ( ) . whole_0 ;
    hole_right = right ;    
    platform_math :: mul_wholes ( hole_mid_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( hole_mid_left , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_mid_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_mid_right , _platform_math_consts . get ( ) . whole_7 ) ;    
    platform_math :: mul_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hole_top , _platform_math_consts . get ( ) . whole_5 ) ;    
    hole_bottom = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_rect ( hole_left , hole_top , hole_mid_left , hole_bottom ) ;
    _rasterize_rect ( hole_mid_right , hole_top , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_U ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole top_limit ;
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_top ;
    num_whole ellipse_bottom ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    ellipse_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: mul_wholes ( ellipse_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( ellipse_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: div_wholes ( ellipse_top , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;    
    ellipse_bottom = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;    
    
    num_whole ellipse_center_y ;
    platform_math :: div_wholes ( ellipse_center_y , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( ellipse_left , top_limit , ellipse_right , ellipse_center_y ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform_math :: div_wholes ( hole_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: add_to_whole ( hole_left , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( hole_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( hole_right , _platform_math_consts . get ( ) . whole_5 ) ;
    platform_math :: sub_from_whole ( hole_right , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( hole_top , _letter_size_y , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: sub_from_whole ( hole_top , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( hole_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_6 ) ;
    platform_math :: add_to_whole ( hole_bottom , _platform_math_consts . get ( ) . whole_1 ) ;
    _rasterize_use_texel ( _eraser ) ;
    _rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _rasterize_rect ( hole_left , top_limit , hole_right , ellipse_center_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_V ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole top_limit ;
    num_whole high_1_left ;
    num_whole high_1_right ;
    num_whole high_2_left ;
    num_whole high_2_right ;
    num_whole low_left ;
    num_whole low_right ;
    platform_math :: sub_wholes ( top_limit , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;
    high_1_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( high_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( high_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( high_2_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( high_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( low_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( low_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( low_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( low_right , _platform_math_consts . get ( ) . whole_5 ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( high_1_left , top_limit , high_1_right , top_limit , low_right , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( high_1_left , top_limit , low_left , _platform_math_consts . get ( ) . whole_0 , low_right , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( high_2_left , top_limit , high_2_right , top_limit , low_right , _platform_math_consts . get ( ) . whole_0 ) ;
    _rasterize_triangle ( high_2_left , top_limit , low_left , _platform_math_consts . get ( ) . whole_0 , low_right , _platform_math_consts . get ( ) . whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_W ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole high_1_left ;
    num_whole high_1_right ;
    num_whole high_2_left ;
    num_whole high_2_right ;
    num_whole high_3_left ;
    num_whole high_3_right ;
    num_whole low_1_left ;
    num_whole low_1_right ;
    num_whole low_2_left ;
    num_whole low_2_right ;
    num_whole high_top ;
    num_whole low_bottom ;
    high_1_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( high_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( high_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( high_2_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( high_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( high_2_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( high_3_left , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( high_3_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( high_3_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: div_wholes ( low_1_left , _letter_size_x , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( low_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( low_1_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( low_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( low_2_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( low_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( low_2_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( high_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    low_bottom = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_1_right , low_bottom ) ;
    _rasterize_triangle ( high_1_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    _rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_1_right , low_bottom ) ;
    _rasterize_triangle ( high_2_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    _rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_2_right , low_bottom ) ;
    _rasterize_triangle ( high_2_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
    _rasterize_triangle ( high_3_left , high_top , high_3_right , high_top , low_2_right , low_bottom ) ;
    _rasterize_triangle ( high_3_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_X ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole left_1 ;
    num_whole right_1 ;
    num_whole left_2 ;
    num_whole right_2 ;
    num_whole top_y ;
    num_whole bottom_y ;
    left_1 = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( right_1 , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: mul_wholes ( left_2 , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( left_2 , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: sub_wholes ( right_2 , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: sub_wholes ( top_y , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    bottom_y = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( left_1 , top_y , right_1 , top_y , right_2 , bottom_y ) ;
    _rasterize_triangle ( left_1 , top_y , left_2 , bottom_y , right_2 , bottom_y ) ;
    _rasterize_triangle ( left_2 , top_y , right_2 , top_y , right_1 , bottom_y ) ;
    _rasterize_triangle ( left_2 , top_y , left_1 , bottom_y , right_1 , bottom_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Y ( )
{
    _prepare_rasterizer_for_drawing ( ) ;

    num_whole high_1_left ;
    num_whole high_1_right ;
    num_whole high_2_left ;
    num_whole high_2_right ;
    num_whole high_top ;
    num_whole low_left ;
    num_whole low_right ;
    num_whole low_bottom ;
    num_whole mid_y ;
    high_1_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( high_1_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: mul_wholes ( high_2_left , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( high_2_left , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: sub_wholes ( high_2_right , _letter_size_x , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: sub_wholes ( high_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( low_left , _letter_size_x , _platform_math_consts . get ( ) . whole_2 ) ;
    platform_math :: div_whole_by ( low_left , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: mul_wholes ( low_right , _letter_size_x , _platform_math_consts . get ( ) . whole_3 ) ;
    platform_math :: div_whole_by ( low_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    low_bottom = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: div_wholes ( mid_y , _letter_size_y , _platform_math_consts . get ( ) . whole_2 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_right , mid_y ) ;
    _rasterize_triangle ( high_1_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    _rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_right , mid_y ) ;
    _rasterize_triangle ( high_2_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    _rasterize_rect ( low_left , mid_y , low_right , low_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Z ( )
{
    _prepare_rasterizer_for_drawing ( ) ;
    
    num_whole hor_left ;
    num_whole hor_right ;
    num_whole high_top ;
    num_whole high_bottom ;
    hor_left = _platform_math_consts . get ( ) . whole_0 ;
    platform_math :: mul_wholes ( hor_right , _letter_size_x , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( hor_right , _platform_math_consts . get ( ) . whole_5 ) ;    
    platform_math :: sub_wholes ( high_top , _letter_size_y , _platform_math_consts . get ( ) . whole_1 ) ;    
    platform_math :: mul_wholes ( high_bottom , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;
    platform_math :: div_whole_by ( high_bottom , _platform_math_consts . get ( ) . whole_5 ) ;    
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( hor_left , high_top , hor_right , high_bottom ) ;
    
    num_whole low_top ;
    num_whole low_bottom ;
    platform_math :: div_wholes ( low_top , _letter_size_y , _platform_math_consts . get ( ) . whole_5 ) ;    
    low_bottom = _platform_math_consts . get ( ) . whole_0 ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_rect ( hor_left , low_top , hor_right , low_bottom ) ;
    
    num_whole board_width ;
    num_whole right_minus_board_width ;
    platform_math :: div_wholes ( board_width , _letter_size_y , _platform_math_consts . get ( ) . whole_4 ) ;    
    platform_math :: sub_wholes ( right_minus_board_width , hor_right , board_width ) ;
    _rasterize_use_texel ( _filler ) ;
    _rasterize_triangle ( right_minus_board_width , high_bottom , hor_right , high_bottom , board_width , low_top ) ;
    _rasterize_triangle ( right_minus_board_width , high_bottom , hor_left , low_top , board_width , low_top ) ;
}
