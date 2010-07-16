template < typename platform_insider >
class shy_iphone_platform_render_insider
{
public :
    shy_iphone_platform_render_insider ( ) ;
    void set_platform_insider ( platform_insider * arg_platform_insider ) ;
    void set_texture_loader ( shy_iphone_texture_loader * texture_loader ) ;
    void set_aspect_width ( float width ) ;
    void set_aspect_height ( float height ) ;
private :
    platform_insider * _platform_insider ;
} ;

template < typename platform_insider >
shy_iphone_platform_render_insider < platform_insider > :: shy_iphone_platform_render_insider ( )
: _platform_insider ( 0 )
{
}

template < typename platform_insider >
void shy_iphone_platform_render_insider < platform_insider > :: set_platform_insider ( platform_insider * arg_platform_insider )
{
    _platform_insider = arg_platform_insider ;
}

template < typename platform_insider >
void shy_iphone_platform_render_insider < platform_insider > :: set_texture_loader ( shy_iphone_texture_loader * texture_loader )
{
    _platform_insider -> render . _texture_loader = texture_loader ;
}

template < typename platform_insider >
void shy_iphone_platform_render_insider < platform_insider > :: set_aspect_width ( float width )
{
    _platform_insider -> render . _aspect_width = width ;
}

template < typename platform_insider >
void shy_iphone_platform_render_insider < platform_insider > :: set_aspect_height ( float height )
{
    _platform_insider -> render . _aspect_height = height ;
}
