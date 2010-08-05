template < typename mediator >
class shy_logic_game_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_game_messages
    {
    public :
        class logic_game_launch_permit { } ;
        class logic_game_render { } ;
        class logic_game_update { } ;
    } ;
    
    template < typename receivers >
    class logic_game_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_game_messages :: logic_game_launch_permit ) ;
        void send ( typename logic_game_messages :: logic_game_render ) ;
        void send ( typename logic_game_messages :: logic_game_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_game_stateless < mediator >
:: logic_game_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_game_stateless < mediator >
:: logic_game_sender < receivers >
:: send ( typename logic_game_messages :: logic_game_render msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_game_stateless < mediator >
:: logic_game_sender < receivers >
:: send ( typename logic_game_messages :: logic_game_update msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_game_stateless < mediator >
:: logic_game_sender < receivers >
:: send ( typename logic_game_messages :: logic_game_launch_permit msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}
