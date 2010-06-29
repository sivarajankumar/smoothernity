template < typename mediator >
class shy_logic_image
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: engine_render engine_render ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    static const_int_32 _logo_resource_index = 1 ;
    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _image_r = 255 ;
    static const_int_32 _image_g = 255 ;
    static const_int_32 _image_b = 255 ;
    static const_int_32 _image_a = 255 ;
    static const num_fract _final_scale ( ) { num_fract n ; platform_math :: make_num_fract ( n , 1 , 2 ) ; return n ; }
public :
    shy_logic_image ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: image_done msg ) ;
    void receive ( typename messages :: image_render_request msg ) ;
    void receive ( typename messages :: image_update msg ) ;
    void receive ( typename messages :: image_prepare_permit msg ) ;
    void receive ( typename messages :: render_texture_create_reply msg ) ;
    void receive ( typename messages :: render_mesh_create_reply msg ) ;
private :
    void _render_image_mesh ( ) ;
    void _update_image_mesh ( ) ;
    void _create_image_mesh ( ) ;
    void _create_image_texture ( ) ;
    void _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z ) ;
    void _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v ) ;
    void _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    num_whole _image_mesh_created ;
    num_whole _image_texture_created ;
    num_whole _image_texture_loaded ;
    num_whole _image_prepare_permitted ;
    num_whole _texture_create_requested ;
    num_whole _mesh_create_requested ;
    num_whole _scale_frames ;
    mesh_id _image_mesh_id ;
    texture_id _image_texture_id ;
} ;

template < typename mediator >
shy_logic_image < mediator > :: shy_logic_image ( )
{
    _image_mesh_created = platform :: math_consts . whole_false ;
    _image_texture_created = platform :: math_consts . whole_false ;
    _image_texture_loaded = platform :: math_consts . whole_false ;
    _image_prepare_permitted = platform :: math_consts . whole_false ;
    _texture_create_requested = platform :: math_consts . whole_false ;
    _mesh_create_requested = platform :: math_consts . whole_false ;
    _scale_frames = platform :: math_consts . whole_0 ;
}

template < typename mediator >
void shy_logic_image < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_done msg )
{
    if ( platform_conditions :: whole_is_true ( _image_mesh_created ) )
    {
        typename messages :: render_mesh_delete mesh_delete_msg ;
        mesh_delete_msg . mesh = _image_mesh_id ;
        _mediator . get ( ) . send ( mesh_delete_msg ) ;
    }
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_render_request msg )
{
    if ( platform_conditions :: whole_is_true ( _image_mesh_created ) && platform_conditions :: whole_is_true ( _image_texture_loaded ) )
        _render_image_mesh ( ) ;
    _mediator . get ( ) . send ( typename messages :: image_render_reply ( ) ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_prepare_permit msg )
{
    _image_prepare_permitted = platform :: math_consts . whole_true ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: render_texture_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _texture_create_requested ) )
    {
        _texture_create_requested = platform :: math_consts . whole_false ;
        _image_texture_created = platform :: math_consts . whole_true ;
        _image_texture_id = msg . texture ;
        _create_image_texture ( ) ;
    }
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: render_mesh_create_reply msg )
{
    if ( platform_conditions :: whole_is_true ( _mesh_create_requested ) )
    {
        _mesh_create_requested = platform :: math_consts . whole_false ;
        _image_mesh_id = msg . mesh ;
        _create_image_mesh ( ) ;
        platform_math :: make_num_whole ( _image_mesh_created , true ) ;
    }
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_update msg )
{
    if ( platform_conditions :: whole_is_true ( _image_prepare_permitted ) )
    {
        if ( platform_conditions :: whole_is_false ( _image_mesh_created ) )
        {
            _mesh_create_requested = platform :: math_consts . whole_true ;
            
            typename messages :: render_mesh_create_request mesh_create_msg ;
            mesh_create_msg . vertices = platform :: math_consts . whole_4 ;
            mesh_create_msg . triangle_strip_indices = platform :: math_consts . whole_4 ;
            mesh_create_msg . triangle_fan_indices = platform :: math_consts . whole_0 ;
            _mediator . get ( ) . send ( mesh_create_msg ) ;        
        }
        if ( platform_conditions :: whole_is_false ( _image_texture_created ) )
        {
            _texture_create_requested = platform :: math_consts . whole_true ;
            _mediator . get ( ) . send ( typename messages :: render_texture_create_request ( ) ) ;
        }
        if ( platform_conditions :: whole_is_true ( _image_texture_created ) 
          && platform_conditions :: whole_is_false ( _image_texture_loaded )
           )
        {
            num_whole loader_ready ;
            engine_render :: texture_loader_ready ( loader_ready ) ;
            if ( platform_conditions :: whole_is_true ( loader_ready ) )
            {
                {
                    typename messages :: render_texture_finalize texture_finalize_msg ;
                    texture_finalize_msg . texture = _image_texture_id ;
                    _mediator . get ( ) . send ( texture_finalize_msg ) ;
                }
                platform_math :: make_num_whole ( _image_texture_loaded , true ) ;
                _mediator . get ( ) . send ( typename messages :: image_prepared ( ) ) ;
            }
        }
    }
    if ( platform_conditions :: whole_is_true ( _image_mesh_created ) && platform_conditions :: whole_is_true ( _image_texture_loaded ) )
        _update_image_mesh ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _update_image_mesh ( )
{
    matrix_data matrix ;
    num_fract scale ;
    num_fract origin_x ;
    num_fract origin_y ;
    num_fract origin_z ;
    num_fract fract_scale_frames ;
    num_fract fract_scale_in_frames ;
    num_whole whole_scale_in_frames ;
    platform_math :: make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform_math :: make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform_math :: make_fract_from_whole ( fract_scale_frames , _scale_frames ) ;
    engine_math :: math_lerp ( scale , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , _final_scale ( ) , fract_scale_in_frames , fract_scale_frames ) ;
    platform_math :: make_num_fract ( origin_x , 1 , 2 ) ;
    platform_math :: make_num_fract ( origin_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( origin_z , - 3 , 1 ) ;
    platform_matrix :: set_axis_x ( matrix , scale , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_y ( matrix , platform :: math_consts . fract_0 , scale , platform :: math_consts . fract_0 ) ;
    platform_matrix :: set_axis_z ( matrix , platform :: math_consts . fract_0 , platform :: math_consts . fract_0 , scale ) ;
    platform_matrix :: set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    {
        typename messages :: render_mesh_set_transform mesh_set_transform_msg ;
        mesh_set_transform_msg . mesh = _image_mesh_id ;
        mesh_set_transform_msg . transform = matrix ;
        _mediator . get ( ) . send ( mesh_set_transform_msg ) ;
    }
    if ( platform_conditions :: whole_less_than_whole ( _scale_frames , whole_scale_in_frames ) )
        platform_math :: inc_whole ( _scale_frames ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _render_image_mesh ( )
{
    _mediator . get ( ) . send ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha ( ) ) ;
    {
        typename messages :: render_texture_select texture_select_msg ;
        texture_select_msg . texture = _image_texture_id ;
        _mediator . get ( ) . send ( texture_select_msg ) ;
    }
    {
        typename messages :: render_mesh_render mesh_render_msg ;
        mesh_render_msg . mesh = _image_mesh_id ;
        _mediator . get ( ) . send ( mesh_render_msg ) ;
    }
    _mediator . get ( ) . send ( typename messages :: render_blend_disable ( ) ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_mesh ( )
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
    num_whole index ;
    
    platform_math :: make_num_fract ( x_left , - 1 , 1 ) ;
    platform_math :: make_num_fract ( x_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( y_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( y_bottom , - 1 , 1 ) ;
    platform_math :: make_num_fract ( u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( v_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( v_bottom , 0 , 1 ) ;
    platform_math :: make_num_fract ( z , 0 , 1 ) ;
    platform_math :: make_num_fract ( color_r , _image_r , 255 ) ;
    platform_math :: make_num_fract ( color_g , _image_g , 255 ) ;
    platform_math :: make_num_fract ( color_b , _image_b , 255 ) ;
    platform_math :: make_num_fract ( color_a , _image_a , 255 ) ;

    _mesh_set_vertex_position            ( platform :: math_consts . whole_0 , x_left , y_top , z ) ;
    _mesh_set_vertex_color               ( platform :: math_consts . whole_0 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( platform :: math_consts . whole_0 , u_left , v_top ) ;
    _mesh_set_triangle_strip_index_value ( platform :: math_consts . whole_0 , platform :: math_consts . whole_0 ) ;

    _mesh_set_vertex_position            ( platform :: math_consts . whole_1 , x_left , y_bottom , z ) ;
    _mesh_set_vertex_color               ( platform :: math_consts . whole_1 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( platform :: math_consts . whole_1 , u_left , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( platform :: math_consts . whole_1 , platform :: math_consts . whole_1 ) ;

    _mesh_set_vertex_position            ( platform :: math_consts . whole_2 , x_right , y_top , z ) ;
    _mesh_set_vertex_color               ( platform :: math_consts . whole_2 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( platform :: math_consts . whole_2 , u_right , v_top ) ;
    _mesh_set_triangle_strip_index_value ( platform :: math_consts . whole_2 , platform :: math_consts . whole_2 ) ;

    _mesh_set_vertex_position            ( platform :: math_consts . whole_3 , x_right , y_bottom , z ) ;
    _mesh_set_vertex_color               ( platform :: math_consts . whole_3 , color_r , color_g , color_b , color_a ) ;
    _mesh_set_vertex_tex_coord           ( platform :: math_consts . whole_3 , u_right , v_bottom ) ;
    _mesh_set_triangle_strip_index_value ( platform :: math_consts . whole_3 , platform :: math_consts . whole_3 ) ;

    typename messages :: render_mesh_finalize mesh_finalize_msg ;
    mesh_finalize_msg . mesh = _image_mesh_id ;
    _mediator . get ( ) . send ( mesh_finalize_msg ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _mesh_set_vertex_position ( num_whole offset , num_fract x , num_fract y , num_fract z )
{
    typename messages :: render_mesh_set_vertex_position msg ;
    msg . mesh = _image_mesh_id ;
    msg . offset = offset ;
    msg . x = x ;
    msg . y = y ;
    msg . z = z ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _mesh_set_vertex_tex_coord ( num_whole offset , num_fract u , num_fract v )
{
    typename messages :: render_mesh_set_vertex_tex_coord msg ;
    msg . mesh = _image_mesh_id ;
    msg . offset = offset ;
    msg . u = u ;
    msg . v = v ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _mesh_set_vertex_color ( num_whole offset , num_fract r , num_fract g , num_fract b , num_fract a )
{
    typename messages :: render_mesh_set_vertex_color msg ;
    msg . mesh = _image_mesh_id ;
    msg . offset = offset ;
    msg . r = r ;
    msg . g = g ;
    msg . b = b ;
    msg . a = a ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _mesh_set_triangle_strip_index_value ( num_whole offset , num_whole index )
{
    typename messages :: render_mesh_set_triangle_strip_index_value msg ;
    msg . mesh = _image_mesh_id ;
    msg . offset = offset ;
    msg . index = index ;
    _mediator . get ( ) . send ( msg ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_texture ( )
{
    num_whole resource_index ;
    texture_resource_id logo_resource_id ;
    platform_math :: make_num_whole ( resource_index , _logo_resource_index ) ;
    engine_render :: create_texture_resource_id ( logo_resource_id , resource_index ) ;
    {
        typename messages :: render_texture_load_from_resource texture_load_from_resource_msg ;
        texture_load_from_resource_msg . texture = _image_texture_id ;
        texture_load_from_resource_msg . resource = logo_resource_id ;
        _mediator . get ( ) . send ( texture_load_from_resource_msg ) ;
    }
}
