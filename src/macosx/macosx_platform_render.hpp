template < typename platform_insider >
class shy_macosx_platform_render_insider ;

template < typename platform_insider >
class shy_macosx_platform_render
{
    friend class shy_macosx_platform_render_insider < platform_insider > ;

    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    typedef typename platform_insider :: platform_matrix_insider platform_matrix_insider ;
    typedef typename platform_insider :: platform_static_array_insider platform_static_array_insider ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_matrix :: matrix_data matrix_data ;
    
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
        friend class shy_macosx_platform_insider ;
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
    shy_macosx_platform_render ( ) ;

    static void set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z ) ;
    static void set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v ) ;
    static void set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void set_index_value ( index_data & data , num_whole index ) ;
    static void create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;

    void enable_face_culling ( ) ;
    
    void enable_depth_test ( ) ;
    void disable_depth_test ( ) ;
    
    void fog_disable ( ) ;
    void fog_linear ( num_fract near , num_fract far , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    
    void blend_disable ( ) ;
    void blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	void enable_texturing ( ) ;
	void disable_texturing ( ) ;
	void texture_mode_modulate ( ) ;
    void use_texture ( const render_texture_id & arg_texture_id ) ;
	void create_texture_id ( render_texture_id & arg_texture_id ) ;
    void texture_loader_ready ( num_whole & is_ready ) ;

    void clear_screen ( num_fract r , num_fract g , num_fract b ) ;    
    void projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
    void projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract near , num_fract far ) ;
        
    void matrix_identity ( ) ;
    void matrix_load ( const matrix_data & matrix ) ;
    void matrix_mult ( const matrix_data & matrix ) ;
    void matrix_push ( ) ;
    void matrix_pop ( ) ;
    
	void get_aspect_width ( num_fract & result ) ;
	void get_aspect_height ( num_fract & result ) ;
    
    void delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id ) ;
    void delete_index_buffer ( render_index_buffer_id & arg_buffer_id ) ;
    
    template < typename texels_array >
    void load_texture_data ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename texels_array >
    void load_texture_resource ( const texture_resource_id & resource_id , num_whole size_pow2_base , texels_array & data ) ;
    
    template < typename vertices_array >
    void create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data ) ;
    
    template < typename indices_array >
    void create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data ) ;
    
    void draw_triangle_strip 
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
    void draw_triangle_fan
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
        
private :
    shy_macosx_texture_loader * _texture_loader ;
	float _aspect_width ;
	float _aspect_height ;
    vertex_data _reference_vertex ;
    void * _vertex_position_offset ;
    void * _vertex_tex_coord_offset ;
    void * _vertex_color_offset ;    
} ;

template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: shy_macosx_platform_render ( )
: _texture_loader ( 0 )
, _aspect_width ( 1 )
, _aspect_height ( 1 )
, _vertex_position_offset ( 0 )
, _vertex_tex_coord_offset ( 0 )
, _vertex_color_offset ( 0 )
{
    _vertex_position_offset = reinterpret_cast < void * >
        ( reinterpret_cast < char * > ( & _reference_vertex . _position ) 
        - reinterpret_cast < char * > ( & _reference_vertex )
        ) ;
    _vertex_tex_coord_offset = reinterpret_cast < void * >
        ( reinterpret_cast < char * > ( & _reference_vertex . _tex_coord ) 
        - reinterpret_cast < char * > ( & _reference_vertex )
        ) ;
    _vertex_color_offset = reinterpret_cast < void * >
        ( reinterpret_cast < char * > ( & _reference_vertex . _color ) 
        - reinterpret_cast < char * > ( & _reference_vertex )
        ) ;
}

template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: render_index_buffer_id :: render_index_buffer_id ( )
: _buffer_id ( GLuint ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: render_vertex_buffer_id :: render_vertex_buffer_id ( )
: _buffer_id ( GLuint ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: render_texture_id :: render_texture_id ( )
: _texture_id ( GLuint ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: texture_resource_id :: texture_resource_id ( )
: _resource_id ( platform_insider :: uninitialized_value )
{
}
	
template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: texel_data :: texel_data ( )
{
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) platform_insider :: uninitialized_value ;
}
    
template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: vertex_data :: vertex_data ( )
{
    for ( int i = 0 ; i < 3 ; i ++ )
        _position [ i ] = platform_insider :: uninitialized_value ;
    for ( int i = 0 ; i < 2 ; i ++ )
        _tex_coord [ i ] = platform_insider :: uninitialized_value ;
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) platform_insider :: uninitialized_value ;
}
    
template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: index_data :: index_data ( )
: _index ( ( GLushort ) platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: enable_face_culling ( )
{
    glEnable ( GL_CULL_FACE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: enable_depth_test ( )
{
    glEnable ( GL_DEPTH_TEST ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: disable_depth_test ( )
{
    glDisable ( GL_DEPTH_TEST ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: blend_disable ( )
{
    glDisable ( GL_BLEND ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: blend_src_alpha_dst_one_minus_alpha ( )
{
    glEnable ( GL_BLEND ) ;
    glBlendFunc ( GL_SRC_ALPHA , GL_ONE_MINUS_SRC_ALPHA ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: enable_texturing ( )
{
	glEnable ( GL_TEXTURE_2D ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: disable_texturing ( )
{
	glDisable ( GL_TEXTURE_2D ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: texture_mode_modulate ( )
{
    glTexEnvf ( GL_TEXTURE_ENV , GL_TEXTURE_ENV_MODE , GL_MODULATE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: fog_disable ( )
{
    glDisable ( GL_FOG ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: fog_linear 
    ( num_fract near 
    , num_fract far 
    , num_fract r 
    , num_fract g 
    , num_fract b 
    , num_fract a 
    )
{
    GLfloat color [ ] = 
        { platform_math_insider :: num_fract_value_get ( r )
        , platform_math_insider :: num_fract_value_get ( g )
        , platform_math_insider :: num_fract_value_get ( b )
        , platform_math_insider :: num_fract_value_get ( a )
        } ;
    glEnable ( GL_FOG ) ;
    glFogf ( GL_FOG_MODE , GL_LINEAR ) ;
    glFogf ( GL_FOG_START , ( GLfloat ) platform_math_insider :: num_fract_value_get ( near ) ) ;
    glFogf ( GL_FOG_END , ( GLfloat ) platform_math_insider :: num_fract_value_get ( far ) ) ;
    glFogfv ( GL_FOG_COLOR , color ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_texture_id ( render_texture_id & arg_texture_id )
{
    glGenTextures ( 1 , & arg_texture_id . _texture_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: use_texture ( const render_texture_id & arg_texture_id )
{
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_texel_color 
    ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    texel . _color [ 0 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( b ) * 255.0f ) ;
    texel . _color [ 1 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( g ) * 255.0f ) ;
    texel . _color [ 2 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( r ) * 255.0f ) ;
    texel . _color [ 3 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( a ) * 255.0f ) ;
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_macosx_platform_render < platform_insider > :: load_texture_data 
    ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data )
{
    GLsizei size = 1 << platform_math_insider :: num_whole_value_get ( size_pow2_base ) ;
    glPixelStorei ( GL_UNPACK_ALIGNMENT , 1 ) ;
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_S , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_T , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MAG_FILTER , GL_LINEAR ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MIN_FILTER , GL_LINEAR ) ;
    const texel_data * texels = 0 ;
    platform_static_array_insider :: elements_ptr ( texels , data ) ;
    glTexImage2D ( GL_TEXTURE_2D , 0 , GL_RGBA , size , size , 0 , GL_BGRA , GL_UNSIGNED_BYTE , texels ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    resource_id . _resource_id = platform_math_insider :: num_whole_value_get ( resource_index ) ;
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_macosx_platform_render < platform_insider > :: load_texture_resource
    ( const texture_resource_id & resource_id , num_whole size_pow2_base , texels_array & data )
{
    texel_data * texels = 0 ;
    platform_static_array_insider :: elements_ptr ( texels , data ) ;
    [ _texture_loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) texels
        with_side_size_of : 1 << platform_math_insider :: num_whole_value_get ( size_pow2_base )
    ] ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: texture_loader_ready ( num_whole & is_ready )
{
    platform_math_insider :: num_whole_value_set ( is_ready , [ _texture_loader loader_ready ] ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: clear_screen ( num_fract r , num_fract g , num_fract b )
{
    glClearColor 
        ( ( GLfloat ) platform_math_insider :: num_fract_value_get ( r )
        , ( GLfloat ) platform_math_insider :: num_fract_value_get ( g )
        , ( GLfloat ) platform_math_insider :: num_fract_value_get ( b )
        , ( GLfloat ) 0
        ) ;
    glClearDepth ( 1 ) ;
    glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: projection_frustum 
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
        ( platform_math_insider :: num_fract_value_get ( left )
        , platform_math_insider :: num_fract_value_get ( right )
        , platform_math_insider :: num_fract_value_get ( bottom )
        , platform_math_insider :: num_fract_value_get ( top )
        , platform_math_insider :: num_fract_value_get ( near )
        , platform_math_insider :: num_fract_value_get ( far )
        ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: projection_ortho 
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
        ( platform_math_insider :: num_fract_value_get ( left )
        , platform_math_insider :: num_fract_value_get ( right )
        , platform_math_insider :: num_fract_value_get ( bottom )
        , platform_math_insider :: num_fract_value_get ( top )
        , platform_math_insider :: num_fract_value_get ( near )
        , platform_math_insider :: num_fract_value_get ( far )
        ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

template < typename platform_insider >
template < typename vertices_array >
inline void shy_macosx_platform_render < platform_insider > :: create_vertex_buffer 
    ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    const vertex_data * vertices = 0 ;
    platform_static_array_insider :: elements_ptr ( vertices , data ) ;
    glBufferData
        ( GL_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( vertex_data ) * ( unsigned int ) platform_math_insider :: num_whole_value_get ( elements ) ) 
        , vertices
        , GL_STATIC_DRAW 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
    vertex . _position [ 0 ] = ( GLfloat ) platform_math_insider :: num_fract_value_get ( x ) ;
    vertex . _position [ 1 ] = ( GLfloat ) platform_math_insider :: num_fract_value_get ( y ) ;
    vertex . _position [ 2 ] = ( GLfloat ) platform_math_insider :: num_fract_value_get ( z ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
    vertex . _tex_coord [ 0 ] = ( GLfloat ) platform_math_insider :: num_fract_value_get ( u ) ;
    vertex . _tex_coord [ 1 ] = ( GLfloat ) platform_math_insider :: num_fract_value_get ( v ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_color 
    ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
    vertex . _color [ 0 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( r ) * 255.0f ) ;
    vertex . _color [ 1 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( g ) * 255.0f ) ;
    vertex . _color [ 2 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( b ) * 255.0f ) ;
    vertex . _color [ 3 ] = ( GLubyte ) ( platform_math_insider :: num_fract_value_get ( a ) * 255.0f ) ;
}

template < typename platform_insider >
template < typename indices_array >
inline void shy_macosx_platform_render < platform_insider > :: create_index_buffer 
    ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    const index_data * indices = 0 ;
    platform_static_array_insider :: elements_ptr ( indices , data ) ;
    glBufferData
        ( GL_ELEMENT_ARRAY_BUFFER
        , ( GLsizeiptr ) ( sizeof ( index_data ) * ( unsigned int ) platform_math_insider :: num_whole_value_get ( elements ) )
        , indices
        , GL_STATIC_DRAW
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_index_value ( index_data & data , num_whole index )
{
    data . _index = ( GLushort ) platform_math_insider :: num_whole_value_get ( index ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_load ( const matrix_data & matrix )
{
    glLoadMatrixf ( platform_matrix_insider :: elements_ptr ( matrix ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_mult ( const matrix_data & matrix )
{
    glMultMatrixf ( platform_matrix_insider :: elements_ptr ( matrix ) ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_push ( )
{
    glPushMatrix ( ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_pop ( )
{
    glPopMatrix ( ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: draw_triangle_strip 
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
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
    glDrawElements 
        ( GL_TRIANGLE_STRIP 
        , ( GLsizei ) platform_math_insider :: num_whole_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: draw_triangle_fan
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
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
    glDrawElements 
        ( GL_TRIANGLE_FAN 
        , ( GLsizei ) platform_math_insider :: num_whole_value_get ( indices_count )
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: get_aspect_width ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _aspect_width ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: get_aspect_height ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _aspect_height ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: delete_index_buffer ( render_index_buffer_id & arg_buffer_id )
{
}
