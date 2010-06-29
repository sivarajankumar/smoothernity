template < typename mediator >
class shy_engine_render
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix platform_matrix ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: render_index_buffer_id render_index_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: platform_render :: render_vertex_buffer_id render_vertex_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: texture_id texture_id ;
    
    static const_int_32 _max_meshes = 100 ;
    static const_int_32 _max_vertices = 1000 ;
    static const_int_32 _max_indices = 1000 ;
    static const_int_32 _max_textures = 5 ;
    static const_int_32 _texture_size_pow2_base = engine_render_stateless :: _texture_size_pow2_base ;
    static const_int_32 _texture_size = engine_render_stateless :: _texture_size ;
    
    class _texture_data
    {
    public :
        typename platform_static_array :: template static_array < texel_data , _texture_size * _texture_size > texels ;
        render_texture_id render_id ;
    } ;
    
    class _mesh_data
    {
    public :
        render_vertex_buffer_id vertex_buffer_id ;
        render_index_buffer_id triangle_strip_index_buffer_id ;
        render_index_buffer_id triangle_fan_index_buffer_id ;
        num_whole vertices_count ;
        num_whole triangle_strip_indices_count ;
        num_whole triangle_fan_indices_count ;
        matrix_data transform ;
        typename platform_static_array :: template static_array < vertex_data , _max_vertices > vertices ;
        typename platform_static_array :: template static_array < index_data , _max_indices > triangle_strip_indices ;
        typename platform_static_array :: template static_array < index_data , _max_indices > triangle_fan_indices ;
    } ;
    
public :
    shy_engine_render ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: render_texture_create_request msg ) ;
    void receive ( typename messages :: render_texture_finalize msg ) ;
    void receive ( typename messages :: render_texture_load_from_resource msg ) ;
    void receive ( typename messages :: render_texture_select msg ) ;
    void receive ( typename messages :: render_texture_unselect msg ) ;
    void receive ( typename messages :: render_texture_set_texels_rect msg ) ;
    void receive ( typename messages :: render_texture_set_texel msg ) ;
    void receive ( typename messages :: render_texture_set_texel_rgba msg ) ;
    void receive ( typename messages :: render_mesh_create_request msg ) ;
    void receive ( typename messages :: render_mesh_finalize msg ) ;
    void receive ( typename messages :: render_mesh_set_vertex_position msg ) ;
    void receive ( typename messages :: render_mesh_set_vertex_tex_coord msg ) ;
    void receive ( typename messages :: render_mesh_set_vertex_color msg ) ;
    void receive ( typename messages :: render_mesh_set_triangle_strip_index_value msg ) ;
    void receive ( typename messages :: render_mesh_set_triangle_fan_index_value msg ) ;
    void receive ( typename messages :: render_mesh_set_transform msg ) ;
    void receive ( typename messages :: render_mesh_render msg ) ;
    void receive ( typename messages :: render_mesh_delete msg ) ;
    void receive ( typename messages :: render_clear_screen msg ) ;
    void receive ( typename messages :: render_disable_depth_test msg ) ;
    void receive ( typename messages :: render_enable_depth_test msg ) ;
    void receive ( typename messages :: render_matrix_load msg ) ;
    void receive ( typename messages :: render_fog_disable msg ) ;
    void receive ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha msg ) ;
    void receive ( typename messages :: render_blend_disable msg ) ;
    void receive ( typename messages :: render_fog_linear msg ) ;
    void receive ( typename messages :: render_projection_frustum msg ) ;
    void receive ( typename messages :: render_projection_ortho msg ) ;
    void receive ( typename messages :: render_matrix_identity msg ) ;
    void receive ( typename messages :: render_enable_face_culling msg ) ;
    void receive ( typename messages :: render_texture_mode_modulate msg ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_static_array :: template static_array < _texture_data , _max_textures > _textures_datas ;
    typename platform_static_array :: template static_array < _mesh_data , _max_meshes > _meshes_data ;
    num_whole _next_texture_id ;
    num_whole _next_mesh_id ;
} ;

template < typename mediator >
shy_engine_render < mediator > :: shy_engine_render ( )
{
    platform_math :: make_num_whole ( _next_texture_id , 0 ) ;
    platform_math :: make_num_whole ( _next_mesh_id , 0 ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_clear_screen msg )
{
    platform_render :: clear_screen ( msg . r , msg . g , msg . b ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_disable_depth_test msg )
{
    platform_render :: disable_depth_test ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_enable_depth_test msg )
{
    platform_render :: enable_depth_test ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_matrix_load msg )
{
    platform_render :: matrix_load ( msg . matrix ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_fog_disable msg )
{
    platform_render :: fog_disable ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha msg )
{
    platform_render :: blend_src_alpha_dst_one_minus_alpha ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_blend_disable msg )
{
    platform_render :: blend_disable ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_fog_linear msg )
{
    platform_render :: fog_linear ( msg . near , msg . far , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_projection_frustum msg )
{
    platform_render :: projection_frustum ( msg . left , msg . right , msg . bottom , msg . top , msg . near , msg . far ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_projection_ortho msg )
{
    platform_render :: projection_ortho ( msg . left , msg . right , msg . bottom , msg . top , msg . near , msg . far ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_matrix_identity msg )
{
    platform_render :: matrix_identity ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_enable_face_culling msg )
{
    platform_render :: enable_face_culling ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_mode_modulate msg )
{
    platform_render :: texture_mode_modulate ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_create_request msg )
{
    typename messages :: render_texture_create_reply texture_create_reply_msg ;
    texture_create_reply_msg . texture . _texture_id = _next_texture_id ;
    platform_math :: inc_whole ( _next_texture_id ) ;
    _mediator . get ( ) . send ( texture_create_reply_msg ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_finalize msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform_render :: create_texture_id ( texture . render_id ) ;
    platform_render :: load_texture_data ( texture . render_id , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_load_from_resource msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform_render :: load_texture_resource ( msg . resource , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_select msg )
{
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_render :: enable_texturing ( ) ;
    platform_render :: use_texture ( texture . render_id ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_unselect msg )
{
    platform_render :: disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texel msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    platform_math :: mul_wholes ( texel_offset , num_texture_size , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    platform_static_array :: element ( texture . texels , texel_offset ) = msg . texel ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texel_rgba msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    platform_math :: mul_wholes ( texel_offset , num_texture_size , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    texel_data & texel = platform_static_array :: element ( texture . texels , texel_offset ) ;
    platform_render :: set_texel_color ( texel , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texels_rect msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    for ( num_whole y = msg . bottom
        ; platform_conditions :: whole_less_or_equal_to_whole ( y , msg . top )
        ; platform_math :: inc_whole ( y )
        )
    {
        for ( num_whole x = msg . left
            ; platform_conditions :: whole_less_or_equal_to_whole ( x , msg . right )
            ; platform_math :: inc_whole ( x )
            )
        {
            platform_math :: mul_wholes ( texel_offset , num_texture_size , y ) ;
            platform_math :: add_to_whole ( texel_offset , x ) ;
            platform_static_array :: element ( texture . texels , texel_offset ) = msg . texel ;
        }
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_create_request msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , _next_mesh_id ) ;
    mesh . vertices_count = msg . vertices ;
    mesh . triangle_strip_indices_count = msg . triangle_strip_indices ;
    mesh . triangle_fan_indices_count = msg . triangle_fan_indices ;
    platform_matrix :: identity ( mesh . transform ) ;
    
    typename messages :: render_mesh_create_reply reply_msg ;
    reply_msg . mesh . _mesh_id = _next_mesh_id ;
    platform_math :: inc_whole ( _next_mesh_id ) ;
    _mediator . get ( ) . send ( reply_msg ) ;    
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_finalize msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: create_vertex_buffer ( mesh . vertex_buffer_id , mesh . vertices_count , mesh . vertices ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
    {
        platform_render :: create_index_buffer 
            ( mesh . triangle_strip_index_buffer_id 
            , mesh . triangle_strip_indices_count 
            , mesh . triangle_strip_indices 
            ) ;
    }
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
    {
        platform_render :: create_index_buffer 
            ( mesh . triangle_fan_index_buffer_id 
            , mesh . triangle_fan_indices_count 
            , mesh . triangle_fan_indices 
            ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_position msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , msg . offset ) ;
    platform_render :: set_vertex_position ( vertex , msg . x , msg . y , msg . z ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_tex_coord msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , msg . offset ) ;
    platform_render :: set_vertex_tex_coord ( vertex , msg . u , msg . v ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_color msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    vertex_data & vertex = platform_static_array :: element ( mesh . vertices , msg . offset ) ;
    platform_render :: set_vertex_color ( vertex , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_triangle_strip_index_value msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    index_data & index = platform_static_array :: element ( mesh . triangle_strip_indices , msg . offset ) ;
    platform_render :: set_index_value ( index , msg . index ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_triangle_fan_index_value msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    index_data & index = platform_static_array :: element ( mesh . triangle_fan_indices , msg . offset ) ;
    platform_render :: set_index_value ( index , msg . index ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_delete msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: delete_vertex_buffer ( mesh . vertex_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
        platform_render :: delete_index_buffer ( mesh . triangle_strip_index_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
        platform_render :: delete_index_buffer ( mesh . triangle_fan_index_buffer_id ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_render msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    platform_render :: matrix_push ( ) ;
    platform_render :: matrix_mult ( mesh . transform ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_strip_indices_count ) )
    {
        platform_render :: draw_triangle_strip 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_strip_index_buffer_id 
            , mesh . triangle_strip_indices_count
            ) ;
    }
    if ( platform_conditions :: whole_greater_than_zero ( mesh . triangle_fan_indices_count ) )
    {
        platform_render :: draw_triangle_fan 
            ( mesh . vertex_buffer_id 
            , mesh . triangle_fan_index_buffer_id 
            , mesh . triangle_fan_indices_count
            ) ;
    }
    platform_render :: matrix_pop ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_transform msg )
{
    _mesh_data & mesh = platform_static_array :: element ( _meshes_data , msg . mesh . _mesh_id ) ;
    mesh . transform = msg . transform ;
}
