#include "macosx_platform.hpp"

shy_macosx_platform :: vertex_data shy_macosx_platform :: _reference_vertex ;
void * shy_macosx_platform :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;

void * shy_macosx_platform :: _vertex_tex_coord_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;
void * shy_macosx_platform :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;
    
shy_macosx_sound_loader * shy_macosx_platform :: _sound_loader = 0 ;
shy_macosx_texture_loader * shy_macosx_platform :: _texture_loader = 0 ;

shy_macosx_platform :: float_32 shy_macosx_platform :: _aspect_width = 1.0f ;
shy_macosx_platform :: float_32 shy_macosx_platform :: _aspect_height = 1.0f ;

shy_macosx_platform :: int_32 shy_macosx_platform :: _mouse_left_button_down = false ;
shy_macosx_platform :: float_32 shy_macosx_platform :: _mouse_x = 0 ;
shy_macosx_platform :: float_32 shy_macosx_platform :: _mouse_y = 0 ;
