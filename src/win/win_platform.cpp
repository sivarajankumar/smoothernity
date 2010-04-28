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
