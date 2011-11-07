class shy_platform_render_directx_texture_id_type
{
    friend class shy_platform_render_directx ;
    friend class shy_platform_render_directx_insider ;
public :
    shy_platform_render_directx_texture_id_type ( ) ;
private :
    so_called_lib_directx_IDirect3DTexture9 * _texture ; 
    so_called_lib_std_int32_t _width ;
    so_called_lib_std_int32_t _height ;
} ;
