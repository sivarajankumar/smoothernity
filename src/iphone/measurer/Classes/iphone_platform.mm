#include "iphone_platform.hpp"

shy_iphone_platform :: vertex_data shy_iphone_platform :: _reference_vertex ;
void * shy_iphone_platform :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex )
    ) ;
void * shy_iphone_platform :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_iphone_platform :: _reference_vertex )
    ) ;
    
shy_iphone_sound_loader * shy_iphone_platform :: _sound_loader = 0 ;

shy_iphone_platform :: int_32 shy_iphone_platform :: _touch_occured = false ;
shy_iphone_platform :: float_32 shy_iphone_platform :: _touch_x = 0 ;
shy_iphone_platform :: float_32 shy_iphone_platform :: _touch_y = 0 ;
