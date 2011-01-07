#ifndef _shy_type_macosx_platform_render_vertex_data_included
#define _shy_type_macosx_platform_render_vertex_data_included

class shy_type_macosx_platform_render_vertex_data
{
    friend class shy_macosx_platform_render ;
public :
    shy_type_macosx_platform_render_vertex_data ( ) ;
private :
    GLfloat _position [ 3 ] ;
    GLfloat _tex_coord [ 2 ] ;
    GLubyte _color [ 4 ] ;
} ;

#endif
