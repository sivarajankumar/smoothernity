template < typename mediator >
class shy_logic_blanket_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_blanket_stateless_consts_type
    {
    public :
        logic_blanket_stateless_consts_type ( ) ;
    public :
        num_fract mesh_vertex_x_left ;
        num_fract mesh_vertex_x_right ;
        num_fract mesh_vertex_y_bottom ;
        num_fract mesh_vertex_y_top ;
        num_fract mesh_vertex_z ;
        num_fract mesh_color_r ;
        num_fract mesh_color_g ;
        num_fract mesh_color_b ;
        num_fract mesh_color_a ;
    } ;

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

public :
    const logic_blanket_stateless_consts_type logic_blanket_stateless_consts ;
} ;

template < typename mediator >
shy_logic_blanket_stateless < mediator > :: logic_blanket_stateless_consts_type :: logic_blanket_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( mesh_vertex_x_left , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_vertex_x_right , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_vertex_y_bottom , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_vertex_y_top , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_vertex_z , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_a , 1 , 1 ) ;
}

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

