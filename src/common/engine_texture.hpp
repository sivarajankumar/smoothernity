template < typename mediator >
class shy_engine_texture
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    
    static const int_32 _max_textures = 5 ;
    static const int_32 _texture_size_pow2_base = 8 ;
    static const int_32 _texture_size = 1 << _texture_size_pow2_base ;
    
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
        texel_data texels [ _texture_size * _texture_size ] ;
        render_texture_id render_id ;
    } ;
public :
    shy_engine_texture ( ) ;
    void texture_create ( texture_id & result ) ;
    void texture_finalize ( texture_id arg_texture_id ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_unselect ( ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a ) ;
    void texture_width ( int_32 & result ) ;
    void texture_height ( int_32 & result ) ;
private :
    int_32 _next_texture_id ;
    _texture_data _textures_datas [ _max_textures ] ;
} ;

template < typename mediator >
shy_engine_texture < mediator > :: shy_engine_texture ( )
: _next_texture_id ( 0 )
{
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_create ( texture_id & result )
{
    result . _texture_id = _next_texture_id ;
    _next_texture_id ++ ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_finalize ( texture_id arg_texture_id )
{
    _texture_data & tex_data = _textures_datas [ arg_texture_id . _texture_id ] ;
    platform :: render_create_texture_id ( tex_data . render_id ) ;
    platform :: render_load_texture_data ( tex_data . render_id , _texture_size_pow2_base , tex_data . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id )
{
    _texture_data & tex_data = _textures_datas [ arg_texture_id . _texture_id ] ;
    platform :: render_load_texture_resource ( arg_resource_id , _texture_size_pow2_base , tex_data . texels ) ;
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
    _textures_datas [ arg_texture_id . _texture_id ] . texels [ x + _texture_size * y ] = texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , int_32 x , int_32 y , int_32 r , int_32 g , int_32 b , int_32 a )
{
    num_whole num_r ;
    num_whole num_g ;
    num_whole num_b ;
    num_whole num_a ;
    platform :: math_make_num_whole ( num_r , r ) ;
    platform :: math_make_num_whole ( num_g , g ) ;
    platform :: math_make_num_whole ( num_b , b ) ;
    platform :: math_make_num_whole ( num_a , a ) ;
    platform :: render_set_texel_color 
        ( _textures_datas [ arg_texture_id . _texture_id ] . texels [ x + _texture_size * y ] 
        , num_r 
        , num_g 
        , num_b 
        , num_a 
        ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_width ( int_32 & result )
{
    result = _texture_size ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_height ( int_32 & result )
{
    result = _texture_size ;
}
