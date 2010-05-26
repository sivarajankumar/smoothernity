template < typename mediator >
class shy_logic_text
{
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _canvas_r = 255 ;
    static const_int_32 _canvas_g = 255 ;
    static const_int_32 _canvas_b = 255 ;
    static const_int_32 _canvas_a = 255 ;
    static const num_fract _final_scale ( ) { num_fract n ; platform :: math_make_num_fract ( n , 1 , 2 ) ; return n ; }
public :
    shy_logic_text ( mediator * arg_mediator ) ;
    void text_prepare_permit ( ) ;
    void text_render ( ) ;
    void text_update ( ) ;
private :
    void _render_text_mesh ( ) ;
    void _update_text_mesh ( ) ;
    void _create_text_mesh ( ) ;
    void _create_text_texture ( ) ;
    void _next_letter_col ( ) ;
    void _next_letter_row ( ) ;
    void _rasterize_english_alphabet ( num_whole letter_size_x , num_whole letter_size_y ) ;
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
    void _rasterize_font_whitespace ( ) ;
private :
    mediator * _mediator ;
    num_whole _text_mesh_created ;
    num_whole _text_prepare_permitted ;
    mesh_id _text_mesh_id ;
    texture_id _text_texture_id ;
    texel_data _filler ;
    texel_data _eraser ;
    num_whole _origin_x ;
    num_whole _origin_y ;
    num_whole _letter_size_x ;
    num_whole _letter_size_y ;
    num_whole _scale_frames ;
} ;

template < typename mediator >
shy_logic_text < mediator > :: shy_logic_text ( mediator * arg_mediator )
: _mediator ( arg_mediator )
{
    platform :: math_make_num_whole ( _text_mesh_created , false ) ;
    platform :: math_make_num_whole ( _text_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _scale_frames , 0 ) ;
    platform :: math_make_num_whole ( _letter_size_x , 0 ) ;
    platform :: math_make_num_whole ( _letter_size_y , 0 ) ;
    platform :: math_make_num_whole ( _origin_x , 0 ) ;
    platform :: math_make_num_whole ( _origin_y , 0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: text_prepare_permit ( )
{
    platform :: math_make_num_whole ( _text_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: text_render ( )
{
    if ( platform :: condition_true ( _text_mesh_created ) )
        _render_text_mesh ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: text_update ( )
{
    if ( platform :: condition_true ( _text_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _text_mesh_created ) )
        {
            _create_text_mesh ( ) ;
            _create_text_texture ( ) ;
            platform :: math_make_num_whole ( _text_mesh_created , true ) ;
            _mediator -> text_prepared ( ) ;
        }
    }
    if ( platform :: condition_true ( _text_mesh_created ) )
        _update_text_mesh ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _update_text_mesh ( )
{
    matrix_data matrix ;
    num_fract fract_scale_frames ;    
    num_whole whole_scale_in_frames ;
    num_fract fract_scale_in_frames ;
    num_fract scale ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    
    platform :: math_make_fract_from_whole ( fract_scale_frames , _scale_frames ) ;
    platform :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    _mediator -> math_lerp ( scale , platform :: fract_0 , platform :: fract_0 , _final_scale ( ) , fract_scale_in_frames , fract_scale_frames ) ;
    platform :: math_make_num_fract ( origin_x , - 1 , 2 ) ;
    platform :: math_make_num_fract ( origin_y , 0 , 1 ) ;
    platform :: math_make_num_fract ( origin_z , - 3 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , scale , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , platform :: fract_0 , scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , scale ) ;
    platform :: matrix_set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    _mediator -> mesh_set_transform ( _text_mesh_id , matrix ) ;
    if ( platform :: condition_whole_less_than_whole ( _scale_frames , whole_scale_in_frames ) )
        platform :: math_inc_whole ( _scale_frames ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _render_text_mesh ( )
{
    platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    _mediator -> texture_select ( _text_texture_id ) ;
    _mediator -> mesh_render ( _text_mesh_id ) ;
    platform :: render_blend_disable ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_mesh ( )
{
    vertex_data vertices [ 4 ] ;
    index_data indices [ 4 ] ;

    num_fract x_left ;
    num_fract x_right ;
    num_fract y_top ;
    num_fract y_bottom ;
    num_fract u_left ;
    num_fract u_right ;
    num_fract v_top ;
    num_fract v_bottom ;
    num_fract z ;
    num_whole color_r ;
    num_whole color_g ;
    num_whole color_b ;
    num_whole color_a ;
    num_whole index ;
    platform :: math_make_num_fract ( x_left , - 1 , 1 ) ;
    platform :: math_make_num_fract ( x_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_bottom , - 1 , 1 ) ;
    platform :: math_make_num_fract ( u_left , 0 , 1 ) ;
    platform :: math_make_num_fract ( u_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_bottom , 0 , 1 ) ;
    platform :: math_make_num_fract ( z , 0 , 1 ) ;
    platform :: math_make_num_whole ( color_r , _canvas_r ) ;
    platform :: math_make_num_whole ( color_g , _canvas_g ) ;
    platform :: math_make_num_whole ( color_b , _canvas_b ) ;
    platform :: math_make_num_whole ( color_a , _canvas_a ) ;

    platform :: math_make_num_whole ( index , 0 ) ;
    platform :: render_set_vertex_position  ( vertices [ 0 ] , x_left , y_top , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 0 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 0 ] , u_left , v_top ) ;
    platform :: render_set_index_value      ( indices  [ 0 ] , index ) ;

    platform :: math_make_num_whole ( index , 1 ) ;
    platform :: render_set_vertex_position  ( vertices [ 1 ] , x_left , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 1 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 1 ] , u_left , v_bottom ) ;
    platform :: render_set_index_value      ( indices  [ 1 ] , index ) ;

    platform :: math_make_num_whole ( index , 2 ) ;
    platform :: render_set_vertex_position  ( vertices [ 2 ] , x_right , y_top , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 2 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 2 ] , u_right , v_top ) ;
    platform :: render_set_index_value      ( indices  [ 2 ] , index ) ;

    platform :: math_make_num_whole ( index , 3 ) ;
    platform :: render_set_vertex_position  ( vertices [ 3 ] , x_right , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( vertices [ 3 ] , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( vertices [ 3 ] , u_right , v_bottom ) ;
    platform :: render_set_index_value      ( indices  [ 3 ] , index ) ;

    _mediator -> mesh_create ( _text_mesh_id , vertices , indices , 0 , platform :: whole_4 , platform :: whole_4 , platform :: whole_0 ) ;    
}

template < typename mediator >
void shy_logic_text < mediator > :: _create_text_texture ( )
{
    num_whole texture_width ;
    num_whole texture_height ;
    num_whole filler_r ;
    num_whole filler_g ;
    num_whole filler_b ;
    num_whole filler_a ;
    num_whole eraser_r ;
    num_whole eraser_g ;
    num_whole eraser_b ;
    num_whole eraser_a ;
    num_whole small_size ;
    num_whole big_size ;
    _mediator -> texture_width ( texture_width ) ;
    _mediator -> texture_height ( texture_height ) ;
    platform :: math_make_num_whole ( small_size , 16 ) ;
    platform :: math_make_num_whole ( big_size , 32 ) ;
    platform :: math_make_num_whole ( filler_r , 0 ) ;
    platform :: math_make_num_whole ( filler_g , 255 ) ;
    platform :: math_make_num_whole ( filler_b , 0 ) ;
    platform :: math_make_num_whole ( filler_a , 255 ) ;
    platform :: math_make_num_whole ( eraser_r , 0 ) ;
    platform :: math_make_num_whole ( eraser_g , 0 ) ;
    platform :: math_make_num_whole ( eraser_b , 0 ) ;
    platform :: math_make_num_whole ( eraser_a , 128 ) ;
    platform :: render_set_texel_color ( _filler , filler_r , filler_g , filler_b , filler_a ) ;
    platform :: render_set_texel_color ( _eraser , eraser_r , eraser_g , eraser_b , eraser_a ) ;
    _mediator -> texture_create ( _text_texture_id ) ;
    for ( num_whole x = platform :: whole_0
        ; platform :: condition_whole_less_than_whole ( x , texture_width ) 
        ; platform :: math_inc_whole ( x )
        )
    {
        for ( num_whole y = platform :: whole_0 
            ; platform :: condition_whole_less_than_whole ( y , texture_height ) 
            ; platform :: math_inc_whole ( y )
            )
        {
            _mediator -> texture_set_texel ( _text_texture_id , x , y , _eraser ) ;
        }
    }
    _origin_y = texture_height ;
    _rasterize_english_alphabet ( small_size , small_size ) ;
    _rasterize_english_alphabet ( big_size , big_size ) ;
    _mediator -> texture_finalize ( _text_texture_id ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_english_alphabet ( num_whole letter_size_x , num_whole letter_size_y )
{
    _letter_size_x = letter_size_x ;
    _letter_size_y = letter_size_y ;
    _next_letter_row ( ) ;
    _rasterize_font_english_A ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_B ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_C ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_D ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_E ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_F ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_G ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_H ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_I ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_J ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_K ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_L ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_M ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_N ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_O ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_P ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_Q ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_R ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_S ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_T ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_U ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_V ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_W ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_X ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_Y ( ) ; _next_letter_col ( ) ;
    _rasterize_font_english_Z ( ) ; _next_letter_col ( ) ;
    _rasterize_font_whitespace ( ) ;
    _next_letter_row ( ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_col ( )
{
    num_whole texture_width ;
    _mediator -> texture_width ( texture_width ) ;
    platform :: math_add_to_whole ( _origin_x , _letter_size_x ) ;
    if ( platform :: condition_whole_greater_or_equal_to_whole ( _origin_x , texture_width ) )
    {
        num_whole delta_y ;
        platform :: math_div_wholes ( delta_y , _letter_size_y , platform :: whole_4 ) ;
        platform :: math_sub_from_whole ( _origin_y , delta_y ) ;
        _next_letter_row ( ) ;
    }
}

template < typename mediator >
void shy_logic_text < mediator > :: _next_letter_row ( )
{
    platform :: math_sub_from_whole ( _origin_y , _letter_size_y ) ;
    platform :: math_make_num_whole ( _origin_x , 0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_A ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole outer_top ;
    num_whole outer_bottom = platform :: whole_0 ;
    num_whole outer_center ;
    num_whole outer_left = platform :: whole_0 ;
    num_whole outer_right ;
    platform :: math_sub_wholes ( outer_top , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_div_wholes ( outer_center , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_sub_wholes ( outer_right , _letter_size_x , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( outer_center , outer_top , outer_left , outer_bottom , outer_right , outer_bottom ) ;

    num_whole inner_top ;
    num_whole inner_bottom = platform :: whole_0 ;
    num_whole inner_center ;
    num_whole inner_left ;
    num_whole inner_right ;
    platform :: math_mul_wholes ( inner_top , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( inner_top , platform :: whole_3 ) ;
    platform :: math_div_wholes ( inner_center , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_wholes ( inner_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( inner_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( inner_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_triangle ( inner_center , inner_top , inner_left , inner_bottom , inner_right , inner_bottom ) ;

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
    platform :: math_mul_wholes ( board_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( board_top , platform :: whole_7 ) ;
    platform :: math_mul_wholes ( board_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( board_bottom , platform :: whole_7 ) ;
    platform :: math_sub_wholes ( outer_left_minus_center , outer_left , outer_center ) ;
    platform :: math_sub_wholes ( outer_right_minus_center , outer_right , outer_center ) ;
    platform :: math_sub_wholes ( outer_top_minus_board_top , outer_top , board_top ) ;
    platform :: math_sub_wholes ( outer_top_minus_board_bottom , outer_top , board_bottom ) ;
    platform :: math_sub_wholes ( outer_top_minus_bottom , outer_top , outer_bottom ) ;    
    platform :: math_mul_wholes ( board_top_left , outer_left_minus_center , outer_top_minus_board_top ) ;
    platform :: math_div_whole_by ( board_top_left , outer_top_minus_bottom ) ;
    platform :: math_add_to_whole ( board_top_left , outer_center ) ;
    platform :: math_mul_wholes ( board_bottom_left , outer_left_minus_center , outer_top_minus_board_bottom ) ;
    platform :: math_div_whole_by ( board_bottom_left , outer_top_minus_bottom ) ;
    platform :: math_add_to_whole ( board_bottom_left , outer_center ) ;
    platform :: math_mul_wholes ( board_top_right , outer_right_minus_center , outer_top_minus_board_top ) ;
    platform :: math_div_whole_by ( board_top_right , outer_top_minus_bottom ) ;
    platform :: math_add_to_whole ( board_top_right , outer_center ) ;
    platform :: math_mul_wholes ( board_bottom_right , outer_right_minus_center , outer_top_minus_board_bottom ) ;
    platform :: math_div_whole_by ( board_bottom_right , outer_top_minus_bottom ) ;
    platform :: math_add_to_whole ( board_bottom_right , outer_center ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( board_top_left , board_top , board_bottom_left , board_bottom , board_bottom_right , board_bottom ) ;
    _mediator -> rasterize_triangle ( board_top_left , board_top , board_top_right , board_top , board_bottom_right , board_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_B ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole ellipse_y_top ;
    num_whole ellipse_y_mid ;
    num_whole ellipse_x_right ;
    platform :: math_sub_wholes ( ellipse_y_top , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_div_wholes ( ellipse_y_mid , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_sub_wholes ( ellipse_x_right , _letter_size_x , platform :: whole_1 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , ellipse_x_right , ellipse_y_mid ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , ellipse_y_mid , ellipse_x_right , ellipse_y_top ) ;

    num_whole spine_right ;
    num_whole spine_top ;
    platform :: math_div_wholes ( spine_right , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_sub_wholes ( spine_top , _letter_size_y , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , spine_top , spine_right , platform :: whole_0 ) ;
    
    num_whole hole_divider ;
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_height ;
    num_whole hole_top_minus_height ;
    num_whole hole_bottom_plus_height ;
    platform :: math_make_num_whole ( hole_divider , 16 ) ;
    platform :: math_mul_wholes ( hole_left , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_left , hole_divider ) ;
    platform :: math_make_num_whole ( hole_right , 12 ) ;
    platform :: math_mul_whole_by ( hole_right , _letter_size_x ) ;
    platform :: math_div_whole_by ( hole_right , hole_divider ) ;
    platform :: math_make_num_whole ( hole_top , 13 ) ;
    platform :: math_mul_whole_by ( hole_top , _letter_size_y ) ;
    platform :: math_div_whole_by ( hole_top , hole_divider ) ;
    platform :: math_mul_wholes ( hole_bottom , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_bottom , hole_divider ) ;
    platform :: math_mul_wholes ( hole_height , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_height , hole_divider ) ;
    platform :: math_sub_wholes ( hole_top_minus_height , hole_top , hole_height ) ;
    platform :: math_add_wholes ( hole_bottom_plus_height , hole_bottom , hole_height ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_top_minus_height ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_bottom , hole_right , hole_bottom_plus_height ) ;
    
    num_whole hole_center_x ;
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_center_x , hole_top_minus_height ) ;
    _mediator -> rasterize_rect ( hole_left , hole_bottom , hole_center_x , hole_bottom_plus_height ) ;    
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_C ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    num_whole hole_center_x ;
    num_whole hole_center_top ;
    num_whole hole_center_bottom ;
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;    
    platform :: math_mul_wholes ( hole_center_top , _letter_size_y , platform :: whole_5 ) ;
    platform :: math_div_whole_by ( hole_center_top , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_center_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_center_bottom , platform :: whole_7 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_D ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;

    num_whole half_size_x ;
    platform :: math_div_wholes ( half_size_x , _letter_size_x , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , half_size_x , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole hole_center_x ;
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_center_x , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_E ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole right ;
    num_whole top_limit ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    num_whole hole_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( hole_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( hole_mid_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_mid_top , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( hole_mid_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_mid_bottom , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_F ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_sub_wholes ( hole_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_mid_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_mid_top , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_mid_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_mid_bottom , platform :: whole_5 ) ;        
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_G ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;

    num_whole hole_center_x ;
    num_whole hole_center_top ;
    num_whole hole_center_bottom ;
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;    
    platform :: math_mul_wholes ( hole_center_top , _letter_size_y , platform :: whole_5 ) ;
    platform :: math_div_whole_by ( hole_center_top , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_center_bottom , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_center_bottom , platform :: whole_7 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_center_x , hole_center_top , right_limit , hole_center_bottom ) ;
    
    num_whole brick_top ;
    num_whole brick_bottom ;
    num_whole brick_left ;
    num_whole brick_right ;
    platform :: math_mul_wholes ( brick_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( brick_top , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( brick_bottom , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( brick_bottom , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( brick_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( brick_left , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( brick_right , _letter_size_x , platform :: whole_1 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( brick_left , brick_top , brick_right , brick_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_H ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;        
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_mid_top ;
    num_whole hole_mid_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_mid_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_mid_top , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_mid_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_mid_bottom , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , top_limit , hole_right , hole_mid_top ) ;
    _mediator -> rasterize_rect ( hole_left , hole_mid_bottom , hole_right , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_I ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_6 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_7 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_mid_left ;
    num_whole hole_mid_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform :: math_mul_wholes ( hole_mid_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_mid_left , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_mid_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_mid_right , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , hole_top , hole_mid_left , hole_bottom ) ;
    _mediator -> rasterize_rect ( hole_mid_right , hole_top , right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_J ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    num_whole circle_top ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( circle_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( circle_top , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right , circle_top ) ;

    num_whole circle_center_y ;
    platform :: math_div_wholes ( circle_center_y , circle_top , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , circle_center_y , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole hole_center_y ;
    platform :: math_add_wholes ( hole_center_y , hole_top , hole_bottom ) ;
    platform :: math_div_whole_by ( hole_center_y , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , circle_top , hole_right , hole_center_y ) ;
    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , top_limit , hole_left , hole_center_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_K ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right_limit ;
    num_whole half_size_y ;    
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    platform :: math_div_wholes ( half_size_y , _letter_size_y , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;

    num_whole hole_1_left ;
    platform :: math_mul_wholes ( hole_1_left , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_1_left , platform :: whole_9 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_triangle ( hole_1_left , half_size_y , right_limit , top_limit , right_limit , platform :: whole_0 ) ;

    num_whole hole_2_right ;
    platform :: math_mul_wholes ( hole_2_right , _letter_size_x , platform :: whole_6 ) ;
    platform :: math_div_whole_by ( hole_2_right , platform :: whole_9 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_triangle ( platform :: whole_0 , top_limit , hole_2_right , top_limit , platform :: whole_0 , half_size_y ) ;

    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_triangle ( platform :: whole_0 , platform :: whole_0 , hole_2_right , platform :: whole_0 , platform :: whole_0 , half_size_y ) ;

    num_whole spine_right ;
    platform :: math_div_wholes ( spine_right , _letter_size_x , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , spine_right , top_limit ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_L ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , top_limit , right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_M ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole spine_1_right ;
    num_whole spine_2_left ;
    num_whole spine_2_right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( spine_1_right , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( spine_2_left , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( spine_2_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( spine_2_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( spine_2_right , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , spine_1_right , top_limit ) ;
    _mediator -> rasterize_rect ( spine_2_left , platform :: whole_0 , spine_2_right , top_limit ) ;

    num_whole board_height ;
    num_whole board_center_x ;
    num_whole top_minus_board_height ;
    platform :: math_mul_wholes ( board_height , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( board_height , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( board_center_x , spine_2_right , platform :: whole_2 ) ;    
    platform :: math_sub_wholes ( top_minus_board_height , _letter_size_y , board_height ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( spine_1_right , top_limit , board_center_x , board_height , board_center_x , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , board_center_x , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( board_center_x , board_height , spine_2_left , top_limit , spine_2_left , top_minus_board_height ) ;
    _mediator -> rasterize_triangle ( board_center_x , board_height , board_center_x , platform :: whole_0 , spine_2_left , top_minus_board_height ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_N ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole spine_1_right ;
    num_whole spine_2_left ;
    num_whole spine_2_right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( spine_1_right , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( spine_2_left , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( spine_2_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( spine_2_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( spine_2_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , spine_1_right , top_limit ) ;
    _mediator -> rasterize_rect ( spine_2_left , platform :: whole_0 , spine_2_right , top_limit ) ;
    
    num_whole board_height ;
    num_whole top_minus_board_height ;
    platform :: math_div_wholes ( board_height , _letter_size_y , platform :: whole_3 ) ;    
    platform :: math_sub_wholes ( top_minus_board_height , _letter_size_y , board_height ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( spine_1_right , top_limit , spine_2_left , board_height , spine_2_left , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( spine_1_right , top_limit , spine_1_right , top_minus_board_height , spine_2_left , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_O ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole right_limit ;
    num_whole top_limit ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_P ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole spine_right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( spine_right , _letter_size_x , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , spine_right , top_limit ) ;
    
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_bottom ;
    platform :: math_div_wholes ( ellipse_left , _letter_size_x , platform :: whole_2 ) ;    
    platform :: math_sub_wholes ( ellipse_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( ellipse_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( ellipse_bottom , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( ellipse_left , top_limit , ellipse_right , ellipse_bottom ) ;
    
    num_whole ellipse_center_x ;
    platform :: math_add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    platform :: math_div_whole_by ( ellipse_center_x , platform :: whole_2 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( spine_right , top_limit , ellipse_center_x , ellipse_bottom ) ;

    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_center_x ;
    platform :: math_mul_wholes ( hole_left , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_left , platform :: whole_6 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_6 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_bottom , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_bottom , platform :: whole_5 ) ;    
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _mediator -> rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Q ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right_limit ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_sub_wholes ( right_limit , _letter_size_x , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( platform :: whole_0 , platform :: whole_0 , right_limit , top_limit ) ;
    
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_left ;
    num_whole hole_right ;
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    
    num_whole board_width ;
    num_whole board_left ;
    num_whole board_top ;
    num_whole right_minus_board_width ;
    num_whole left_plus_board_width ;
    platform :: math_div_wholes ( board_width , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( board_left , _letter_size_x , platform :: whole_2 ) ;    
    platform :: math_mul_wholes ( board_top , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( board_top , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( right_minus_board_width , _letter_size_x , board_width ) ;
    platform :: math_add_wholes ( left_plus_board_width , board_left , board_width ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( board_left , board_top , right_minus_board_width , platform :: whole_0 , _letter_size_x , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( board_left , board_top , left_plus_board_width , board_top , _letter_size_x , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_R ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole top_limit ;
    num_whole spine_right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( spine_right , _letter_size_x , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , spine_right , top_limit ) ;
    
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_top ;
    num_whole ellipse_bottom ;
    platform :: math_div_wholes ( ellipse_left , _letter_size_x , platform :: whole_2 ) ;    
    platform :: math_sub_wholes ( ellipse_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_sub_wholes ( ellipse_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( ellipse_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( ellipse_bottom , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;
    
    num_whole ellipse_center_x ;
    platform :: math_add_wholes ( ellipse_center_x , ellipse_left , ellipse_right ) ;
    platform :: math_div_whole_by ( ellipse_center_x , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( spine_right , ellipse_top , ellipse_center_x , ellipse_bottom ) ;

    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    num_whole hole_center_x ;
    platform :: math_mul_wholes ( hole_left , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_left , platform :: whole_6 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_6 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( hole_bottom , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_bottom , platform :: whole_5 ) ;    
    platform :: math_add_wholes ( hole_center_x , hole_left , hole_right ) ;
    platform :: math_div_whole_by ( hole_center_x , platform :: whole_2 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _mediator -> rasterize_rect ( spine_right , hole_top , hole_center_x , hole_bottom ) ;

    num_whole board_width ;
    num_whole right_minus_board_width ;
    num_whole spine_plus_board_width ;
    platform :: math_mul_wholes ( board_width , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( board_width , platform :: whole_7 ) ;    
    platform :: math_sub_wholes ( right_minus_board_width , _letter_size_x , board_width ) ;    
    platform :: math_add_wholes ( spine_plus_board_width , spine_right , board_width ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( spine_right , ellipse_bottom , right_minus_board_width , platform :: whole_0 , _letter_size_x , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( spine_right , ellipse_bottom , spine_plus_board_width , ellipse_bottom , _letter_size_x , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_S ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole circle_high_left ;
    num_whole circle_high_right ;
    num_whole circle_high_top ;
    num_whole circle_high_bottom ;
    platform :: math_make_num_whole ( circle_high_left , 0 ) ;    
    platform :: math_div_wholes ( circle_high_right , _letter_size_x , platform :: whole_2 ) ;    
    platform :: math_sub_wholes ( circle_high_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( circle_high_bottom , _letter_size_y , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( circle_high_bottom , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( circle_high_left , circle_high_top , circle_high_right , circle_high_bottom ) ;
    
    num_whole circle_low_left ;
    num_whole circle_low_right ;
    num_whole circle_low_top ;
    num_whole circle_low_bottom ;
    platform :: math_div_wholes ( circle_low_left , _letter_size_x , platform :: whole_2 ) ;    
    platform :: math_sub_wholes ( circle_low_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( circle_low_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( circle_low_top , platform :: whole_5 ) ;    
    platform :: math_make_num_whole ( circle_low_bottom , 0 ) ;
    _mediator -> rasterize_ellipse_in_rect ( circle_low_left , circle_low_top , circle_low_right , circle_low_bottom ) ;

    num_whole board_mid_left ;
    num_whole board_mid_right ;
    num_whole board_mid_top ;
    num_whole board_mid_bottom ;
    platform :: math_div_wholes ( board_mid_left , _letter_size_x , platform :: whole_4 ) ;    
    platform :: math_mul_wholes ( board_mid_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( board_mid_right , platform :: whole_4 ) ;    
    board_mid_top = circle_low_top ;
    board_mid_bottom = circle_high_bottom ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( board_mid_left , board_mid_top , board_mid_right , board_mid_bottom ) ;
    
    num_whole board_high_left ;
    num_whole board_high_right ;
    num_whole board_high_top ;
    num_whole board_high_bottom ;
    board_high_left = board_mid_left ;    
    platform :: math_mul_wholes ( board_high_right , _letter_size_x , platform :: whole_8 ) ;
    platform :: math_div_whole_by ( board_high_right , platform :: whole_9 ) ;
    platform :: math_sub_wholes ( board_high_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( board_high_bottom , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( board_high_bottom , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( board_high_left , board_high_top , board_high_right , board_high_bottom ) ;
    
    num_whole board_low_left ;
    num_whole board_low_right ;
    num_whole board_low_top ;
    num_whole board_low_bottom ;
    platform :: math_div_wholes ( board_low_left , _letter_size_x , platform :: whole_9 ) ;    
    board_low_right = board_mid_right ;
    platform :: math_div_wholes ( board_low_top , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_make_num_whole ( board_low_bottom , 0 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( board_low_left , board_low_top , board_low_right , board_low_bottom ) ;
        
    num_whole hole_high_left ;
    num_whole hole_high_right ;
    num_whole hole_high_top ;
    num_whole hole_high_bottom ;
    platform :: math_div_wholes ( hole_high_left , _letter_size_x , platform :: whole_6 ) ;    
    platform :: math_div_wholes ( hole_high_right , _letter_size_x , platform :: whole_3 ) ;    
    platform :: math_sub_wholes ( hole_high_top , board_high_bottom , platform :: whole_1 ) ;    
    platform :: math_add_wholes ( hole_high_bottom , board_mid_top , platform :: whole_1 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_high_left , hole_high_top , hole_high_right , hole_high_bottom ) ;

    num_whole hole_low_left ;
    num_whole hole_low_right ;
    num_whole hole_low_top ;
    num_whole hole_low_bottom ;
    platform :: math_mul_wholes ( hole_low_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_low_left , platform :: whole_3 ) ;    
    platform :: math_mul_wholes ( hole_low_right , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_div_whole_by ( hole_low_right , platform :: whole_6 ) ;    
    platform :: math_sub_wholes ( hole_low_top , board_mid_bottom , platform :: whole_1 ) ;    
    platform :: math_add_wholes ( hole_low_bottom , board_low_top , platform :: whole_1 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_low_left , hole_low_top , hole_low_right , hole_low_bottom ) ;
    
    num_whole hole_high_center_x ;
    platform :: math_add_wholes ( hole_high_center_x , hole_high_left , hole_high_right ) ;
    platform :: math_div_whole_by ( hole_high_center_x , platform :: whole_2 ) ;    
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_high_center_x , hole_high_top , circle_high_right , hole_high_bottom ) ;
    
    num_whole hole_low_center_x ;
    platform :: math_add_wholes ( hole_low_center_x , hole_low_left , hole_low_right ) ;
    platform :: math_div_whole_by ( hole_low_center_x , platform :: whole_2 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( circle_low_left , hole_low_top , hole_low_center_x , hole_low_bottom ) ;    
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_T ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole top_limit ;
    num_whole right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_mul_wholes ( right , _letter_size_x , platform :: whole_6 ) ;
    platform :: math_div_whole_by ( right , platform :: whole_7 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( platform :: whole_0 , platform :: whole_0 , right , top_limit ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_mid_left ;
    num_whole hole_mid_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform :: math_make_num_whole ( hole_left , 0 ) ;
    hole_right = right ;    
    platform :: math_mul_wholes ( hole_mid_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( hole_mid_left , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_mid_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_mid_right , platform :: whole_7 ) ;    
    platform :: math_mul_wholes ( hole_top , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hole_top , platform :: whole_5 ) ;    
    platform :: math_make_num_whole ( hole_bottom , 0 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_rect ( hole_left , hole_top , hole_mid_left , hole_bottom ) ;
    _mediator -> rasterize_rect ( hole_mid_right , hole_top , hole_right , hole_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_U ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole top_limit ;
    num_whole ellipse_left ;
    num_whole ellipse_right ;
    num_whole ellipse_top ;
    num_whole ellipse_bottom ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_make_num_whole ( ellipse_left , 0 ) ;    
    platform :: math_mul_wholes ( ellipse_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( ellipse_right , platform :: whole_5 ) ;    
    platform :: math_div_wholes ( ellipse_top , _letter_size_y , platform :: whole_2 ) ;    
    platform :: math_make_num_whole ( ellipse_bottom , 0 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_ellipse_in_rect ( ellipse_left , ellipse_top , ellipse_right , ellipse_bottom ) ;    
    
    num_whole ellipse_center_y ;
    platform :: math_div_wholes ( ellipse_center_y , _letter_size_y , platform :: whole_4 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( ellipse_left , top_limit , ellipse_right , ellipse_center_y ) ;
    
    num_whole hole_left ;
    num_whole hole_right ;
    num_whole hole_top ;
    num_whole hole_bottom ;
    platform :: math_div_wholes ( hole_left , _letter_size_x , platform :: whole_5 ) ;
    platform :: math_add_to_whole ( hole_left , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( hole_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( hole_right , platform :: whole_5 ) ;
    platform :: math_sub_from_whole ( hole_right , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( hole_top , _letter_size_y , platform :: whole_3 ) ;
    platform :: math_sub_from_whole ( hole_top , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( hole_bottom , _letter_size_y , platform :: whole_6 ) ;
    platform :: math_add_to_whole ( hole_bottom , platform :: whole_1 ) ;
    _mediator -> rasterize_use_texel ( _eraser ) ;
    _mediator -> rasterize_ellipse_in_rect ( hole_left , hole_top , hole_right , hole_bottom ) ;
    _mediator -> rasterize_rect ( hole_left , top_limit , hole_right , ellipse_center_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_V ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole top_limit ;
    num_whole high_1_left ;
    num_whole high_1_right ;
    num_whole high_2_left ;
    num_whole high_2_right ;
    num_whole low_left ;
    num_whole low_right ;
    platform :: math_sub_wholes ( top_limit , _letter_size_y , platform :: whole_1 ) ;
    platform :: math_make_num_whole ( high_1_left , 0 ) ;    
    platform :: math_div_wholes ( high_1_right , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( high_2_left , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( high_2_left , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( high_2_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( low_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( low_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( low_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( low_right , platform :: whole_5 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( high_1_left , top_limit , high_1_right , top_limit , low_right , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( high_1_left , top_limit , low_left , platform :: whole_0 , low_right , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( high_2_left , top_limit , high_2_right , top_limit , low_right , platform :: whole_0 ) ;
    _mediator -> rasterize_triangle ( high_2_left , top_limit , low_left , platform :: whole_0 , low_right , platform :: whole_0 ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_W ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

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
    platform :: math_make_num_whole ( high_1_left , 0 ) ;    
    platform :: math_div_wholes ( high_1_right , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( high_2_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( high_2_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( high_2_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( high_2_right , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( high_3_left , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( high_3_left , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( high_3_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_div_wholes ( low_1_left , _letter_size_x , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( low_1_right , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( low_1_right , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( low_2_left , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( low_2_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( low_2_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( low_2_right , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( high_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_make_num_whole ( low_bottom , 0 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_1_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_1_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_1_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , low_1_left , low_bottom , low_1_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_2_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_3_left , high_top , high_3_right , high_top , low_2_right , low_bottom ) ;
    _mediator -> rasterize_triangle ( high_3_left , high_top , low_2_left , low_bottom , low_2_right , low_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_X ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole left_1 ;
    num_whole right_1 ;
    num_whole left_2 ;
    num_whole right_2 ;
    num_whole top_y ;
    num_whole bottom_y ;
    platform :: math_make_num_whole ( left_1 , 0 ) ;    
    platform :: math_div_wholes ( right_1 , _letter_size_x , platform :: whole_4 ) ;    
    platform :: math_mul_wholes ( left_2 , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( left_2 , platform :: whole_4 ) ;    
    platform :: math_sub_wholes ( right_2 , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_sub_wholes ( top_y , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_make_num_whole ( bottom_y , 0 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( left_1 , top_y , right_1 , top_y , right_2 , bottom_y ) ;
    _mediator -> rasterize_triangle ( left_1 , top_y , left_2 , bottom_y , right_2 , bottom_y ) ;
    _mediator -> rasterize_triangle ( left_2 , top_y , right_2 , top_y , right_1 , bottom_y ) ;
    _mediator -> rasterize_triangle ( left_2 , top_y , left_1 , bottom_y , right_1 , bottom_y ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Y ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;

    num_whole high_1_left ;
    num_whole high_1_right ;
    num_whole high_2_left ;
    num_whole high_2_right ;
    num_whole high_top ;
    num_whole low_left ;
    num_whole low_right ;
    num_whole low_bottom ;
    num_whole mid_y ;
    platform :: math_make_num_whole ( high_1_left , 0 ) ;    
    platform :: math_div_wholes ( high_1_right , _letter_size_x , platform :: whole_4 ) ;    
    platform :: math_mul_wholes ( high_2_left , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( high_2_left , platform :: whole_4 ) ;    
    platform :: math_sub_wholes ( high_2_right , _letter_size_x , platform :: whole_1 ) ;    
    platform :: math_sub_wholes ( high_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( low_left , _letter_size_x , platform :: whole_2 ) ;
    platform :: math_div_whole_by ( low_left , platform :: whole_5 ) ;    
    platform :: math_mul_wholes ( low_right , _letter_size_x , platform :: whole_3 ) ;
    platform :: math_div_whole_by ( low_right , platform :: whole_5 ) ;    
    platform :: math_make_num_whole ( low_bottom , 0 ) ;    
    platform :: math_div_wholes ( mid_y , _letter_size_y , platform :: whole_2 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( high_1_left , high_top , high_1_right , high_top , low_right , mid_y ) ;
    _mediator -> rasterize_triangle ( high_1_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , high_2_right , high_top , low_right , mid_y ) ;
    _mediator -> rasterize_triangle ( high_2_left , high_top , low_left , mid_y , low_right , mid_y ) ;
    _mediator -> rasterize_rect ( low_left , mid_y , low_right , low_bottom ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_english_Z ( )
{
    _mediator -> rasterize_use_texture ( _text_texture_id , _origin_x , _origin_y ) ;
    
    num_whole hor_left ;
    num_whole hor_right ;
    num_whole high_top ;
    num_whole high_bottom ;
    platform :: math_make_num_whole ( hor_left , 0 ) ;    
    platform :: math_mul_wholes ( hor_right , _letter_size_x , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( hor_right , platform :: whole_5 ) ;    
    platform :: math_sub_wholes ( high_top , _letter_size_y , platform :: whole_1 ) ;    
    platform :: math_mul_wholes ( high_bottom , _letter_size_y , platform :: whole_4 ) ;
    platform :: math_div_whole_by ( high_bottom , platform :: whole_5 ) ;    
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( hor_left , high_top , hor_right , high_bottom ) ;
    
    num_whole low_top ;
    num_whole low_bottom ;
    platform :: math_div_wholes ( low_top , _letter_size_y , platform :: whole_5 ) ;    
    platform :: math_make_num_whole ( low_bottom , 0 ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_rect ( hor_left , low_top , hor_right , low_bottom ) ;
    
    num_whole board_width ;
    num_whole right_minus_board_width ;
    platform :: math_div_wholes ( board_width , _letter_size_y , platform :: whole_4 ) ;    
    platform :: math_sub_wholes ( right_minus_board_width , hor_right , board_width ) ;
    _mediator -> rasterize_use_texel ( _filler ) ;
    _mediator -> rasterize_triangle ( right_minus_board_width , high_bottom , hor_right , high_bottom , board_width , low_top ) ;
    _mediator -> rasterize_triangle ( right_minus_board_width , high_bottom , hor_left , low_top , board_width , low_top ) ;
}

template < typename mediator >
void shy_logic_text < mediator > :: _rasterize_font_whitespace ( )
{
}
