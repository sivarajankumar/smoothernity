#include "macosx_platform.hpp"

shy_macosx_platform :: platform_render :: vertex_data shy_macosx_platform_utility :: _reference_vertex ;
void * shy_macosx_platform_utility :: _vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex )
    ) ;

void * shy_macosx_platform_utility :: _vertex_tex_coord_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex )
    ) ;
void * shy_macosx_platform_utility :: _vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_utility :: _reference_vertex )
    ) ;
    
shy_macosx_sound_loader * shy_macosx_platform_utility :: _sound_loader = 0 ;
shy_macosx_texture_loader * shy_macosx_platform_utility :: _texture_loader = 0 ;

float shy_macosx_platform_utility :: _aspect_width = 1.0f ;
float shy_macosx_platform_utility :: _aspect_height = 1.0f ;

int shy_macosx_platform_utility :: _mouse_left_button_down = false ;
float shy_macosx_platform_utility :: _mouse_x = 0 ;
float shy_macosx_platform_utility :: _mouse_y = 0 ;

const shy_platform_math_consts < shy_macosx_platform > shy_macosx_platform :: math_consts ;
