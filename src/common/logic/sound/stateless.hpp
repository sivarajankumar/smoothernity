template < typename mediator >
class shy_logic_sound_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_sound_messages
    {
    public :
        class sound_prepare_permit { } ;
        class sound_prepared { } ;
        class sound_update { } ;
    } ;

    template < typename receivers >
    class logic_sound_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_sound_messages :: sound_prepare_permit ) ;
        void send ( typename logic_sound_messages :: sound_prepared ) ;
        void send ( typename logic_sound_messages :: sound_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_sound_stateless < mediator >
:: logic_sound_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_sound_stateless < mediator >
:: logic_sound_sender < receivers >
:: send ( typename logic_sound_messages :: sound_prepare_permit msg )
{
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_sound_stateless < mediator >
:: logic_sound_sender < receivers >
:: send ( typename logic_sound_messages :: sound_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_sound_stateless < mediator >
:: logic_sound_sender < receivers >
:: send ( typename logic_sound_messages :: sound_update msg )
{
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
}
