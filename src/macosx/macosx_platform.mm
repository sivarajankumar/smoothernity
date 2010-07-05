#include "macosx_platform.hpp"

shy_macosx_platform :: platform_render :: vertex_data shy_macosx_platform_insider :: reference_vertex ;
void * shy_macosx_platform_insider :: vertex_position_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex )
    ) ;

void * shy_macosx_platform_insider :: vertex_tex_coord_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex )
    ) ;
void * shy_macosx_platform_insider :: vertex_color_offset = reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform_insider :: reference_vertex )
    ) ;
    
shy_macosx_sound_loader * shy_macosx_platform_insider :: sound_loader = 0 ;
shy_macosx_texture_loader * shy_macosx_platform_insider :: texture_loader = 0 ;

float shy_macosx_platform_insider :: aspect_width = 1.0f ;
float shy_macosx_platform_insider :: aspect_height = 1.0f ;

const shy_platform_math_consts < shy_macosx_platform_insider > shy_macosx_platform :: math_consts ;

shy_macosx_platform_insider :: shy_macosx_platform_insider ( )
{
    mouse_insider . set_platform_insider ( this ) ;
}

void shy_macosx_platform_insider :: register_platform_modules ( shy_macosx_platform & platform )
{
    platform . mouse . set ( mouse ) ;
}
