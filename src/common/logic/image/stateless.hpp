template < typename mediator >
class shy_logic_image_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_image_messages
    {
    public :
    } ;
    
    template < typename receivers >
    class logic_image_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template < const receivers > arg_receivers ) ;
        void send ( ) { }
    private :
        typename platform_pointer :: template < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_image_stateless < mediator >
:: logic_image_sender < receivers >
:: set_receivers ( typename platform_pointer :: template < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}
