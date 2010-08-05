template < typename mediator >
class shy_logic_image_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_image_messages
    {
    public :
        class logic_image_prepare_permit { } ;
        class logic_image_prepared { } ;
        class logic_image_render_reply { } ;
        class logic_image_render_request { } ;
        class logic_image_update { } ;
    } ;
    
    template < typename receivers >
    class logic_image_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_image_messages :: logic_image_prepare_permit ) ;
        void send ( typename logic_image_messages :: logic_image_prepared ) ;
        void send ( typename logic_image_messages :: logic_image_render_reply ) ;
        void send ( typename logic_image_messages :: logic_image_render_request ) ;
        void send ( typename logic_image_messages :: logic_image_update ) ;
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
:: send ( typename logic_image_messages :: logic_image_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: logic_image_prepare_permit msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: logic_image_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: logic_image_render_request msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: send ( typename logic_image_messages :: logic_image_update msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}
