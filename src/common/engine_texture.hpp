template < typename mediator >
class shy_engine_texture
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: platform_conditions platform_conditions ;
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: platform_static_array platform_static_array ;
    
    static const_int_32 _max_textures = 5 ;
    static const_int_32 _texture_size_pow2_base = 8 ;
    static const_int_32 _texture_size = 1 << _texture_size_pow2_base ;
    
public :
    class texture_id
    {
        friend class shy_engine_texture ;
    private :
        num_whole _texture_id ;
    } ;
private :
    class _texture_data
    {
    public :
        typename platform_static_array :: template static_array < texel_data , _texture_size * _texture_size > texels ;
        render_texture_id render_id ;
    } ;
public :
    shy_engine_texture ( ) ;
    void set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator ) ;
    void texture_create ( texture_id & result ) ;
    void receive ( typename messages :: texture_create_request msg ) ;
    void receive ( typename messages :: texture_finalize msg ) ;
    void receive ( typename messages :: texture_load_from_resource msg ) ;
    void receive ( typename messages :: texture_select msg ) ;
    void receive ( typename messages :: texture_unselect msg ) ;
    void receive ( typename messages :: texture_set_texels_rect msg ) ;
    void receive ( typename messages :: texture_set_texel msg ) ;
    void receive ( typename messages :: texture_set_texel_rgba msg ) ;
    void texture_width ( num_whole & result ) ;
    void texture_height ( num_whole & result ) ;
private :
    typename platform_pointer :: template pointer < mediator > _mediator ;
    typename platform_static_array :: template static_array < _texture_data , _max_textures > _textures_datas ;
    num_whole _next_texture_id ;
} ;

template < typename mediator >
shy_engine_texture < mediator > :: shy_engine_texture ( )
{
    platform_math :: make_num_whole ( _next_texture_id , 0 ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: set_mediator ( typename platform_pointer :: template pointer < mediator > arg_mediator )
{
    _mediator = arg_mediator ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_create ( texture_id & result )
{
    result . _texture_id = _next_texture_id ;
    platform_math :: inc_whole ( _next_texture_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_create_request msg )
{
    typename messages :: texture_create_reply texture_create_reply_msg ;
    texture_create_reply_msg . texture . _texture_id = _next_texture_id ;
    platform_math :: inc_whole ( _next_texture_id ) ;
    _mediator . get ( ) . send ( texture_create_reply_msg ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_finalize msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform_render :: create_texture_id ( texture . render_id ) ;
    platform_render :: load_texture_data ( texture . render_id , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_load_from_resource msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform_render :: load_texture_resource ( msg . resource , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_select msg )
{
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_render :: enable_texturing ( ) ;
    platform_render :: use_texture ( texture . render_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_unselect msg )
{
    platform_render :: disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_set_texel msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    platform_math :: mul_wholes ( texel_offset , num_texture_size , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    platform_static_array :: element ( texture . texels , texel_offset ) = msg . texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_set_texel_rgba msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    platform_math :: mul_wholes ( texel_offset , num_texture_size , msg . y ) ;
    platform_math :: add_to_whole ( texel_offset , msg . x ) ;
    texel_data & texel = platform_static_array :: element ( texture . texels , texel_offset ) ;
    platform_render :: set_texel_color ( texel , msg . r , msg . g , msg . b , msg . a ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_set_texels_rect msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform_static_array :: element ( _textures_datas , msg . texture . _texture_id ) ;
    platform_math :: make_num_whole ( num_texture_size , _texture_size ) ;
    for ( num_whole y = msg . bottom
        ; platform_conditions :: whole_less_or_equal_to_whole ( y , msg . top )
        ; platform_math :: inc_whole ( y )
        )
    {
        for ( num_whole x = msg . left
            ; platform_conditions :: whole_less_or_equal_to_whole ( x , msg . right )
            ; platform_math :: inc_whole ( x )
            )
        {
            platform_math :: mul_wholes ( texel_offset , num_texture_size , y ) ;
            platform_math :: add_to_whole ( texel_offset , x ) ;
            platform_static_array :: element ( texture . texels , texel_offset ) = msg . texel ;
        }
    }
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_width ( num_whole & result )
{
    platform_math :: make_num_whole ( result , _texture_size ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_height ( num_whole & result )
{
    platform_math :: make_num_whole ( result , _texture_size ) ;
}
