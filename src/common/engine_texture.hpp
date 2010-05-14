template < typename mediator >
class shy_engine_texture
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    
    static const int_32 MAX_TEXTURES = 5 ;
    static const int_32 TEXTURE_SIZE_POW2_BASE = 9 ;
    static const int_32 TEXTURE_SIZE = 1 << TEXTURE_SIZE_POW2_BASE ;
    
public :
    class texture_id
    {
        friend class shy_engine_texture ;
    private :
        int_32 _texture_id ;
    } ;
private :
    class _texture_data
    {
    public :
        texel_data texels [ TEXTURE_SIZE * TEXTURE_SIZE ] ;
        render_texture_id render_id ;
    } ;
public :
    shy_engine_texture ( ) ;
    texture_id texture_create ( ) ;
    void texture_finalize ( texture_id arg_texture_id ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_unselect ( ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    int_32 texture_width ( ) ;
    int_32 texture_height ( ) ;
private :
    int_32 _next_texture_id ;
    _texture_data _textures_datas [ MAX_TEXTURES ] ;
} ;

template < typename mediator >
shy_engine_texture < mediator > :: shy_engine_texture ( )
: _next_texture_id ( 0 )
{
}

template < typename mediator >
typename shy_engine_texture < mediator > :: texture_id
shy_engine_texture < mediator > :: texture_create ( )
{
    texture_id new_id ;
    new_id . _texture_id = _next_texture_id ;
    _next_texture_id ++ ;
    return new_id ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_finalize ( texture_id arg_texture_id )
{
    _texture_data & tex_data = _textures_datas [ arg_texture_id . _texture_id ] ;
    platform :: render_create_texture_id ( tex_data . render_id ) ;
    platform :: render_load_texture_data ( tex_data . render_id , TEXTURE_SIZE_POW2_BASE , tex_data . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id )
{
    _texture_data & tex_data = _textures_datas [ arg_texture_id . _texture_id ] ;
    platform :: render_load_texture_resource ( arg_resource_id , TEXTURE_SIZE_POW2_BASE , tex_data . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_select ( texture_id arg_texture_id )
{
    platform :: render_enable_texturing ( ) ;
    platform :: render_use_texture ( _textures_datas [ arg_texture_id . _texture_id ] . render_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_unselect ( )
{
    platform :: render_disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel )
{
    _textures_datas [ arg_texture_id . _texture_id ] . texels [ x + TEXTURE_SIZE * y ] = texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a )
{
    platform :: render_set_texel_color ( _textures_datas [ arg_texture_id . _texture_id ] . texels [ x + TEXTURE_SIZE * y ] , r , g , b , a ) ;
}

template < typename mediator >
typename shy_engine_texture < mediator > :: int_32
shy_engine_texture < mediator > :: texture_width ( )
{
    return TEXTURE_SIZE ;
}

template < typename mediator >
typename shy_engine_texture < mediator > :: int_32 
shy_engine_texture < mediator > :: texture_height ( )
{
    return TEXTURE_SIZE ;
}
