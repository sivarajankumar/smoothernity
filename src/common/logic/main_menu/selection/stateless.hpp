template < typename mediator >
class shy_logic_main_menu_selection_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;

public :
    class logic_main_menu_selection_stateless_consts_type
    {
    public :
        logic_main_menu_selection_stateless_consts_type ( ) ;
    public :
        num_fract mesh_size ;
    } ;

    class logic_main_menu_selection_messages
    {
    public :
        class logic_main_menu_selection_mesh_create { } ;
        class logic_main_menu_selection_mesh_create_finished { } ;
        class logic_main_menu_selection_mesh_destroy_reply { } ;
        class logic_main_menu_selection_mesh_destroy_request { } ;
        class logic_main_menu_selection_mesh_place { } ;
        class logic_main_menu_selection_mesh_render_reply { } ;
        class logic_main_menu_selection_mesh_render_request { } ;
        class logic_main_menu_selection_track_reply { } ;
        class logic_main_menu_selection_track_request { } ;
        class logic_main_menu_selection_track_row_selected { public : num_whole row ; } ;
        class logic_main_menu_selection_track_void_selected { } ;
        class logic_main_menu_selection_tracking_director_update { } ;
    } ;

    template < typename receivers >
    class logic_main_menu_selection_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create_finished ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_reply ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_request ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_place ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_reply ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_request ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_reply ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_request ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_row_selected ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_void_selected ) ;
        void send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_tracking_director_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

public :
    shy_logic_main_menu_selection_stateless ( ) ;
private :
    shy_logic_main_menu_selection_stateless < mediator > & operator= ( const shy_logic_main_menu_selection_stateless < mediator > & ) ;
public :
    const logic_main_menu_selection_stateless_consts_type logic_main_menu_selection_stateless_consts ;
} ;

template < typename mediator >
shy_logic_main_menu_selection_stateless < mediator > :: logic_main_menu_selection_stateless_consts_type :: logic_main_menu_selection_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( mesh_size , 1 , 1 ) ;
}

template < typename mediator >
shy_logic_main_menu_selection_stateless < mediator > :: shy_logic_main_menu_selection_stateless ( )
{
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_create_finished msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_destroy_reply msg )
{
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_place msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_mesh_render_reply msg )
{
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_request msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracker . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_reply msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_row_selected msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_track_void_selected msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_main_menu_selection_stateless < mediator > 
:: logic_main_menu_selection_sender < receivers > 
:: send ( typename logic_main_menu_selection_messages :: logic_main_menu_selection_tracking_director_update msg )
{
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
}

