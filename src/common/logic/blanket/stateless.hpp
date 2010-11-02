template < typename mediator >
class shy_logic_blanket_stateless
{
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_blanket_messages
    {
    public :
        class logic_blanket_creation_finished { } ;
        class logic_blanket_creation_permit { } ;
        class logic_blanket_mesh_create { } ;
        class logic_blanket_mesh_creation_finished { } ;
        class logic_blanket_mesh_render_reply { } ;
        class logic_blanket_mesh_render_request { } ;
        class logic_blanket_mesh_set_transform { public : matrix_data transform ; } ;
        class logic_blanket_place { } ;
        class logic_blanket_render_reply { } ;
        class logic_blanket_render_request { } ;
        class logic_blanket_update { } ;
    } ;
    
    template < typename receivers >
    class logic_blanket_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_creation_finished ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_creation_permit ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_mesh_create ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_mesh_creation_finished ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_mesh_render_reply ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_mesh_render_request ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_mesh_set_transform ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_place ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_render_reply ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_render_request ) ;
        void send ( typename logic_blanket_messages :: logic_blanket_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_creation_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_creation_permit msg )
{
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_mesh_create msg )
{
    _receivers . get ( ) . logic_blanket_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_mesh_creation_finished msg )
{
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_blanket_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_mesh_render_request msg )
{
    _receivers . get ( ) . logic_blanket_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_mesh_set_transform msg )
{
    _receivers . get ( ) . logic_blanket_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_place msg )
{
    _receivers . get ( ) . logic_blanket_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_render_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_render_request msg )
{
    _receivers . get ( ) . logic_blanket_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_blanket_stateless < mediator >
:: logic_blanket_sender < receivers >
:: send ( typename logic_blanket_messages :: logic_blanket_update msg )
{
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation_disappear . get ( ) . receive ( msg ) ;
}

