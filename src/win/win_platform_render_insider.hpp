template < typename platform_insider >
class shy_win_platform_render_insider
{
public :
    shy_win_platform_render_insider ( ) ;
    ~ shy_win_platform_render_insider ( ) ;

	static void convert_from_opengl ( D3DXMATRIX & d3d_matrix , D3DXMATRIX ogl_matrix ) ;
    void set_platform_insider ( platform_insider & arg_platform_insider ) ;

public :
	float aspect_width ;
	float aspect_height ;
	LPD3DXMATRIXSTACK matrix_stack ;
} ;

template < typename platform_insider >
shy_win_platform_render_insider < platform_insider > :: shy_win_platform_render_insider ( )
: aspect_width ( 1.33f )
, aspect_height ( 1.0f )
, matrix_stack ( 0 )
{
	HRESULT hr ;
	V ( D3DXCreateMatrixStack ( 0 , & matrix_stack ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_LIGHTING , FALSE ) ) ;
    V ( DXUTGetD3D9Device ( ) -> SetSamplerState ( 0 , D3DSAMP_MINFILTER , D3DTEXF_POINT ) ) ;
    V ( DXUTGetD3D9Device ( ) -> SetSamplerState ( 0 , D3DSAMP_MAGFILTER , D3DTEXF_LINEAR ) ) ;
    V ( DXUTGetD3D9Device ( ) -> SetSamplerState ( 0 , D3DSAMP_MIPFILTER , D3DTEXF_NONE ) ) ;
}

template < typename platform_insider >
shy_win_platform_render_insider < platform_insider > :: ~ shy_win_platform_render_insider ( )
{
    HRESULT hr ;
    V ( matrix_stack -> Release ( ) ) ;
}

template < typename platform_insider >
void shy_win_platform_render_insider < platform_insider > :: set_platform_insider ( platform_insider & arg_platform_insider )
{
    arg_platform_insider . render . _platform_insider = & arg_platform_insider ;
}

template < typename platform_insider >
void shy_win_platform_render_insider < platform_insider > :: convert_from_opengl ( D3DXMATRIX & d3d_matrix , D3DXMATRIX ogl_matrix )
{
	d3d_matrix = ogl_matrix ;
	d3d_matrix . _31 = - d3d_matrix . _31 ;
	d3d_matrix . _32 = - d3d_matrix . _32 ;
	d3d_matrix . _33 = - d3d_matrix . _33 ;
	d3d_matrix . _34 = - d3d_matrix . _34 ;
}
