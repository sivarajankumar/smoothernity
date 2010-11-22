template < typename mediator >
class shy_logic_ortho_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_ortho_messages
    {
    public :
        class logic_ortho_planes_reply { public : num_fract x_left ; num_fract x_right ; num_fract y_bottom ; num_fract y_top ; num_fract z_far ; num_fract z_near ; } ;
        class logic_ortho_planes_request { } ;
    } ;

    template < typename receivers >
    class logic_ortho_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_ortho_messages :: logic_ortho_planes_reply ) ;
        void send ( typename logic_ortho_messages :: logic_ortho_planes_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_ortho_stateless < mediator >
:: logic_ortho_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_ortho_stateless < mediator >
:: logic_ortho_sender < receivers >
:: send ( typename logic_ortho_messages :: logic_ortho_planes_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_ortho_stateless < mediator >
:: logic_ortho_sender < receivers >
:: send ( typename logic_ortho_messages :: logic_ortho_planes_request msg )
{
    _receivers . get ( ) . logic_ortho . get ( ) . receive ( msg ) ;
}

