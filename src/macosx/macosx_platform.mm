#include "macosx_platform.hpp"

shy_macosx_platform :: vertex_data shy_macosx_platform :: _reference_vertex ;
void * shy_macosx_platform :: _vertex_position_offset = 0 ;
/*reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _position ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;
*/
void * shy_macosx_platform :: _vertex_tex_coord_offset = 0 ;
/*reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _tex_coord ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;
*/
void * shy_macosx_platform :: _vertex_color_offset = 0 ;
/*reinterpret_cast < void * >
    ( reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex . _color ) 
    - reinterpret_cast < char * > ( & shy_macosx_platform :: _reference_vertex )
    ) ;
*/
    
//shy_macosx_sound_loader * shy_macosx_platform :: _sound_loader = 0 ;

//shy_macosx_platform :: int_32 shy_macosx_platform :: _touch_occured = false ;
//shy_macosx_platform :: float_32 shy_macosx_platform :: _touch_x = 0 ;
//shy_macosx_platform :: float_32 shy_macosx_platform :: _touch_y = 0 ;
