template < typename mediator >
class shy_logic_image
{
    typedef typename mediator :: engine_math engine_math ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: texture_id texture_id ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: index_data index_data ;
    typedef typename mediator :: platform :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: vertex_data vertex_data ;
    
    static const_int_32 _logo_resource_index = 1 ;
    static const_int_32 _scale_in_frames = 60 ;
    static const_int_32 _image_r = 255 ;
    static const_int_32 _image_g = 255 ;
    static const_int_32 _image_b = 255 ;
    static const_int_32 _image_a = 255 ;
    static const num_fract _final_scale ( ) { num_fract n ; platform :: math_make_num_fract ( n , 1 , 2 ) ; return n ; }
public :
    shy_logic_image ( ) ;
    void set_mediator ( mediator * arg_mediator ) ;
    void receive ( typename messages :: image_done msg ) ;
    void receive ( typename messages :: image_render msg ) ;
    void receive ( typename messages :: image_update msg ) ;
    void receive ( typename messages :: image_prepare_permit msg ) ;
private :
    void _render_image_mesh ( ) ;
    void _update_image_mesh ( ) ;
    void _create_image_mesh ( ) ;
    void _create_image_texture ( ) ;
private :
    mediator * _mediator ;
    num_whole _image_mesh_created ;
    num_whole _image_texture_created ;
    num_whole _image_texture_loaded ;
    num_whole _image_prepare_permitted ;
    num_whole _scale_frames ;
    mesh_id _image_mesh_id ;
    texture_id _image_texture_id ;
} ;

template < typename mediator >
shy_logic_image < mediator > :: shy_logic_image ( )
: _mediator ( 0 )
{
    platform :: math_make_num_whole ( _image_mesh_created , false ) ;
    platform :: math_make_num_whole ( _image_texture_created , false ) ;
    platform :: math_make_num_whole ( _image_texture_loaded , false ) ;
    platform :: math_make_num_whole ( _image_prepare_permitted , false ) ;
    platform :: math_make_num_whole ( _scale_frames , 0 ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: set_mediator ( mediator * arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_done msg )
{
    if ( platform :: condition_true ( _image_mesh_created ) )
        _mediator -> mesh_delete ( _image_mesh_id ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_render msg )
{
    if ( platform :: condition_true ( _image_mesh_created ) && platform :: condition_true ( _image_texture_loaded ) )
        _render_image_mesh ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_prepare_permit msg )
{
    platform :: math_make_num_whole ( _image_prepare_permitted , true ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: receive ( typename messages :: image_update msg )
{
    if ( platform :: condition_true ( _image_prepare_permitted ) )
    {
        if ( platform :: condition_false ( _image_mesh_created ) )
        {
            _create_image_mesh ( ) ;
            platform :: math_make_num_whole ( _image_mesh_created , true ) ;
        }
        if ( platform :: condition_false ( _image_texture_created ) )
        {
            _create_image_texture ( ) ;
            platform :: math_make_num_whole ( _image_texture_created , true ) ;
        }
        if ( platform :: condition_false ( _image_texture_loaded ) )
        {
            num_whole loader_ready ;
            platform :: render_texture_loader_ready ( loader_ready ) ;
            if ( platform :: condition_true ( loader_ready ) )
            {
                _mediator -> texture_finalize ( _image_texture_id ) ;
                platform :: math_make_num_whole ( _image_texture_loaded , true ) ;
                _mediator -> send ( typename messages :: image_prepared ( ) ) ;
            }
        }
    }
    if ( platform :: condition_true ( _image_mesh_created ) && platform :: condition_true ( _image_texture_loaded ) )
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
    platform :: math_make_num_whole ( whole_scale_in_frames , _scale_in_frames ) ;
    platform :: math_make_num_fract ( fract_scale_in_frames , _scale_in_frames , 1 ) ;
    platform :: math_make_fract_from_whole ( fract_scale_frames , _scale_frames ) ;
    engine_math :: math_lerp ( scale , platform :: fract_0 , platform :: fract_0 , _final_scale ( ) , fract_scale_in_frames , fract_scale_frames ) ;
    platform :: math_make_num_fract ( origin_x , 1 , 2 ) ;
    platform :: math_make_num_fract ( origin_y , 0 , 1 ) ;
    platform :: math_make_num_fract ( origin_z , - 3 , 1 ) ;
    platform :: matrix_set_axis_x ( matrix , scale , platform :: fract_0 , platform :: fract_0 ) ;
    platform :: matrix_set_axis_y ( matrix , platform :: fract_0 , scale , platform :: fract_0 ) ;
    platform :: matrix_set_axis_z ( matrix , platform :: fract_0 , platform :: fract_0 , scale ) ;
    platform :: matrix_set_origin ( matrix , origin_x , origin_y , origin_z ) ;
    _mediator -> mesh_set_transform ( _image_mesh_id , matrix ) ;
    if ( platform :: condition_whole_less_than_whole ( _scale_frames , whole_scale_in_frames ) )
        platform :: math_inc_whole ( _scale_frames ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _render_image_mesh ( )
{
    platform :: render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    _mediator -> texture_select ( _image_texture_id ) ;
    _mediator -> mesh_render ( _image_mesh_id ) ;
    platform :: render_blend_disable ( ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_mesh ( )
{
    typename platform :: template static_array < vertex_data , 4 > vertices ;
    typename platform :: template static_array < index_data , 4 > indices ;

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
    num_whole vertices_count ;
    
    platform :: math_make_num_fract ( x_left , - 1 , 1 ) ;
    platform :: math_make_num_fract ( x_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( y_bottom , - 1 , 1 ) ;
    platform :: math_make_num_fract ( u_left , 0 , 1 ) ;
    platform :: math_make_num_fract ( u_right , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_top , 1 , 1 ) ;
    platform :: math_make_num_fract ( v_bottom , 0 , 1 ) ;
    platform :: math_make_num_fract ( z , 0 , 1 ) ;
    platform :: math_make_num_fract ( color_r , _image_r , 255 ) ;
    platform :: math_make_num_fract ( color_g , _image_g , 255 ) ;
    platform :: math_make_num_fract ( color_b , _image_b , 255 ) ;
    platform :: math_make_num_fract ( color_a , _image_a , 255 ) ;
    platform :: math_make_num_whole ( vertices_count , 4 ) ;

    platform :: math_make_num_whole ( index , 0 ) ;
    platform :: render_set_vertex_position  ( platform :: array_element ( vertices , platform :: whole_0 ) , x_left , y_top , z ) ;
    platform :: render_set_vertex_color     ( platform :: array_element ( vertices , platform :: whole_0 ) , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( platform :: array_element ( vertices , platform :: whole_0 ) , u_left , v_top ) ;
    platform :: render_set_index_value      ( platform :: array_element ( indices  , platform :: whole_0 ) , index ) ;

    platform :: math_make_num_whole ( index , 1 ) ;
    platform :: render_set_vertex_position  ( platform :: array_element ( vertices , platform :: whole_1 ) , x_left , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( platform :: array_element ( vertices , platform :: whole_1 ) , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( platform :: array_element ( vertices , platform :: whole_1 ) , u_left , v_bottom ) ;
    platform :: render_set_index_value      ( platform :: array_element ( indices  , platform :: whole_1 ) , index ) ;

    platform :: math_make_num_whole ( index , 2 ) ;
    platform :: render_set_vertex_position  ( platform :: array_element ( vertices , platform :: whole_2 ) , x_right , y_top , z ) ;
    platform :: render_set_vertex_color     ( platform :: array_element ( vertices , platform :: whole_2 ) , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( platform :: array_element ( vertices , platform :: whole_2 ) , u_right , v_top ) ;
    platform :: render_set_index_value      ( platform :: array_element ( indices  , platform :: whole_2 ) , index ) ;

    platform :: math_make_num_whole ( index , 3 ) ;
    platform :: render_set_vertex_position  ( platform :: array_element ( vertices , platform :: whole_3 ) , x_right , y_bottom , z ) ;
    platform :: render_set_vertex_color     ( platform :: array_element ( vertices , platform :: whole_3 ) , color_r , color_g , color_b , color_a ) ;
    platform :: render_set_vertex_tex_coord ( platform :: array_element ( vertices , platform :: whole_3 ) , u_right , v_bottom ) ;
    platform :: render_set_index_value      ( platform :: array_element ( indices  , platform :: whole_3 ) , index ) ;

    _mediator -> mesh_create
        ( _image_mesh_id 
        , vertices 
        , indices 
        , indices
        , vertices_count 
        , vertices_count 
        , platform :: whole_0 
        ) ;
}

template < typename mediator >
void shy_logic_image < mediator > :: _create_image_texture ( )
{
    num_whole resource_index ;
    texture_resource_id logo_resource_id ;
    platform :: math_make_num_whole ( resource_index , _logo_resource_index ) ;
    platform :: render_create_texture_resource_id ( logo_resource_id , resource_index ) ;
    _mediator -> texture_create ( _image_texture_id ) ;
    _mediator -> texture_load_from_resource ( _image_texture_id , logo_resource_id ) ;
}
