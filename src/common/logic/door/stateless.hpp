template < typename mediator >
class shy_logic_door_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_door_stateless_consts_type
    {
    public :
        logic_door_stateless_consts_type ( ) ;
    public :
        num_fract mesh_color_r ;
        num_fract mesh_color_g ;
        num_fract mesh_color_b ;
        num_fract mesh_color_a ;
        num_fract mesh_x_left ;
        num_fract mesh_x_right ;
        num_fract mesh_y_bottom ;
        num_fract mesh_y_top ;
        num_fract mesh_z ;
        num_fract mesh_u_top_left ;
        num_fract mesh_v_top_left ;
        num_fract mesh_u_top_right ;
        num_fract mesh_v_top_right ;
        num_fract mesh_u_bottom_left ;
        num_fract mesh_v_bottom_left ;
        num_fract mesh_u_bottom_right ;
        num_fract mesh_v_bottom_right ;
        num_fract texture_pen_r ;
        num_fract texture_pen_g ;
        num_fract texture_pen_b ;
        num_fract texture_pen_a ;
        num_fract texture_paper_r ;
        num_fract texture_paper_g ;
        num_fract texture_paper_b ;
        num_fract texture_paper_a ;
        num_whole texture_stripes ;
    } ;

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

public :
    const logic_door_stateless_consts_type logic_door_stateless_consts ;
} ;

template < typename mediator >
shy_logic_door_stateless < mediator > :: logic_door_stateless_consts_type :: logic_door_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( mesh_color_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_x_left , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_x_right , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_y_bottom , - 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_y_top , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_z , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_u_top_left , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_v_top_left , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_u_bottom_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_v_bottom_left , 1 , 2 ) ;

    platform_math :: make_num_fract ( mesh_u_top_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_v_top_right , 1 , 2 ) ;

    platform_math :: make_num_fract ( mesh_u_bottom_right , 1 , 2 ) ;
    platform_math :: make_num_fract ( mesh_v_bottom_right , 0 , 1 ) ;

    platform_math :: make_num_fract ( texture_pen_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( texture_pen_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( texture_pen_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( texture_pen_a , 1 , 1 ) ;
    platform_math :: make_num_fract ( texture_paper_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( texture_paper_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( texture_paper_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( texture_paper_a , 1 , 1 ) ;
    platform_math :: make_num_whole ( texture_stripes , 9 ) ;
}

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

