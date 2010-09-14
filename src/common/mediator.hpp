template < typename mediator_types >
class shy_mediator
{
public :
    class messages ;

    typedef typename mediator_types :: platform platform ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_camera engine_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_math engine_math ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless engine_render_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_stateless logic_main_menu_letters_layout_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_stateless logic_main_menu_letters_meshes_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_stateless logic_main_menu_selection_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless logic_main_menu_stateless ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless logic_text_stateless ;
    
private :
    class receivers ;

    typedef typename mediator_types :: platform :: platform_pointer platform_pointer ;

    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: engine_render_stateless_consts_type engine_render_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_stateless :: logic_main_menu_letters_layout_stateless_consts_type logic_main_menu_letters_layout_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_stateless_consts_type logic_main_menu_letters_meshes_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_stateless :: logic_main_menu_selection_stateless_consts_type logic_main_menu_selection_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless :: logic_main_menu_stateless_consts_type logic_main_menu_stateless_consts_type ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: logic_text_stateless_consts_type logic_text_stateless_consts_type ;

	typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer engine_rasterizer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render engine_render ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application logic_application ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera logic_camera ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_core logic_core ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities logic_entities ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget logic_fidget ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game logic_game ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image logic_image ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_land logic_land ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu logic_main_menu ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation logic_main_menu_letters_animation ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_appear logic_main_menu_letters_animation_appear ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_disappear logic_main_menu_letters_animation_disappear ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_idle logic_main_menu_letters_animation_idle ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_creation_director logic_main_menu_letters_creation_director ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_position logic_main_menu_letters_layout_position ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_row_rect logic_main_menu_letters_layout_row_rect ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_creation_director logic_main_menu_letters_meshes_creation_director ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_creator logic_main_menu_letters_meshes_creator ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_destroyer logic_main_menu_letters_meshes_destroyer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_placement logic_main_menu_letters_meshes_placement ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_renderer logic_main_menu_letters_meshes_renderer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_storage logic_main_menu_letters_meshes_storage ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_storage logic_main_menu_letters_storage ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_renderer logic_main_menu_renderer ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation logic_main_menu_selection_animation ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation_idle logic_main_menu_selection_animation_idle ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_mesh logic_main_menu_selection_mesh ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_tracker logic_main_menu_selection_tracker ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_sound logic_sound ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text logic_text ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title logic_title ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch logic_touch ;

	typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer_stateless :: engine_rasterizer_messages engine_rasterizer_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: engine_render_messages engine_render_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application_stateless :: logic_application_messages logic_application_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera_stateless :: logic_camera_messages logic_camera_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_core_stateless :: logic_core_messages logic_core_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities_stateless :: logic_entities_messages logic_entities_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget_stateless :: logic_fidget_messages logic_fidget_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game_stateless :: logic_game_messages logic_game_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image_stateless :: logic_image_messages logic_image_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_land_stateless :: logic_land_messages logic_land_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_stateless :: logic_main_menu_letters_animation_messages logic_main_menu_letters_animation_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_stateless :: logic_main_menu_letters_layout_messages logic_main_menu_letters_layout_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_stateless :: logic_main_menu_letters_meshes_messages logic_main_menu_letters_meshes_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_stateless :: logic_main_menu_letters_messages logic_main_menu_letters_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation_stateless :: logic_main_menu_selection_animation_messages logic_main_menu_selection_animation_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_stateless :: logic_main_menu_selection_messages logic_main_menu_selection_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless :: logic_main_menu_messages logic_main_menu_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_sound_stateless :: logic_sound_messages logic_sound_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: logic_text_messages logic_text_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title_stateless :: logic_title_messages logic_title_messages ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch_stateless :: logic_touch_messages logic_touch_messages ;

    typedef typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer_stateless :: template engine_rasterizer_sender < receivers > engine_rasterizer_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: engine_render_stateless :: template engine_render_sender < receivers > engine_render_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_application_stateless :: template logic_application_sender < receivers > logic_application_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_camera_stateless :: template logic_camera_sender < receivers > logic_camera_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_core_stateless :: template logic_core_sender < receivers > logic_core_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_entities_stateless :: template logic_entities_sender < receivers > logic_entities_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_fidget_stateless :: template logic_fidget_sender < receivers > logic_fidget_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_game_stateless :: template logic_game_sender < receivers > logic_game_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_image_stateless :: template logic_image_sender < receivers > logic_image_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_land_stateless :: template logic_land_sender < receivers > logic_land_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_stateless :: template logic_main_menu_letters_animation_sender < receivers > logic_main_menu_letters_animation_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_stateless :: template logic_main_menu_letters_layout_sender < receivers > logic_main_menu_letters_layout_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_stateless :: template logic_main_menu_letters_meshes_sender < receivers > logic_main_menu_letters_meshes_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_stateless :: template logic_main_menu_letters_sender < receivers > logic_main_menu_letters_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation_stateless :: template logic_main_menu_selection_animation_sender < receivers > logic_main_menu_selection_animation_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_stateless :: template logic_main_menu_selection_sender < receivers > logic_main_menu_selection_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_stateless :: template logic_main_menu_sender < receivers > logic_main_menu_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_sound_stateless :: template logic_sound_sender < receivers > logic_sound_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_text_stateless :: template logic_text_sender < receivers > logic_text_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_title_stateless :: template logic_title_sender < receivers > logic_title_sender ;
    typedef typename mediator_types :: template modules < shy_mediator > :: logic_touch_stateless :: template logic_touch_sender < receivers > logic_touch_sender ;
    
public :
    class messages
    : public engine_rasterizer_messages
    , public engine_render_messages
    , public logic_application_messages
    , public logic_camera_messages
    , public logic_core_messages
    , public logic_entities_messages
    , public logic_fidget_messages
    , public logic_game_messages
    , public logic_image_messages
    , public logic_land_messages
    , public logic_main_menu_letters_animation_messages
    , public logic_main_menu_letters_layout_messages
    , public logic_main_menu_letters_meshes_messages
    , public logic_main_menu_letters_messages
    , public logic_main_menu_selection_animation_messages
    , public logic_main_menu_selection_messages
    , public logic_main_menu_messages
    , public logic_sound_messages
    , public logic_text_messages
	, public logic_title_messages
	, public logic_touch_messages
    {
    } ;

private :
    class sender
    : public engine_rasterizer_sender
    , public engine_render_sender
    , public logic_application_sender
    , public logic_camera_sender
    , public logic_core_sender
    , public logic_entities_sender
    , public logic_fidget_sender
    , public logic_game_sender
    , public logic_image_sender
    , public logic_land_sender
    , public logic_main_menu_letters_animation_sender
    , public logic_main_menu_letters_layout_sender
    , public logic_main_menu_letters_meshes_sender
    , public logic_main_menu_letters_sender
    , public logic_main_menu_selection_animation_sender
    , public logic_main_menu_selection_sender
    , public logic_main_menu_sender
    , public logic_sound_sender
    , public logic_text_sender
	, public logic_title_sender
	, public logic_touch_sender
    {
    public :    
        using engine_rasterizer_sender :: send ;
        using engine_render_sender :: send ;
        using logic_application_sender :: send ;
        using logic_camera_sender :: send ;
        using logic_core_sender :: send ;
        using logic_entities_sender :: send ;
        using logic_fidget_sender :: send ;
        using logic_game_sender :: send ;
        using logic_image_sender :: send ;
        using logic_land_sender :: send ;
        using logic_main_menu_letters_animation_sender :: send ;
        using logic_main_menu_letters_layout_sender :: send ;
        using logic_main_menu_letters_meshes_sender :: send ;
        using logic_main_menu_letters_sender :: send ;
        using logic_main_menu_selection_animation_sender :: send ;
        using logic_main_menu_selection_sender :: send ;
        using logic_main_menu_sender :: send ;
        using logic_sound_sender :: send ;
        using logic_text_sender :: send ;
		using logic_title_sender :: send ;
		using logic_touch_sender :: send ;
        
        void set_receivers ( typename platform_pointer :: template pointer < const receivers > ) ;
    } ;

    class receivers
    {
    public :
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: engine_rasterizer > engine_rasterizer ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: engine_render > engine_render ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_application > logic_application ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_camera > logic_camera ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_core > logic_core ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_entities > logic_entities ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_fidget > logic_fidget ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_game > logic_game ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_image > logic_image ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_land > logic_land ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu > logic_main_menu ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation > logic_main_menu_letters_animation ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_appear > logic_main_menu_letters_animation_appear ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_disappear > logic_main_menu_letters_animation_disappear ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_animation_idle > logic_main_menu_letters_animation_idle ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_creation_director > logic_main_menu_letters_creation_director ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_position > logic_main_menu_letters_layout_position ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_layout_row_rect > logic_main_menu_letters_layout_row_rect ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_creation_director > logic_main_menu_letters_meshes_creation_director ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_creator > logic_main_menu_letters_meshes_creator ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_destroyer > logic_main_menu_letters_meshes_destroyer ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_placement > logic_main_menu_letters_meshes_placement ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_renderer > logic_main_menu_letters_meshes_renderer ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_meshes_storage > logic_main_menu_letters_meshes_storage ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_letters_storage > logic_main_menu_letters_storage ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_renderer > logic_main_menu_renderer ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation > logic_main_menu_selection_animation ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_animation_idle > logic_main_menu_selection_animation_idle ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_mesh > logic_main_menu_selection_mesh ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_main_menu_selection_tracker > logic_main_menu_selection_tracker ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_sound > logic_sound ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_text > logic_text ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_title > logic_title ;
        typename platform_pointer :: template pointer < typename mediator_types :: template modules < shy_mediator > :: logic_touch > logic_touch ;
    } ;

public :
    shy_mediator ( typename platform_pointer :: template pointer < const platform > ) ;
    void engine_render_stateless_consts ( typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > & ) ;
    void logic_main_menu_letters_layout_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_letters_layout_stateless_consts_type > & ) ;
    void logic_main_menu_letters_meshes_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_letters_meshes_stateless_consts_type > & ) ;
    void logic_main_menu_selection_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_selection_stateless_consts_type > & ) ;
    void logic_main_menu_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > & ) ;
    void logic_text_stateless_consts ( typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > & ) ;
    void platform_obj ( typename platform_pointer :: template pointer < const platform > & ) ;
    void register_modules
        ( typename platform_pointer :: template pointer < engine_rasterizer >
        , typename platform_pointer :: template pointer < engine_render >
        , typename platform_pointer :: template pointer < engine_render_stateless >
        , typename platform_pointer :: template pointer < logic_application >
        , typename platform_pointer :: template pointer < logic_camera >
        , typename platform_pointer :: template pointer < logic_core >
        , typename platform_pointer :: template pointer < logic_entities >
        , typename platform_pointer :: template pointer < logic_fidget >
        , typename platform_pointer :: template pointer < logic_game >
        , typename platform_pointer :: template pointer < logic_image >
        , typename platform_pointer :: template pointer < logic_land >
        , typename platform_pointer :: template pointer < logic_main_menu >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_animation >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_appear >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_disappear >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_idle >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_creation_director >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_position >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_row_rect >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_stateless >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creation_director >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creator >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_destroyer >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_placement >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_renderer >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_stateless >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_storage >
        , typename platform_pointer :: template pointer < logic_main_menu_letters_storage >
        , typename platform_pointer :: template pointer < logic_main_menu_renderer >
        , typename platform_pointer :: template pointer < logic_main_menu_selection_animation >
        , typename platform_pointer :: template pointer < logic_main_menu_selection_animation_idle >
        , typename platform_pointer :: template pointer < logic_main_menu_selection_mesh >
        , typename platform_pointer :: template pointer < logic_main_menu_selection_stateless >
        , typename platform_pointer :: template pointer < logic_main_menu_selection_tracker >
        , typename platform_pointer :: template pointer < logic_main_menu_stateless >
        , typename platform_pointer :: template pointer < logic_sound >
        , typename platform_pointer :: template pointer < logic_text >
        , typename platform_pointer :: template pointer < logic_text_stateless >
        , typename platform_pointer :: template pointer < logic_title >
        , typename platform_pointer :: template pointer < logic_touch >
        ) ;
    template < typename message_type >
    void send ( message_type ) ;
private :
    typename platform_pointer :: template pointer < engine_render_stateless > _engine_render_stateless ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_layout_stateless > _logic_main_menu_letters_layout_stateless ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_stateless > _logic_main_menu_letters_meshes_stateless ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_stateless > _logic_main_menu_selection_stateless ;
    typename platform_pointer :: template pointer < logic_main_menu_stateless > _logic_main_menu_stateless ;
    typename platform_pointer :: template pointer < logic_text_stateless > _logic_text_stateless ;
    typename platform_pointer :: template pointer < const platform > _platform ;
    receivers _receivers ;
    sender _sender ;
} ;

template < typename mediator_types >
void shy_mediator < mediator_types > :: sender :: set_receivers ( typename platform_pointer :: template pointer < const receivers > arg_receivers )
{
    engine_rasterizer_sender :: set_receivers ( arg_receivers ) ;
    engine_render_sender :: set_receivers ( arg_receivers ) ;
    logic_application_sender :: set_receivers ( arg_receivers ) ;
    logic_camera_sender :: set_receivers ( arg_receivers ) ;
    logic_core_sender :: set_receivers ( arg_receivers ) ;
    logic_entities_sender :: set_receivers ( arg_receivers ) ;
    logic_fidget_sender :: set_receivers ( arg_receivers ) ;
    logic_game_sender :: set_receivers ( arg_receivers ) ;
    logic_image_sender :: set_receivers ( arg_receivers ) ;
    logic_land_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_letters_animation_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_letters_layout_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_letters_meshes_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_letters_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_selection_animation_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_selection_sender :: set_receivers ( arg_receivers ) ;
    logic_main_menu_sender :: set_receivers ( arg_receivers ) ;
    logic_sound_sender :: set_receivers ( arg_receivers ) ;
    logic_text_sender :: set_receivers ( arg_receivers ) ;
    logic_title_sender :: set_receivers ( arg_receivers ) ;
    logic_touch_sender :: set_receivers ( arg_receivers ) ;
}

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
    , typename platform_pointer :: template pointer < logic_application > arg_logic_application
    , typename platform_pointer :: template pointer < logic_camera > arg_logic_camera
    , typename platform_pointer :: template pointer < logic_core > arg_logic_core
    , typename platform_pointer :: template pointer < logic_entities > arg_logic_entities
    , typename platform_pointer :: template pointer < logic_fidget > arg_logic_fidget
    , typename platform_pointer :: template pointer < logic_game > arg_logic_game
    , typename platform_pointer :: template pointer < logic_image > arg_logic_image
    , typename platform_pointer :: template pointer < logic_land > arg_logic_land
    , typename platform_pointer :: template pointer < logic_main_menu > arg_logic_main_menu
    , typename platform_pointer :: template pointer < logic_main_menu_letters_animation > arg_logic_main_menu_letters_animation
    , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_appear > arg_logic_main_menu_letters_animation_appear
    , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_disappear > arg_logic_main_menu_letters_animation_disappear
    , typename platform_pointer :: template pointer < logic_main_menu_letters_animation_idle > arg_logic_main_menu_letters_animation_idle
    , typename platform_pointer :: template pointer < logic_main_menu_letters_creation_director > arg_logic_main_menu_letters_creation_director
    , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_position > arg_logic_main_menu_letters_layout_position
    , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_row_rect > arg_logic_main_menu_letters_layout_row_rect
    , typename platform_pointer :: template pointer < logic_main_menu_letters_layout_stateless > arg_logic_main_menu_letters_layout_stateless
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creation_director > arg_logic_main_menu_letters_meshes_creation_director
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creator > arg_logic_main_menu_letters_meshes_creator
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_destroyer > arg_logic_main_menu_letters_meshes_destroyer
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_placement > arg_logic_main_menu_letters_meshes_placement
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_renderer > arg_logic_main_menu_letters_meshes_renderer
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_stateless > arg_logic_main_menu_letters_meshes_stateless
    , typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_storage > arg_logic_main_menu_letters_meshes_storage
    , typename platform_pointer :: template pointer < logic_main_menu_letters_storage > arg_logic_main_menu_letters_storage
    , typename platform_pointer :: template pointer < logic_main_menu_renderer > arg_logic_main_menu_renderer
    , typename platform_pointer :: template pointer < logic_main_menu_selection_animation > arg_logic_main_menu_selection_animation
    , typename platform_pointer :: template pointer < logic_main_menu_selection_animation_idle > arg_logic_main_menu_selection_animation_idle
    , typename platform_pointer :: template pointer < logic_main_menu_selection_mesh > arg_logic_main_menu_selection_mesh
    , typename platform_pointer :: template pointer < logic_main_menu_selection_stateless > arg_logic_main_menu_selection_stateless
    , typename platform_pointer :: template pointer < logic_main_menu_selection_tracker > arg_logic_main_menu_selection_tracker
    , typename platform_pointer :: template pointer < logic_main_menu_stateless > arg_logic_main_menu_stateless
    , typename platform_pointer :: template pointer < logic_sound > arg_logic_sound
    , typename platform_pointer :: template pointer < logic_text > arg_logic_text
    , typename platform_pointer :: template pointer < logic_text_stateless > arg_logic_text_stateless
    , typename platform_pointer :: template pointer < logic_title > arg_logic_title
    , typename platform_pointer :: template pointer < logic_touch > arg_logic_touch
    )
{
    _engine_render_stateless = arg_engine_render_stateless ;
    _logic_main_menu_letters_layout_stateless = arg_logic_main_menu_letters_layout_stateless ;
    _logic_main_menu_letters_meshes_stateless = arg_logic_main_menu_letters_meshes_stateless ;
    _logic_main_menu_selection_stateless = arg_logic_main_menu_selection_stateless ;
    _logic_main_menu_stateless = arg_logic_main_menu_stateless ;
    _logic_text_stateless = arg_logic_text_stateless ;
    
    _receivers . engine_rasterizer = arg_engine_rasterizer ;
    _receivers . engine_render = arg_engine_render ;
    _receivers . logic_application = arg_logic_application ;
    _receivers . logic_camera = arg_logic_camera ;
    _receivers . logic_core = arg_logic_core ;
    _receivers . logic_entities = arg_logic_entities ;
    _receivers . logic_fidget = arg_logic_fidget ;
    _receivers . logic_game = arg_logic_game ;
    _receivers . logic_image = arg_logic_image ;
    _receivers . logic_land = arg_logic_land ;
    _receivers . logic_main_menu = arg_logic_main_menu ;
    _receivers . logic_main_menu_letters_animation = arg_logic_main_menu_letters_animation ;
    _receivers . logic_main_menu_letters_animation_appear = arg_logic_main_menu_letters_animation_appear ;
    _receivers . logic_main_menu_letters_animation_disappear = arg_logic_main_menu_letters_animation_disappear ;
    _receivers . logic_main_menu_letters_animation_idle = arg_logic_main_menu_letters_animation_idle ;
    _receivers . logic_main_menu_letters_creation_director = arg_logic_main_menu_letters_creation_director ;
    _receivers . logic_main_menu_letters_layout_position = arg_logic_main_menu_letters_layout_position ;
    _receivers . logic_main_menu_letters_layout_row_rect = arg_logic_main_menu_letters_layout_row_rect ;
    _receivers . logic_main_menu_letters_meshes_creation_director = arg_logic_main_menu_letters_meshes_creation_director ;
    _receivers . logic_main_menu_letters_meshes_creator = arg_logic_main_menu_letters_meshes_creator ;
    _receivers . logic_main_menu_letters_meshes_destroyer = arg_logic_main_menu_letters_meshes_destroyer ;
    _receivers . logic_main_menu_letters_meshes_placement = arg_logic_main_menu_letters_meshes_placement ;
    _receivers . logic_main_menu_letters_meshes_renderer = arg_logic_main_menu_letters_meshes_renderer ;
    _receivers . logic_main_menu_letters_meshes_storage = arg_logic_main_menu_letters_meshes_storage ;
    _receivers . logic_main_menu_letters_storage = arg_logic_main_menu_letters_storage ;
    _receivers . logic_main_menu_renderer = arg_logic_main_menu_renderer ;
    _receivers . logic_main_menu_selection_animation = arg_logic_main_menu_selection_animation ;
    _receivers . logic_main_menu_selection_animation_idle = arg_logic_main_menu_selection_animation_idle ;
    _receivers . logic_main_menu_selection_mesh = arg_logic_main_menu_selection_mesh ;
    _receivers . logic_main_menu_selection_tracker = arg_logic_main_menu_selection_tracker ;
    _receivers . logic_sound = arg_logic_sound ;
    _receivers . logic_text = arg_logic_text ;
    _receivers . logic_title = arg_logic_title ;
    _receivers . logic_touch = arg_logic_touch ;

    typename platform_pointer :: template pointer < const receivers > receivers_ptr ;
    platform_pointer :: bind ( receivers_ptr , _receivers ) ;
    _sender . set_receivers ( receivers_ptr ) ;

    typename platform_pointer :: template pointer < shy_mediator < mediator_types > > mediator_ptr ;
    platform_pointer :: bind ( mediator_ptr , * this ) ;

    _receivers . engine_rasterizer . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . engine_render . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_application . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_camera . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_core . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_entities . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_fidget . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_game . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_image . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_land . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_animation . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_animation_appear . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_animation_disappear . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_animation_idle . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_creation_director . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_layout_position . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_layout_row_rect . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_creation_director . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_creator . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_destroyer . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_placement . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_renderer . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_meshes_storage . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_letters_storage . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_renderer . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_selection_animation . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_selection_animation_idle . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_selection_mesh . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_main_menu_selection_tracker . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_sound . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_text . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_title . get ( ) . set_mediator ( mediator_ptr ) ;
    _receivers . logic_touch . get ( ) . set_mediator ( mediator_ptr ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: platform_obj ( typename platform_pointer :: template pointer < const platform > & result )
{
    result = _platform ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: engine_render_stateless_consts ( typename platform_pointer :: template pointer < const engine_render_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _engine_render_stateless . get ( ) . engine_render_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_main_menu_letters_layout_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_letters_layout_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _logic_main_menu_letters_layout_stateless . get ( ) . logic_main_menu_letters_layout_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_main_menu_letters_meshes_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_letters_meshes_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _logic_main_menu_letters_meshes_stateless . get ( ) . logic_main_menu_letters_meshes_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_main_menu_selection_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_selection_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _logic_main_menu_selection_stateless . get ( ) . logic_main_menu_selection_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_main_menu_stateless_consts ( typename platform_pointer :: template pointer < const logic_main_menu_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _logic_main_menu_stateless . get ( ) . logic_main_menu_stateless_consts ) ;
}

template < typename mediator_types >
void shy_mediator < mediator_types > :: logic_text_stateless_consts ( typename platform_pointer :: template pointer < const logic_text_stateless_consts_type > & result )
{
    platform_pointer :: bind ( result , _logic_text_stateless . get ( ) . logic_text_stateless_consts ) ;
}

template < typename mediator_types >
template < typename message_type >
void shy_mediator < mediator_types > :: send ( message_type msg )
{
    _sender . send ( msg ) ;
}
