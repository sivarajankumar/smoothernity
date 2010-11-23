template < typename mediator >
class shy_logic_amusement_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_amusement_stateless_consts_type
    {
    public :
        logic_amusement_stateless_consts_type ( ) ;
    public :
        num_fract renderer_clear_color_r ;
        num_fract renderer_clear_color_g ;
        num_fract renderer_clear_color_b ;
    } ;

    class logic_amusement_messages
    {
    public :
        class logic_amusement_creation_permit { } ;
        class logic_amusement_finished { } ;
        class logic_amusement_launch_permit { } ;
        class logic_amusement_render { } ;
        class logic_amusement_update { } ;
    } ;

    template < typename receivers >
    class logic_amusement_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_creation_permit ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_finished ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_launch_permit ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_render ) ;
        void send ( typename logic_amusement_messages :: logic_amusement_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
public :
    const logic_amusement_stateless_consts_type logic_amusement_stateless_consts ;
} ;

template < typename mediator >
shy_logic_amusement_stateless < mediator > :: logic_amusement_stateless_consts_type :: logic_amusement_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( renderer_clear_color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( renderer_clear_color_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( renderer_clear_color_b , 1 , 3 ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_creation_permit msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_launch_permit msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_render msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_amusement_stateless < mediator >
:: logic_amusement_sender < receivers >
:: send ( typename logic_amusement_messages :: logic_amusement_update msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

