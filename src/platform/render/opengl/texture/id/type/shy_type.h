class shy_platform_render_opengl_texture_id_type
{
    friend class shy_platform_render_opengl ;
    friend class shy_platform_render_opengl_insider ;
public :
    shy_platform_render_opengl_texture_id_type ( ) ;
private :
    so_called_lib_opengl_GLuint _texture_id ;
    so_called_lib_std_int32_t _width ;
    so_called_lib_std_int32_t _height ;
} ;
