template < typename mediator >
class shy_logic_camera_stateless
{
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_camera_messages
    {
    public :
        class camera_matrix_reply { public : matrix_data matrix ; } ;
        class camera_matrix_request { } ;
        class camera_prepare_permit { } ;
        class camera_prepared { } ;
        class camera_update { } ;
    } ;
    
    template < typename receivers >
    class logic_camera_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
        void send ( typename logic_camera_messages :: camera_matrix_reply msg ) ;
        void send ( typename logic_camera_messages :: camera_matrix_request msg ) ;
        void send ( typename logic_camera_messages :: camera_prepare_permit msg ) ;
        void send ( typename logic_camera_messages :: camera_prepared msg ) ;
        void send ( typename logic_camera_messages :: camera_update msg ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: send ( typename logic_camera_messages :: camera_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: send ( typename logic_camera_messages :: camera_update msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: send ( typename logic_camera_messages :: camera_prepare_permit msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: send ( typename logic_camera_messages :: camera_matrix_request msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_camera_stateless < mediator >
:: logic_camera_sender < receivers >
:: send ( typename logic_camera_messages :: camera_matrix_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}
