namespace shy_guts
{
    static so_called_type_platform_render_opengl_vertex_data reference_vertex ;
    static void * vertex_position_offset = 0 ;
    static void * vertex_tex_coord_offset = 0 ;
    static void * vertex_color_offset = 0 ;
}

void shy_platform_render_opengl :: init ( )
{
    shy_guts :: vertex_position_offset = reinterpret_cast < void * >
        ( reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex . _position ) 
        - reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex )
        ) ;
    shy_guts :: vertex_tex_coord_offset = reinterpret_cast < void * >
        ( reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex . _tex_coord ) 
        - reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex )
        ) ;
    shy_guts :: vertex_color_offset = reinterpret_cast < void * >
        ( reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex . _color ) 
        - reinterpret_cast < so_called_lib_std_char * > ( & shy_guts :: reference_vertex )
        ) ;
}

void shy_platform_render_opengl :: done ( )
{
}

void shy_platform_render_opengl :: _load_texture_subdata 
    ( so_called_type_platform_render_opengl_texture_id arg_texture_id 
    , so_called_type_platform_math_num_whole x_offset 
    , so_called_type_platform_math_num_whole y_offset 
    , so_called_type_platform_math_num_whole width
    , so_called_type_platform_math_num_whole height
    , const so_called_type_platform_render_opengl_texel_data * texels
    )
{
    so_called_lib_std_int32_t x_offset_int = 0 ;
    so_called_lib_std_int32_t y_offset_int = 0 ;
    so_called_lib_std_int32_t width_int = 0 ;
    so_called_lib_std_int32_t height_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( x_offset_int , x_offset ) ;
    so_called_platform_math_insider :: num_whole_value_get ( y_offset_int , y_offset ) ;
    so_called_platform_math_insider :: num_whole_value_get ( width_int , width ) ;
    so_called_platform_math_insider :: num_whole_value_get ( height_int , height ) ;
    
    so_called_lib_opengl_glBindTexture ( so_called_lib_opengl_GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    so_called_lib_opengl_glTexSubImage2D 
        ( so_called_lib_opengl_GL_TEXTURE_2D    // target
        , 0                                     // level
        , x_offset_int                          // x offset
        , y_offset_int                          // y offset
        , width_int                             // width
        , height_int                            // height
        , so_called_lib_opengl_GL_BGRA          // format
        , so_called_lib_opengl_GL_UNSIGNED_BYTE // type
        , texels                                // data
        ) ;
}

void shy_platform_render_opengl :: enable_face_culling ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_CULL_FACE ) ;
}

void shy_platform_render_opengl :: enable_depth_test ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_DEPTH_TEST ) ;
}

void shy_platform_render_opengl :: disable_depth_test ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_DEPTH_TEST ) ;
}

void shy_platform_render_opengl :: blend_disable ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_BLEND ) ;
}

void shy_platform_render_opengl :: blend_src_alpha_dst_one_minus_alpha ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_BLEND ) ;
    so_called_lib_opengl_glBlendFunc ( so_called_lib_opengl_GL_SRC_ALPHA , so_called_lib_opengl_GL_ONE_MINUS_SRC_ALPHA ) ;
}

void shy_platform_render_opengl :: enable_texturing ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_TEXTURE_2D ) ;
}

void shy_platform_render_opengl :: disable_texturing ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_TEXTURE_2D ) ;
}

void shy_platform_render_opengl :: texture_mode_modulate ( )
{
    so_called_lib_opengl_glTexEnvf ( so_called_lib_opengl_GL_TEXTURE_ENV , so_called_lib_opengl_GL_TEXTURE_ENV_MODE , so_called_lib_opengl_GL_MODULATE ) ;
}

void shy_platform_render_opengl :: fog_disable ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_FOG ) ;
}

void shy_platform_render_opengl :: fog_linear 
    ( so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    , so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    , so_called_type_platform_math_num_fract a 
    )
{
    so_called_lib_std_float r_float ;
    so_called_lib_std_float g_float ;
    so_called_lib_std_float b_float ;
    so_called_lib_std_float a_float ;
    so_called_lib_std_float near_float ;
    so_called_lib_std_float far_float ;

    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;

    so_called_lib_opengl_GLfloat color [ ] = { r_float , g_float , b_float , a_float } ;
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_FOG ) ;
    so_called_lib_opengl_glFogf ( so_called_lib_opengl_GL_FOG_MODE , so_called_lib_opengl_GL_LINEAR ) ;
    so_called_lib_opengl_glFogf ( so_called_lib_opengl_GL_FOG_START , ( so_called_lib_opengl_GLfloat ) near_float ) ;
    so_called_lib_opengl_glFogf ( so_called_lib_opengl_GL_FOG_END , ( so_called_lib_opengl_GLfloat ) far_float ) ;
    so_called_lib_opengl_glFogfv ( so_called_lib_opengl_GL_FOG_COLOR , color ) ;
}

void shy_platform_render_opengl :: create_texture_id 
    ( so_called_type_platform_render_opengl_texture_id & arg_texture_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    )
{
    so_called_lib_opengl_glGenTextures ( 1 , & arg_texture_id . _texture_id ) ;
    so_called_lib_std_int32_t size_pow2_base_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    so_called_lib_opengl_GLsizei size = 1 << size_pow2_base_int ;
    so_called_lib_opengl_glPixelStorei ( so_called_lib_opengl_GL_UNPACK_ALIGNMENT , 1 ) ;
    so_called_lib_opengl_glBindTexture ( so_called_lib_opengl_GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    so_called_lib_opengl_glTexParameteri ( so_called_lib_opengl_GL_TEXTURE_2D , so_called_lib_opengl_GL_TEXTURE_WRAP_S , so_called_lib_opengl_GL_REPEAT ) ;
    so_called_lib_opengl_glTexParameteri ( so_called_lib_opengl_GL_TEXTURE_2D , so_called_lib_opengl_GL_TEXTURE_WRAP_T , so_called_lib_opengl_GL_REPEAT ) ;
    so_called_lib_opengl_glTexParameteri ( so_called_lib_opengl_GL_TEXTURE_2D , so_called_lib_opengl_GL_TEXTURE_MAG_FILTER , so_called_lib_opengl_GL_LINEAR ) ;
    so_called_lib_opengl_glTexParameteri ( so_called_lib_opengl_GL_TEXTURE_2D , so_called_lib_opengl_GL_TEXTURE_MIN_FILTER , so_called_lib_opengl_GL_LINEAR ) ;
    so_called_lib_opengl_glTexImage2D
        ( so_called_lib_opengl_GL_TEXTURE_2D    // target
        , 0                                     // level
        , so_called_lib_opengl_GL_RGBA          // internal format
        , size                                  // width
        , size                                  // height
        , 0                                     // border
        , so_called_lib_opengl_GL_BGRA          // format
        , so_called_lib_opengl_GL_UNSIGNED_BYTE // type
        , 0                                     // data
        ) ;
}

void shy_platform_render_opengl :: use_texture ( so_called_type_platform_render_opengl_texture_id arg_texture_id )
{
    so_called_lib_opengl_glBindTexture ( so_called_lib_opengl_GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

void shy_platform_render_opengl :: set_texel_color 
    ( so_called_type_platform_render_opengl_texel_data & texel 
    , so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    , so_called_type_platform_math_num_fract a 
    )
{
    so_called_lib_std_float r_float ;
    so_called_lib_std_float g_float ;
    so_called_lib_std_float b_float ;
    so_called_lib_std_float a_float ;
    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    texel . _color [ 0 ] = ( so_called_lib_opengl_GLubyte ) ( b_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _color [ 1 ] = ( so_called_lib_opengl_GLubyte ) ( g_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _color [ 2 ] = ( so_called_lib_opengl_GLubyte ) ( r_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _color [ 3 ] = ( so_called_lib_opengl_GLubyte ) ( a_float * so_called_lib_std_float ( 255 ) ) ;
}

void shy_platform_render_opengl :: clear_screen 
    ( so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    )
{
    so_called_lib_std_float r_float ;
    so_called_lib_std_float g_float ;
    so_called_lib_std_float b_float ;
    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    so_called_lib_opengl_glClearColor ( r_float , g_float , b_float , 0 ) ;
    so_called_lib_opengl_glClearDepth ( 1 ) ;
    so_called_lib_opengl_glClear ( so_called_lib_opengl_GL_COLOR_BUFFER_BIT | so_called_lib_opengl_GL_DEPTH_BUFFER_BIT ) ;
}

void shy_platform_render_opengl :: projection_frustum 
    ( so_called_type_platform_math_num_fract left 
    , so_called_type_platform_math_num_fract right 
    , so_called_type_platform_math_num_fract bottom 
    , so_called_type_platform_math_num_fract top 
    , so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    )
{
    so_called_lib_std_float left_float ;
    so_called_lib_std_float right_float ;
    so_called_lib_std_float bottom_float ;
    so_called_lib_std_float top_float ;
    so_called_lib_std_float near_float ;
    so_called_lib_std_float far_float ;

    so_called_platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    so_called_platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    so_called_platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    so_called_platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    so_called_lib_opengl_glMatrixMode ( so_called_lib_opengl_GL_PROJECTION ) ;
    so_called_lib_opengl_glLoadIdentity ( ) ;
    so_called_lib_opengl_glFrustum ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    so_called_lib_opengl_glMatrixMode ( so_called_lib_opengl_GL_MODELVIEW ) ;
}

void shy_platform_render_opengl :: projection_ortho 
    ( so_called_type_platform_math_num_fract left 
    , so_called_type_platform_math_num_fract right 
    , so_called_type_platform_math_num_fract bottom 
    , so_called_type_platform_math_num_fract top 
    , so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    )
{
    so_called_lib_std_float left_float ;
    so_called_lib_std_float right_float ;
    so_called_lib_std_float bottom_float ;
    so_called_lib_std_float top_float ;
    so_called_lib_std_float near_float ;
    so_called_lib_std_float far_float ;

    so_called_platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    so_called_platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    so_called_platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    so_called_platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    so_called_lib_opengl_glMatrixMode ( so_called_lib_opengl_GL_PROJECTION ) ;
    so_called_lib_opengl_glLoadIdentity ( ) ;
    so_called_lib_opengl_glOrtho ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    so_called_lib_opengl_glMatrixMode ( so_called_lib_opengl_GL_MODELVIEW ) ;
}

void shy_platform_render_opengl :: create_vertex_buffer 
    ( so_called_type_platform_render_opengl_vertex_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    so_called_lib_opengl_glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;

    so_called_lib_std_int32_t elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;

    so_called_lib_opengl_glBufferData
        ( so_called_lib_opengl_GL_ARRAY_BUFFER 
        , ( so_called_lib_opengl_GLsizeiptr ) ( so_called_lib_std_int32_t ( sizeof ( so_called_type_platform_render_opengl_vertex_data ) ) * elements_int ) 
        , 0
        , so_called_lib_opengl_GL_STATIC_DRAW 
        ) ;
}

void shy_platform_render_opengl :: map_vertex_buffer
    ( so_called_type_platform_render_opengl_vertex_buffer_mapped_data & data 
    , so_called_type_platform_render_opengl_vertex_buffer_id arg_buffer_id 
    )
{
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = so_called_lib_opengl_glMapBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , so_called_lib_opengl_GL_WRITE_ONLY ) ;
}

void shy_platform_render_opengl :: unmap_vertex_buffer ( so_called_type_platform_render_opengl_vertex_buffer_id arg_buffer_id )
{
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    so_called_lib_opengl_glUnmapBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER ) ;
}

void shy_platform_render_opengl :: mapped_vertex_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_opengl_vertex_data > & ptr 
    , so_called_type_platform_render_opengl_vertex_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_type_platform_render_opengl_vertex_data * mapped_vertices = ( so_called_type_platform_render_opengl_vertex_data * ) data . _data ;
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( ptr , mapped_vertices [ index_int ] ) ;
}

void shy_platform_render_opengl :: set_vertex_position 
    ( so_called_type_platform_render_opengl_vertex_data & vertex 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 0 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 1 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 2 ] , z ) ;
}

void shy_platform_render_opengl :: set_vertex_tex_coord 
    ( so_called_type_platform_render_opengl_vertex_data & vertex 
    , so_called_type_platform_math_num_fract u 
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 0 ] , u ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 1 ] , v ) ;
}

void shy_platform_render_opengl :: set_vertex_color 
    ( so_called_type_platform_render_opengl_vertex_data & vertex 
    , so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    , so_called_type_platform_math_num_fract a 
    )
{
    so_called_lib_std_float r_float ;
    so_called_lib_std_float g_float ;
    so_called_lib_std_float b_float ;
    so_called_lib_std_float a_float ;

    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;

    vertex . _color [ 0 ] = ( so_called_lib_opengl_GLubyte ) ( r_float * so_called_lib_std_float ( 255 ) ) ;
    vertex . _color [ 1 ] = ( so_called_lib_opengl_GLubyte ) ( g_float * so_called_lib_std_float ( 255 ) ) ;
    vertex . _color [ 2 ] = ( so_called_lib_opengl_GLubyte ) ( b_float * so_called_lib_std_float ( 255 ) ) ;
    vertex . _color [ 3 ] = ( so_called_lib_opengl_GLubyte ) ( a_float * so_called_lib_std_float ( 255 ) ) ;
}

void shy_platform_render_opengl :: create_index_buffer 
    ( so_called_type_platform_render_opengl_index_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    so_called_lib_opengl_glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;

    so_called_lib_std_int32_t elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;

    so_called_lib_opengl_glBufferData
        ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER 
        , ( so_called_lib_opengl_GLsizeiptr ) ( so_called_lib_std_int32_t ( sizeof ( so_called_type_platform_render_opengl_index_data ) ) * elements_int ) 
        , 0
        , so_called_lib_opengl_GL_STATIC_DRAW 
        ) ;
}

void shy_platform_render_opengl :: map_index_buffer
    ( so_called_type_platform_render_opengl_index_buffer_mapped_data & data 
    , so_called_type_platform_render_opengl_index_buffer_id arg_buffer_id 
    )
{
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = so_called_lib_opengl_glMapBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , so_called_lib_opengl_GL_WRITE_ONLY ) ;
}

void shy_platform_render_opengl :: unmap_index_buffer ( so_called_type_platform_render_opengl_index_buffer_id arg_buffer_id )
{
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    so_called_lib_opengl_glUnmapBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER ) ;
}

void shy_platform_render_opengl :: mapped_index_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_opengl_index_data > & ptr 
    , so_called_type_platform_render_opengl_index_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_type_platform_render_opengl_index_data * mapped_indices = ( so_called_type_platform_render_opengl_index_data * ) data . _data ;
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( ptr , mapped_indices [ index_int ] ) ;
}

void shy_platform_render_opengl :: set_index_value ( so_called_type_platform_render_opengl_index_data & data , so_called_type_platform_math_num_whole index )
{
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    data . _index = ( GLushort ) index_int ;
}

void shy_platform_render_opengl :: matrix_identity ( )
{
    so_called_lib_opengl_glLoadIdentity ( ) ;
}

void shy_platform_render_opengl :: matrix_load ( const so_called_type_platform_matrix_data & matrix )
{
    const so_called_lib_std_float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    so_called_lib_opengl_glLoadMatrixf ( elements ) ;
}

void shy_platform_render_opengl :: matrix_mult ( const so_called_type_platform_matrix_data & matrix )
{
    const so_called_lib_std_float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    so_called_lib_opengl_glMultMatrixf ( elements ) ;
}

void shy_platform_render_opengl :: matrix_push ( )
{
    so_called_lib_opengl_glPushMatrix ( ) ;
}

void shy_platform_render_opengl :: matrix_pop ( )
{
    so_called_lib_opengl_glPopMatrix ( ) ;
}

void shy_platform_render_opengl :: draw_triangle_strip 
    ( so_called_type_platform_render_opengl_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_opengl_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    so_called_lib_std_int32_t indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;

    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_VERTEX_ARRAY ) ;
    so_called_lib_opengl_glVertexPointer ( 3 , so_called_lib_opengl_GL_FLOAT , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_position_offset ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_TEXTURE_COORD_ARRAY ) ;
    so_called_lib_opengl_glTexCoordPointer ( 2 , so_called_lib_opengl_GL_FLOAT , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_tex_coord_offset ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_COLOR_ARRAY ) ;
    so_called_lib_opengl_glColorPointer ( 4 , so_called_lib_opengl_GL_UNSIGNED_BYTE , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_color_offset ) ;
    so_called_lib_opengl_glDrawElements 
        ( so_called_lib_opengl_GL_TRIANGLE_STRIP 
        , ( so_called_lib_opengl_GLsizei ) indices_count_int
        , so_called_lib_opengl_GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

void shy_platform_render_opengl :: draw_triangle_fan
    ( so_called_type_platform_render_opengl_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_opengl_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    so_called_lib_std_int32_t indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;

    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    so_called_lib_opengl_glBindBuffer ( so_called_lib_opengl_GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_VERTEX_ARRAY ) ;
    so_called_lib_opengl_glVertexPointer ( 3 , so_called_lib_opengl_GL_FLOAT , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_position_offset ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_TEXTURE_COORD_ARRAY ) ;
    so_called_lib_opengl_glTexCoordPointer ( 2 , so_called_lib_opengl_GL_FLOAT , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_tex_coord_offset ) ;
    so_called_lib_opengl_glEnableClientState ( so_called_lib_opengl_GL_COLOR_ARRAY ) ;
    so_called_lib_opengl_glColorPointer ( 4 , so_called_lib_opengl_GL_UNSIGNED_BYTE , sizeof ( so_called_type_platform_render_opengl_vertex_data ) , shy_guts :: vertex_color_offset ) ;
    so_called_lib_opengl_glDrawElements 
        ( so_called_lib_opengl_GL_TRIANGLE_FAN 
        , ( so_called_lib_opengl_GLsizei ) indices_count_int
        , so_called_lib_opengl_GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

void shy_platform_render_opengl :: get_aspect_width ( so_called_type_platform_math_num_fract & result )
{
    so_called_lib_std_float float_aspect_width = 0 ;
    so_called_platform_render_opengl_insider :: get_aspect_width ( float_aspect_width ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , float_aspect_width ) ;
}

void shy_platform_render_opengl :: get_aspect_height ( so_called_type_platform_math_num_fract & result )
{
    so_called_lib_std_float float_aspect_height = 0 ;
    so_called_platform_render_opengl_insider :: get_aspect_height ( float_aspect_height ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , float_aspect_height ) ;
}

void shy_platform_render_opengl :: get_frame_loss ( so_called_type_platform_math_num_whole & result )
{
    so_called_lib_std_bool bool_frame_loss = so_called_lib_std_false ;
    so_called_platform_render_opengl_insider :: get_frame_loss ( bool_frame_loss ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , bool_frame_loss ) ;
}

void shy_platform_render_opengl :: delete_vertex_buffer ( so_called_type_platform_render_opengl_vertex_buffer_id & arg_buffer_id )
{
}

void shy_platform_render_opengl :: delete_index_buffer ( so_called_type_platform_render_opengl_index_buffer_id & arg_buffer_id )
{
}

void shy_platform_render_opengl :: delete_texture_id ( so_called_type_platform_render_opengl_texture_id & arg_texture_id )
{
}

