template < typename platform_insider >
class shy_win_platform_render
{
    typedef typename platform_insider :: platform_math_insider platform_math_insider ;
    typedef typename platform_insider :: platform_matrix_insider platform_matrix_insider ;
    typedef typename platform_insider :: platform_static_array_insider platform_static_array_insider ;
    typedef typename platform_insider :: platform_math :: num_fract num_fract ;
    typedef typename platform_insider :: platform_math :: num_whole num_whole ;
    typedef typename platform_insider :: platform_matrix :: matrix_data matrix_data ;
    
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
    
	class render_texture_id
	{
		friend class shy_win_platform_render ;
    public :
        render_texture_id ( ) ;
	private :
		int _dummy ;
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

    static void enable_face_culling ( ) ;
    
    static void enable_depth_test ( ) ;
    static void disable_depth_test ( ) ;
    
    static void fog_disable ( ) ;
    static void fog_linear ( num_fract znear , num_fract zfar , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    
    static void blend_disable ( ) ;
    static void blend_src_alpha_dst_one_minus_alpha ( ) ;
    
	static void enable_texturing ( ) ;
	static void disable_texturing ( ) ;
	static void texture_mode_modulate ( ) ;
    static void use_texture ( const render_texture_id & arg_texture_id ) ;
	static void create_texture_id ( render_texture_id & arg_texture_id ) ;
    static void set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    static void texture_loader_ready ( num_whole & is_ready ) ;

    static void clear_screen ( num_fract r , num_fract g , num_fract b ) ;    
    static void projection_frustum ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract znear , num_fract zfar ) ;
    static void projection_ortho ( num_fract left , num_fract right , num_fract bottom , num_fract top , num_fract znear , num_fract zfar ) ;
    
    static void set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z ) ;
    static void set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v ) ;
    static void set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void set_index_value ( index_data & data , num_whole index ) ;
    
    static void matrix_identity ( ) ;
    static void matrix_load ( const matrix_data & matrix ) ;
    static void matrix_mult ( const matrix_data & matrix ) ;
    static void matrix_push ( ) ;
    static void matrix_pop ( ) ;
    
	static void get_aspect_width ( num_fract & result ) ;
	static void get_aspect_height ( num_fract & result ) ;
    
    static void delete_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id ) ;
    static void delete_index_buffer ( render_index_buffer_id & arg_buffer_id ) ;
    
    template < typename texels_array >
    static void load_texture_data ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename texels_array >
    static void load_texture_resource ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data ) ;
    
    template < typename vertices_array >
    static void create_vertex_buffer ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data ) ;
    
    template < typename indices_array >
    static void create_index_buffer ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data ) ;
    
    static void draw_triangle_strip 
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;
    static void draw_triangle_fan
        ( const render_vertex_buffer_id & vertices_buffer 
        , const render_index_buffer_id & indices_buffer
        , num_whole indices_count
        ) ;        
} ;

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
: _dummy ( platform_insider :: uninitialized_value )
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
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: disable_depth_test ( )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: blend_disable ( )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: blend_src_alpha_dst_one_minus_alpha ( )
{
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
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_texture_id ( render_texture_id & arg_texture_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: use_texture ( const render_texture_id & arg_texture_id )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_texel_color 
    ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_win_platform_render < platform_insider > :: load_texture_data 
    ( const render_texture_id & arg_texture_id , num_whole size_pow2_base , const texels_array & data )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
}

template < typename platform_insider >
template < typename texels_array >
inline void shy_win_platform_render < platform_insider > :: load_texture_resource
    ( const texture_resource_id & resource_id , num_whole size_pow2_base , const texels_array & data )
{
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: texture_loader_ready ( num_whole & is_ready )
{
    platform_math_insider :: num_whole_unsafe_value_set ( is_ready , true ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: clear_screen ( num_fract r , num_fract g , num_fract b )
{
    HRESULT hr ;
	D3DCOLOR color = D3DCOLOR_ARGB \
        ( 0 
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) 
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f ) 
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f ) 
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
    HRESULT hr ;
	D3DXMATRIX matrix ;
	D3DXMatrixPerspectiveOffCenterRH 
        ( & matrix 
        , platform_math_insider :: num_fract_unsafe_value_get ( left )
        , platform_math_insider :: num_fract_unsafe_value_get ( right )
        , platform_math_insider :: num_fract_unsafe_value_get ( bottom )
        , platform_math_insider :: num_fract_unsafe_value_get ( top )
        , platform_math_insider :: num_fract_unsafe_value_get ( znear )
        , platform_math_insider :: num_fract_unsafe_value_get ( zfar )
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
    HRESULT hr ;
	D3DXMATRIX matrix ;
	D3DXMatrixOrthoOffCenterRH 
        ( & matrix 
        , platform_math_insider :: num_fract_unsafe_value_get ( left )
        , platform_math_insider :: num_fract_unsafe_value_get ( right )
        , platform_math_insider :: num_fract_unsafe_value_get ( bottom )
        , platform_math_insider :: num_fract_unsafe_value_get ( top )
        , platform_math_insider :: num_fract_unsafe_value_get ( znear )
        , platform_math_insider :: num_fract_unsafe_value_get ( zfar )
        ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_PROJECTION , & matrix ) ) ;
}

template < typename platform_insider >
template < typename vertices_array >
inline void shy_win_platform_render < platform_insider > :: create_vertex_buffer 
    ( render_vertex_buffer_id & arg_buffer_id , num_whole elements , const vertices_array & data )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> CreateVertexBuffer 
		( sizeof ( vertex_data ) * platform_math_insider :: num_whole_unsafe_value_get ( elements )
		, D3DUSAGE_WRITEONLY
		, D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer
		, 0
		) ) ;
	void * mapped_vertices = 0 ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & mapped_vertices , 0 ) ) ;
	memcpy 
        ( mapped_vertices 
        , platform_static_array_insider :: elements_unsafe_ptr ( data )
        , sizeof ( vertex_data ) * platform_math_insider :: num_whole_unsafe_value_get ( elements ) 
        ) ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
	vertex . _x = platform_math_insider :: num_fract_unsafe_value_get ( x ) ;
	vertex . _y = platform_math_insider :: num_fract_unsafe_value_get ( y ) ;
	vertex . _z = platform_math_insider :: num_fract_unsafe_value_get ( z ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
	vertex . _u = platform_math_insider :: num_fract_unsafe_value_get ( u ) ;
	vertex . _v = platform_math_insider :: num_fract_unsafe_value_get ( v ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_vertex_color 
    ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
	vertex . _color = D3DCOLOR_ARGB \
        ( int ( platform_math_insider :: num_fract_unsafe_value_get ( a ) * 255.0f ) 
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( r ) * 255.0f ) 
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( g ) * 255.0f )
        , int ( platform_math_insider :: num_fract_unsafe_value_get ( b ) * 255.0f )
        ) ;
}

template < typename platform_insider >
template < typename indices_array >
inline void shy_win_platform_render < platform_insider > :: create_index_buffer 
    ( render_index_buffer_id & arg_buffer_id , num_whole elements , const indices_array & data )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> CreateIndexBuffer
		( sizeof ( index_data ) * platform_math_insider :: num_whole_unsafe_value_get ( elements )
		, D3DUSAGE_WRITEONLY
		, D3DFMT_INDEX32
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer 
		, 0
		) ) ;
	void * mapped_indices = 0 ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & mapped_indices , 0 ) ) ;
	memcpy 
        ( mapped_indices 
        , platform_static_array_insider :: elements_unsafe_ptr ( data )
        , sizeof ( index_data ) * platform_math_insider :: num_whole_unsafe_value_get ( elements ) 
        ) ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: set_index_value ( index_data & data , num_whole index )
{
	data . _index = ( UINT ) platform_math_insider :: num_whole_unsafe_value_get ( index ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_identity ( )
{
    HRESULT hr ;
	V ( platform_insider :: matrix_stack -> LoadIdentity ( ) ) ;
    D3DXMATRIX d3d_matrix = platform_insider :: convert_from_opengl ( * platform_insider :: matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_load ( const matrix_data & matrix )
{
    HRESULT hr ;
    V ( platform_insider :: matrix_stack -> LoadMatrix ( ( const D3DXMATRIX * ) ( platform_matrix_insider :: elements_unsafe_ptr ( matrix ) ) ) ) ;
    D3DXMATRIX d3d_matrix = platform_insider :: convert_from_opengl ( * platform_insider :: matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_mult ( const matrix_data & matrix )
{
    HRESULT hr ;
	V ( platform_insider :: matrix_stack -> MultMatrixLocal ( ( const D3DXMATRIX * ) ( platform_matrix_insider :: elements_unsafe_ptr ( matrix ) ) ) ) ;
    D3DXMATRIX d3d_matrix = platform_insider :: convert_from_opengl ( * platform_insider :: matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_push ( )
{
	HRESULT hr ;
    V ( platform_insider :: matrix_stack -> Push ( ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: matrix_pop ( )
{
	HRESULT hr ;
    V ( platform_insider :: matrix_stack -> Pop ( ) ) ;
    D3DXMATRIX d3d_matrix = platform_insider :: convert_from_opengl ( * platform_insider :: matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: draw_triangle_strip 
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
    int int_indices_count = platform_math_insider :: num_whole_unsafe_value_get ( indices_count ) ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLESTRIP , 0 , 0 , int_indices_count , 0 , int_indices_count - 2 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: draw_triangle_fan
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
    int int_indices_count = platform_math_insider :: num_whole_unsafe_value_get ( indices_count ) ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLEFAN , 0 , 0 , int_indices_count , 0 , int_indices_count - 2 ) ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: get_aspect_width ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , platform_insider :: aspect_width ) ;
}

template < typename platform_insider >
inline void shy_win_platform_render < platform_insider > :: get_aspect_height ( num_fract & result )
{
    platform_math_insider :: num_fract_unsafe_value_set ( result , platform_insider :: aspect_height ) ;
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
