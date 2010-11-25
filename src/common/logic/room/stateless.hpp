template < typename mediator >
class shy_logic_room_stateless
{
    typedef typename mediator :: platform :: platform_math platform_math ;
    typedef typename mediator :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator :: platform :: platform_pointer platform_pointer ;
public :
    class logic_room_stateless_consts_type
    {
    public :
        logic_room_stateless_consts_type ( ) ;
    public :
        num_fract mesh_color_right_r ;
        num_fract mesh_color_right_g ;
        num_fract mesh_color_right_b ;
        num_fract mesh_color_right_a ;
        num_fract mesh_color_left_r ;
        num_fract mesh_color_left_g ;
        num_fract mesh_color_left_b ;
        num_fract mesh_color_left_a ;
        num_fract mesh_color_near_r ;
        num_fract mesh_color_near_g ;
        num_fract mesh_color_near_b ;
        num_fract mesh_color_near_a ;
        num_fract mesh_color_far_r ;
        num_fract mesh_color_far_g ;
        num_fract mesh_color_far_b ;
        num_fract mesh_color_far_a ;
        num_fract mesh_color_top_r ;
        num_fract mesh_color_top_g ;
        num_fract mesh_color_top_b ;
        num_fract mesh_color_top_a ;
        num_fract mesh_color_bottom_r ;
        num_fract mesh_color_bottom_g ;
        num_fract mesh_color_bottom_b ;
        num_fract mesh_color_bottom_a ;
        num_fract mesh_position_x ;
        num_fract mesh_position_y ;
        num_fract mesh_position_z ;
        num_fract mesh_x_left ;
        num_fract mesh_x_right ;
        num_fract mesh_y_top ;
        num_fract mesh_y_bottom ;
        num_fract mesh_z_near ;
        num_fract mesh_z_far ;
        num_fract mesh_right_side_u_left ;
        num_fract mesh_right_side_u_right ;
        num_fract mesh_right_side_v_top ;
        num_fract mesh_right_side_v_bottom ;
        num_fract mesh_left_side_u_left ;
        num_fract mesh_left_side_u_right ;
        num_fract mesh_left_side_v_top ;
        num_fract mesh_left_side_v_bottom ;
        num_fract mesh_near_side_u_left ;
        num_fract mesh_near_side_u_right ;
        num_fract mesh_near_side_v_top ;
        num_fract mesh_near_side_v_bottom ;
        num_fract mesh_far_side_u_left ;
        num_fract mesh_far_side_u_right ;
        num_fract mesh_far_side_v_top ;
        num_fract mesh_far_side_v_bottom ;
        num_fract mesh_top_side_u_left ;
        num_fract mesh_top_side_u_right ;
        num_fract mesh_top_side_v_top ;
        num_fract mesh_top_side_v_bottom ;
        num_fract mesh_bottom_side_u_left ;
        num_fract mesh_bottom_side_u_right ;
        num_fract mesh_bottom_side_v_top ;
        num_fract mesh_bottom_side_v_bottom ;
        num_fract room_show_time ;
        num_fract texture_pen_intensity ;
        num_fract texture_paper_intensity ;
        num_fract texture_alpha ;
        num_whole texture_grid_size ;
    } ;

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

public :
    shy_logic_room_stateless ( ) ;
private :
    shy_logic_room_stateless < mediator > & operator= ( const shy_logic_room_stateless < mediator > & ) ;
public :
    const logic_room_stateless_consts_type logic_room_stateless_consts ;
} ;

template < typename mediator >
shy_logic_room_stateless < mediator > :: logic_room_stateless_consts_type :: logic_room_stateless_consts_type ( )
{
    platform_math :: make_num_fract ( mesh_color_left_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_left_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_left_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_left_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_color_right_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_right_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_right_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_right_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_color_near_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_near_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_near_b , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_near_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_color_far_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_far_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_far_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_far_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_color_top_r , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_top_g , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_top_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_top_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_color_bottom_r , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_bottom_g , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_bottom_b , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_color_bottom_a , 1 , 1 ) ;

    platform_math :: make_num_fract ( mesh_position_x , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_position_y , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_position_z , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_x_left , - 10 , 1 ) ;
    platform_math :: make_num_fract ( mesh_x_right , 10 , 1 ) ;

    platform_math :: make_num_fract ( mesh_y_top , 3 , 1 ) ; 
    platform_math :: make_num_fract ( mesh_y_bottom , - 3 , 1 ) ;

    platform_math :: make_num_fract ( mesh_z_near , 10 , 1 ) ;
    platform_math :: make_num_fract ( mesh_z_far , - 10 , 1 ) ;

    platform_math :: make_num_fract ( mesh_right_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_right_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_right_side_v_top , 1 , 3 ) ;
    platform_math :: make_num_fract ( mesh_right_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_left_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_left_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_left_side_v_top , 1 , 3 ) ;
    platform_math :: make_num_fract ( mesh_left_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_near_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_near_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_near_side_v_top , 1 , 3 ) ;
    platform_math :: make_num_fract ( mesh_near_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_far_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_far_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_far_side_v_top , 1 , 3 ) ;
    platform_math :: make_num_fract ( mesh_far_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_top_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_top_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_top_side_v_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_top_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( mesh_bottom_side_u_left , 0 , 1 ) ;
    platform_math :: make_num_fract ( mesh_bottom_side_u_right , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_bottom_side_v_top , 1 , 1 ) ;
    platform_math :: make_num_fract ( mesh_bottom_side_v_bottom , 0 , 1 ) ;

    platform_math :: make_num_fract ( room_show_time , 10 , 1 ) ;

    platform_math :: make_num_fract ( texture_pen_intensity , 1 , 1 ) ;
    platform_math :: make_num_fract ( texture_paper_intensity , 1 , 2 ) ;
    platform_math :: make_num_fract ( texture_alpha , 1 , 1 ) ;
    platform_math :: make_num_whole ( texture_grid_size , 10 ) ;
}

template < typename mediator >
shy_logic_room_stateless < mediator > :: shy_logic_room_stateless ( )
{
}

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
}

