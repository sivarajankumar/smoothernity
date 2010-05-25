template < typename mediator >
class shy_engine_texture
{
    typedef typename mediator :: platform platform ;
    typedef typename mediator :: platform :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: render_texture_id render_texture_id ;
    typedef typename mediator :: platform :: texel_data texel_data ;
    typedef typename mediator :: platform :: texture_resource_id texture_resource_id ;
    typedef typename mediator :: platform :: int_32 int_32 ;
    typedef typename mediator :: platform :: num_whole num_whole ;
    
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
    num_whole _next_texture_id ;
    _texture_data _textures_datas [ _max_textures ] ;
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
    _texture_data * texture_ptr = 0 ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: memory_pointer_offset ( texture_ptr , _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: render_create_texture_id ( texture_ptr -> render_id ) ;
    platform :: render_load_texture_data ( texture_ptr -> render_id , size_pow2_base , texture_ptr -> texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_load_from_resource ( texture_id arg_texture_id , texture_resource_id arg_resource_id )
{
    num_whole size_pow2_base ;
    _texture_data * texture_ptr = 0 ;
    platform :: math_make_num_whole ( size_pow2_base , _texture_size_pow2_base ) ;
    platform :: memory_pointer_offset ( texture_ptr , _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: render_load_texture_resource ( arg_resource_id , size_pow2_base , texture_ptr -> texels ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_select ( texture_id arg_texture_id )
{
    _texture_data * texture_ptr = 0 ;
    platform :: memory_pointer_offset ( texture_ptr , _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: render_enable_texturing ( ) ;
    platform :: render_use_texture ( texture_ptr -> render_id ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_unselect ( )
{
    platform :: render_disable_texturing ( ) ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , int_32 x_int_32 , int_32 y_int_32 , const texel_data & texel )
{
    num_whole x ;
    num_whole y ;
    num_whole texel_offset ;
    num_whole num_texture_size ;
    texel_data * texel_ptr = 0 ;
    _texture_data * texture_ptr = 0 ;
    platform :: math_make_num_whole ( x , x_int_32 ) ;
    platform :: math_make_num_whole ( y , y_int_32 ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
    platform :: math_add_to_whole ( texel_offset , x ) ;
    platform :: memory_pointer_offset ( texture_ptr , _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: memory_pointer_offset ( texel_ptr , texture_ptr -> texels , texel_offset ) ;
    * texel_ptr = texel ;
}

template < typename mediator >
void shy_engine_texture < mediator > :: texture_set_texel
    ( texture_id arg_texture_id , int_32 x_int_32 , int_32 y_int_32 , int_32 r_int_32 , int_32 g_int_32 , int_32 b_int_32 , int_32 a_int_32 )
{
    num_whole x ;
    num_whole y ;
    num_whole r ;
    num_whole g ;
    num_whole b ;
    num_whole a ;
    num_whole texel_offset ;
    num_whole num_texture_size ;
    texel_data * texel_ptr = 0 ;
    _texture_data * texture_ptr = 0 ;
    platform :: math_make_num_whole ( x , x_int_32 ) ;
    platform :: math_make_num_whole ( y , y_int_32 ) ;
    platform :: math_make_num_whole ( r , r_int_32 ) ;
    platform :: math_make_num_whole ( g , g_int_32 ) ;
    platform :: math_make_num_whole ( b , b_int_32 ) ;
    platform :: math_make_num_whole ( a , a_int_32 ) ;
    platform :: math_make_num_whole ( num_texture_size , _texture_size ) ;
    platform :: math_mul_wholes ( texel_offset , num_texture_size , y ) ;
    platform :: math_add_to_whole ( texel_offset , x ) ;
    platform :: memory_pointer_offset ( texture_ptr , _textures_datas , arg_texture_id . _texture_id ) ;
    platform :: memory_pointer_offset ( texel_ptr , texture_ptr -> texels , texel_offset ) ;
    platform :: render_set_texel_color ( * texel_ptr , r , g , b , a ) ;
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
