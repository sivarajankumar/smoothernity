template < typename mediator >
class shy_engine_rasterizer_stateless
{
	typedef typename mediator :: engine_render_stateless :: texture_id texture_id ;
	typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
	typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
public :
	class engine_rasterizer_messages
	{
	public :
        class rasterize_ellipse_in_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_finalize_reply { } ;
        class rasterize_finalize_request { } ;
        class rasterize_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_triangle { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; num_whole x3 ; num_whole y3 ; } ;
        class rasterize_use_texel { public : texel_data texel ; } ;
        class rasterize_use_texture { public : texture_id texture ; num_whole origin_x ; num_whole origin_y ; } ;
	} ;

	template < typename receivers >
	class engine_rasterizer_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_ellipse_in_rect ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_finalize_reply ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_finalize_request ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_rect ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_triangle ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_use_texel ) ;
        void send ( typename engine_rasterizer_messages :: rasterize_use_texture ) ;
	private :
		typename platform_pointer :: template pointer < const receivers > _receivers ;
	} ;
} ;

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
	_receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_ellipse_in_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_finalize_reply msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_finalize_request msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_triangle msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_use_texture msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: rasterize_use_texel msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}
