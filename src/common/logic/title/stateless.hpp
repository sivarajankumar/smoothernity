template < typename mediator >
class shy_logic_title_stateless
{
	typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
	class logic_title_messages
	{
	public :
        class logic_title_created { } ;
        class logic_title_finished { } ;
        class logic_title_launch_permit { } ;
        class logic_title_render { } ;
        class logic_title_update { } ;
	} ;

	template < typename receivers >
	class logic_title_sender
	{
	public :
		void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_title_messages :: logic_title_created ) ;
        void send ( typename logic_title_messages :: logic_title_finished ) ;
        void send ( typename logic_title_messages :: logic_title_launch_permit ) ;
        void send ( typename logic_title_messages :: logic_title_render ) ;
        void send ( typename logic_title_messages :: logic_title_update ) ;
	private :
		typename platform_pointer :: template pointer < const receivers > _receivers ;
	} ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
	_receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_created msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_launch_permit msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_render msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_title_stateless < mediator >
:: logic_title_sender < receivers >
:: send ( typename logic_title_messages :: logic_title_update msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}
