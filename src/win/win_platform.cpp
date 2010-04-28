#include "DXUT.h"
#include "win_platform.hpp"

shy_win_platform :: float_32 shy_win_platform :: _aspect_width = 1 ;
shy_win_platform :: float_32 shy_win_platform :: _aspect_height = 1 ;

LPD3DXMATRIXSTACK shy_win_platform :: _matrix_stack = 0 ;

void shy_win_platform :: _init ( )
{
	HRESULT hr ;
	V ( D3DXCreateMatrixStack ( 0 , & _matrix_stack ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_LIGHTING , FALSE ) ) ;
}

void shy_win_platform :: _done ( )
{
}

D3DXMATRIX shy_win_platform :: _convert_from_opengl ( D3DXMATRIX ogl_matrix )
{
	D3DXMATRIX d3d_matrix ( ogl_matrix ) ;
	d3d_matrix . _31 = - d3d_matrix . _31 ;
	d3d_matrix . _32 = - d3d_matrix . _32 ;
	d3d_matrix . _33 = - d3d_matrix . _33 ;
	d3d_matrix . _34 = - d3d_matrix . _34 ;
	return d3d_matrix ;
}
