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
        class logic_core_near_plane_distance_reply { public : num_fract distance ; } ;
        class logic_core_near_plane_distance_request { } ;
        class logic_core_use_ortho_projection_reply { } ;
        class logic_core_use_ortho_projection_request { } ;
        class logic_core_use_perspective_projection_reply { } ;
        class logic_core_use_perspective_projection_request { } ;
        class render { } ;
        class update { } ;
        class video_mode_changed { } ;
    } ;

    template < typename receivers >
    class logic_core_sender
    {
    public :
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
        void send ( typename logic_core_messages :: done ) ;
        void send ( typename logic_core_messages :: init ) ;
        void send ( typename logic_core_messages :: logic_core_near_plane_distance_reply ) ;
        void send ( typename logic_core_messages :: logic_core_near_plane_distance_request ) ;
        void send ( typename logic_core_messages :: logic_core_use_ortho_projection_reply ) ;
        void send ( typename logic_core_messages :: logic_core_use_ortho_projection_request ) ;
        void send ( typename logic_core_messages :: logic_core_use_perspective_projection_reply ) ;
        void send ( typename logic_core_messages :: logic_core_use_perspective_projection_request ) ;
        void send ( typename logic_core_messages :: render ) ;
        void send ( typename logic_core_messages :: update ) ;
        void send ( typename logic_core_messages :: video_mode_changed ) ;
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
    _receivers . get ( ) . logic_amusement . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation_disappear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_animation_fit . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_placement . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_blanket_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_controls . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_placement . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_door_texture . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_animation_shake . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_choice . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_disappear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_idle . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_selection . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_push . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_selection_weight . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_animation_unselection_weight . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout_position . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_layout_row_rect . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creation_director . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_creator . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_destroyer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_placement . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_meshes_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_appear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_disappear . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_idle . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_idle_attention . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_push . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_push_attention . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_push_weight . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_select . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_animation_unselect . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_tracker . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_selection_tracking_director . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_observer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_observer_animation . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_observer_animation_flight . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_observer_size . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_perspective . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_mesh . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_room_texture . get ( ) . receive ( msg ) ;
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
:: send ( typename logic_core_messages :: logic_core_near_plane_distance_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_observer_size . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: logic_core_near_plane_distance_request msg )
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
:: send ( typename logic_core_messages :: logic_core_use_ortho_projection_reply msg )
{
    _receivers . get ( ) . logic_amusement_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_renderer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: logic_core_use_ortho_projection_request msg )
{
    _receivers . get ( ) . logic_core . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: logic_core_use_perspective_projection_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator >
template < typename receivers >
void shy_logic_core_stateless < mediator >
:: logic_core_sender < receivers >
:: send ( typename logic_core_messages :: logic_core_use_perspective_projection_request msg )
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
