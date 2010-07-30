template < typename mediator_types >
class shy_mediator
{
public :
    class messages ;

    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_camera engine_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_math engine_math ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: mesh_id mesh_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: texture_id texture_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless logic_text_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: alphabet_english_type alphabet_english_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: letter_id letter_id ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;
    
private :
    class receivers ;

    typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer engine_rasterizer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render engine_render ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic logic ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application logic_application ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application_stateless logic_application_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera logic_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera_stateless logic_camera_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities logic_entities ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities_stateless logic_entities_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget logic_fidget ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget_stateless logic_fidget_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game logic_game ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game_stateless logic_game_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image logic_image ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image_stateless logic_image_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_land logic_land ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu logic_main_menu ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_storage logic_main_menu_letters_storage ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless logic_main_menu_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_text_creator logic_main_menu_text_creator ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_sound logic_sound ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text logic_text ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title logic_title ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch logic_touch ;
    typedef typename mediator_types :: platform :: platform_math :: num_fract num_fract ;
    typedef typename mediator_types :: platform :: platform_math :: num_whole num_whole ;
    typedef typename mediator_types :: platform :: platform_matrix :: matrix_data matrix_data ;
    typedef typename mediator_types :: platform :: platform_pointer platform_pointer ;
    typedef typename mediator_types :: platform :: platform_render :: index_data index_data ;
    typedef typename mediator_types :: platform :: platform_render :: texel_data texel_data ;
    typedef typename mediator_types :: platform :: platform_render :: texture_resource_id texture_resource_id ;
    typedef typename mediator_types :: platform :: platform_render :: vertex_data vertex_data ;
    typedef typename mediator_types :: platform :: platform_vector :: vector_data vector_data ;

    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: engine_render_messages engine_render_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application_stateless :: logic_application_messages logic_application_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera_stateless :: logic_camera_messages logic_camera_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities_stateless :: logic_entities_messages logic_entities_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget_stateless :: logic_fidget_messages logic_fidget_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game_stateless :: logic_game_messages logic_game_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image_stateless :: logic_image_messages logic_image_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless :: logic_main_menu_messages logic_main_menu_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: logic_text_messages logic_text_messages ;

    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: template engine_render_sender < receivers > engine_render_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application_stateless :: template logic_application_sender < receivers > logic_application_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera_stateless :: template logic_camera_sender < receivers > logic_camera_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities_stateless :: template logic_entities_sender < receivers > logic_entities_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget_stateless :: template logic_fidget_sender < receivers > logic_fidget_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game_stateless :: template logic_game_sender < receivers > logic_game_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image_stateless :: template logic_image_sender < receivers > logic_image_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless :: template logic_main_menu_sender < receivers > logic_main_menu_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: template logic_text_sender < receivers > logic_text_sender ;
    
public :
    class messages
    : public engine_render_messages
    , public logic_application_messages
    , public logic_camera_messages
    , public logic_entities_messages
    , public logic_fidget_messages
    , public logic_game_messages
    , public logic_image_messages
    , public logic_main_menu_messages
    , public logic_text_messages
    {
    public :
        class done { } ;
        class image_prepare_permit { } ;
        class image_prepared { } ;
        class image_render_reply { } ;
        class image_render_request { } ;
        class image_update { } ;
        class init { } ;
        class land_prepare_permit { } ;
        class land_prepared { } ;
        class land_render_reply { } ;
        class land_render_request { } ;
        class land_update { } ;
        class near_plane_distance_reply { public : num_fract distance ; } ;
        class near_plane_distance_request { } ;
        class rasterize_ellipse_in_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_finalize_reply { } ;
        class rasterize_finalize_request { } ;
        class rasterize_rect { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; } ;
        class rasterize_triangle { public : num_whole x1 ; num_whole y1 ; num_whole x2 ; num_whole y2 ; num_whole x3 ; num_whole y3 ; } ;
        class rasterize_use_texel { public : texel_data texel ; } ;
        class rasterize_use_texture { public : texture_id texture ; num_whole origin_x ; num_whole origin_y ; } ;
        class render { } ;
        class sound_prepare_permit { } ;
        class sound_prepared { } ;
        class sound_update { } ;
        class title_finished { } ;
        class title_launch_permit { } ;
        class title_render { } ;
        class title_update { } ;
        class touch_prepare_permit { } ;
        class touch_prepared { } ;
        class touch_render { } ;
        class touch_update { } ;
        class update { } ;
        class use_ortho_projection_reply { } ;
        class use_ortho_projection_request { } ;
        class use_perspective_projection_reply { } ;
        class use_perspective_projection_request { } ;
        class use_text_texture_reply { } ;
        class use_text_texture_request { } ;
        class video_mode_changed { } ;
    } ;

private :
    class sender
    : public engine_render_sender
    , public logic_application_sender
    , public logic_camera_sender
    , public logic_entities_sender
    , public logic_fidget_sender
    , public logic_game_sender
    , public logic_image_sender
    , public logic_main_menu_sender
    , public logic_text_sender
    {
    public :    
        using engine_render_sender :: send ;
        using logic_application_sender :: send ;
        using logic_camera_sender :: send ;
        using logic_entities_sender :: send ;
        using logic_fidget_sender :: send ;
        using logic_game_sender :: send ;
        using logic_image_sender :: send ;
        using logic_main_menu_sender :: send ;
        using logic_text_sender :: send ;
        
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers ) ;
  
        void send ( typename messages :: done msg ) ;
        void send ( typename messages :: image_prepare_permit msg ) ;
        void send ( typename messages :: image_prepared msg ) ;
        void send ( typename messages :: image_render_reply msg ) ;
        void send ( typename messages :: image_render_request msg ) ;
        void send ( typename messages :: image_update msg ) ;
        void send ( typename messages :: init msg ) ;
        void send ( typename messages :: land_prepare_permit msg ) ;
        void send ( typename messages :: land_prepared msg ) ;
        void send ( typename messages :: land_render_reply msg ) ;
        void send ( typename messages :: land_render_request msg ) ;
        void send ( typename messages :: land_update msg ) ;
        void send ( typename messages :: near_plane_distance_reply msg ) ;
        void send ( typename messages :: near_plane_distance_request msg ) ;
        void send ( typename messages :: rasterize_ellipse_in_rect msg ) ;
        void send ( typename messages :: rasterize_finalize_reply msg ) ;
        void send ( typename messages :: rasterize_finalize_request msg ) ;
        void send ( typename messages :: rasterize_rect msg ) ;
        void send ( typename messages :: rasterize_triangle msg ) ;
        void send ( typename messages :: rasterize_use_texel msg ) ;
        void send ( typename messages :: rasterize_use_texture msg ) ;
        void send ( typename messages :: render msg ) ;
        void send ( typename messages :: sound_prepare_permit msg ) ;
        void send ( typename messages :: sound_prepared msg ) ;
        void send ( typename messages :: sound_update msg ) ;
        void send ( typename messages :: title_finished msg ) ;
        void send ( typename messages :: title_launch_permit msg ) ;
        void send ( typename messages :: title_render msg ) ;
        void send ( typename messages :: title_update msg ) ;
        void send ( typename messages :: touch_prepare_permit msg ) ;
        void send ( typename messages :: touch_prepared msg ) ;
        void send ( typename messages :: touch_render msg ) ;
        void send ( typename messages :: touch_update msg ) ;
        void send ( typename messages :: update msg ) ;
        void send ( typename messages :: use_ortho_projection_reply msg ) ;
        void send ( typename messages :: use_ortho_projection_request msg ) ;
        void send ( typename messages :: use_perspective_projection_reply msg ) ;
        void send ( typename messages :: use_perspective_projection_request msg ) ;
        void send ( typename messages :: use_text_texture_reply msg ) ;
        void send ( typename messages :: use_text_texture_request msg ) ;
        void send ( typename messages :: video_mode_changed msg ) ;
    private :
        typename platform_pointer :: template pointer < const receivers > _receivers ;
    } ;

    class receivers
    {
    public :
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer > engine_rasterizer ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: engine_render > engine_render ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic > logic ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_application > logic_application ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_camera > logic_camera ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_entities > logic_entities ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_fidget > logic_fidget ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_game > logic_game ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_image > logic_image ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_land > logic_land ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu > logic_main_menu ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_storage > logic_main_menu_letters_storage ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_text_creator > logic_main_menu_text_creator ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_sound > logic_sound ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_text > logic_text ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_title > logic_title ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_touch > logic_touch ;
    } ;

public :
    shy_mediator ( typename platform_pointer :: template pointer < const platform > arg_platform ) ;
    void logic_text_stateless_consts ( typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > & result ) ;
    void engine_render_stateless_consts ( typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > & result ) ;
    void platform_obj ( typename platform_pointer :: template pointer < const platform > & result ) ;
    void register_modules
        ( typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
        , typename platform_pointer :: template pointer < engine_render > arg_engine_render
        , typename platform_pointer :: template pointer < engine_render_stateless > arg_engine_render_stateless
        , typename platform_pointer :: template pointer < logic > arg_logic
        , typename platform_pointer :: template pointer < logic_application > arg_logic_application
        , typename platform_pointer :: template pointer < logic_application_stateless > arg_logic_application_stateless
        , typename platform_pointer :: template pointer < logic_camera > arg_logic_camera
        , typename platform_pointer :: template pointer < logic_camera_stateless > arg_logic_camera_stateless
        , typename platform_pointer :: template pointer < logic_entities > arg_logic_entities
        , typename platform_pointer :: template pointer < logic_entities_stateless > arg_logic_entities_stateless
        , typename platform_pointer :: template pointer < logic_fidget > arg_logic_fidget
        , typename platform_pointer :: template pointer < logic_fidget_stateless > arg_logic_fidget_stateless
        , typename platform_pointer :: template pointer < logic_game > arg_logic_game
        , typename platform_pointer :: template pointer < logic_game_stateless > arg_logic_game_stateless
        , typename platform_pointer :: template pointer < logic_image > arg_logic_image
        , typename platform_pointer :: template pointer < logic_image_stateless > arg_logic_image_stateless
        , typename platform_pointer :: template pointer < logic_land > arg_logic_land
        , typename platform_pointer :: template pointer < logic_main_menu > arg_logic_main_menu
        , typename platform_pointer :: template pointer < logic_main_menu_letters_storage > arg_logic_main_menu_letters_storage
        , typename platform_pointer :: template pointer < logic_main_menu_stateless > arg_logic_main_menu_stateless
        , typename platform_pointer :: template pointer < logic_main_menu_text_creator > arg_logic_main_menu_text_creator
        , typename platform_pointer :: template pointer < logic_sound > arg_logic_sound
        , typename platform_pointer :: template pointer < logic_text > arg_logic_text
        , typename platform_pointer :: template pointer < logic_text_stateless > arg_logic_text_stateless
        , typename platform_pointer :: template pointer < logic_title > arg_logic_title
        , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
        ) ;
    template < typename message_type >
    void send ( message_type msg ) ;
private :
    typename platform_pointer :: template pointer < engine_render_stateless > _engine_render_stateless ;
    typename platform_pointer :: template pointer < logic_application_stateless > _logic_application_stateless ;
    typename platform_pointer :: template pointer < logic_camera_stateless > _logic_camera_stateless ;
    typename platform_pointer :: template pointer < logic_entities_stateless > _logic_entities_stateless ;
    typename platform_pointer :: template pointer < logic_fidget_stateless > _logic_fidget_stateless ;
    typename platform_pointer :: template pointer < logic_game_stateless > _logic_game_stateless ;
    typename platform_pointer :: template pointer < logic_image_stateless > _logic_image_stateless ;
    typename platform_pointer :: template pointer < logic_main_menu_stateless > _logic_main_menu_stateless ;
    typename platform_pointer :: template pointer < logic_text_stateless > _logic_text_stateless ;
    typename platform_pointer :: template pointer < const platform > _platform ;
    receivers _receivers ;
    sender _sender ;
} ;

template < typename mediator_types >
shy_mediator < mediator_types > :: shy_mediator ( typename platform_pointer :: template pointer < const platform > arg_platform )
{
    _platform = arg_platform ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: register_modules
    ( typename platform_pointer :: template pointer < engine_rasterizer > arg_engine_rasterizer
    , typename platform_pointer :: template pointer < engine_render > arg_engine_render
    , typename platform_pointer :: template pointer < engine_render_stateless > arg_engine_render_stateless
    , typename platform_pointer :: template pointer < logic > arg_logic
    , typename platform_pointer :: template pointer < logic_application > arg_logic_application
    , typename platform_pointer :: template pointer < logic_application_stateless > arg_logic_application_stateless
    , typename platform_pointer :: template pointer < logic_camera > arg_logic_camera
    , typename platform_pointer :: template pointer < logic_camera_stateless > arg_logic_camera_stateless
    , typename platform_pointer :: template pointer < logic_entities > arg_logic_entities
    , typename platform_pointer :: template pointer < logic_entities_stateless > arg_logic_entities_stateless
    , typename platform_pointer :: template pointer < logic_fidget > arg_logic_fidget
    , typename platform_pointer :: template pointer < logic_fidget_stateless > arg_logic_fidget_stateless
    , typename platform_pointer :: template pointer < logic_game > arg_logic_game
    , typename platform_pointer :: template pointer < logic_game_stateless > arg_logic_game_stateless
    , typename platform_pointer :: template pointer < logic_image > arg_logic_image
    , typename platform_pointer :: template pointer < logic_image_stateless > arg_logic_image_stateless
    , typename platform_pointer :: template pointer < logic_land > arg_logic_land
    , typename platform_pointer :: template pointer < logic_main_menu > arg_logic_main_menu
    , typename platform_pointer :: template pointer < logic_main_menu_letters_storage > arg_logic_main_menu_letters_storage
    , typename platform_pointer :: template pointer < logic_main_menu_stateless > arg_logic_main_menu_stateless
    , typename platform_pointer :: template pointer < logic_main_menu_text_creator > arg_logic_main_menu_text_creator
    , typename platform_pointer :: template pointer < logic_sound > arg_logic_sound
    , typename platform_pointer :: template pointer < logic_text > arg_logic_text
    , typename platform_pointer :: template pointer < logic_text_stateless > arg_logic_text_stateless
    , typename platform_pointer :: template pointer < logic_title > arg_logic_title
    , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
    )
{
    _engine_render_stateless = arg_engine_render_stateless ;
    _logic_application_stateless = arg_logic_application_stateless ;
    _logic_camera_stateless = arg_logic_camera_stateless ;
    _logic_entities_stateless = arg_logic_entities_stateless ;
    _logic_fidget_stateless = arg_logic_fidget_stateless ;
    _logic_game_stateless = arg_logic_game_stateless ;
    _logic_image_stateless = arg_logic_image_stateless ;
    _logic_main_menu_stateless = arg_logic_main_menu_stateless ;
    _logic_text_stateless = arg_logic_text_stateless ;
    
    _receivers . engine_rasterizer = arg_engine_rasterizer ;
    _receivers . engine_render = arg_engine_render ;
    _receivers . logic = arg_logic ;
    _receivers . logic_application = arg_logic_application ;
    _receivers . logic_camera = arg_logic_camera ;
    _receivers . logic_entities = arg_logic_entities ;
    _receivers . logic_fidget = arg_logic_fidget ;
    _receivers . logic_game = arg_logic_game ;
    _receivers . logic_image = arg_logic_image ;
    _receivers . logic_land = arg_logic_land ;
    _receivers . logic_main_menu = arg_logic_main_menu ;
    _receivers . logic_main_menu_letters_storage = arg_logic_main_menu_letters_storage ;
    _receivers . logic_main_menu_text_creator = arg_logic_main_menu_text_creator ;
    _receivers . logic_sound = arg_logic_sound ;
    _receivers . logic_text = arg_logic_text ;
    _receivers . logic_title = arg_logic_title ;
    _receivers . logic_touch = arg_logic_touch ;

    _sender . set_receivers ( _receivers ) ;

    _receivers . engine_rasterizer . get ( ) . set_mediator ( * this ) ;
    _receivers . engine_render . get ( ) . set_mediator ( * this ) ;
    _receivers . logic . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_application . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_camera . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_entities . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_fidget . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_game . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_image . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_land . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_main_menu . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_main_menu_letters_storage . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_main_menu_text_creator . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_sound . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_text . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_title . get ( ) . set_mediator ( * this ) ;
    _receivers . logic_touch . get ( ) . set_mediator ( * this ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: platform_obj ( typename platform_pointer :: template pointer < const platform > & result )
{
    result = _platform ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: engine_render_stateless_consts ( typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > & result )
{
    result . set ( _engine_render_stateless . get ( ) . engine_render_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_text_stateless_consts ( typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > & result )
{
    result . set ( _logic_text_stateless . get ( ) . logic_text_stateless_consts ) ;
}

template < typename mediator_types >
template < typename message_type >
void shy_mediator < mediator_types > :: send ( message_type msg )
{
    _sender . send ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    _receivers = arg_receivers ;
    engine_render_sender :: set_receivers ( arg_receivers ) ;
    logic_application_sender :: set_receivers ( arg_receivers ) ;
    logic_camera_sender :: set_receivers ( arg_receivers ) ;
    logic_entities_sender :: set_receivers ( arg_receivers ) ;
    logic_fidget_sender :: set_receivers ( arg_receivers ) ;
    logic_game_sender :: set_receivers ( arg_receivers ) ;
    logic_image_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_sender :: set_receivers ( arg_receivers ) ;
    logic_text_sender :: set_receivers ( arg_receivers ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: done msg )
{
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: near_plane_distance_request msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: near_plane_distance_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: image_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: init msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . engine_render . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_camera . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_entities . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_fidget . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_main_menu_letters_storage . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: land_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: image_prepare_permit msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: land_prepare_permit msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: sound_prepare_permit msg )
{
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: touch_prepare_permit msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_use_texel msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_ellipse_in_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_finalize_reply msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_finalize_request msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_rect msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_use_texture msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: rasterize_triangle msg )
{
    _receivers . get ( ) . engine_rasterizer . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: render msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: image_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: image_render_request msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: land_render_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: land_render_request msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: touch_render msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: sound_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: update msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: touch_update msg )
{
    _receivers . get ( ) . logic_touch . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: sound_update msg )
{
    _receivers . get ( ) . logic_sound . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: land_update msg )
{
    _receivers . get ( ) . logic_land . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: image_update msg )
{
    _receivers . get ( ) . logic_image . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: title_finished msg )
{
    _receivers . get ( ) . logic_application . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: title_launch_permit msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: title_render msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: title_update msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: touch_prepared msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: video_mode_changed msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_perspective_projection_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_perspective_projection_request msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_ortho_projection_request msg )
{
    _receivers . get ( ) . logic . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_ortho_projection_reply msg )
{
    _receivers . get ( ) . logic_game . get ( ) . receive ( msg ) ;
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_text_texture_request msg )
{
    _receivers . get ( ) . logic_text . get ( ) . receive ( msg ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: send ( typename messages :: use_text_texture_reply msg )
{
    _receivers . get ( ) . logic_title . get ( ) . receive ( msg ) ;
}
