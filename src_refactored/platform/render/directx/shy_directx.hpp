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
    platform_pointer :: bind ( ptr , mapped_vertices [ index_int ] ) ;
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
    platform_pointer :: bind ( ptr , mapped_indices [ index_int ] ) ;
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

namespace shy_guts
{
}

void shy_platform_render_directx :: init ( )
{
}

void shy_platform_render_directx :: done ( )
{
}

void shy_platform_render_directx :: _load_texture_subdata 
    ( so_called_type_platform_render_directx_texture_id arg_texture_id 
    , so_called_type_platform_math_num_whole x_offset 
    , so_called_type_platform_math_num_whole y_offset 
    , so_called_type_platform_math_num_whole width
    , so_called_type_platform_math_num_whole height
    , const so_called_type_platform_render_directx_texel_data * data_ptr
    )
{
    so_called_lib_directx_HRESULT hr ;
    so_called_lib_directx_D3DLOCKED_RECT locked_rect ;
    so_called_lib_directx_RECT d3d_rect ;
    so_called_lib_std_int32_t x_offset_int = 0 ;
    so_called_lib_std_int32_t y_offset_int = 0 ;
    so_called_lib_std_int32_t width_int = 0 ;
    so_called_lib_std_int32_t height_int = 0 ;
    so_called_lib_std_int32_t ogl_left = 0 ;
    so_called_lib_std_int32_t ogl_right = 0 ;
    so_called_lib_std_int32_t ogl_bottom = 0 ;
    so_called_lib_std_int32_t ogl_top = 0 ;

    platform_math_insider :: num_whole_value_get ( x_offset_int , x_offset ) ;
    platform_math_insider :: num_whole_value_get ( y_offset_int , y_offset ) ;
    platform_math_insider :: num_whole_value_get ( width_int , width ) ;
    platform_math_insider :: num_whole_value_get ( height_int , height ) ;
    platform_static_array_insider :: elements_ptr ( data_ptr , data ) ;

    ogl_left = x_offset_int ;
    ogl_bottom = y_offset_int ;
    ogl_right = x_offset_int + width_int - 1 ;
    ogl_top = y_offset_int + height_int - 1 ;

    d3d_rect . left = x_offset_int ;
    d3d_rect . right = x_offset_int + width_int - 1 ;
    d3d_rect . top = y_offset_int ;
    d3d_rect . bottom = y_offset_int + height_int - 1 ;

    so_called_lib_directx_V
        ( arg_texture_id . _texture -> LockRect
            ( 0 
            , & locked_rect 
            , & d3d_rect 
            , 0 
            ) 
        ) ;
    for ( so_called_lib_std_int32_t y = 0 ; y < height_int ; y ++ )
    {
        so_called_lib_std_int32_t d3d_y = y + y_offset_int ;
        so_called_lib_std_char * dst_data_ptr = 0 ;
        const so_called_type_platform_render_directx_texel_data * src_data_ptr = 0 ;
        dst_data_ptr = ( so_called_lib_std_char * ) locked_rect . pBits ;
        dst_data_ptr += locked_rect . Pitch * d3d_y ;
        dst_data_ptr += x_offset_int * sizeof ( so_called_type_platform_render_directx_texel_data ) ;
        src_data_ptr = data_ptr ;
        src_data_ptr += width_int * y ;
        so_called_lib_std_memcpy 
            ( dst_data_ptr 
            , src_data_ptr 
            , width_int * sizeof ( so_called_type_platform_render_directx_texel_data ) 
            ) ;
    }
    so_called_lib_directx_V
        ( arg_texture_id . _texture -> UnlockRect ( 0 ) 
        ) ;
}

void shy_platform_render_directx :: enable_face_culling ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState 
            ( so_called_lib_directx_D3DRS_CULLMODE 
            , so_called_lib_directx_D3DCULL_NONE 
            ) 
        ) ;
}

void shy_platform_render_directx :: enable_depth_test ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V 
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState 
            ( so_called_lib_directx_D3DRS_ZENABLE 
            , so_called_lib_directx_D3DZB_TRUE 
            ) 
        ) ;
}

void shy_platform_render_directx :: disable_depth_test ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_ZENABLE 
            , so_called_lib_directx_D3DZB_FALSE 
            ) 
        ) ;
}

void shy_platform_render_directx :: blend_disable ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_ALPHABLENDENABLE
            , so_called_lib_directx_FALSE
            )
        ) ;
}

void shy_platform_render_directx :: blend_src_alpha_dst_one_minus_alpha ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V 
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState 
            ( so_called_lib_directx_D3DRS_ALPHABLENDENABLE 
            , so_called_lib_directx_TRUE 
            ) 
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_SRCBLEND 
            , so_called_lib_directx_D3DBLEND_SRCALPHA 
            ) 
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_DESTBLEND 
            , so_called_lib_directx_D3DBLEND_INVSRCALPHA 
            ) 
        ) ;
}

void shy_platform_render_directx :: enable_texturing ( )
{
}

void shy_platform_render_directx :: disable_texturing ( )
{
    so_called_lib_directx_HRESULT hr ;
    so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetTexture ( 0 , 0 ) 
        ) ;
}

void shy_platform_render_directx :: texture_mode_modulate ( )
{
}

void shy_platform_render_directx :: fog_disable ( )
{
	so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_V 
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGENABLE 
            , so_called_lib_directx_FALSE 
            ) 
        ) ;
}

void shy_platform_render_directx :: fog_linear 
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

	so_called_lib_directx_HRESULT hr ;
    so_called_lib_directx_D3DCOLOR color ;
	color = so_called_lib_directx_D3DCOLOR_ARGB \
        ( so_called_lib_int32_t ( a_float * so_called_lib_float ( 255 ) )
        , so_called_lib_int32_t ( r_float * so_called_lib_float ( 255 ) ) 
        , so_called_lib_int32_t ( g_float * so_called_lib_float ( 255 ) ) 
        , so_called_lib_int32_t ( b_float * so_called_lib_float ( 255 ) ) 
        ) ;

	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGENABLE
            , so_called_lib_directx_TRUE
            )
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGCOLOR 
            , color 
            ) 
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGVERTEXMODE
            , so_called_lib_directx_D3DFOG_LINEAR
            )
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGSTART 
            , * ( so_called_lib_directx_DWORD * ) ( & znear_float ) 
            ) 
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetRenderState
            ( so_called_lib_directx_D3DRS_FOGEND 
            , * ( so_called_lib_directx_DWORD * ) ( & zfar_float ) 
            ) 
        ) ;
}

void shy_platform_render_directx :: create_texture_id 
    ( so_called_type_platform_render_directx_texture_id & arg_texture_id 
    , so_called_type_platform_math_num_whole size_pow2_base 
    )
{
    so_called_lib_directx_HRESULT hr ;
    so_called_lib_std_int32_t size_pow2_base_int = 0 ;
    so_called_lib_directx_DWORD size = 0 ;

    so_called_platform_math_insider :: num_whole_value_get ( size_pow2_base_int , size_pow2_base ) ;
    arg_texture_id . _size = 1 << size_pow2_base_int ;
    size = ( so_called_lib_directx_DWORD ) arg_texture_id . _size ;

    so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> CreateTexture
            ( size
            , size
            , 0
            , 0
            , so_called_lib_directx_D3DFMT_A8R8G8B8
            , so_called_lib_directx_D3DPOOL_MANAGED
            , & arg_texture_id . _texture
            , 0
            ) 
        ) ;
}

void shy_platform_render_directx :: use_texture ( so_called_type_platform_render_directx_texture_id arg_texture_id )
{
    so_called_lib_directx_HRESULT hr ;
    so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetTexture
            ( 0 
            , arg_texture_id . _texture 
            ) 
        ) ;
}

void shy_platform_render_directx :: set_texel_color 
    ( so_called_type_platform_render_directx_texel_data & texel 
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
    texel . _r = so_called_lib_directx_BYTE ( r_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _g = so_called_lib_directx_BYTE ( g_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _b = so_called_lib_directx_BYTE ( b_float * so_called_lib_std_float ( 255 ) ) ;
    texel . _a = so_called_lib_directx_BYTE ( a_float * so_called_lib_std_float ( 255 ) ) ;
}

void shy_platform_render_directx :: clear_screen 
    ( so_called_type_platform_math_num_fract r 
    , so_called_type_platform_math_num_fract g 
    , so_called_type_platform_math_num_fract b 
    )
{
    so_called_lib_directx_HRESULT hr ;
    so_called_lib_std_float r_float = 0 ;
    so_called_lib_std_float g_float = 0 ;
    so_called_lib_std_float b_float = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( r_float , r ) ;
    so_called_platform_math_insider :: num_fract_value_get ( g_float , g ) ;
    so_called_platform_math_insider :: num_fract_value_get ( b_float , b ) ;
	so_called_lib_directx_D3DCOLOR color = so_called_lib_directx_D3DCOLOR_ARGB \
        ( 0 
        , so_called_lib_std_int32_t ( r_float * so_called_lib_std_float ( 255 ) ) 
        , so_called_lib_std_int32_t ( g_float * so_called_lib_std_float ( 255 ) ) 
        , so_called_lib_std_int32_t ( b_float * so_called_lib_std_float ( 255 ) ) 
        ) ;
	so_called_lib_directx_V
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> Clear 
            ( 0 
            , 0 
            , so_called_lib_directx_D3DCLEAR_TARGET | so_called_lib_directx_D3DCLEAR_ZBUFFER 
            , color 
            , 1
            , 0 
            ) 
        ) ;
}

void shy_platform_render_directx :: projection_frustum 
    ( so_called_type_platform_math_num_fract left 
    , so_called_type_platform_math_num_fract right 
    , so_called_type_platform_math_num_fract bottom 
    , so_called_type_platform_math_num_fract top 
    , so_called_type_platform_math_num_fract znear 
    , so_called_type_platform_math_num_fract zfar 
    )
{
    so_called_lib_std_float float_left = 0 ;
    so_called_lib_std_float float_right = 0 ;
    so_called_lib_std_float float_bottom = 0 ;
    so_called_lib_std_float float_top = 0 ;
    so_called_lib_std_float float_znear = 0 ;
    so_called_lib_std_float float_zfar = 0 ;
    so_called_platform_math_insider :: num_fract_value_get ( float_left , left ) ;
    so_called_platform_math_insider :: num_fract_value_get ( float_right , right ) ;
    so_called_platform_math_insider :: num_fract_value_get ( float_bottom , bottom ) ;
    so_called_platform_math_insider :: num_fract_value_get ( float_top , top ) ;
    so_called_platform_math_insider :: num_fract_value_get ( float_znear , znear ) ;
    so_called_platform_math_insider :: num_fract_value_get ( float_zfar , zfar ) ;

    so_called_lib_directx_HRESULT hr ;
	so_called_lib_directx_D3DXMATRIX matrix ;
	so_called_lib_directx_D3DXMatrixPerspectiveOffCenterRH 
        ( & matrix 
        , float_left
        , float_right
        , float_bottom
        , float_top
        , float_znear
        , float_zfar
        ) ;
	so_called_lib_directx_V 
        ( so_called_lib_directx_DXUTGetD3D9Device ( ) -> SetTransform 
            ( so_called_lib_directx_D3DTS_PROJECTION 
            , & matrix 
            ) 
        ) ;
}

void shy_platform_render_directx :: projection_ortho 
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
}

void shy_platform_render_directx :: create_vertex_buffer 
    ( so_called_type_platform_render_directx_vertex_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    so_called_lib_std_int32_t elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
}

void shy_platform_render_directx :: map_vertex_buffer
    ( so_called_type_platform_render_directx_vertex_buffer_mapped_data & data 
    , so_called_type_platform_render_directx_vertex_buffer_id arg_buffer_id 
    )
{
}

void shy_platform_render_directx :: unmap_vertex_buffer ( so_called_type_platform_render_directx_vertex_buffer_id arg_buffer_id )
{
}

void shy_platform_render_directx :: mapped_vertex_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_directx_vertex_data > & ptr 
    , so_called_type_platform_render_directx_vertex_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
}

void shy_platform_render_directx :: set_vertex_position 
    ( so_called_type_platform_render_directx_vertex_data & vertex 
    , so_called_type_platform_math_num_fract x 
    , so_called_type_platform_math_num_fract y 
    , so_called_type_platform_math_num_fract z 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 0 ] , x ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 1 ] , y ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _position [ 2 ] , z ) ;
}

void shy_platform_render_directx :: set_vertex_tex_coord 
    ( so_called_type_platform_render_directx_vertex_data & vertex 
    , so_called_type_platform_math_num_fract u 
    , so_called_type_platform_math_num_fract v 
    )
{
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 0 ] , u ) ;
    so_called_platform_math_insider :: num_fract_value_get ( vertex . _tex_coord [ 1 ] , v ) ;
}

void shy_platform_render_directx :: set_vertex_color 
    ( so_called_type_platform_render_directx_vertex_data & vertex 
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
}

void shy_platform_render_directx :: create_index_buffer 
    ( so_called_type_platform_render_directx_index_buffer_id & arg_buffer_id 
    , so_called_type_platform_math_num_whole elements 
    )
{
    so_called_lib_std_int32_t elements_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( elements_int , elements ) ;
}

void shy_platform_render_directx :: map_index_buffer
    ( so_called_type_platform_render_directx_index_buffer_mapped_data & data 
    , so_called_type_platform_render_directx_index_buffer_id arg_buffer_id 
    )
{
}

void shy_platform_render_directx :: unmap_index_buffer ( so_called_type_platform_render_directx_index_buffer_id arg_buffer_id )
{
}

void shy_platform_render_directx :: mapped_index_buffer_element
    ( so_called_type_platform_pointer_data < so_called_type_platform_render_directx_index_data > & ptr 
    , so_called_type_platform_render_directx_index_buffer_mapped_data data
    , so_called_type_platform_math_num_whole index
    )
{
    so_called_type_platform_render_directx_index_data * mapped_indices = ( so_called_type_platform_render_directx_index_data * ) data . _data ;
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
    so_called_platform_pointer :: bind ( ptr , mapped_indices [ index_int ] ) ;
}

void shy_platform_render_directx :: set_index_value ( so_called_type_platform_render_directx_index_data & data , so_called_type_platform_math_num_whole index )
{
    so_called_lib_std_int32_t index_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( index_int , index ) ;
}

void shy_platform_render_directx :: matrix_identity ( )
{
}

void shy_platform_render_directx :: matrix_load ( const so_called_type_platform_matrix_data & matrix )
{
    const so_called_lib_std_float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
}

void shy_platform_render_directx :: matrix_mult ( const so_called_type_platform_matrix_data & matrix )
{
    const so_called_lib_std_float * elements = 0 ;
    so_called_platform_matrix_insider :: elements_ptr ( elements , matrix ) ;
}

void shy_platform_render_directx :: matrix_push ( )
{
}

void shy_platform_render_directx :: matrix_pop ( )
{
}

void shy_platform_render_directx :: draw_triangle_strip 
    ( so_called_type_platform_render_directx_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_directx_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    so_called_lib_std_int32_t indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
}

void shy_platform_render_directx :: draw_triangle_fan
    ( so_called_type_platform_render_directx_vertex_buffer_id vertices_buffer 
    , so_called_type_platform_render_directx_index_buffer_id indices_buffer 
    , so_called_type_platform_math_num_whole indices_count 
    )
{
    so_called_lib_std_int32_t indices_count_int = 0 ;
    so_called_platform_math_insider :: num_whole_value_get ( indices_count_int , indices_count ) ;
}

void shy_platform_render_directx :: get_aspect_width ( so_called_type_platform_math_num_fract & result )
{
    so_called_lib_std_float float_aspect_width = 0 ;
    so_called_platform_render_directx_insider :: get_aspect_width ( float_aspect_width ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , float_aspect_width ) ;
}

void shy_platform_render_directx :: get_aspect_height ( so_called_type_platform_math_num_fract & result )
{
    so_called_lib_std_float float_aspect_height = 0 ;
    so_called_platform_render_directx_insider :: get_aspect_height ( float_aspect_height ) ;
    so_called_platform_math_insider :: num_fract_value_set ( result , float_aspect_height ) ;
}

void shy_platform_render_directx :: get_frame_loss ( so_called_type_platform_math_num_whole & result )
{
    so_called_lib_std_bool bool_frame_loss = so_called_lib_std_false ;
    so_called_platform_render_directx_insider :: get_frame_loss ( bool_frame_loss ) ;
    so_called_platform_math_insider :: num_whole_value_set ( result , bool_frame_loss ) ;
}

void shy_platform_render_directx :: delete_vertex_buffer ( so_called_type_platform_render_directx_vertex_buffer_id & arg_buffer_id )
{
}

void shy_platform_render_directx :: delete_index_buffer ( so_called_type_platform_render_directx_index_buffer_id & arg_buffer_id )
{
}

void shy_platform_render_directx :: delete_texture_id ( so_called_type_platform_render_directx_texture_id & arg_texture_id )
{
}
