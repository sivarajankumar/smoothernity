template < typename mediator >
class shy_logic_touch_stateless
{
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
	class logic_touch_messages
	{
	public :
        class touch_prepare_permit { } ;
        class touch_prepared { } ;
        class touch_render { } ;
        class touch_update { } ;
	} ;

	template < typename receivers >
	class logic_touch_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_touch_messages :: touch_prepare_permit ) ;
        void send ( typename logic_touch_messages :: touch_prepared ) ;
        void send ( typename logic_touch_messages :: touch_render ) ;
        void send ( typename logic_touch_messages :: touch_update ) ;
	private :
		typename platform_pointer :: template pointer < const receivers > _receivers ;
	} ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_touch_stateless < mediator >
:: logic_touch_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
	_receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_touch_stateless < mediator >
:: logic_touch_sender < receivers >
:: send ( typename logic_touch_messages :: touch_prepare_permit msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_touch_stateless < mediator >
:: logic_touch_sender < receivers >
:: send ( typename logic_touch_messages :: touch_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_touch_stateless < mediator >
:: logic_touch_sender < receivers >
:: send ( typename logic_touch_messages :: touch_render msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_touch_stateless < mediator >
:: logic_touch_sender < receivers >
:: send ( typename logic_touch_messages :: touch_update msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}
