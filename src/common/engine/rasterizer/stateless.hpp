template < typename mediator >
class shy_engine_rasterizer_stateless
{
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
	class engine_rasterizer_messages
	{
	public :
	} ;

	template < typename receivers >
	class engine_rasterizer_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
		void send ( ) { }
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
