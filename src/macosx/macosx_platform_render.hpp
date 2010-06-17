template < typename platform >
class shy_macosx_platform_render
{
    typedef typename platform :: _platform_insider _platform_insider ;
    typedef typename platform :: _platform_math_insider _platform_math_insider ;
    typedef typename platform :: _platform_matrix_insider _platform_matrix_insider ;
    typedef typename platform :: _platform_static_array_insider _platform_static_array_insider ;
    typedef typename platform :: num_fract num_fract ;
    typedef typename platform :: num_whole num_whole ;
    typedef typename platform :: matrix_data matrix_data ;
    
public :
    class render_index_buffer_id
    {
        friend class shy_macosx_platform_render ;
    public :
        render_index_buffer_id ( ) ;
    private :
        GLuint _buffer_id ;
    } ;
    
    class render_vertex_buffer_id
    {
        friend class shy_macosx_platform_render ;
    public :
        render_vertex_buffer_id ( ) ;
    private :
        GLuint _buffer_id ;
    } ;
    
	class render_texture_id
	{
		friend class shy_macosx_platform_render ;
    public :
        render_texture_id ( ) ;
	private :
		GLuint _texture_id ;
	} ;

    class texture_resource_id
    {
        friend class shy_macosx_platform_render ;
    public :
        texture_resource_id ( ) ;
    private :
        int _resource_id ;
    } ;
	
    class texel_data
    {
        friend class shy_macosx_platform_render ;
    public :
        texel_data ( ) ;
    private :
        GLubyte _color [ 4 ] ;
    } ;
    
    class vertex_data
    {
        friend class shy_macosx_platform_render ;
        friend class shy_macosx_platform_utility ;
    public :
        vertex_data ( ) ;
    private :
        GLfloat _position [ 3 ] ;
        GLfloat _tex_coord [ 2 ] ;
        GLubyte _color [ 4 ] ;
    } ;
    
    class index_data
    {
        friend class shy_macosx_platform_render ;
    public :
        index_data ( ) ;
    private :
        GLushort _index ;
    } ;

public :

    static void render_enable_face_culling ( ) ;
    
    static void render_enable_depth_test ( ) ;
    static void render_disable_depth_test ( ) ;
    
    static void render_fog_disable ( ) ;
    static void render_fog_linear ( num_fract near , num_fract far , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    
    static void render_blend_disable ( ) ;
    static void render_blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	static void render_enable_texturing ( ) ;
	static void render_disable_texturing ( ) ;
	static void render_set_modulate_texture_mode ( ) ;
    static void render_use_texture ( const render_texture_id & arg_texture_id ) ;
	static void render_create_texture_id ( render_texture_id & arg_texture_id ) ;
    static void render_set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void render_create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    static void render_texture_loader_ready ( num_whole & is_ready ) ;

    static void render_clear_screen ( num_fract r , num_fract g , num_fract b ) ;    
    static void render_projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    static void render_projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    
    static void render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z ) ;
    static void render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v ) ;
    static void render_set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void render_set_index_value ( index_data & data , num_whole index ) ;
    
    static void render_matrix_identity ( ) ;
    static void render_matrix_load ( const matrix_data & matrix ) ;
    static void render_matrix_mult ( const matrix_data & matrix ) ;
    static void render_matrix_push ( ) ;
    static void render_matrix_pop ( ) ;
    
	static void render_get_aspect_width ( num_fract & result ) ;
	static void render_get_aspect_height ( num_fract & result ) ;
    
    static void render_delete_vertex_buffer ( const render_vertex_buffer_id & arg_buffer_id ) ;
    static void render_delete_index_buffer ( const render_index_buffer_id & arg_buffer_id ) ;
    
    template < typename texels_array >
    static void render_load_texture_data ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename texels_array >
    static void render_load_texture_resource ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename vertices_array >
    static void render_create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data ) ;
    
    template < typename indices_array >
    static void render_create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data ) ;
    
    static void render_draw_triangle_strip 
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
    static void render_draw_triangle_fan
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;        
private :
    static int _uninitialized_value ( ) ;
} ;

template < typename platform >
int shy_macosx_platform_render < platform > :: _uninitialized_value ( )
{
    return platform :: _uninitialized_value ;
}

template < typename platform >
shy_macosx_platform_render < platform > :: render_index_buffer_id :: render_index_buffer_id ( )
: _buffer_id ( shy_macosx_platform_render < platform > :: _uninitialized_value ( ) )
{
}
    
template < typename platform >
shy_macosx_platform_render < platform > :: render_vertex_buffer_id :: render_vertex_buffer_id ( )
: _buffer_id ( shy_macosx_platform_render < platform > :: _uninitialized_value ( ) )
{
}
    
template < typename platform >
shy_macosx_platform_render < platform > :: render_texture_id :: render_texture_id ( )
: _texture_id ( shy_macosx_platform_render < platform > :: _uninitialized_value ( ) )
{
}

template < typename platform >
shy_macosx_platform_render < platform > :: texture_resource_id :: texture_resource_id ( )
: _resource_id ( shy_macosx_platform_render < platform > :: _uninitialized_value ( ) )
{
}
	
template < typename platform >
shy_macosx_platform_render < platform > :: texel_data :: texel_data ( )
{
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) shy_macosx_platform_render < platform > :: _uninitialized_value ( ) ;
}
    
template < typename platform >
shy_macosx_platform_render < platform > :: vertex_data :: vertex_data ( )
{
    for ( int i = 0 ; i < 3 ; i ++ )
        _position [ i ] = shy_macosx_platform_render < platform > :: _uninitialized_value ( ) ;
    for ( int i = 0 ; i < 2 ; i ++ )
        _tex_coord [ i ] = shy_macosx_platform_render < platform > :: _uninitialized_value ( ) ;
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) shy_macosx_platform_render < platform > :: _uninitialized_value ( ) ;
}
    
template < typename platform >
shy_macosx_platform_render < platform > :: index_data :: index_data ( )
: _index ( ( GLushort ) shy_macosx_platform_render < platform > :: _uninitialized_value ( ) )
{
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_enable_face_culling ( )
{
    glEnable ( GL_CULL_FACE ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_enable_depth_test ( )
{
    glEnable ( GL_DEPTH_TEST ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_disable_depth_test ( )
{
    glDisable ( GL_DEPTH_TEST ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_blend_disable ( )
{
    glDisable ( GL_BLEND ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_blend_src_alpha_dst_one_minus_alpha ( )
{
    glEnable ( GL_BLEND ) ;
    glBlendFunc ( GL_SRC_ALPHA , GL_ONE_MINUS_SRC_ALPHA ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_enable_texturing ( )
{
	glEnable ( GL_TEXTURE_2D ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_disable_texturing ( )
{
	glDisable ( GL_TEXTURE_2D ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_modulate_texture_mode ( )
{
    glTexEnvf ( GL_TEXTURE_ENV , GL_TEXTURE_ENV_MODE , GL_MODULATE ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_fog_disable ( )
{
    glDisable ( GL_FOG ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_fog_linear 
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_create_texture_id ( render_texture_id & arg_texture_id )
{
    glGenTextures ( 1 , & arg_texture_id . _texture_id ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_use_texture ( const render_texture_id & arg_texture_id )
{
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    texel . _color [ 0 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f ) ;
    texel . _color [ 1 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f ) ;
    texel . _color [ 2 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) ;
    texel . _color [ 3 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( a ) * 255.0f ) ;
}

template < typename platform >
template < typename texels_array >
inline void shy_macosx_platform_render < platform > :: render_load_texture_data 
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    resource_id . _resource_id = _platform_math_insider :: num_whole_unsafe_value_get ( resource_index ) ;
}

template < typename platform >
template < typename texels_array >
inline void shy_macosx_platform_render < platform > :: render_load_texture_resource
    ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data )
{
    [ _platform_insider :: _texture_loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) _platform_static_array_insider :: array_elements_unsafe_ptr ( data )
        with_side_size_of : 1 << _platform_math_insider :: num_whole_unsafe_value_get ( size_pow2_base )
    ] ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_texture_loader_ready ( num_whole & is_ready )
{
    _platform_math_insider :: num_whole_unsafe_value_set ( is_ready , [ _platform_insider :: _texture_loader loader_ready ] ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_clear_screen ( num_fract r , num_fract g , num_fract b )
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_projection_frustum 
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_projection_ortho 
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

template < typename platform >
template < typename vertices_array >
inline void shy_macosx_platform_render < platform > :: render_create_vertex_buffer 
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
    vertex . _position [ 0 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
    vertex . _position [ 1 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
    vertex . _position [ 2 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
    vertex . _tex_coord [ 0 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( u ) ;
    vertex . _tex_coord [ 1 ] = ( GLfloat ) _platform_math_insider :: num_fract_unsafe_value_get ( v ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
    vertex . _color [ 0 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) ;
    vertex . _color [ 1 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f ) ;
    vertex . _color [ 2 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f ) ;
    vertex . _color [ 3 ] = ( GLubyte ) ( _platform_math_insider :: num_fract_unsafe_value_get ( a ) * 255.0f ) ;
}

template < typename platform >
template < typename indices_array >
inline void shy_macosx_platform_render < platform > :: render_create_index_buffer 
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

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_set_index_value ( index_data & data , num_whole index )
{
    data . _index = ( GLushort ) _platform_math_insider :: num_whole_unsafe_value_get ( index ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_matrix_load ( const matrix_data & matrix )
{
    glLoadMatrixf ( _platform_matrix_insider :: matrix_elements_unsafe_ptr ( matrix ) ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_matrix_mult ( const matrix_data & matrix )
{
    glMultMatrixf ( _platform_matrix_insider :: matrix_elements_unsafe_ptr ( matrix ) ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_matrix_push ( )
{
    glPushMatrix ( ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_matrix_pop ( )
{
    glPopMatrix ( ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_draw_triangle_strip 
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , _platform_insider :: _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , _platform_insider :: _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , _platform_insider :: _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_STRIP 
        , ( GLsizei ) _platform_math_insider :: num_whole_unsafe_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_draw_triangle_fan
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
    glBindBuffer ( GL_ARRAY_BUFFER , vertices_buffer . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , indices_buffer . _buffer_id ) ;
    glEnableClientState ( GL_VERTEX_ARRAY ) ;
    glVertexPointer ( 3 , GL_FLOAT , sizeof ( vertex_data ) , _platform_insider :: _vertex_position_offset ) ;
    glEnableClientState ( GL_TEXTURE_COORD_ARRAY ) ;
    glTexCoordPointer ( 2 , GL_FLOAT , sizeof ( vertex_data ) , _platform_insider :: _vertex_tex_coord_offset ) ;
    glEnableClientState ( GL_COLOR_ARRAY ) ;
    glColorPointer ( 4 , GL_UNSIGNED_BYTE , sizeof ( vertex_data ) , _platform_insider :: _vertex_color_offset ) ;
    glDrawElements 
        ( GL_TRIANGLE_FAN 
        , ( GLsizei ) _platform_math_insider :: num_whole_unsafe_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_get_aspect_width ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , _platform_insider :: _aspect_width ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_get_aspect_height ( num_fract & result )
{
    _platform_math_insider :: num_fract_unsafe_value_set ( result , _platform_insider :: _aspect_height ) ;
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_delete_vertex_buffer ( const render_vertex_buffer_id & arg_buffer_id )
{
}

template < typename platform >
inline void shy_macosx_platform_render < platform > :: render_delete_index_buffer ( const render_index_buffer_id & arg_buffer_id )
{
}
