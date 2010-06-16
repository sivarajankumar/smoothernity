inline void shy_macosx_platform :: render_enable_face_culling ( )
{
    glEnable ( GL_CULL_FACE ) ;
}

inline void shy_macosx_platform :: render_enable_depth_test ( )
{
    glEnable ( GL_DEPTH_TEST ) ;
}

inline void shy_macosx_platform :: render_disable_depth_test ( )
{
    glDisable ( GL_DEPTH_TEST ) ;
}

inline void shy_macosx_platform :: render_blend_disable ( )
{
    glDisable ( GL_BLEND ) ;
}

inline void shy_macosx_platform :: render_blend_src_alpha_dst_one_minus_alpha ( )
{
    glEnable ( GL_BLEND ) ;
    glBlendFunc ( GL_SRC_ALPHA , GL_ONE_MINUS_SRC_ALPHA ) ;
}

inline void shy_macosx_platform :: render_enable_texturing ( )
{
	glEnable ( GL_TEXTURE_2D ) ;
}

inline void shy_macosx_platform :: render_disable_texturing ( )
{
	glDisable ( GL_TEXTURE_2D ) ;
}

inline void shy_macosx_platform :: render_set_modulate_texture_mode ( )
{
    glTexEnvf ( GL_TEXTURE_ENV , GL_TEXTURE_ENV_MODE , GL_MODULATE ) ;
}

inline void shy_macosx_platform :: render_fog_disable ( )
{
    glDisable ( GL_FOG ) ;
}

inline void shy_macosx_platform :: render_fog_linear 
    ( num_fract near 
    , num_fract far 
    , num_fract r 
    , num_fract g 
    , num_fract b 
    , num_fract a 
    )
{
    GLfloat color [ ] = 
        { _platform_math_insider :: num_fract_unsafe_value_get ( r )
        , _platform_math_insider :: num_fract_unsafe_value_get ( g )
        , _platform_math_insider :: num_fract_unsafe_value_get ( b )
        , _platform_math_insider :: num_fract_unsafe_value_get ( a )
        } ;
    glEnable ( GL_FOG ) ;
    glFogf ( GL_FOG_MODE , GL_LINEAR ) ;
    glFogf ( GL_FOG_START , ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( near ) ) ;
    glFogf ( GL_FOG_END , ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( far ) ) ;
    glFogfv ( GL_FOG_COLOR , color ) ;
}

inline void shy_macosx_platform :: render_create_texture_id ( render_texture_id & arg_texture_id )
{
    glGenTextures ( 1 , & arg_texture_id . _texture_id ) ;
}

inline void shy_macosx_platform :: render_use_texture ( const render_texture_id & arg_texture_id )
{
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

inline void shy_macosx_platform :: render_set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    texel . _color [ 0 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f ) ;
    texel . _color [ 1 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f ) ;
    texel . _color [ 2 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) ;
    texel . _color [ 3 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( a ) * 255.0f ) ;
}

template < typename texels_array >
inline void shy_macosx_platform :: render_load_texture_data 
    ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data )
{
    GLsizei size = 1 << _platform_math_insider :: num_whole_unsafe_value_get ( size_pow2_base ) ;
    glPixelStorei ( GL_UNPACK_ALIGNMENT , 1 ) ;
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_S , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_T , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MAG_FILTER , GL_LINEAR ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MIN_FILTER , GL_LINEAR ) ;
    glTexImage2D ( GL_TEXTURE_2D , 0 , GL_RGBA , size , size , 0 , GL_BGRA , GL_UNSIGNED_BYTE 
        , _platform_static_array_insider :: array_elements_unsafe_ptr ( data ) 
        ) ;
}

inline void shy_macosx_platform :: render_create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    resource_id . _resource_id = _platform_math_insider :: num_whole_unsafe_value_get ( resource_index ) ;
}

template < typename texels_array >
inline void shy_macosx_platform :: render_load_texture_resource
    ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data )
{
    [ shy_macosx_platform_utility :: _texture_loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) _platform_static_array_insider :: array_elements_unsafe_ptr ( data )
        with_side_size_of : 1 << _platform_math_insider :: num_whole_unsafe_value_get ( size_pow2_base )
    ] ;
}

inline void shy_macosx_platform :: render_texture_loader_ready ( num_whole & is_ready )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( is_ready , [ shy_macosx_platform_utility :: _texture_loader loader_ready ] ) ;
}

inline void shy_macosx_platform :: render_clear_screen ( num_fract r , num_fract g , num_fract b )
{
    glClearColor 
        ( ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( r )
        , ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( g )
        , ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( b )
        , ( GLfloat ) 0
        ) ;
    glClearDepth ( 1 ) ;
    glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) ;
}

inline void shy_macosx_platform :: render_projection_frustum 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract near 
    , num_fract far 
    )
{
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glFrustum 
        ( _platform_math_insider :: num_fract_unsafe_value_get ( left )
        , _platform_math_insider :: num_fract_unsafe_value_get ( right )
        , _platform_math_insider :: num_fract_unsafe_value_get ( bottom )
        , _platform_math_insider :: num_fract_unsafe_value_get ( top )
        , _platform_math_insider :: num_fract_unsafe_value_get ( near )
        , _platform_math_insider :: num_fract_unsafe_value_get ( far )
        ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

inline void shy_macosx_platform :: render_projection_ortho 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract near 
    , num_fract far 
    )
{
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glOrtho 
        ( _platform_math_insider :: num_fract_unsafe_value_get ( left )
        , _platform_math_insider :: num_fract_unsafe_value_get ( right )
        , _platform_math_insider :: num_fract_unsafe_value_get ( bottom )
        , _platform_math_insider :: num_fract_unsafe_value_get ( top )
        , _platform_math_insider :: num_fract_unsafe_value_get ( near )
        , _platform_math_insider :: num_fract_unsafe_value_get ( far )
        ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

template < typename vertices_array >
inline void shy_macosx_platform :: render_create_vertex_buffer 
    ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glBufferData
        ( GL_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( vertex_data ) * ( unsigned int ) _platform_math_insider :: num_whole_unsafe_value_get ( elements ) ) 
        , _platform_static_array_insider :: array_elements_unsafe_ptr ( data )
        , GL_STATIC_DRAW 
        ) ;
}

inline void shy_macosx_platform :: render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
    vertex . _position [ 0 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    vertex . _position [ 1 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    vertex . _position [ 2 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

inline void shy_macosx_platform :: render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
    vertex . _tex_coord [ 0 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( u ) ;
    vertex . _tex_coord [ 1 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( v ) ;
}

inline void shy_macosx_platform :: render_set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
    vertex . _color [ 0 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) ;
    vertex . _color [ 1 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f ) ;
    vertex . _color [ 2 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f ) ;
    vertex . _color [ 3 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( a ) * 255.0f ) ;
}

template < typename indices_array >
inline void shy_macosx_platform :: render_create_index_buffer 
    ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glBufferData
        ( GL_ELEMENT_ARRAY_BUFFER
        , ( GLsizeiptr ) ( sizeof ( index_data ) * ( unsigned int ) _platform_math_insider :: num_whole_unsafe_value_get ( elements ) )
        , _platform_static_array_insider :: array_elements_unsafe_ptr ( data )
        , GL_STATIC_DRAW
        ) ;
}

inline void shy_macosx_platform :: render_set_index_value ( index_data & data , num_whole index )
{
    data . _index = ( GLushort ) _platform_math_insider :: num_whole_unsafe_value_get ( index ) ;
}

inline void shy_macosx_platform :: render_matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

inline void shy_macosx_platform :: render_matrix_load ( const matrix_data & matrix )
{
    glLoadMatrixf ( matrix . _elements ) ;
}

inline void shy_macosx_platform :: render_matrix_mult ( const matrix_data & matrix )
{
    glMultMatrixf ( matrix . _elements ) ;
}

inline void shy_macosx_platform :: render_matrix_push ( )
{
    glPushMatrix ( ) ;
}

inline void shy_macosx_platform :: render_matrix_pop ( )
{
    glPopMatrix ( ) ;
}

inline void shy_macosx_platform :: render_draw_triangle_strip 
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_STRIP 
        , ( GLsizei ) _platform_math_insider :: num_whole_unsafe_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

inline void shy_macosx_platform :: render_draw_triangle_fan
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , shy_macosx_platform_utility :: _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_FAN 
        , ( GLsizei ) _platform_math_insider :: num_whole_unsafe_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

inline void shy_macosx_platform :: render_get_aspect_width ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , shy_macosx_platform_utility :: _aspect_width ) ;
}

inline void shy_macosx_platform :: render_get_aspect_height ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , shy_macosx_platform_utility :: _aspect_height ) ;
}

inline void shy_macosx_platform :: render_delete_vertex_buffer ( const render_vertex_buffer_id & arg_buffer_id )
{
}

inline void shy_macosx_platform :: render_delete_index_buffer ( const render_index_buffer_id & arg_buffer_id )
{
}
