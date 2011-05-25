so_called_lib_std_float shy_macosx_platform_render :: _aspect_width = 1 ;
so_called_lib_std_float shy_macosx_platform_render :: _aspect_height = 1 ;
so_called_lib_std_bool shy_macosx_platform_render :: _frame_loss = so_called_lib_std_false ;

so_called_type_platform_render_vertex_data shy_macosx_platform_render :: _reference_vertex ;
void * shy_macosx_platform_render :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex )
    ) ;
void * shy_macosx_platform_render :: _vertex_tex_coord_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex )
    ) ;
void * shy_macosx_platform_render :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_render :: _reference_vertex )
    ) ;

void shy_macosx_platform_render :: _load_texture_subdata 
    ( so_called_type_platform_render_texture_id arg_texture_id 
    , so_called_type_platform_math_num_whole x_offset 
    , so_called_type_platform_math_num_whole y_offset 
    , so_called_type_platform_math_num_whole width
    , so_called_type_platform_math_num_whole height
    , const so_called_type_platform_render_texel_data * texels
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

void shy_macosx_platform_render :: enable_face_culling ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_CULL_FACE ) ;
}

void shy_macosx_platform_render :: enable_depth_test ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_DEPTH_TEST ) ;
}

void shy_macosx_platform_render :: disable_depth_test ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_DEPTH_TEST ) ;
}

void shy_macosx_platform_render :: blend_disable ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_BLEND ) ;
}

void shy_macosx_platform_render :: blend_src_alpha_dst_one_minus_alpha ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_BLEND ) ;
    so_called_lib_opengl_glBlendFunc ( so_called_lib_opengl_GL_SRC_ALPHA , so_called_lib_opengl_GL_ONE_MINUS_SRC_ALPHA ) ;
}

void shy_macosx_platform_render :: enable_texturing ( )
{
    so_called_lib_opengl_glEnable ( so_called_lib_opengl_GL_TEXTURE_2D ) ;
}

void shy_macosx_platform_render :: disable_texturing ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_TEXTURE_2D ) ;
}

void shy_macosx_platform_render :: texture_mode_modulate ( )
{
    so_called_lib_opengl_glTexEnvf ( so_called_lib_opengl_GL_TEXTURE_ENV , so_called_lib_opengl_GL_TEXTURE_ENV_MODE , so_called_lib_opengl_GL_MODULATE ) ;
}

void shy_macosx_platform_render :: fog_disable ( )
{
    so_called_lib_opengl_glDisable ( so_called_lib_opengl_GL_FOG ) ;
}

void shy_macosx_platform_render :: fog_linear 
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

void shy_macosx_platform_render :: create_texture_id 
    ( so_called_type_platform_render_texture_id & arg_texture_id 
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

void shy_macosx_platform_render :: use_texture ( so_called_type_platform_render_texture_id arg_texture_id )
{
    so_called_lib_opengl_glBindTexture ( so_called_lib_opengl_GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

void shy_macosx_platform_render :: set_texel_color 
    ( so_called_type_platform_render_texel_data & texel 
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

void shy_macosx_platform_render :: clear_screen 
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

void shy_macosx_platform_render :: projection_frustum 
    ( so_called_type_platform_math_num_fract left 
    , so_called_type_platform_math_num_fract right 
    , so_called_type_platform_math_num_fract bottom 
    , so_called_type_platform_math_num_fract top 
    , so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    )
{
    float left_float ;
    float right_float ;
    float bottom_float ;
    float top_float ;
    float near_float ;
    float far_float ;
    so_called_platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    so_called_platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    so_called_platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    so_called_platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glFrustum ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

void shy_macosx_platform_render :: projection_ortho 
    ( so_called_type_platform_math_num_fract left 
    , so_called_type_platform_math_num_fract right 
    , so_called_type_platform_math_num_fract bottom 
    , so_called_type_platform_math_num_fract top 
    , so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    )
{
    float left_float ;
    float right_float ;
    float bottom_float ;
    float top_float ;
    float near_float ;
    float far_float ;
    so_called_platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    so_called_platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    so_called_platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    so_called_platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    so_called_platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glOrtho ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

void shy_macosx_platform_render :: create_vertex_buffer 
    ( so_called_type_platform_render_vertex_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    int elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
    glBufferData
        ( GL_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( so_called_type_platform_render_vertex_data ) * ( unsigned int ) elements_int ) 
        , 0
        , GL_STATIC_DRAW 
        ) ;
}

void shy_macosx_platform_render :: map_vertex_buffer
    ( so_called_type_platform_render_vertex_buffer_mapped_data & data 
    , so_called_type_platform_render_vertex_buffer_id arg_buffer_id 
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = glMapBuffer ( GL_ARRAY_BUFFER , GL_READ_WRITE ) ;
}

void shy_macosx_platform_render :: unmap_vertex_buffer ( so_called_type_platform_render_vertex_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glUnmapBuffer ( GL_ARRAY_BUFFER ) ;
}

void shy_macosx_platform_render :: mapped_vertex_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_vertex_data > & ptr 
    , so_called_type_platform_render_vertex_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_type_platform_render_vertex_data * mapped_vertices = ( so_called_type_platform_render_vertex_data * ) data . _data ;
    int index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( ptr , mapped_vertices [ index_int ] ) ;
}

void shy_macosx_platform_render :: set_vertex_position 
    ( so_called_type_platform_render_vertex_data & vertex 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 0 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 1 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 2 ] , z ) ;
}

void shy_macosx_platform_render :: set_vertex_tex_coord 
    ( so_called_type_platform_render_vertex_data & vertex 
    , so_called_type_platform_math_num_fract u 
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 0 ] , u ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 1 ] , v ) ;
}

void shy_macosx_platform_render :: set_vertex_color 
    ( so_called_type_platform_render_vertex_data & vertex 
    , so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    , so_called_type_platform_math_num_fract a 
    )
{
    float r_float ;
    float g_float ;
    float b_float ;
    float a_float ;
    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    so_called_platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    vertex . _color [ 0 ] = ( GLubyte ) ( r_float * 255.0f ) ;
    vertex . _color [ 1 ] = ( GLubyte ) ( g_float * 255.0f ) ;
    vertex . _color [ 2 ] = ( GLubyte ) ( b_float * 255.0f ) ;
    vertex . _color [ 3 ] = ( GLubyte ) ( a_float * 255.0f ) ;
}

void shy_macosx_platform_render :: create_index_buffer 
    ( so_called_type_platform_render_index_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    int elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
    glBufferData
        ( GL_ELEMENT_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( so_called_type_platform_render_index_data ) * ( unsigned int ) elements_int ) 
        , 0
        , GL_STATIC_DRAW 
        ) ;
}

void shy_macosx_platform_render :: map_index_buffer
    ( so_called_type_platform_render_index_buffer_mapped_data & data 
    , so_called_type_platform_render_index_buffer_id arg_buffer_id 
    )
{
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = glMapBuffer ( GL_ELEMENT_ARRAY_BUFFER , GL_READ_WRITE ) ;
}

void shy_macosx_platform_render :: unmap_index_buffer ( so_called_type_platform_render_index_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glUnmapBuffer ( GL_ELEMENT_ARRAY_BUFFER ) ;
}

void shy_macosx_platform_render :: mapped_index_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_index_data > & ptr 
    , so_called_type_platform_render_index_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_type_platform_render_index_data * mapped_indices = ( so_called_type_platform_render_index_data * ) data . _data ;
    int index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( ptr , mapped_indices [ index_int ] ) ;
}

void shy_macosx_platform_render :: set_index_value ( so_called_type_platform_render_index_data & data , so_called_type_platform_math_num_whole index )
{
    int index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    data . _index = ( GLushort ) index_int ;
}

void shy_macosx_platform_render :: matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

void shy_macosx_platform_render :: matrix_load ( const so_called_type_platform_matrix_data & matrix )
{
    const float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    glLoadMatrixf ( elements ) ;
}

void shy_macosx_platform_render :: matrix_mult ( const so_called_type_platform_matrix_data & matrix )
{
    const float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    glMultMatrixf ( elements ) ;
}

void shy_macosx_platform_render :: matrix_push ( )
{
    glPushMatrix ( ) ;
}

void shy_macosx_platform_render :: matrix_pop ( )
{
    glPopMatrix ( ) ;
}

void shy_macosx_platform_render :: draw_triangle_strip 
    ( so_called_type_platform_render_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    int indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_STRIP 
        , ( GLsizei ) indices_count_int
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

void shy_macosx_platform_render :: draw_triangle_fan
    ( so_called_type_platform_render_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    int indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( so_called_type_platform_render_vertex_data ) , _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_FAN 
        , ( GLsizei ) indices_count_int
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

void shy_macosx_platform_render :: get_aspect_width ( so_called_type_platform_math_num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _aspect_width ) ;
}

void shy_macosx_platform_render :: get_aspect_height ( so_called_type_platform_math_num_fract & result )
{
    so_called_platform_math_insider :: num_fract_value_set ( result , _aspect_height ) ;
}

void shy_macosx_platform_render :: get_frame_loss ( so_called_type_platform_math_num_whole & result )
{
    so_called_platform_math_insider :: num_whole_value_set ( result , _frame_loss ) ;
}

void shy_macosx_platform_render :: delete_vertex_buffer ( so_called_type_platform_render_vertex_buffer_id & arg_buffer_id )
{
}

void shy_macosx_platform_render :: delete_index_buffer ( so_called_type_platform_render_index_buffer_id & arg_buffer_id )
{
}

void shy_macosx_platform_render :: delete_texture_id ( so_called_type_platform_render_texture_id & arg_texture_id )
{
}
