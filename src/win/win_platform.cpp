#include "DXUT.h"
#include "win_platform.hpp"

const shy_platform_math_consts < shy_win_platform_insider > shy_win_platform :: math_consts ;

float shy_win_platform_insider :: aspect_width = 1.33f ;
float shy_win_platform_insider :: aspect_height = 1 ;

LPD3DXMATRIXSTACK shy_win_platform_insider :: matrix_stack = 0 ;

void shy_win_platform_insider :: init ( )
{
	HRESULT hr ;
	V ( D3DXCreateMatrixStack ( 0 , & matrix_stack ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_LIGHTING , FALSE ) ) ;
}

void shy_win_platform_insider :: done ( )
{
    HRESULT hr ;
    V ( matrix_stack -> Release ( ) ) ;
}

D3DXMATRIX shy_win_platform_insider :: convert_from_opengl ( D3DXMATRIX ogl_matrix )
{
	D3DXMATRIX d3d_matrix ( ogl_matrix ) ;
	d3d_matrix . _31 = - d3d_matrix . _31 ;
	d3d_matrix . _32 = - d3d_matrix . _32 ;
	d3d_matrix . _33 = - d3d_matrix . _33 ;
	d3d_matrix . _34 = - d3d_matrix . _34 ;
	return d3d_matrix ;
}
