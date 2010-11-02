template < typename mediator >
class shy_logic_blanket_animation_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_blanket_animation_messages
    {
    public :
        class logic_blanket_animation_appear_finished { } ;
        class logic_blanket_animation_appear_start { } ;
        class logic_blanket_animation_appear_transform_reply { public : num_fract scale ; num_fract rotation ; } ;
        class logic_blanket_animation_appear_transform_request { } ;
        class logic_blanket_animation_disappear_finished { } ;
        class logic_blanket_animation_disappear_start { } ;
        class logic_blanket_animation_disappear_transform_reply { public : num_fract scale ; num_fract rotation ; } ;
        class logic_blanket_animation_disappear_transform_request { } ;
        class logic_blanket_animation_fit_transform_reply { public : num_fract scale ; } ;
        class logic_blanket_animation_fit_transform_request { } ;
        class logic_blanket_animation_transform_reply { public : matrix_data transform ; } ;
        class logic_blanket_animation_transform_request { } ;
    } ;

    template < typename receivers >
    class logic_blanket_animation_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_finished ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_start ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_transform_reply ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_transform_request ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_finished ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_start ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_transform_reply ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_transform_request ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_fit_transform_reply ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_fit_transform_request ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_transform_reply ) ;
        void send ( typename logic_blanket_animation_messages :: logic_blanket_animation_transform_request ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_start msg )
{
    _receivers . get ( ) . logic_blanket_animation_appear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_transform_reply msg )
{
    _receivers . get ( ) . logic_blanket_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_appear_transform_request msg )
{
    _receivers . get ( ) . logic_blanket_animation_appear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_start msg )
{
    _receivers . get ( ) . logic_blanket_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_transform_reply msg )
{
    _receivers . get ( ) . logic_blanket_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_disappear_transform_request msg )
{
    _receivers . get ( ) . logic_blanket_animation_disappear . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_fit_transform_reply msg )
{
    _receivers . get ( ) . logic_blanket_animation . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_fit_transform_request msg )
{
    _receivers . get ( ) . logic_blanket_animation_fit . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_transform_reply msg )
{
    _receivers . get ( ) . logic_blanket_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_animation_stateless < mediator >
:: logic_blanket_animation_sender < receivers >
:: send ( typename logic_blanket_animation_messages :: logic_blanket_animation_transform_request msg )
{
    _receivers . get ( ) . logic_blanket_animation . get ( ) . receive ( msg ) ;
}

