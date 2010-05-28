template < typename mediator >
class shy_engine_texture
{
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
    void texture_finalize ( texture_id arg_texture_id ) ;
    void texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id ) ;
    void texture_select ( texture_id arg_texture_id ) ;
    void texture_unselect ( ) ;
    void texture_set_texel ( texture_id arg_texture_id , num_whole x , num_whole y , const texel_data & texel ) ;
    void texture_set_texel ( texture_id arg_texture_id , num_whole x , num_whole y , num_whole r , num_whole g , num_whole b , num_whole a ) ;
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
void shy_engine_texture < mediator > :: texture_finalize ( texture_id arg_texture_id )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: render_create_texture_id ( texture . render_id ) ;
    platform :: render_load_texture_data ( texture . render_id , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id )
{
    num_whole size_pow2_base ;
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: render_load_texture_resource ( arg_resource_id , size_pow2_base , texture . texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_select ( texture_id arg_texture_id )
{
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: render_enable_texturing ( ) ;
    platform :: render_use_texture ( texture . render_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_unselect ( )
{
    platform :: render_disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , num_whole x , num_whole y , const texel_data & texel )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
    platform :: math_add_to_whole ( texel_offset , x ) ;
    platform :: array_element ( texture . texels , texel_offset ) = texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , num_whole x , num_whole y , num_whole whole_r , num_whole whole_g , num_whole whole_b , num_whole whole_a )
{
    num_whole texel_offset ;
    num_whole num_texture_size ;
    num_fract color_scale ;
    num_fract r ;
    num_fract g ;
    num_fract b ;
    num_fract a ;
    platform :: math_make_num_fract ( color_scale , 255 , 1 ) ;
    platform :: math_make_fract_from_whole ( r , whole_r ) ;
    platform :: math_make_fract_from_whole ( g , whole_g ) ;
    platform :: math_make_fract_from_whole ( b , whole_b ) ;
    platform :: math_make_fract_from_whole ( a , whole_a ) ;
    platform :: math_div_fract_by ( r , color_scale ) ;
    platform :: math_div_fract_by ( g , color_scale ) ;
    platform :: math_div_fract_by ( b , color_scale ) ;
    platform :: math_div_fract_by ( a , color_scale ) ;
    _texture_data & texture = platform :: array_element ( _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
    platform :: math_add_to_whole ( texel_offset , x ) ;
    texel_data & texel = platform :: array_element ( texture . texels , texel_offset ) ;
    platform :: render_set_texel_color ( texel , r , g , b , a ) ;
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
