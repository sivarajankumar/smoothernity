template < typename mediator >
class shy_engine_texture
{
    typedef typename mediator :: messages messages ;
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: num_fract num_fract ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    
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
        typename platform :: template static_array < texel_data , _texture_size * _texture_size > texels ;
        render_texture_id render_id ;
    } ;
public :
    shy_engine_texture ( ) ;
    void texture_create ( texture_id & result ) ;
    void receive ( typename messages :: texture_finalize msg ) ;
    void receive ( typename messages :: texture_load_from_resource msg ) ;
    void receive ( typename messages :: texture_select msg ) ;
    void receive ( typename messages :: texture_unselect msg ) ;
    void receive ( typename messages :: texture_set_texels_rect msg ) ;
    void receive ( typename messages :: texture_set_texel msg ) ;
    void texture_set_texel ( texture_id arg_texture_id , num_whole x , num_whole y , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    void texture_width ( num_whole & result ) ;
    void texture_height ( num_whole & result ) ;
private :
    num_whole _next_texture_id ;
    typename platform :: template static_array < _texture_data , _max_textures > _textures_datas ;
} ;

template < typename mediator >
shy_engine_texture < mediator > :: shy_engine_texture ( )
{
    platform :: math_make_num_whole ( _next_texture_id , 0 ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_create ( texture_id & result )
{
    result . _texture_id = _next_texture_id ;
    platform :: math_inc_whole ( _next_texture_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_finalize msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform :: array_element ( _textures_datas , msg . texture . _texture_id ) ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: render_create_texture_id ( texture . render_id ) ;
    platform :: render_load_texture_data ( texture . render_id , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_load_from_resource msg )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform :: array_element ( _textures_datas , msg . texture . _texture_id ) ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: render_load_texture_resource ( msg . resource , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_select msg )
{
    _texture_data & texture = platform :: array_element ( _textures_datas , msg . texture . _texture_id ) ;
    platform :: render_enable_texturing ( ) ;
    platform :: render_use_texture ( texture . render_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_unselect msg )
{
    platform :: render_disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_set_texel msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform :: array_element ( _textures_datas , msg . texture . _texture_id ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , msg . y ) ;
    platform :: math_add_to_whole ( texel_offset , msg . x ) ;
    platform :: array_element ( texture . texels , texel_offset ) = msg . texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , num_whole x , num_whole y , num_fract r , num_fract g , num_fract b , num_fract a )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
    platform :: math_add_to_whole ( texel_offset , x ) ;
    texel_data & texel = platform :: array_element ( texture . texels , texel_offset ) ;
    platform :: render_set_texel_color ( texel , r , g , b , a ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: receive ( typename messages :: texture_set_texels_rect msg )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform :: array_element ( _textures_datas , msg . texture . _texture_id ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    for ( num_whole y = msg . bottom
        ; platform :: condition_whole_less_or_equal_to_whole ( y , msg . top )
        ; platform :: math_inc_whole ( y )
        )
    {
        for ( num_whole x = msg . left
            ; platform :: condition_whole_less_or_equal_to_whole ( x , msg . right )
            ; platform :: math_inc_whole ( x )
            )
        {
            platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
            platform :: math_add_to_whole ( texel_offset , x ) ;
            platform :: array_element ( texture . texels , texel_offset ) = msg . texel ;
        }
    }
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_width ( num_whole & result )
{
    platform :: math_make_num_whole ( result , _texture_size ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_height ( num_whole & result )
{
    platform :: math_make_num_whole ( result , _texture_size ) ;
}
