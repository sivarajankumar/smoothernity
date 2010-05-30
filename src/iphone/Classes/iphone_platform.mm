#include "iphone_platform.hpp"

shy_iphone_platform :: vertex_data shy_iphone_platform_utility :: _reference_vertex ;
void * shy_iphone_platform_utility :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex )
    ) ;

void * shy_iphone_platform_utility :: _vertex_tex_coord_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex )
    ) ;
void * shy_iphone_platform_utility :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform_utility :: _reference_vertex )
    ) ;
    
shy_iphone_sound_loader * shy_iphone_platform_utility :: _sound_loader = 0 ;
shy_iphone_texture_loader * shy_iphone_platform_utility :: _texture_loader = 0 ;

float shy_iphone_platform_utility :: _aspect_width = 1 ;
float shy_iphone_platform_utility :: _aspect_height = 1.5f ;

int shy_iphone_platform_utility :: _touch_occured = false ;
float shy_iphone_platform_utility :: _touch_x = 0 ;
float shy_iphone_platform_utility :: _touch_y = 0 ;

const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_pi ( 3.141592f ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_2pi ( 6.283184f ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_0 ( 0 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_1 ( 1 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_2 ( 2 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_3 ( 3 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_4 ( 4 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_5 ( 5 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_6 ( 6 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_7 ( 7 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_8 ( 8 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_9 ( 9 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_0 ( 0 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_1 ( 1 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_2 ( 2 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_3 ( 3 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_4 ( 4 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_5 ( 5 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_6 ( 6 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_7 ( 7 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_8 ( 8 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_9 ( 9 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_1 ( - 1 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_2 ( - 2 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_3 ( - 3 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_4 ( - 4 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_5 ( - 5 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_6 ( - 6 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_7 ( - 7 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_8 ( - 8 ) ;
const shy_iphone_platform :: num_fract shy_iphone_platform :: fract_minus_9 ( - 9 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_1 ( - 1 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_2 ( - 2 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_3 ( - 3 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_4 ( - 4 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_5 ( - 5 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_6 ( - 6 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_7 ( - 7 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_8 ( - 8 ) ;
const shy_iphone_platform :: num_whole shy_iphone_platform :: whole_minus_9 ( - 9 ) ;

shy_iphone_platform :: num_whole :: num_whole ( )
: _value ( shy_iphone_platform_utility :: _uninitialized_value )
{
}

shy_iphone_platform :: num_whole :: num_whole ( int arg_value )
: _value ( arg_value )
{
}

shy_iphone_platform :: num_fract :: num_fract ( )
: _value ( shy_iphone_platform_utility :: _uninitialized_value )
{
}

shy_iphone_platform :: num_fract :: num_fract ( float arg_value )
: _value ( arg_value )
{
}

shy_iphone_platform :: matrix_data :: matrix_data ( )
{
    for ( int i = 0 ; i < 16 ; i ++ )
        _elements [ i ] = shy_iphone_platform_utility :: _uninitialized_value ;
}
    
shy_iphone_platform :: vector_data :: vector_data ( )
: _x ( shy_iphone_platform_utility :: _uninitialized_value )
, _y ( shy_iphone_platform_utility :: _uninitialized_value )
, _z ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: render_index_buffer_id :: render_index_buffer_id ( )
: _buffer_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: render_vertex_buffer_id :: render_vertex_buffer_id ( )
: _buffer_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: render_texture_id :: render_texture_id ( )
: _texture_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}

shy_iphone_platform :: texture_resource_id :: texture_resource_id ( )
: _resource_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
	
shy_iphone_platform :: texel_data :: texel_data ( )
{
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) shy_iphone_platform_utility :: _uninitialized_value ;
}
    
shy_iphone_platform :: vertex_data :: vertex_data ( )
{
    for ( int i = 0 ; i < 3 ; i ++ )
        _position [ i ] = shy_iphone_platform_utility :: _uninitialized_value ;
    for ( int i = 0 ; i < 2 ; i ++ )
        _tex_coord [ i ] = shy_iphone_platform_utility :: _uninitialized_value ;
    for ( int i = 0 ; i < 4 ; i ++ )
        _color [ i ] = ( GLubyte ) shy_iphone_platform_utility :: _uninitialized_value ;
}
    
shy_iphone_platform :: index_data :: index_data ( )
: _index ( ( GLushort ) shy_iphone_platform_utility :: _uninitialized_value )
{
}

shy_iphone_platform :: time_data :: time_data ( )
: _time ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: mono_sound_sample :: mono_sound_sample ( )
: _value ( ( GLubyte ) shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: stereo_sound_sample :: stereo_sound_sample ( )
: _left_channel_value ( ( GLushort ) shy_iphone_platform_utility :: _uninitialized_value )
, _right_channel_value ( ( GLushort ) shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: sound_buffer_id :: sound_buffer_id ( )
: _buffer_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: sound_source_id :: sound_source_id ( )
: _source_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
    
shy_iphone_platform :: stereo_sound_resource_id :: stereo_sound_resource_id ( )
: _resource_id ( shy_iphone_platform_utility :: _uninitialized_value )
{
}
