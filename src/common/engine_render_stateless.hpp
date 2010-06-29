template < typename mediator >
class shy_engine_render_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_render platform_render ;
    typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    
public :
    static void texture_loader_ready ( num_whole & is_ready ) ;
    static void set_texel_color ( texel_data & texel , num_fract r , num_fract g , num_fract b , num_fract a ) ;
    static void create_texture_resource_id ( texture_resource_id & resource_id , num_whole resource_index ) ;
	static void get_aspect_width ( num_fract & result ) ;
	static void get_aspect_height ( num_fract & result ) ;
} ;

template < typename mediator >
void shy_engine_render_stateless < mediator > :: texture_loader_ready ( num_whole & is_ready )
{
    platform_render :: texture_loader_ready ( is_ready ) ;
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

template < typename mediator >
void shy_engine_render_stateless < mediator > :: get_aspect_width ( num_fract & result )
{
    platform_render :: get_aspect_width ( result ) ;
}

template < typename mediator >
void shy_engine_render_stateless < mediator > :: get_aspect_height ( num_fract & result )
{
    platform_render :: get_aspect_height ( result ) ;
}
