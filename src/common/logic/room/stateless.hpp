template < typename mediator >
class shy_logic_room_stateless
{
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_room_messages
    {
    public :
        class logic_room_creation_permit { } ;
        class logic_room_finished { } ;
        class logic_room_launch_permit { } ;
        class logic_room_mesh_create { } ;
        class logic_room_mesh_creation_finished { } ;
        class logic_room_mesh_render_reply { } ;
        class logic_room_mesh_render_request { } ;
        class logic_room_render_permit { } ;
        class logic_room_render_reply { } ;
        class logic_room_render_request { } ;
        class logic_room_texture_create { } ;
        class logic_room_texture_creation_finished { } ;
        class logic_room_texture_select_reply { } ;
        class logic_room_texture_select_request { } ;
        class logic_room_update { } ;
    } ;

    template < typename receivers >
    class logic_room_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_room_messages :: logic_room_creation_permit ) ;
        void send ( typename logic_room_messages :: logic_room_finished ) ;
        void send ( typename logic_room_messages :: logic_room_launch_permit ) ;
        void send ( typename logic_room_messages :: logic_room_mesh_create ) ;
        void send ( typename logic_room_messages :: logic_room_mesh_creation_finished ) ;
        void send ( typename logic_room_messages :: logic_room_mesh_render_reply ) ;
        void send ( typename logic_room_messages :: logic_room_mesh_render_request ) ;
        void send ( typename logic_room_messages :: logic_room_render_permit ) ;
        void send ( typename logic_room_messages :: logic_room_render_reply ) ;
        void send ( typename logic_room_messages :: logic_room_render_request ) ;
        void send ( typename logic_room_messages :: logic_room_texture_create ) ;
        void send ( typename logic_room_messages :: logic_room_texture_creation_finished ) ;
        void send ( typename logic_room_messages :: logic_room_texture_select_reply ) ;
        void send ( typename logic_room_messages :: logic_room_texture_select_request ) ;
        void send ( typename logic_room_messages :: logic_room_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_creation_permit msg )
{
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_launch_permit msg )
{
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_mesh_create msg )
{
    _receivers . get ( ) . logic_room_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_mesh_creation_finished msg )
{
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_room_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_mesh_render_request msg )
{
    _receivers . get ( ) . logic_room_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_render_permit msg )
{
    _receivers . get ( ) . logic_room_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_render_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_render_request msg )
{
    _receivers . get ( ) . logic_room_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_texture_create msg )
{
    _receivers . get ( ) . logic_room_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_texture_creation_finished msg )
{
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_texture_select_reply msg )
{
    _receivers . get ( ) . logic_room_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_texture_select_request msg )
{
    _receivers . get ( ) . logic_room_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_room_stateless < mediator >
:: logic_room_sender < receivers >
:: send ( typename logic_room_messages :: logic_room_update msg )
{
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_mesh . get ( ) . receive ( msg ) ;
}

