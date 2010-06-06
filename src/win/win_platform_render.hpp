inline void shy_win_platform :: render_enable_face_culling ( )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_CULLMODE , D3DCULL_NONE ) ) ;
}

inline void shy_win_platform :: render_enable_depth_test ( )
{
}

inline void shy_win_platform :: render_disable_depth_test ( )
{
}

inline void shy_win_platform :: render_blend_disable ( )
{
}

inline void shy_win_platform :: render_blend_src_alpha_dst_one_minus_alpha ( )
{
}

inline void shy_win_platform :: render_enable_texturing ( )
{
}

inline void shy_win_platform :: render_disable_texturing ( )
{
}

inline void shy_win_platform :: render_set_modulate_texture_mode ( )
{
}

inline void shy_win_platform :: render_fog_disable ( )
{
}

inline void shy_win_platform :: render_fog_linear 
    ( num_fract near 
    , num_fract far 
    , num_fract r 
    , num_fract g 
    , num_fract b 
    , num_fract a 
    )
{
}

inline void shy_win_platform :: render_create_texture_id ( render_texture_id & arg_texture_id )
{
}

inline void shy_win_platform :: render_use_texture ( const render_texture_id & arg_texture_id )
{
}

inline void shy_win_platform :: render_set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
}

template < shy_win_platform :: const_int_32 texel_array_size >
inline void shy_win_platform :: render_load_texture_data 
    ( const render_texture_id & arg_texture_id 
    , num_whole size_pow2_base 
    , const static_array < texel_data , texel_array_size > & data
    )
{
}

inline void shy_win_platform :: render_create_texture_resource_id 
    ( texture_resource_id & resource_id 
    , num_whole resource_index 
    )
{
}

template < shy_win_platform :: const_int_32 texel_array_size >
inline void shy_win_platform :: render_load_texture_resource
    ( const texture_resource_id & resource_id 
    , num_whole size_pow2_base 
    , const static_array < texel_data , texel_array_size > & data 
    )
{
}

inline void shy_win_platform :: render_texture_loader_ready ( num_whole & is_ready )
{
    is_ready . _value = true ;
}

inline void shy_win_platform :: render_clear_screen ( num_fract r , num_fract g , num_fract b )
{
    HRESULT hr ;
	D3DCOLOR color = D3DCOLOR_ARGB ( 0 , int ( r . _value * 255.0f ) , int ( g . _value * 255.0f ) , int ( b . _value * 255.0f ) ) ;
	V ( DXUTGetD3D9Device ( ) -> Clear ( 0 , NULL , D3DCLEAR_TARGET | D3DCLEAR_ZBUFFER , color , 1.0f , 0 ) ) ;
}

inline void shy_win_platform :: render_projection_frustum 
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
	D3DXMatrixPerspectiveOffCenterRH ( & matrix , left . _value , right . _value , bottom . _value , top . _value , znear . _value , zfar . _value ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_PROJECTION , & matrix ) ) ;
}

inline void shy_win_platform :: render_projection_ortho 
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
	D3DXMatrixOrthoOffCenterRH ( & matrix , left . _value , right . _value , bottom . _value , top . _value , znear . _value , zfar . _value ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_PROJECTION , & matrix ) ) ;
}

template < shy_win_platform :: const_int_32 vertex_array_size >
inline void shy_win_platform :: render_create_vertex_buffer 
    ( render_vertex_buffer_id & arg_buffer_id 
    , num_whole elements 
    , const static_array < vertex_data , vertex_array_size > & data 
    )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> CreateVertexBuffer 
		( sizeof ( vertex_data ) * elements . _value
		, D3DUSAGE_WRITEONLY
		, D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer
		, 0
		) ) ;
	void * mapped_vertices = 0 ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & mapped_vertices , 0 ) ) ;
	memcpy ( mapped_vertices , data . _elements , sizeof ( vertex_data ) * elements . _value ) ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

inline void shy_win_platform :: render_delete_vertex_buffer ( render_vertex_buffer_id arg_buffer_id )
{
    arg_buffer_id . _buffer -> Release ( ) ;
    arg_buffer_id . _buffer = 0 ;
}

inline void shy_win_platform :: render_set_vertex_position ( vertex_data & vertex , num_fract x , num_fract y , num_fract z )
{
	vertex . _x = x . _value ;
	vertex . _y = y . _value ;
	vertex . _z = z . _value ;
}

inline void shy_win_platform :: render_set_vertex_tex_coord ( vertex_data & vertex , num_fract u , num_fract v )
{
	vertex . _u = u . _value ;
	vertex . _v = v . _value ;
}

inline void shy_win_platform :: render_set_vertex_color ( vertex_data & vertex , num_fract r , num_fract g , num_fract b , num_fract a )
{
	vertex . _color = D3DCOLOR_ARGB \
        ( int ( a . _value * 255.0f ) 
        , int ( r . _value * 255.0f ) 
        , int ( g . _value * 255.0f )
        , int ( b . _value * 255.0f )
        ) ;
}

template < shy_win_platform :: const_int_32 index_array_size >
inline void shy_win_platform :: render_create_index_buffer 
    ( render_index_buffer_id & arg_buffer_id 
    , num_whole elements 
    , const static_array < index_data , index_array_size > & data 
    )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> CreateIndexBuffer
		( sizeof ( index_data ) * elements . _value
		, D3DUSAGE_WRITEONLY
		, D3DFMT_INDEX32
		, D3DPOOL_MANAGED
		, & arg_buffer_id . _buffer 
		, 0
		) ) ;
	void * mapped_indices = 0 ;
	V ( arg_buffer_id . _buffer -> Lock ( 0 , 0 , & mapped_indices , 0 ) ) ;
	memcpy ( mapped_indices , data . _elements , sizeof ( index_data ) * elements . _value ) ;
	V ( arg_buffer_id . _buffer -> Unlock ( ) ) ;
}

inline void shy_win_platform :: render_delete_index_buffer ( render_index_buffer_id arg_buffer_id )
{
    arg_buffer_id . _buffer -> Release ( ) ;
    arg_buffer_id . _buffer = 0 ;
}

inline void shy_win_platform :: render_set_index_value ( index_data & data , num_whole index )
{
	data . _index = ( UINT ) index . _value ;
}

inline void shy_win_platform :: render_matrix_identity ( )
{
    HRESULT hr ;
	V ( _matrix_stack -> LoadIdentity ( ) ) ;
	D3DXMATRIX d3d_matrix = _convert_from_opengl ( * _matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

inline void shy_win_platform :: render_matrix_load 
    ( const shy_win_platform :: matrix_data & matrix 
    )
{
    HRESULT hr ;
	V ( _matrix_stack -> LoadMatrix ( ( const D3DXMATRIX * ) ( & matrix ) ) ) ;
	D3DXMATRIX d3d_matrix = _convert_from_opengl ( * _matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

inline void shy_win_platform :: render_matrix_mult 
    ( const shy_win_platform :: matrix_data & matrix 
    )
{
    HRESULT hr ;
	V ( _matrix_stack -> MultMatrixLocal ( ( const D3DXMATRIX * ) ( & matrix ) ) ) ;
	D3DXMATRIX d3d_matrix = _convert_from_opengl ( * _matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

inline void shy_win_platform :: render_matrix_push ( )
{
	HRESULT hr ;
	V ( _matrix_stack -> Push ( ) ) ;
}

inline void shy_win_platform :: render_matrix_pop ( )
{
	HRESULT hr ;
	V ( _matrix_stack -> Pop ( ) ) ;
	D3DXMATRIX d3d_matrix = _convert_from_opengl ( * _matrix_stack -> GetTop ( ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetTransform ( D3DTS_VIEW , & d3d_matrix ) ) ;
}

inline void shy_win_platform :: render_draw_triangle_strip 
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLESTRIP , 0 , 0 , indices_count . _value , 0 , indices_count . _value - 2 ) ) ;
}

inline void shy_win_platform :: render_draw_triangle_fan
    ( const render_vertex_buffer_id & vertices_buffer 
    , const render_index_buffer_id & indices_buffer
    , num_whole indices_count
    )
{
	HRESULT hr ;
	V ( DXUTGetD3D9Device ( ) -> SetStreamSource ( 0 , vertices_buffer . _buffer , 0 , sizeof ( vertex_data ) ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetFVF ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_TEX1 ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetIndices ( indices_buffer . _buffer ) ) ;
	V ( DXUTGetD3D9Device ( ) -> DrawIndexedPrimitive ( D3DPT_TRIANGLEFAN , 0 , 0 , indices_count . _value , 0 , indices_count . _value - 2 ) ) ;
}

inline void shy_win_platform :: render_get_aspect_width ( num_fract & result )
{
	result . _value = _aspect_width ;
}

inline void shy_win_platform :: render_get_aspect_height ( num_fract & result )
{
	result . _value = _aspect_height ;
}
