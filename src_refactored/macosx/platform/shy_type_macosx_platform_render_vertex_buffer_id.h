#ifndef _shy_type_macosx_platform_render_vertex_buffer_id_included
#define _shy_type_macosx_platform_render_vertex_buffer_id_included

#include <OpenGL/gl.h>

class shy_type_macosx_platform_render_vertex_buffer_id
{
    friend class shy_macosx_platform_render ;
public :
    shy_type_macosx_platform_render_vertex_buffer_id ( ) ;
private :
    GLuint _buffer_id ;
} ;

#endif
