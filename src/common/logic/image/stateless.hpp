template < typename mediator >
class shy_logic_image_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_image_messages
    {
    public :
        class image_prepare_permit { } ;
        class image_prepared { } ;
        class image_render_reply { } ;
        class image_render_request { } ;
        class image_update { } ;
    } ;
    
    template < typename receivers >
    class logic_image_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
        void send ( typename logic_image_messages :: image_prepare_permit msg ) ;
        void send ( typename logic_image_messages :: image_prepared msg ) ;
        void send ( typename logic_image_messages :: image_render_reply msg ) ;
        void send ( typename logic_image_messages :: image_render_request msg ) ;
        void send ( typename logic_image_messages :: image_update msg ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: image_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: image_prepare_permit msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: image_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: image_render_request msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: image_update msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}
