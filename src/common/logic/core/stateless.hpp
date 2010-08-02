template < typename mediator >
class shy_logic_core_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_core_messages
    {
    public :
        class done { } ;
        class init { } ;
        class near_plane_distance_reply { public : num_fract distance ; } ;
        class near_plane_distance_request { } ;
        class render { } ;
        class update { } ;
        class use_ortho_projection_reply { } ;
        class use_ortho_projection_request { } ;
        class use_perspective_projection_reply { } ;
        class use_perspective_projection_request { } ;
        class video_mode_changed { } ;
    } ;

    template < typename receivers >
    class logic_core_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
        void send ( typename logic_core_messages :: done msg ) ;
        void send ( typename logic_core_messages :: init msg ) ;
        void send ( typename logic_core_messages :: near_plane_distance_reply msg ) ;
        void send ( typename logic_core_messages :: near_plane_distance_request msg ) ;
        void send ( typename logic_core_messages :: render msg ) ;
        void send ( typename logic_core_messages :: update msg ) ;
        void send ( typename logic_core_messages :: use_ortho_projection_reply msg ) ;
        void send ( typename logic_core_messages :: use_ortho_projection_request msg ) ;
        void send ( typename logic_core_messages :: use_perspective_projection_reply msg ) ;
        void send ( typename logic_core_messages :: use_perspective_projection_request msg ) ;
        void send ( typename logic_core_messages :: video_mode_changed msg ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: init msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_mesh_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: done msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: near_plane_distance_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: near_plane_distance_request msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: render msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: update msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: use_ortho_projection_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: use_ortho_projection_request msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: use_perspective_projection_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: use_perspective_projection_request msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: video_mode_changed msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}
