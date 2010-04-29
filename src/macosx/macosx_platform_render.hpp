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
    ( shy_macosx_platform :: float_32 near 
    , shy_macosx_platform :: float_32 far 
    , shy_macosx_platform :: float_32 r 
    , shy_macosx_platform :: float_32 g 
    , shy_macosx_platform :: float_32 b 
    , shy_macosx_platform :: float_32 a 
    )
{
    GLfloat color [ ] = { r , g , b , a } ;
    glEnable ( GL_FOG ) ;
    glFogf ( GL_FOG_MODE , GL_LINEAR ) ;
    glFogf ( GL_FOG_START , ( GLfloat ) near ) ;
    glFogf ( GL_FOG_END , ( GLfloat ) far ) ;
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

inline void shy_macosx_platform :: render_set_texel_color ( texel_data & texel , int_32 r , int_32 g , int_32 b , int_32 a )
{
    texel . _color [ 0 ] = ( GLubyte ) r ;
    texel . _color [ 1 ] = ( GLubyte ) g ;
    texel . _color [ 2 ] = ( GLubyte ) b ;
    texel . _color [ 3 ] = ( GLubyte ) a ;
}

inline void shy_macosx_platform :: render_load_texture_data 
    ( const render_texture_id & arg_texture_id 
    , int_32 size_pow2_base 
    , texel_data * data
    )
{
    GLsizei size = 1 << size_pow2_base ;
    glPixelStorei ( GL_UNPACK_ALIGNMENT , 1 ) ;
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_S , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_T , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MAG_FILTER , GL_LINEAR ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MIN_FILTER , GL_LINEAR ) ;
    glTexImage2D ( GL_TEXTURE_2D , 0 , GL_RGBA , size , size , 0 , GL_RGBA , GL_UNSIGNED_BYTE , data ) ;
}

inline void shy_macosx_platform :: render_clear_screen 
    ( shy_macosx_platform :: float_32 r 
    , shy_macosx_platform :: float_32 g 
    , shy_macosx_platform :: float_32 b 
    )
{
    glClearColor ( ( GLfloat ) r , ( GLfloat ) g , ( GLfloat ) b , ( GLfloat ) 0 ) ;
    glClearDepth ( 1 ) ;
    glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) ;
}

inline void shy_macosx_platform :: render_projection_frustum 
    ( shy_macosx_platform :: float_32 left 
    , shy_macosx_platform :: float_32 right 
    , shy_macosx_platform :: float_32 bottom 
    , shy_macosx_platform :: float_32 top 
    , shy_macosx_platform :: float_32 near 
    , shy_macosx_platform :: float_32 far 
    )
{
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glFrustum ( left , right , bottom , top , near , far ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

inline void shy_macosx_platform :: render_projection_ortho 
    ( shy_macosx_platform :: float_32 left 
    , shy_macosx_platform :: float_32 right 
    , shy_macosx_platform :: float_32 bottom 
    , shy_macosx_platform :: float_32 top 
    , shy_macosx_platform :: float_32 near 
    , shy_macosx_platform :: float_32 far 
    )
{
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glOrtho ( left , right , bottom , top , near , far ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

inline void shy_macosx_platform :: render_create_vertex_buffer 
    ( shy_macosx_platform :: render_vertex_buffer_id & arg_buffer_id 
    , shy_macosx_platform :: int_32 elements 
    , shy_macosx_platform :: vertex_data * data 
    )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glBufferData
        ( GL_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( vertex_data ) * ( unsigned int ) elements ) 
        , data
        , GL_STATIC_DRAW 
        ) ;
}

inline void shy_macosx_platform :: render_set_vertex_position 
    ( shy_macosx_platform :: vertex_data & vertex 
    , shy_macosx_platform :: float_32 x 
    , shy_macosx_platform :: float_32 y 
    , shy_macosx_platform :: float_32 z 
    )
{
    vertex . _position [ 0 ] = ( GLfloat ) x ;
    vertex . _position [ 1 ] = ( GLfloat ) y ;
    vertex . _position [ 2 ] = ( GLfloat ) z ;
}

inline void shy_macosx_platform :: render_set_vertex_tex_coord
    ( shy_macosx_platform :: vertex_data & vertex 
    , shy_macosx_platform :: float_32 u
    , shy_macosx_platform :: float_32 v 
    )
{
    vertex . _tex_coord [ 0 ] = ( GLfloat ) u ;
    vertex . _tex_coord [ 1 ] = ( GLfloat ) v ;
}

inline void shy_macosx_platform :: render_set_vertex_color 
    ( shy_macosx_platform :: vertex_data & vertex 
    , shy_macosx_platform :: int_32 r 
    , shy_macosx_platform :: int_32 g 
    , shy_macosx_platform :: int_32 b 
    , shy_macosx_platform :: int_32 a 
    )
{
    vertex . _color [ 0 ] = ( GLubyte ) r ;
    vertex . _color [ 1 ] = ( GLubyte ) g ;
    vertex . _color [ 2 ] = ( GLubyte ) b ;
    vertex . _color [ 3 ] = ( GLubyte ) a ;
}

inline void shy_macosx_platform :: render_create_index_buffer 
    ( shy_macosx_platform :: render_index_buffer_id & arg_buffer_id 
    , shy_macosx_platform :: int_32 elements 
    , shy_macosx_platform :: index_data * data 
    )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glBufferData
        ( GL_ELEMENT_ARRAY_BUFFER
        , ( GLsizeiptr ) ( sizeof ( index_data ) * ( unsigned int ) elements )
        , data
        , GL_STATIC_DRAW
        ) ;
}

inline void shy_macosx_platform :: render_set_index_value 
    ( shy_macosx_platform :: index_data & data 
    , shy_macosx_platform :: int_32 index 
    )
{
    data . _index = ( GLushort ) index ;
}

inline void shy_macosx_platform :: render_matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

inline void shy_macosx_platform :: render_matrix_load 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
{
    glLoadMatrixf ( matrix . _elements ) ;
}

inline void shy_macosx_platform :: render_matrix_mult 
    ( const shy_macosx_platform :: matrix_data & matrix 
    )
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
    ( const shy_macosx_platform :: render_vertex_buffer_id & vertices_buffer 
    , const shy_macosx_platform :: render_index_buffer_id & indices_buffer
    , shy_macosx_platform :: int_32 indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , _vertex_color_offset ) ;
    glDrawElements ( GL_TRIANGLE_STRIP , ( GLsizei ) indices_count , GL_UNSIGNED_SHORT , ( void * ) 0 ) ;
}

inline void shy_macosx_platform :: render_draw_triangle_fan
    ( const shy_macosx_platform :: render_vertex_buffer_id & vertices_buffer 
    , const shy_macosx_platform :: render_index_buffer_id & indices_buffer
    , shy_macosx_platform :: int_32 indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , _vertex_color_offset ) ;
    glDrawElements ( GL_TRIANGLE_FAN , ( GLsizei ) indices_count , GL_UNSIGNED_SHORT , ( void * ) 0 ) ;
}

inline
shy_macosx_platform :: float_32
shy_macosx_platform :: render_get_aspect_width ( )
{
	return _aspect_width ;
}

inline
shy_macosx_platform :: float_32
shy_macosx_platform :: render_get_aspect_height ( )
{
	return _aspect_height ;
}
