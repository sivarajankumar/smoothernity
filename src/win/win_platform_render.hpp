template < typename platform_insider >
class shy_win_platform_render_insider ;

template < typename platform_insider >
class shy_win_platform_render
{
    friend class shy_win_platform_render_insider < platform_insider > ;

    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    typedef typename platform_insider :: platform_matrix_insider platform_matrix_insider ;
    typedef typename platform_insider :: platform_render_insider platform_render_insider ;
    typedef typename platform_insider :: platform_static_array_insider platform_static_array_insider ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_matrix :: matrix_data matrix_data ;
    typedef typename platform_insider :: platform_pointer platform_pointer ;
    
public :
    class render_index_buffer_id
    {
        friend class shy_win_platform_render ;
    public :
        render_index_buffer_id ( ) ;
    private :
		IDirect3DIndexBuffer9 * _buffer ;
    } ;
    
    class render_vertex_buffer_id
    {
        friend class shy_win_platform_render ;
    public :
        render_vertex_buffer_id ( ) ;
    private :
		IDirect3DVertexBuffer9 * _buffer ;
    } ;
    
    class render_vertex_buffer_mapped_data
    {
        friend class shy_win_platform_render ;
    public :
        render_vertex_buffer_mapped_data ( ) ;
    private :
        void * _data ;
    } ;

    class render_index_buffer_mapped_data
    {
        friend class shy_win_platform_render ;
    public :
        render_index_buffer_mapped_data ( ) ;
    private :
        void * _data ;
    } ;

	class render_texture_id
	{
		friend class shy_win_platform_render ;
    public :
        render_texture_id ( ) ;
	private :
        IDirect3DTexture9 * _texture ; 
	} ;

    class texture_resource_id
    {
        friend class shy_win_platform_render ;
    public :
        texture_resource_id ( ) ;
    private :
        int _dummy ;
    } ;
	
    class texel_data
    {
        friend class shy_win_platform_render ;
    public :
        texel_data ( ) ;
    private :
        int _dummy ;
    } ;
    
    class vertex_data
    {
        friend class shy_win_platform_render ;
        friend class shy_win_platform_insider ;
    public :
        vertex_data ( ) ;
    private :
		FLOAT _x ;
		FLOAT _y ;
		FLOAT _z ;
		DWORD _color ;
		FLOAT _u ;
		FLOAT _v ;
    } ;
    
    class index_data
    {
        friend class shy_win_platform_render ;
    public :
        index_data ( ) ;
    private :
		UINT _index ;
    } ;

public :
    shy_win_platform_render ( ) ;

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
    void delete_texture_id ( render_texture_id & arg_texture_id ) ;
    
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
    shy_win_platform_render < platform_insider > & operator= ( const shy_win_platform_render < platform_insider > & src ) ;

private :
    platform_insider * _platform_insider ;
} ;

template < typename platform_insider >
shy_win_platform_render < platform_insider > :: shy_win_platform_render ( )
: _platform_insider ( 0 )
{
}

template < typename platform_insider >
shy_win_platform_render < platform_insider > & 
shy_win_platform_render < platform_insider > :: operator= ( const shy_win_platform_render < platform_insider > & src )
{
    return * this ;
}

template < typename platform_insider >
shy_win_platform_render < platform_insider > :: render_vertex_buffer_mapped_data :: render_vertex_buffer_mapped_data ( )
: _data ( reinterpret_cast < void * > ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
shy_win_platform_render < platform_insider > :: render_index_buffer_mapped_data :: render_index_buffer_mapped_data ( )
: _data ( reinterpret_cast < void * > ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
shy_win_platform_render < platform_insider > :: render_index_buffer_id :: render_index_buffer_id ( )
: _buffer ( reinterpret_cast < IDirect3DIndexBuffer9 * > ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_win_platform_render < platform_insider > :: render_vertex_buffer_id :: render_vertex_buffer_id ( )
: _buffer ( reinterpret_cast < IDirect3DVertexBuffer9 * > ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_win_platform_render < platform_insider > :: render_texture_id :: render_texture_id ( )
: _texture ( reinterpret_cast < IDirect3DTexture9 * > ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
shy_win_platform_render < platform_insider > :: texture_resource_id :: texture_resource_id ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
	
template < typename platform_insider >
shy_win_platform_render < platform_insider > :: texel_data :: texel_data ( )
: _dummy ( platform_insider :: uninitialized_value )
{
}
    
template < typename platform_insider >
shy_win_platform_render < platform_insider > :: vertex_data :: vertex_data ( )
: _x ( FLOAT ( platform_insider :: uninitialized_value ) )
, _y ( FLOAT ( platform_insider :: uninitialized_value ) )
, _z ( FLOAT ( platform_insider :: uninitialized_value ) )
, _color ( DWORD ( platform_insider :: uninitialized_value ) )
, _u ( FLOAT ( platform_insider :: uninitialized_value ) )
, _v ( FLOAT ( platform_insider :: uninitialized_value ) )
{
}
    
template < typename platform_insider >
shy_win_platform_render < platform_insider > :: index_data :: index_data ( )
: _index ( UINT ( platform_insider :: uninitialized_value ) )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: enable_face_culling ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_CULLMODE , D3DCULL_NONE ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: enable_depth_test ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_ZENABLE , D3DZB_TRUE ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: disable_depth_test ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_ZENABLE , D3DZB_FALSE ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: blend_disable ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_ALPHABLENDENABLE , FALSE ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: blend_src_alpha_dst_one_minus_alpha ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_ALPHABLENDENABLE , TRUE ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_SRCBLEND , D3DBLEND_SRCCOLOR ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_DESTBLEND , D3DBLEND_INVSRCCOLOR ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: enable_texturing ( )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: disable_texturing ( )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: texture_mode_modulate ( )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: fog_disable ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGENABLE , FALSE ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: fog_linear 
    ( num_fract znear 
    , num_fract zfar 
    , num_fract r 
    , num_fract g 
    , num_fract b 
    , num_fract a 
    )
{
	HRESULT hr ;
    D3DCOLOR color ;
    float r_float = 0.0f ;
    float g_float = 0.0f ;
    float b_float = 0.0f ;
    float a_float = 0.0f ;
    float znear_float = 0.0f ;
    float zfar_float = 0.0f ;

    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
    platform_math_insider :: num_fract_value_get ( a_float , a ) ;
    platform_math_insider :: num_fract_value_get ( znear_float , znear ) ;
    platform_math_insider :: num_fract_value_get ( zfar_float , zfar ) ;
	color = D3DCOLOR_ARGB \
        ( int ( a_float * 255.0f )
        , int ( r_float * 255.0f ) 
        , int ( g_float * 255.0f ) 
        , int ( b_float * 255.0f ) 
        ) ;

	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGENABLE , TRUE ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGCOLOR , color ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGVERTEXMODE , D3DFOG_LINEAR ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGSTART , * ( DWORD * ) ( & znear_float ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_FOGEND , * ( DWORD * ) ( & zfar_float ) ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_texture_id ( render_texture_id & arg_texture_id , num_whole size_pow2_base )
{
    HRESULT hr ;
    int size_pow2_base_int = 0 ;
    DWORD size = 0 ;

    platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    size = 1 << size_pow2_base_int ;

    V ( DXUTGetD3D9Device ( ) -> CreateTexture
        ( size
        , size
        , 0
        , 0
        , D3DFMT_A8R8G8B8
        , D3DPOOL_MANAGED
        , & arg_texture_id . _texture
        , 0
        ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: use_texture ( render_texture_id arg_texture_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_texel_color 
    ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_win_platform_render < platform_insider > :: load_texture_subdata 
    ( render_texture_id arg_texture_id 
    , num_whole x_offset 
    , num_whole y_offset 
    , num_whole width
    , num_whole height
    , const texels_array & data 
    )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_win_platform_render < platform_insider > :: load_texture_resource
    ( texture_resource_id resource_id , num_whole size_pow2_base , texels_array & data )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: texture_loader_ready ( num_whole & is_ready )
{
    platform_math_insider :: num_whole_value_set ( is_ready , true ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: clear_screen ( num_fract r , num_fract g , num_fract b )
{
    HRESULT hr ;
    float r_float = 0.0f ;
    float g_float = 0.0f ;
    float b_float = 0.0f ;
    platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    platform_math_insider :: num_fract_value_get ( b_float , b ) ;
	D3DCOLOR color = D3DCOLOR_ARGB \
        ( 0 
        , int ( r_float * 255.0f ) 
        , int ( g_float * 255.0f ) 
        , int ( b_float * 255.0f ) 
        ) ;
	V ( DXUTGetD3D9Device ( ) -> Clear ( 0 , NULL , D3DCLEAR_TARGET | D3DCLEAR_ZBUFFER , color , 1.0f , 0 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: projection_frustum 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract znear 
    , num_fract zfar 
    )
{
    float float_left = 0.0f ;
    float float_right = 0.0f ;
    float float_bottom = 0.0f ;
    float float_top = 0.0f ;
    float float_znear = 0.0f ;
    float float_zfar = 0.0f ;
    platform_math_insider :: num_fract_value_get ( float_left , left ) ;
    platform_math_insider :: num_fract_value_get ( float_right , right ) ;
    platform_math_insider :: num_fract_value_get ( float_bottom , bottom ) ;
    platform_math_insider :: num_fract_value_get ( float_top , top ) ;
    platform_math_insider :: num_fract_value_get ( float_znear , znear ) ;
    platform_math_insider :: num_fract_value_get ( float_zfar , zfar ) ;

    HRESULT hr ;
	D3DXMATRIX matrix ;
	D3DXMatrixPerspectiveOffCenterRH 
        ( & matrix 
        , float_left
        , float_right
        , float_bottom
        , float_top
        , float_znear
        , float_zfar
        ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_PROJECTION , & matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: projection_ortho 
    ( num_fract left 
    , num_fract right 
    , num_fract bottom 
    , num_fract top 
    , num_fract znear 
    , num_fract zfar 
    )
{
    float float_left = 0.0f ;
    float float_right = 0.0f ;
    float float_bottom = 0.0f ;
    float float_top = 0.0f ;
    float float_znear = 0.0f ;
    float float_zfar = 0.0f ;
    platform_math_insider :: num_fract_value_get ( float_left , left ) ;
    platform_math_insider :: num_fract_value_get ( float_right , right ) ;
    platform_math_insider :: num_fract_value_get ( float_bottom , bottom ) ;
    platform_math_insider :: num_fract_value_get ( float_top , top ) ;
    platform_math_insider :: num_fract_value_get ( float_znear , znear ) ;
    platform_math_insider :: num_fract_value_get ( float_zfar , zfar ) ;

    HRESULT hr ;
	D3DXMATRIX matrix ;
	D3DXMatrixOrthoOffCenterRH 
        ( & matrix 
        , float_left
        , float_right
        , float_bottom
        , float_top
        , float_znear
        , float_zfar
        ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_PROJECTION , & matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_vertex_buffer 
    ( render_vertex_buffer_id & arg_buffer_id , num_whole elements )
{
	HRESULT hr ;
    int int_elements = 0 ;
    platform_math_insider :: num_whole_value_get ( int_elements , elements ) ;
	V ( DXUTGetD3D9Device ( ) -> CreateVertexBuffer 
		( sizeof ( vertex_data ) * int_elements
		, D3DUSAGE_WRITEONLY
		, D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer
		, 0
		) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: map_vertex_buffer ( render_vertex_buffer_mapped_data & data , render_vertex_buffer_id arg_buffer_id )
{
	HRESULT hr ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & data . _data , 0 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: unmap_vertex_buffer ( render_vertex_buffer_id arg_buffer_id )
{
	HRESULT hr ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: mapped_vertex_buffer_element
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
inline void shy_win_platform_render < platform_insider > :: set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
	platform_math_insider :: num_fract_value_get ( vertex . _x , x ) ;
	platform_math_insider :: num_fract_value_get ( vertex . _y , y ) ;
	platform_math_insider :: num_fract_value_get ( vertex . _z , z ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
	platform_math_insider :: num_fract_value_get ( vertex . _u , u ) ;
	platform_math_insider :: num_fract_value_get ( vertex . _v , v ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_vertex_color 
    ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
    float float_r = 0.0f ;
    float float_g = 0.0f ;
    float float_b = 0.0f ;
    float float_a = 0.0f ;
    platform_math_insider :: num_fract_value_get ( float_r , r ) ;
    platform_math_insider :: num_fract_value_get ( float_g , g ) ;
    platform_math_insider :: num_fract_value_get ( float_b , b ) ;
    platform_math_insider :: num_fract_value_get ( float_a , a ) ;
	vertex . _color = D3DCOLOR_ARGB \
        ( int ( float_a * 255.0f ) 
        , int ( float_r * 255.0f ) 
        , int ( float_g * 255.0f )
        , int ( float_b * 255.0f )
        ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_index_buffer 
    ( render_index_buffer_id & arg_buffer_id , num_whole elements )
{
	HRESULT hr ;
    int int_elements = 0 ;
    platform_math_insider :: num_whole_value_get ( int_elements , elements ) ;
	V ( DXUTGetD3D9Device ( ) -> CreateIndexBuffer
		( sizeof ( index_data ) * int_elements
		, D3DUSAGE_WRITEONLY
		, D3DFMT_INDEX32
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer 
		, 0
		) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: map_index_buffer ( render_index_buffer_mapped_data & data , render_index_buffer_id arg_buffer_id )
{
	HRESULT hr ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & data . _data , 0 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: unmap_index_buffer ( render_index_buffer_id arg_buffer_id )
{
	HRESULT hr ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: mapped_index_buffer_element
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
inline void shy_win_platform_render < platform_insider > :: set_index_value ( index_data & data , num_whole index )
{
    int int_index = 0 ;
    platform_math_insider :: num_whole_value_get ( int_index , index ) ;
	data . _index = ( UINT ) int_index ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_identity ( )
{
    HRESULT hr ;
	V ( _platform_insider -> render_insider . matrix_stack -> LoadIdentity ( ) ) ;
    D3DXMATRIX d3d_matrix ;
    platform_render_insider :: convert_from_opengl ( d3d_matrix , * _platform_insider -> render_insider . matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_load ( const matrix_data & matrix )
{
    HRESULT hr ;
    const float * matrix_elements = 0 ;
    platform_matrix_insider :: elements_ptr ( matrix_elements , matrix ) ;
    V ( _platform_insider -> render_insider . matrix_stack -> LoadMatrix ( ( const D3DXMATRIX * ) matrix_elements ) ) ;
    D3DXMATRIX d3d_matrix ;
    platform_render_insider :: convert_from_opengl ( d3d_matrix , * _platform_insider -> render_insider . matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_mult ( const matrix_data & matrix )
{
    HRESULT hr ;
    const float * matrix_elements = 0 ;
    platform_matrix_insider :: elements_ptr ( matrix_elements , matrix ) ;
	V ( _platform_insider -> render_insider . matrix_stack -> MultMatrixLocal ( ( const D3DXMATRIX * ) matrix_elements ) ) ;
    D3DXMATRIX d3d_matrix ;
    platform_render_insider :: convert_from_opengl ( d3d_matrix , * _platform_insider -> render_insider . matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_push ( )
{
	HRESULT hr ;
    V ( _platform_insider -> render_insider . matrix_stack -> Push ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_pop ( )
{
	HRESULT hr ;
    V ( _platform_insider -> render_insider . matrix_stack -> Pop ( ) ) ;
    D3DXMATRIX d3d_matrix ;
    platform_render_insider :: convert_from_opengl ( d3d_matrix , * _platform_insider -> render_insider . matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: draw_triangle_strip 
    ( render_vertex_buffer_id vertices_buffer 
    , render_index_buffer_id indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
    int int_indices_count = 0 ;
    platform_math_insider :: num_whole_value_get ( int_indices_count , indices_count ) ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLESTRIP , 0 , 0 , int_indices_count , 0 , int_indices_count - 2 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: draw_triangle_fan
    ( render_vertex_buffer_id vertices_buffer 
    , render_index_buffer_id indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
    int int_indices_count = 0 ;
    platform_math_insider :: num_whole_value_get ( int_indices_count , indices_count ) ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLEFAN , 0 , 0 , int_indices_count , 0 , int_indices_count - 2 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: get_aspect_width ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _platform_insider -> render_insider . aspect_width ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: get_aspect_height ( num_fract & result )
{
    platform_math_insider :: num_fract_value_set ( result , _platform_insider -> render_insider . aspect_height ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id )
{
    arg_buffer_id . _buffer -> Release ( ) ;
    arg_buffer_id . _buffer = 0 ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: delete_index_buffer ( render_index_buffer_id & arg_buffer_id )
{
    arg_buffer_id . _buffer -> Release ( ) ;
    arg_buffer_id . _buffer = 0 ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: delete_texture_id ( render_texture_id & arg_texture_id )
{
    arg_texture_id . _texture -> Release ( ) ;
    arg_texture_id . _texture = 0 ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: get_frame_loss ( num_whole & result )
{
    platform_math_insider :: num_whole_value_set ( result , ( int ) false ) ;
}

