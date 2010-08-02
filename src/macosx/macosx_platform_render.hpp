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
    typedef typename platform_insider :: platform_pointer platform_pointer ;
    
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
	
    class render_index_buffer_mapped_data
    {
        friend class shy_macosx_platform_render ;
    public :
        render_index_buffer_mapped_data ( ) ;
    private :
        void * _data ;
    } ;
    
    class render_vertex_buffer_mapped_data
    {
        friend class shy_macosx_platform_render ;
    public :
        render_vertex_buffer_mapped_data ( ) ;
    private :
        void * _data ;
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
    static void mapped_vertex_buffer_element 
        ( typename platform_pointer :: template pointer < vertex_data > & ptr 
        , render_vertex_buffer_mapped_data data 
        , num_whole index 
        ) ;
    static void mapped_index_buffer_element 
        ( typename platform_pointer :: template pointer < index_data > & ptr 
        , render_index_buffer_mapped_data data 
        , num_whole index 
        ) ;

    void enable_face_culling ( ) ;
    
    void enable_depth_test ( ) ;
    void disable_depth_test ( ) ;
    
    void fog_disable ( ) ;
    void fog_linear ( num_fract znear , num_fract zfar , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    
    void blend_disable ( ) ;
    void blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	void enable_texturing ( ) ;
	void disable_texturing ( ) ;
	void texture_mode_modulate ( ) ;
    void use_texture ( render_texture_id arg_texture_id ) ;
	void create_texture_id ( render_texture_id & arg_texture_id , num_whole size_pow2_base ) ;
    void texture_loader_ready ( num_whole & is_ready ) ;

    void clear_screen ( num_fract r , num_fract g , num_fract b ) ;    
    void projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract znear , num_fract zfar ) ;
    void projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract znear , num_fract zfar ) ;
        
    void matrix_identity ( ) ;
    void matrix_load ( const matrix_data & matrix ) ;
    void matrix_mult ( const matrix_data & matrix ) ;
    void matrix_push ( ) ;
    void matrix_pop ( ) ;
    
	void get_aspect_width ( num_fract & result ) ;
	void get_aspect_height ( num_fract & result ) ;
    void get_frame_loss ( num_whole & result ) ;
    
    void delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id ) ;
    void delete_index_buffer ( render_index_buffer_id & arg_buffer_id ) ;
    
    template < typename texels_array >
    void load_texture_subdata 
        ( render_texture_id arg_texture_id 
        , num_whole x_offset 
        , num_whole y_offset 
        , num_whole width
        , num_whole height
        , const texels_array & data 
        ) ;
    
    template < typename texels_array >
    void load_texture_resource ( texture_resource_id resource_id , num_whole size_pow2_base , texels_array & data ) ;
    
    void create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements ) ;
    void map_vertex_buffer ( render_vertex_buffer_mapped_data & data , render_vertex_buffer_id arg_buffer_id ) ;
    void unmap_vertex_buffer ( render_vertex_buffer_id arg_buffer_id ) ;
    
    void create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements ) ;
    void map_index_buffer ( render_index_buffer_mapped_data & data , render_index_buffer_id arg_buffer_id ) ;
    void unmap_index_buffer ( render_index_buffer_id arg_buffer_id ) ;
    
    void draw_triangle_strip ( render_vertex_buffer_id vertices_buffer , render_index_buffer_id indices_buffer , num_whole indices_count ) ;
    void draw_triangle_fan ( render_vertex_buffer_id vertices_buffer , render_index_buffer_id indices_buffer , num_whole indices_count ) ;
        
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
shy_macosx_platform_render < platform_insider > :: render_vertex_buffer_mapped_data :: render_vertex_buffer_mapped_data ( )
: _data ( ( void * ) platform_insider :: uninitialized_value )
{
}

template < typename platform_insider >
shy_macosx_platform_render < platform_insider > :: render_index_buffer_mapped_data :: render_index_buffer_mapped_data ( )
: _data ( ( void * ) platform_insider :: uninitialized_value )
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
    ( num_fract znear 
    , num_fract zfar 
    , num_fract r 
    , num_fract g 
    , num_fract b 
    , num_fract a 
    )
{
    float r_float ;
    float g_float ;
    float b_float ;
    float a_float ;
    float near_float ;
    float far_float ;
    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;

    GLfloat color [ ] = { r_float , g_float , b_float , a_float } ;
    glEnable ( GL_FOG ) ;
    glFogf ( GL_FOG_MODE , GL_LINEAR ) ;
    glFogf ( GL_FOG_START , ( GLfloat ) near_float ) ;
    glFogf ( GL_FOG_END , ( GLfloat ) far_float ) ;
    glFogfv ( GL_FOG_COLOR , color ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_texture_id 
    ( render_texture_id & arg_texture_id , num_whole size_pow2_base )
{
    glGenTextures ( 1 , & arg_texture_id . _texture_id ) ;
    int size_pow2_base_int = 0 ;
    platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    GLsizei size = 1 << size_pow2_base_int ;
    glPixelStorei ( GL_UNPACK_ALIGNMENT , 1 ) ;
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_S , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_WRAP_T , GL_REPEAT ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MAG_FILTER , GL_LINEAR ) ;
    glTexParameteri ( GL_TEXTURE_2D , GL_TEXTURE_MIN_FILTER , GL_LINEAR ) ;
    glTexImage2D
        ( GL_TEXTURE_2D                     // target
        , 0                                 // level
        , GL_RGBA                           // internal format
        , size                              // width
        , size                              // height
        , 0                                 // border
        , GL_BGRA                           // format
        , GL_UNSIGNED_BYTE                  // type
        , 0                                 // data
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: use_texture ( render_texture_id arg_texture_id )
{
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_texel_color 
    ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    float r_float ;
    float g_float ;
    float b_float ;
    float a_float ;
    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    texel . _color [ 0 ] = ( GLubyte ) ( b_float * 255.0f ) ;
    texel . _color [ 1 ] = ( GLubyte ) ( g_float * 255.0f ) ;
    texel . _color [ 2 ] = ( GLubyte ) ( r_float * 255.0f ) ;
    texel . _color [ 3 ] = ( GLubyte ) ( a_float * 255.0f ) ;
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_macosx_platform_render < platform_insider > :: load_texture_subdata 
    ( render_texture_id arg_texture_id 
    , num_whole x_offset 
    , num_whole y_offset 
    , num_whole width
    , num_whole height
    , const texels_array & data 
    )
{
    int x_offset_int = 0 ;
    int y_offset_int = 0 ;
    int width_int = 0 ;
    int height_int = 0 ;
    platform_math_insider :: num_whole_value_get ( x_offset_int , x_offset ) ;
    platform_math_insider :: num_whole_value_get ( y_offset_int , y_offset ) ;
    platform_math_insider :: num_whole_value_get ( width_int , width ) ;
    platform_math_insider :: num_whole_value_get ( height_int , height ) ;
    
    glBindTexture ( GL_TEXTURE_2D , arg_texture_id . _texture_id ) ;
    const texel_data * texels = 0 ;
    platform_static_array_insider :: elements_ptr ( texels , data ) ;
    glTexSubImage2D 
        ( GL_TEXTURE_2D                         // target
        , 0                                     // level
        , x_offset_int                          // x offset
        , y_offset_int                          // y offset
        , width_int                             // width
        , height_int                            // height
        , GL_BGRA                               // format
        , GL_UNSIGNED_BYTE                      // type
        , texels                                // data
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    platform_math_insider :: num_whole_value_get ( resource_id . _resource_id , resource_index ) ;
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_macosx_platform_render < platform_insider > :: load_texture_resource
    ( texture_resource_id resource_id , num_whole size_pow2_base , texels_array & data )
{
    int size_pow2_base_int = 0 ;
    texel_data * texels = 0 ;
    platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    platform_static_array_insider :: elements_ptr ( texels , data ) ;
    [ _texture_loader 
        load_texture_from_png_resource : resource_id . _resource_id 
        to_buffer : ( void * ) texels
        with_side_size_of : 1 << size_pow2_base_int
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
    float r_float ;
    float g_float ;
    float b_float ;
    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    glClearColor ( r_float , g_float , b_float , 0 ) ;
    glClearDepth ( 1 ) ;
    glClear ( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: projection_frustum 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract znear 
    , num_fract zfar 
    )
{
    float left_float ;
    float right_float ;
    float bottom_float ;
    float top_float ;
    float near_float ;
    float far_float ;
    platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glFrustum ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: projection_ortho 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract znear 
    , num_fract zfar 
    )
{
    float left_float ;
    float right_float ;
    float bottom_float ;
    float top_float ;
    float near_float ;
    float far_float ;
    platform_math_insider :: num_fract_value_get ( left_float , left ) ;
    platform_math_insider :: num_fract_value_get ( right_float , right ) ;
    platform_math_insider :: num_fract_value_get ( bottom_float , bottom ) ;
    platform_math_insider :: num_fract_value_get ( top_float , top ) ;
    platform_math_insider :: num_fract_value_get ( near_float , znear ) ;
    platform_math_insider :: num_fract_value_get ( far_float , zfar ) ;
    
    glMatrixMode ( GL_PROJECTION ) ;
    glLoadIdentity ( ) ;
    glOrtho ( left_float , right_float , bottom_float , top_float , near_float , far_float ) ;
    glMatrixMode ( GL_MODELVIEW ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    int elements_int = 0 ;
    platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
    glBufferData
        ( GL_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( vertex_data ) * ( unsigned int ) elements_int ) 
        , 0
        , GL_STATIC_DRAW 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: map_vertex_buffer
    ( render_vertex_buffer_mapped_data & data , render_vertex_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = glMapBuffer ( GL_ARRAY_BUFFER , GL_READ_WRITE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: unmap_vertex_buffer ( render_vertex_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glUnmapBuffer ( GL_ARRAY_BUFFER ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: mapped_vertex_buffer_element
    ( typename platform_pointer :: template pointer < vertex_data > & ptr 
    , render_vertex_buffer_mapped_data data
    , num_whole index
    )
{
    vertex_data * mapped_vertices = ( vertex_data * ) data . _data ;
    int index_int = 0 ;
    platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    ptr = mapped_vertices [ index_int ] ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
    platform_math_insider :: num_fract_value_get ( vertex . _position [ 0 ] , x ) ;
    platform_math_insider :: num_fract_value_get ( vertex . _position [ 1 ] , y ) ;
    platform_math_insider :: num_fract_value_get ( vertex . _position [ 2 ] , z ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
    platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 0 ] , u ) ;
    platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 1 ] , v ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_vertex_color 
    ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
    float r_float ;
    float g_float ;
    float b_float ;
    float a_float ;
    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    vertex . _color [ 0 ] = ( GLubyte ) ( r_float * 255.0f ) ;
    vertex . _color [ 1 ] = ( GLubyte ) ( g_float * 255.0f ) ;
    vertex . _color [ 2 ] = ( GLubyte ) ( b_float * 255.0f ) ;
    vertex . _color [ 3 ] = ( GLubyte ) ( a_float * 255.0f ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements )
{
    glGenBuffers ( 1 , & arg_buffer_id . _buffer_id ) ;
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    int elements_int = 0 ;
    platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
    glBufferData
        ( GL_ELEMENT_ARRAY_BUFFER 
        , ( GLsizeiptr ) ( sizeof ( index_data ) * ( unsigned int ) elements_int ) 
        , 0
        , GL_STATIC_DRAW 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: map_index_buffer
    ( render_index_buffer_mapped_data & data , render_index_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    data . _data = glMapBuffer ( GL_ELEMENT_ARRAY_BUFFER , GL_READ_WRITE ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: unmap_index_buffer ( render_index_buffer_id arg_buffer_id )
{
    glBindBuffer ( GL_ELEMENT_ARRAY_BUFFER , arg_buffer_id . _buffer_id ) ;
    glUnmapBuffer ( GL_ELEMENT_ARRAY_BUFFER ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: mapped_index_buffer_element
    ( typename platform_pointer :: template pointer < index_data > & ptr 
    , render_index_buffer_mapped_data data
    , num_whole index
    )
{
    index_data * mapped_indices = ( index_data * ) data . _data ;
    int index_int = 0 ;
    platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    ptr = mapped_indices [ index_int ] ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: set_index_value ( index_data & data , num_whole index )
{
    int index_int = 0 ;
    platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    data . _index = ( GLushort ) index_int ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_identity ( )
{
    glLoadIdentity ( ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_load ( const matrix_data & matrix )
{
    const float * elements = 0 ;
    platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    glLoadMatrixf ( elements ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: matrix_mult ( const matrix_data & matrix )
{
    const float * elements = 0 ;
    platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
    glMultMatrixf ( elements ) ;
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
    ( render_vertex_buffer_id vertices_buffer , render_index_buffer_id indices_buffer , num_whole indices_count )
{
    int indices_count_int = 0 ;
    platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
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
        , ( GLsizei ) indices_count_int
        , GL_UNSIGNED_SHORT 
        , ( void * ) 0 
        ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: draw_triangle_fan
    ( render_vertex_buffer_id vertices_buffer , render_index_buffer_id indices_buffer , num_whole indices_count )
{
    int indices_count_int = 0 ;
    platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
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
        , ( GLsizei ) indices_count_int
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
inline void shy_macosx_platform_render < platform_insider > :: get_frame_loss ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , ( int ) false ) ;
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id )
{
}

template < typename platform_insider >
inline void shy_macosx_platform_render < platform_insider > :: delete_index_buffer ( render_index_buffer_id & arg_buffer_id )
{
}
