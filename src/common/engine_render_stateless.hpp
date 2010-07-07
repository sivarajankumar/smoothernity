template < typename mediator >
class shy_engine_render_stateless
{
    friend class shy_engine_render < mediator > ;

    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;

    static const_int_32 _texture_size_pow2_base = 8 ;
    static const_int_32 _texture_size = 1 << _texture_size_pow2_base ;
    
public :    
    class mesh_id
    {
        friend class shy_engine_render < mediator > ;
    private :
        num_whole _mesh_id ;
    } ;
    
    class texture_id
    {
        friend class shy_engine_render < mediator > ;
    private :
        num_whole _texture_id ;
    } ;
    
    class engine_render_stateless_consts_type
    {
    public :
        engine_render_stateless_consts_type ( ) ;
    public :
        num_whole texture_width ;
        num_whole texture_height ;
    } ;
    
public :
    shy_engine_render_stateless ( ) ;
    shy_engine_render_stateless & operator= ( const shy_engine_render_stateless & src ) ;
    
    static void set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
    
public :
    const engine_render_stateless_consts_type engine_render_stateless_consts ;
} ;

template < typename mediator >
shy_engine_render_stateless < mediator > :: shy_engine_render_stateless ( )
{
}

template < typename mediator >
shy_engine_render_stateless < mediator > & 
shy_engine_render_stateless < mediator > :: operator= ( const shy_engine_render_stateless < mediator > & src )
{
    return * this ;
}

template < typename mediator >
shy_engine_render_stateless < mediator > :: engine_render_stateless_consts_type :: engine_render_stateless_consts_type ( )
{
    platform_math :: make_num_whole ( texture_width , _texture_size ) ;
    platform_math :: make_num_whole ( texture_height , _texture_size ) ;
}

template < typename mediator >
void shy_engine_render_stateless < mediator > :: set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a )
{
    platform_render :: set_texel_color ( texel , r , g , b , a ) ;
}

template < typename mediator >
void shy_engine_render_stateless < mediator > :: create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index )
{
    platform_render :: create_texture_resource_id ( resource_id , resource_index ) ;
}
