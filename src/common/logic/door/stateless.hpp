template < typename mediator >
class shy_logic_door_stateless
{
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_door_messages
    {
    public :
        class logic_door_creation_finished { } ;
        class logic_door_creation_permit { } ;
        class logic_door_launch_permit { } ;
        class logic_door_mesh_create { } ;
        class logic_door_mesh_creation_finished { } ;
        class logic_door_mesh_render_reply { } ;
        class logic_door_mesh_render_request { } ;
        class logic_door_mesh_set_transform { public : matrix_data transform ; } ;
        class logic_door_place { } ;
        class logic_door_render_reply { } ;
        class logic_door_render_request { } ;
        class logic_door_texture_create { } ;
        class logic_door_texture_creation_finished { } ;
        class logic_door_texture_select_reply { } ;
        class logic_door_texture_select_request { } ;
        class logic_door_update { } ;
    } ;

    template < typename receivers >
    class logic_door_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_door_messages :: logic_door_creation_finished ) ;
        void send ( typename logic_door_messages :: logic_door_creation_permit ) ;
        void send ( typename logic_door_messages :: logic_door_launch_permit ) ;
        void send ( typename logic_door_messages :: logic_door_mesh_create ) ;
        void send ( typename logic_door_messages :: logic_door_mesh_creation_finished ) ;
        void send ( typename logic_door_messages :: logic_door_mesh_render_reply ) ;
        void send ( typename logic_door_messages :: logic_door_mesh_render_request ) ;
        void send ( typename logic_door_messages :: logic_door_mesh_set_transform ) ;
        void send ( typename logic_door_messages :: logic_door_place ) ;
        void send ( typename logic_door_messages :: logic_door_render_reply ) ;
        void send ( typename logic_door_messages :: logic_door_render_request ) ;
        void send ( typename logic_door_messages :: logic_door_texture_create ) ;
        void send ( typename logic_door_messages :: logic_door_texture_creation_finished ) ;
        void send ( typename logic_door_messages :: logic_door_texture_select_reply ) ;
        void send ( typename logic_door_messages :: logic_door_texture_select_request ) ;
        void send ( typename logic_door_messages :: logic_door_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_creation_finished msg )
{
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_creation_permit msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_launch_permit msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_mesh_create msg )
{
    _receivers . get ( ) . logic_door_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_mesh_creation_finished msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_door_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_mesh_render_request msg )
{
    _receivers . get ( ) . logic_door_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_mesh_set_transform msg )
{
    _receivers . get ( ) . logic_door_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_place msg )
{
    _receivers . get ( ) . logic_door_placement . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_render_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_render_request msg )
{
    _receivers . get ( ) . logic_door_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_texture_create msg )
{
    _receivers . get ( ) . logic_door_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_texture_creation_finished msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_texture_select_reply msg )
{
    _receivers . get ( ) . logic_door_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_texture_select_request msg )
{
    _receivers . get ( ) . logic_door_texture . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_door_stateless < mediator >
:: logic_door_sender < receivers >
:: send ( typename logic_door_messages :: logic_door_update msg )
{
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_animation_appear . get ( ) . receive ( msg ) ;
}

