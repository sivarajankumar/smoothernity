template < typename mediator >
class shy_engine_render
{
    typedef typename mediator :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator :: mesh_id mesh_id ;
    typedef typename mediator :: messages messages ;
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
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator :: platform :: platform_render :: render_index_buffer_id render_index_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: render_index_buffer_mapped_data render_index_buffer_mapped_data ;
    typedef typename mediator :: platform :: platform_render :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: platform_render :: render_vertex_buffer_id render_vertex_buffer_id ;
    typedef typename mediator :: platform :: platform_render :: render_vertex_buffer_mapped_data render_vertex_buffer_mapped_data ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    typedef typename mediator :: texture_id texture_id ;
    
    class _engine_render_consts_type
    {
    public :
        _engine_render_consts_type ( ) ;
        num_whole texture_size_pow2_base ;
        static const_int_32 max_meshes = 100 ;
        static const_int_32 max_textures = 5 ;
    } ;
    
    class _texture_data
    {
    public :
        typename platform_static_array :: template static_array 
            < texel_data 
            , engine_render_stateless_consts_type :: texture_size_int
            * engine_render_stateless_consts_type :: texture_size_int
            > texels ;
        render_texture_id render_id ;
    } ;
    
    class _mesh_data
    {
    public :
        num_whole finalized ;
        
        render_vertex_buffer_id vertex_buffer_id ;
        render_index_buffer_id triangle_strip_index_buffer_id ;
        render_index_buffer_id triangle_fan_index_buffer_id ;
        
        render_vertex_buffer_mapped_data vertex_buffer_mapped_data ;
        render_index_buffer_mapped_data triangle_strip_index_buffer_mapped_data ;
        render_index_buffer_mapped_data triangle_fan_index_buffer_mapped_data ;
        
        num_whole vertices_count ;
        num_whole triangle_strip_indices_count ;
        num_whole triangle_fan_indices_count ;
        
        matrix_data transform ;
    } ;
    
public :
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void receive ( typename messages :: init msg ) ;
    void receive ( typename messages :: render_aspect_request msg ) ;
    void receive ( typename messages :: render_texture_create_request msg ) ;
    void receive ( typename messages :: render_texture_finalize msg ) ;
    void receive ( typename messages :: render_texture_load_from_resource msg ) ;
    void receive ( typename messages :: render_texture_loader_ready_request msg ) ;
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
    typename platform_pointer :: template pointer < platform_render > _platform_render ;
    typename platform_pointer :: template pointer < const platform_math_consts > _platform_math_consts ;
    typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > _engine_render_stateless_consts ;
    typename platform_static_array :: template static_array < _texture_data , _engine_render_consts_type :: max_textures > _textures_datas ;
    typename platform_static_array :: template static_array < _mesh_data , _engine_render_consts_type :: max_meshes > _meshes_data ;
    const _engine_render_consts_type _engine_render_consts ;
    num_whole _next_texture_id ;
    num_whole _next_mesh_id ;
} ;

template < typename mediator >
shy_engine_render < mediator > :: _engine_render_consts_type :: _engine_render_consts_type ( )
{
    platform_math :: make_num_whole ( texture_size_pow2_base , engine_render_stateless_consts_type :: texture_size_pow2_base_int ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: init msg )
{
    typename platform_pointer :: template pointer < const platform > platform_obj ;
    _mediator . get ( ) . platform_obj ( platform_obj ) ;
    _mediator . get ( ) . engine_render_stateless_consts ( _engine_render_stateless_consts ) ;
    _platform_render = platform_obj . get ( ) . render ;
    _platform_math_consts = platform_obj . get ( ) . math_consts ;
    _next_texture_id = _platform_math_consts . get ( ) . whole_0 ;
    _next_mesh_id = _platform_math_consts . get ( ) . whole_0 ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_aspect_request msg )
{
    typename messages :: render_aspect_reply reply_msg ;
    _platform_render . get ( ) . get_aspect_width ( reply_msg . width ) ;
    _platform_render . get ( ) . get_aspect_height ( reply_msg . height ) ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_clear_screen msg )
{
    _platform_render . get ( ) . clear_screen ( msg . r , msg . g , msg . b ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_disable_depth_test msg )
{
    _platform_render . get ( ) . disable_depth_test ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_enable_depth_test msg )
{
    _platform_render . get ( ) . enable_depth_test ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_matrix_load msg )
{
    _platform_render . get ( ) . matrix_load ( msg . matrix ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_fog_disable msg )
{
    _platform_render . get ( ) . fog_disable ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_blend_src_alpha_dst_one_minus_alpha msg )
{
    _platform_render . get ( ) . blend_src_alpha_dst_one_minus_alpha ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_blend_disable msg )
{
    _platform_render . get ( ) . blend_disable ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_fog_linear msg )
{
    _platform_render . get ( ) . fog_linear ( msg . znear , msg . zfar , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_projection_frustum msg )
{
    _platform_render . get ( ) . projection_frustum ( msg . left , msg . right , msg . bottom , msg . top , msg . znear , msg . zfar ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_projection_ortho msg )
{
    _platform_render . get ( ) . projection_ortho ( msg . left , msg . right , msg . bottom , msg . top , msg . znear , msg . zfar ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_matrix_identity msg )
{
    _platform_render . get ( ) . matrix_identity ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_enable_face_culling msg )
{
    _platform_render . get ( ) . enable_face_culling ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_mode_modulate msg )
{
    _platform_render . get ( ) . texture_mode_modulate ( ) ;
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
    typename platform_pointer :: template pointer < _texture_data > texture ;
    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
    _platform_render . get ( ) . create_texture_id ( texture . get ( ) . render_id ) ;
    _platform_render . get ( ) . load_texture_data 
        ( texture . get ( ) . render_id 
        , _engine_render_consts . texture_size_pow2_base 
        , texture . get ( ) . texels 
        ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_load_from_resource msg )
{
    num_whole size_pow2_base ;
    typename platform_pointer :: template pointer < _texture_data > texture ;
    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
    _platform_render . get ( ) . load_texture_resource 
        ( msg . resource 
        , _engine_render_consts . texture_size_pow2_base 
        , texture . get ( ) . texels 
        ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_loader_ready_request msg )
{
    typename messages :: render_texture_loader_ready_reply reply_msg ;
    _platform_render . get ( ) . texture_loader_ready ( reply_msg . ready ) ;
    _mediator . get ( ) . send ( reply_msg ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_select msg )
{
    typename platform_pointer :: template pointer < _texture_data > texture ;
    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
    _platform_render . get ( ) . enable_texturing ( ) ;
    _platform_render . get ( ) . use_texture ( texture . get ( ) . render_id ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_unselect msg )
{
    _platform_render . get ( ) . disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texel msg )
{
    num_whole texel_offset ;
    typename platform_pointer :: template pointer < _texture_data > texture ;
    typename platform_pointer :: template pointer < texel_data > texel ;
    
    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: mul_wholes ( texel_offset , _engine_render_stateless_consts . get ( ) . texture_width , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
    texel . get ( ) = msg . texel ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texel_rgba msg )
{
    num_whole texel_offset ;
    typename platform_pointer :: template pointer < _texture_data > texture ;
    typename platform_pointer :: template pointer < texel_data > texel ;

    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: mul_wholes ( texel_offset , _engine_render_stateless_consts . get ( ) . texture_width , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
    platform_render :: set_texel_color ( texel . get ( ) , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_texture_set_texels_rect msg )
{
    num_whole texel_offset ;
    typename platform_pointer :: template pointer < _texture_data > texture ;
    platform_static_array :: element_ptr ( texture , _textures_datas , msg . texture . _texture_id ) ;
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
            typename platform_pointer :: template pointer < texel_data > texel ;
            platform_math :: mul_wholes ( texel_offset , _engine_render_stateless_consts . get ( ) . texture_width , y ) ;
            platform_math :: add_to_whole ( texel_offset , x ) ;
            platform_static_array :: element_ptr ( texel , texture . get ( ) . texels , texel_offset ) ;
            texel . get ( ) = msg . texel ;
        }
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_create_request msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , _next_mesh_id ) ;

    mesh . get ( ) . finalized = _platform_math_consts . get ( ) . whole_false ;
    mesh . get ( ) . vertices_count = msg . vertices ;
    mesh . get ( ) . triangle_strip_indices_count = msg . triangle_strip_indices ;
    mesh . get ( ) . triangle_fan_indices_count = msg . triangle_fan_indices ;
    platform_matrix :: identity ( mesh . get ( ) . transform ) ;
    
    _platform_render . get ( ) . create_vertex_buffer ( mesh . get ( ) . vertex_buffer_id , mesh . get ( ) . vertices_count ) ;
    _platform_render . get ( ) . map_vertex_buffer ( mesh . get ( ) . vertex_buffer_mapped_data , mesh . get ( ) . vertex_buffer_id ) ;
    
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_strip_indices_count ) )
    {
        _platform_render . get ( ) . create_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id , mesh . get ( ) . triangle_strip_indices_count ) ;
        _platform_render . get ( ) . map_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_mapped_data , mesh . get ( ) . triangle_strip_index_buffer_id ) ;
    }
    
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_fan_indices_count ) )
    {
        _platform_render . get ( ) . create_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id , mesh . get ( ) . triangle_fan_indices_count ) ;
        _platform_render . get ( ) . map_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_mapped_data , mesh . get ( ) . triangle_fan_index_buffer_id ) ;
    }
    
    typename messages :: render_mesh_create_reply reply_msg ;
    reply_msg . mesh . _mesh_id = _next_mesh_id ;
    platform_math :: inc_whole ( _next_mesh_id ) ;
    _mediator . get ( ) . send ( reply_msg ) ;    
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_finalize msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    mesh . get ( ) . finalized = _platform_math_consts . get ( ) . whole_true ;
    _platform_render . get ( ) . unmap_vertex_buffer ( mesh . get ( ) . vertex_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_strip_indices_count ) )
        _platform_render . get ( ) . unmap_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_fan_indices_count ) )
        _platform_render . get ( ) . unmap_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_position msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    typename platform_pointer :: template pointer < vertex_data > vertex ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    if ( platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) 
      && platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count )
       )
    {
        platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
        platform_render :: set_vertex_position ( vertex . get ( ) , msg . x , msg . y , msg . z ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_tex_coord msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    typename platform_pointer :: template pointer < vertex_data > vertex ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    if ( platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) 
      && platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count )
       )
    {
        platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
        platform_render :: set_vertex_tex_coord ( vertex . get ( ) , msg . u , msg . v ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_vertex_color msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    typename platform_pointer :: template pointer < vertex_data > vertex ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    if ( platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) 
      && platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . vertices_count )
       )
    {
        platform_render :: mapped_vertex_buffer_element ( vertex , mesh . get ( ) . vertex_buffer_mapped_data , msg . offset ) ;
        platform_render :: set_vertex_color ( vertex . get ( ) , msg . r , msg . g , msg . b , msg . a ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_triangle_strip_index_value msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    typename platform_pointer :: template pointer < index_data > index ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    if ( platform_conditions :: whole_is_false ( mesh . get ( ) . finalized ) 
      && platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . triangle_strip_indices_count )
       )
    {
        platform_render :: mapped_index_buffer_element ( index , mesh . get ( ) . triangle_strip_index_buffer_mapped_data , msg . offset ) ;
        platform_render :: set_index_value ( index . get ( ) , msg . index ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_triangle_fan_index_value msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    typename platform_pointer :: template pointer < index_data > index ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    if ( platform_conditions :: whole_is_false ( mesh . get ( ) . finalized )
      && platform_conditions :: whole_less_than_whole ( msg . offset , mesh . get ( ) . triangle_fan_indices_count )
       )
    {
        platform_render :: mapped_index_buffer_element ( index , mesh . get ( ) . triangle_fan_index_buffer_mapped_data , msg . offset ) ;
        platform_render :: set_index_value ( index . get ( ) , msg . index ) ;
    }
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_delete msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    _platform_render . get ( ) . delete_vertex_buffer ( mesh . get ( ) . vertex_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_strip_indices_count ) )
        _platform_render . get ( ) . delete_index_buffer ( mesh . get ( ) . triangle_strip_index_buffer_id ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_fan_indices_count ) )
        _platform_render . get ( ) . delete_index_buffer ( mesh . get ( ) . triangle_fan_index_buffer_id ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_render msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    _platform_render . get ( ) . matrix_push ( ) ;
    _platform_render . get ( ) . matrix_mult ( mesh . get ( ) . transform ) ;
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_strip_indices_count ) )
    {
        _platform_render . get ( ) . draw_triangle_strip 
            ( mesh . get ( ) . vertex_buffer_id 
            , mesh . get ( ) . triangle_strip_index_buffer_id 
            , mesh . get ( ) . triangle_strip_indices_count
            ) ;
    }
    if ( platform_conditions :: whole_greater_than_zero ( mesh . get ( ) . triangle_fan_indices_count ) )
    {
        _platform_render . get ( ) . draw_triangle_fan 
            ( mesh . get ( ) . vertex_buffer_id 
            , mesh . get ( ) . triangle_fan_index_buffer_id 
            , mesh . get ( ) . triangle_fan_indices_count
            ) ;
    }
    _platform_render . get ( ) . matrix_pop ( ) ;
}

template < typename mediator >
void shy_engine_render < mediator > :: receive ( typename messages :: render_mesh_set_transform msg )
{
    typename platform_pointer :: template pointer < _mesh_data > mesh ;
    platform_static_array :: element_ptr ( mesh , _meshes_data , msg . mesh . _mesh_id ) ;
    mesh . get ( ) . transform = msg . transform ;
}
