class shy_platform_render_opengl_vertex_data_type
{
    friend class shy_platform_render_opengl ;
public :
    shy_platform_render_opengl_vertex_data_type ( ) ;
private :
    so_called_lib_opengl_GLfloat _position [ 3 ] ;
    so_called_lib_opengl_GLfloat _tex_coord [ 2 ] ;
    so_called_lib_opengl_GLubyte _color [ 4 ] ;
} ;
