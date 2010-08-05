template < typename mediator >
class shy_engine_rasterizer_stateless
{
	typedef typename mediator :: engine_render_stateless :: engine_render_texture_id engine_render_texture_id ;
	typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
	typedef typename mediator :: platform :: platform_render :: texel_data texel_data ;
public :
	class engine_rasterizer_messages
	{
	public :
        class engine_rasterizer_draw_ellipse_in_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class engine_rasterizer_draw_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class engine_rasterizer_draw_triangle { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; num_whole x3 ; num_whole y3 ; } ;
        class engine_rasterizer_finalize_reply { } ;
        class engine_rasterizer_finalize_request { } ;
        class engine_rasterizer_use_texel { public : texel_data texel ; } ;
        class engine_rasterizer_use_texture { public : engine_render_texture_id texture ; num_whole origin_x ; num_whole origin_y ; } ;
	} ;

	template < typename receivers >
	class engine_rasterizer_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_ellipse_in_rect ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_rect ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_triangle ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_finalize_reply ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_finalize_request ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_use_texel ) ;
        void send ( typename engine_rasterizer_messages :: engine_rasterizer_use_texture ) ;
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
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_ellipse_in_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_finalize_reply msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_finalize_request msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_draw_triangle msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_use_texture msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_engine_rasterizer_stateless < mediator >
:: engine_rasterizer_sender < receivers >
:: send ( typename engine_rasterizer_messages :: engine_rasterizer_use_texel msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}
