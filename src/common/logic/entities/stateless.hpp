template < typename mediator >
class shy_logic_entities_stateless
{
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator :: platform :: platform_vector :: vector_data vector_data ;
public :
    class logic_entities_messages
    {
    public :
        class entities_height_reply { public : num_fract height ; } ;
        class entities_height_request { } ;
        class entities_mesh_grid_reply { public : num_whole grid ; } ;
        class entities_mesh_grid_request { } ;
        class entities_origin_reply { public : vector_data origin ; num_whole index ; } ;
        class entities_origin_request { public : num_whole index ; } ;
        class entities_prepare_permit { } ;
        class entities_prepared { } ;
        class entities_render_reply { } ;
        class entities_render_request { } ;
        class entities_update { } ;
    } ;
    
    template < typename receivers >
    class logic_entities_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_entities_messages :: entities_height_reply ) ;
        void send ( typename logic_entities_messages :: entities_height_request ) ;
        void send ( typename logic_entities_messages :: entities_mesh_grid_reply ) ;
        void send ( typename logic_entities_messages :: entities_mesh_grid_request ) ;
        void send ( typename logic_entities_messages :: entities_origin_reply ) ;
        void send ( typename logic_entities_messages :: entities_origin_request ) ;
        void send ( typename logic_entities_messages :: entities_prepare_permit ) ;
        void send ( typename logic_entities_messages :: entities_prepared ) ;
        void send ( typename logic_entities_messages :: entities_render_reply ) ;
        void send ( typename logic_entities_messages :: entities_render_request ) ;
        void send ( typename logic_entities_messages :: entities_update ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;
} ;

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_height_reply msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_height_request msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_mesh_grid_reply msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_mesh_grid_request msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_origin_reply msg )
{
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_origin_request msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_prepare_permit msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_render_request msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_entities_stateless < mediator >
:: logic_entities_sender < receivers >
:: send ( typename logic_entities_messages :: entities_update msg )
{
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
}
