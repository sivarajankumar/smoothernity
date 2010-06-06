#include "DXUT.h"
#include "win_platform.hpp"

float shy_win_platform :: _aspect_width = 1.33f ;
float shy_win_platform :: _aspect_height = 1 ;

LPD3DXMATRIXSTACK shy_win_platform :: _matrix_stack = 0 ;

void shy_win_platform :: _init ( )
{
	HRESULT hr ;
	V ( D3DXCreateMatrixStack ( 0 , & _matrix_stack ) ) ;
	V ( DXUTGetD3D9Device ( ) -> SetRenderState ( D3DRS_LIGHTING , FALSE ) ) ;
}

void shy_win_platform :: _done ( )
{
    HRESULT hr ;
    V ( _matrix_stack -> Release ( ) ) ;
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

const shy_win_platform :: num_fract shy_win_platform :: fract_pi ( 3.141592f ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_2pi ( 6.283184f ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_0 ( 0 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_1 ( 1 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_2 ( 2 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_3 ( 3 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_4 ( 4 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_5 ( 5 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_6 ( 6 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_7 ( 7 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_8 ( 8 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_9 ( 9 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_0 ( 0 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_1 ( 1 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_2 ( 2 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_3 ( 3 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_4 ( 4 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_5 ( 5 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_6 ( 6 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_7 ( 7 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_8 ( 8 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_9 ( 9 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_1 ( - 1 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_2 ( - 2 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_3 ( - 3 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_4 ( - 4 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_5 ( - 5 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_6 ( - 6 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_7 ( - 7 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_8 ( - 8 ) ;
const shy_win_platform :: num_fract shy_win_platform :: fract_minus_9 ( - 9 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_1 ( - 1 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_2 ( - 2 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_3 ( - 3 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_4 ( - 4 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_5 ( - 5 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_6 ( - 6 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_7 ( - 7 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_8 ( - 8 ) ;
const shy_win_platform :: num_whole shy_win_platform :: whole_minus_9 ( - 9 ) ;

shy_win_platform :: num_whole :: num_whole ( )
: _value ( shy_win_platform_utility :: _uninitialized_value )
{
}

shy_win_platform :: num_whole :: num_whole ( int arg_value )
: _value ( arg_value )
{
}

shy_win_platform :: num_fract :: num_fract ( )
: _value ( float ( shy_win_platform_utility :: _uninitialized_value ) )
{
}

shy_win_platform :: num_fract :: num_fract ( float arg_value )
: _value ( arg_value )
{
}

shy_win_platform :: matrix_data :: matrix_data ( )
{
    for ( int i = 0 ; i < 16 ; i ++ )
        _elements [ i ] = shy_win_platform_utility :: _uninitialized_value ;
}
    
shy_win_platform :: vector_data :: vector_data ( )
: _x ( float ( shy_win_platform_utility :: _uninitialized_value ) )
, _y ( float ( shy_win_platform_utility :: _uninitialized_value ) )
, _z ( float ( shy_win_platform_utility :: _uninitialized_value ) )
{
}
    
shy_win_platform :: render_index_buffer_id :: render_index_buffer_id ( )
: _buffer ( reinterpret_cast < IDirect3DIndexBuffer9 * > ( shy_win_platform_utility :: _uninitialized_value ) )
{
}
    
shy_win_platform :: render_vertex_buffer_id :: render_vertex_buffer_id ( )
: _buffer ( reinterpret_cast < IDirect3DVertexBuffer9 * > ( shy_win_platform_utility :: _uninitialized_value ) )
{
}
    
shy_win_platform :: render_texture_id :: render_texture_id ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}

shy_win_platform :: texture_resource_id :: texture_resource_id ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
	
shy_win_platform :: texel_data :: texel_data ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: vertex_data :: vertex_data ( )
: _x ( FLOAT ( shy_win_platform_utility :: _uninitialized_value ) )
, _y ( FLOAT ( shy_win_platform_utility :: _uninitialized_value ) )
, _z ( FLOAT ( shy_win_platform_utility :: _uninitialized_value ) )
, _color ( DWORD ( shy_win_platform_utility :: _uninitialized_value ) )
, _u ( FLOAT ( shy_win_platform_utility :: _uninitialized_value ) )
, _v ( FLOAT ( shy_win_platform_utility :: _uninitialized_value ) )
{
}
    
shy_win_platform :: index_data :: index_data ( )
: _index ( UINT ( shy_win_platform_utility :: _uninitialized_value ) )
{
}

shy_win_platform :: time_data :: time_data ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: mono_sound_sample :: mono_sound_sample ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: stereo_sound_sample :: stereo_sound_sample ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: sound_buffer_id :: sound_buffer_id ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: sound_source_id :: sound_source_id ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
    
shy_win_platform :: stereo_sound_resource_id :: stereo_sound_resource_id ( )
: _dummy ( shy_win_platform_utility :: _uninitialized_value )
{
}
