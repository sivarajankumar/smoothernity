template 
    < typename _platform
    , template < typename mediator > class _engine_camera
    , template < typename mediator > class _engine_math
    , template < typename mediator > class _engine_rasterizer
    , template < typename mediator > class _engine_rasterizer_stateless
    , template < typename mediator > class _engine_render
    , template < typename mediator > class _engine_render_stateless
    , template < typename mediator > class _logic_amusement
    , template < typename mediator > class _logic_amusement_renderer
    , template < typename mediator > class _logic_amusement_stateless
    , template < typename mediator > class _logic_application
    , template < typename mediator > class _logic_application_stateless
    , template < typename mediator > class _logic_camera
    , template < typename mediator > class _logic_camera_stateless
    , template < typename mediator > class _logic_controls
    , template < typename mediator > class _logic_controls_stateless
    , template < typename mediator > class _logic_core
    , template < typename mediator > class _logic_core_stateless
    , template < typename mediator > class _logic_door
    , template < typename mediator > class _logic_door_mesh
    , template < typename mediator > class _logic_door_stateless
    , template < typename mediator > class _logic_entities
    , template < typename mediator > class _logic_entities_stateless
    , template < typename mediator > class _logic_fidget
    , template < typename mediator > class _logic_fidget_stateless
    , template < typename mediator > class _logic_game
    , template < typename mediator > class _logic_game_stateless
    , template < typename mediator > class _logic_image
    , template < typename mediator > class _logic_image_stateless
    , template < typename mediator > class _logic_land
    , template < typename mediator > class _logic_land_stateless
    , template < typename mediator > class _logic_main_menu
    , template < typename mediator > class _logic_main_menu_animation
    , template < typename mediator > class _logic_main_menu_animation_shake
    , template < typename mediator > class _logic_main_menu_animation_stateless
    , template < typename mediator > class _logic_main_menu_choice
    , template < typename mediator > class _logic_main_menu_letters_animation
    , template < typename mediator > class _logic_main_menu_letters_animation_appear
    , template < typename mediator > class _logic_main_menu_letters_animation_disappear
    , template < typename mediator > class _logic_main_menu_letters_animation_idle
    , template < typename mediator > class _logic_main_menu_letters_animation_selection
    , template < typename mediator > class _logic_main_menu_letters_animation_selection_push
    , template < typename mediator > class _logic_main_menu_letters_animation_selection_weight
    , template < typename mediator > class _logic_main_menu_letters_animation_stateless
    , template < typename mediator > class _logic_main_menu_letters_animation_unselection_weight
    , template < typename mediator > class _logic_main_menu_letters_creation_director
    , template < typename mediator > class _logic_main_menu_letters_layout_position
    , template < typename mediator > class _logic_main_menu_letters_layout_row_rect
    , template < typename mediator > class _logic_main_menu_letters_layout_stateless
    , template < typename mediator > class _logic_main_menu_letters_meshes_creation_director
    , template < typename mediator > class _logic_main_menu_letters_meshes_creator
    , template < typename mediator > class _logic_main_menu_letters_meshes_destroyer
    , template < typename mediator > class _logic_main_menu_letters_meshes_placement
    , template < typename mediator > class _logic_main_menu_letters_meshes_renderer
    , template < typename mediator > class _logic_main_menu_letters_meshes_stateless
    , template < typename mediator > class _logic_main_menu_letters_meshes_storage
    , template < typename mediator > class _logic_main_menu_letters_stateless
    , template < typename mediator > class _logic_main_menu_letters_storage
    , template < typename mediator > class _logic_main_menu_renderer
    , template < typename mediator > class _logic_main_menu_selection_animation
    , template < typename mediator > class _logic_main_menu_selection_animation_appear
    , template < typename mediator > class _logic_main_menu_selection_animation_disappear
    , template < typename mediator > class _logic_main_menu_selection_animation_idle
    , template < typename mediator > class _logic_main_menu_selection_animation_idle_attention
    , template < typename mediator > class _logic_main_menu_selection_animation_push
    , template < typename mediator > class _logic_main_menu_selection_animation_push_attention
    , template < typename mediator > class _logic_main_menu_selection_animation_push_weight
    , template < typename mediator > class _logic_main_menu_selection_animation_select
    , template < typename mediator > class _logic_main_menu_selection_animation_stateless
    , template < typename mediator > class _logic_main_menu_selection_animation_unselect
    , template < typename mediator > class _logic_main_menu_selection_mesh
    , template < typename mediator > class _logic_main_menu_selection_stateless
    , template < typename mediator > class _logic_main_menu_selection_tracker
    , template < typename mediator > class _logic_main_menu_selection_tracking_director
    , template < typename mediator > class _logic_main_menu_stateless
    , template < typename mediator > class _logic_room
    , template < typename mediator > class _logic_room_mesh
    , template < typename mediator > class _logic_room_renderer
    , template < typename mediator > class _logic_room_stateless
    , template < typename mediator > class _logic_room_texture
    , template < typename mediator > class _logic_sound
    , template < typename mediator > class _logic_sound_stateless
    , template < typename mediator > class _logic_text
    , template < typename mediator > class _logic_text_stateless
    , template < typename mediator > class _logic_title
    , template < typename mediator > class _logic_title_stateless
    , template < typename mediator > class _logic_touch
    , template < typename mediator > class _logic_touch_stateless
    >
class mediator_types
{
public :
    typedef _platform platform ;
    template < typename mediator >
    class modules
    {
    public :
        typedef _engine_camera < mediator > engine_camera ;
        typedef _engine_math < mediator > engine_math ;
        typedef _engine_rasterizer < mediator > engine_rasterizer ;
        typedef _engine_rasterizer_stateless < mediator > engine_rasterizer_stateless ;
        typedef _engine_render < mediator > engine_render ;
        typedef _engine_render_stateless < mediator > engine_render_stateless ;
        typedef _logic_amusement < mediator > logic_amusement ;
        typedef _logic_amusement_renderer < mediator > logic_amusement_renderer ;
        typedef _logic_amusement_stateless < mediator > logic_amusement_stateless ;
        typedef _logic_application < mediator > logic_application ;
        typedef _logic_application_stateless < mediator > logic_application_stateless ;
        typedef _logic_camera < mediator > logic_camera ;
        typedef _logic_camera_stateless < mediator > logic_camera_stateless ;
        typedef _logic_controls < mediator > logic_controls ;
        typedef _logic_controls_stateless < mediator > logic_controls_stateless ;
        typedef _logic_core < mediator > logic_core ;
        typedef _logic_core_stateless < mediator > logic_core_stateless ;
        typedef _logic_door < mediator > logic_door ;
        typedef _logic_door_mesh < mediator > logic_door_mesh ;
        typedef _logic_door_stateless < mediator > logic_door_stateless ;
        typedef _logic_entities < mediator > logic_entities ;
        typedef _logic_entities_stateless < mediator > logic_entities_stateless ;
        typedef _logic_fidget < mediator > logic_fidget ;
        typedef _logic_fidget_stateless < mediator > logic_fidget_stateless ;
        typedef _logic_game < mediator > logic_game ;
        typedef _logic_game_stateless < mediator > logic_game_stateless ;
        typedef _logic_image < mediator > logic_image ;
        typedef _logic_image_stateless < mediator > logic_image_stateless ;
        typedef _logic_land < mediator > logic_land ;
        typedef _logic_land_stateless < mediator > logic_land_stateless ;
        typedef _logic_main_menu < mediator > logic_main_menu ;
        typedef _logic_main_menu_animation < mediator > logic_main_menu_animation ;
        typedef _logic_main_menu_animation_shake < mediator > logic_main_menu_animation_shake ;
        typedef _logic_main_menu_animation_stateless < mediator > logic_main_menu_animation_stateless ;
        typedef _logic_main_menu_choice < mediator > logic_main_menu_choice ;
        typedef _logic_main_menu_letters_animation < mediator > logic_main_menu_letters_animation ;
        typedef _logic_main_menu_letters_animation_appear < mediator > logic_main_menu_letters_animation_appear ;
        typedef _logic_main_menu_letters_animation_disappear < mediator > logic_main_menu_letters_animation_disappear ;
        typedef _logic_main_menu_letters_animation_idle < mediator > logic_main_menu_letters_animation_idle ;
        typedef _logic_main_menu_letters_animation_selection < mediator > logic_main_menu_letters_animation_selection ;
        typedef _logic_main_menu_letters_animation_selection_push < mediator > logic_main_menu_letters_animation_selection_push ;
        typedef _logic_main_menu_letters_animation_selection_weight < mediator > logic_main_menu_letters_animation_selection_weight ;
        typedef _logic_main_menu_letters_animation_stateless < mediator > logic_main_menu_letters_animation_stateless ;
        typedef _logic_main_menu_letters_animation_unselection_weight < mediator > logic_main_menu_letters_animation_unselection_weight ;
        typedef _logic_main_menu_letters_creation_director < mediator > logic_main_menu_letters_creation_director ;
        typedef _logic_main_menu_letters_layout_position < mediator > logic_main_menu_letters_layout_position ;
        typedef _logic_main_menu_letters_layout_row_rect < mediator > logic_main_menu_letters_layout_row_rect ;
        typedef _logic_main_menu_letters_layout_stateless < mediator > logic_main_menu_letters_layout_stateless ;
        typedef _logic_main_menu_letters_meshes_creation_director < mediator > logic_main_menu_letters_meshes_creation_director ;
        typedef _logic_main_menu_letters_meshes_creator < mediator > logic_main_menu_letters_meshes_creator ;
        typedef _logic_main_menu_letters_meshes_destroyer < mediator > logic_main_menu_letters_meshes_destroyer ;
        typedef _logic_main_menu_letters_meshes_placement < mediator > logic_main_menu_letters_meshes_placement ;
        typedef _logic_main_menu_letters_meshes_renderer < mediator > logic_main_menu_letters_meshes_renderer ;
        typedef _logic_main_menu_letters_meshes_stateless < mediator > logic_main_menu_letters_meshes_stateless ;
        typedef _logic_main_menu_letters_meshes_storage < mediator > logic_main_menu_letters_meshes_storage ;
        typedef _logic_main_menu_letters_stateless < mediator > logic_main_menu_letters_stateless ;
        typedef _logic_main_menu_letters_storage < mediator > logic_main_menu_letters_storage ;
        typedef _logic_main_menu_renderer < mediator > logic_main_menu_renderer ;
        typedef _logic_main_menu_selection_animation < mediator > logic_main_menu_selection_animation ;
        typedef _logic_main_menu_selection_animation_appear < mediator > logic_main_menu_selection_animation_appear ;
        typedef _logic_main_menu_selection_animation_disappear < mediator > logic_main_menu_selection_animation_disappear ;
        typedef _logic_main_menu_selection_animation_idle < mediator > logic_main_menu_selection_animation_idle ;
        typedef _logic_main_menu_selection_animation_idle_attention < mediator > logic_main_menu_selection_animation_idle_attention ;
        typedef _logic_main_menu_selection_animation_push < mediator > logic_main_menu_selection_animation_push ;
        typedef _logic_main_menu_selection_animation_push_attention < mediator > logic_main_menu_selection_animation_push_attention ;
        typedef _logic_main_menu_selection_animation_push_weight < mediator > logic_main_menu_selection_animation_push_weight ;
        typedef _logic_main_menu_selection_animation_select < mediator > logic_main_menu_selection_animation_select ;
        typedef _logic_main_menu_selection_animation_stateless < mediator > logic_main_menu_selection_animation_stateless ;
        typedef _logic_main_menu_selection_animation_unselect < mediator > logic_main_menu_selection_animation_unselect ;
        typedef _logic_main_menu_selection_mesh < mediator > logic_main_menu_selection_mesh ;
        typedef _logic_main_menu_selection_stateless < mediator > logic_main_menu_selection_stateless ;
        typedef _logic_main_menu_selection_tracker < mediator > logic_main_menu_selection_tracker ;
        typedef _logic_main_menu_selection_tracking_director < mediator > logic_main_menu_selection_tracking_director ;
        typedef _logic_main_menu_stateless < mediator > logic_main_menu_stateless ;
        typedef _logic_room < mediator > logic_room ;
        typedef _logic_room_mesh < mediator > logic_room_mesh ;
        typedef _logic_room_renderer < mediator > logic_room_renderer ;
        typedef _logic_room_stateless < mediator > logic_room_stateless ;
        typedef _logic_room_texture < mediator > logic_room_texture ;
        typedef _logic_sound < mediator > logic_sound ;
        typedef _logic_sound_stateless < mediator > logic_sound_stateless ;
        typedef _logic_text < mediator > logic_text ;
        typedef _logic_text_stateless < mediator > logic_text_stateless ;
        typedef _logic_title < mediator > logic_title ;
        typedef _logic_title_stateless < mediator > logic_title_stateless ;
        typedef _logic_touch < mediator > logic_touch ;
        typedef _logic_touch_stateless < mediator > logic_touch_stateless ;
    } ;
} ;

template 
    < typename _platform
    , template < typename _mediator_types > class _mediator
    , template < typename _mediator > class _engine_camera
    , template < typename _mediator > class _engine_math
    , template < typename _mediator > class _engine_rasterizer
    , template < typename _mediator > class _engine_rasterizer_stateless
    , template < typename _mediator > class _engine_render
    , template < typename _mediator > class _engine_render_stateless
    , template < typename _mediator > class _logic_amusement
    , template < typename _mediator > class _logic_amusement_renderer
    , template < typename _mediator > class _logic_amusement_stateless
    , template < typename _mediator > class _logic_application
    , template < typename _mediator > class _logic_application_stateless
    , template < typename _mediator > class _logic_camera
    , template < typename _mediator > class _logic_camera_stateless
    , template < typename _mediator > class _logic_controls
    , template < typename _mediator > class _logic_controls_stateless
    , template < typename _mediator > class _logic_core
    , template < typename _mediator > class _logic_core_stateless
    , template < typename _mediator > class _logic_door
    , template < typename _mediator > class _logic_door_mesh
    , template < typename _mediator > class _logic_door_stateless
    , template < typename _mediator > class _logic_entities
    , template < typename _mediator > class _logic_entities_stateless
    , template < typename _mediator > class _logic_fidget
    , template < typename _mediator > class _logic_fidget_stateless
    , template < typename _mediator > class _logic_game
    , template < typename _mediator > class _logic_game_stateless
    , template < typename _mediator > class _logic_image
    , template < typename _mediator > class _logic_image_stateless
    , template < typename _mediator > class _logic_land
    , template < typename _mediator > class _logic_land_stateless
    , template < typename _mediator > class _logic_main_menu
    , template < typename _mediator > class _logic_main_menu_animation
    , template < typename _mediator > class _logic_main_menu_animation_shake
    , template < typename _mediator > class _logic_main_menu_animation_stateless
    , template < typename _mediator > class _logic_main_menu_choice
    , template < typename _mediator > class _logic_main_menu_letters_animation
    , template < typename _mediator > class _logic_main_menu_letters_animation_appear
    , template < typename _mediator > class _logic_main_menu_letters_animation_disappear
    , template < typename _mediator > class _logic_main_menu_letters_animation_idle
    , template < typename _mediator > class _logic_main_menu_letters_animation_selection
    , template < typename _mediator > class _logic_main_menu_letters_animation_selection_push
    , template < typename _mediator > class _logic_main_menu_letters_animation_selection_weight
    , template < typename _mediator > class _logic_main_menu_letters_animation_stateless
    , template < typename _mediator > class _logic_main_menu_letters_animation_unselection_weight
    , template < typename _mediator > class _logic_main_menu_letters_creation_director
    , template < typename _mediator > class _logic_main_menu_letters_layout_position
    , template < typename _mediator > class _logic_main_menu_letters_layout_row_rect
    , template < typename _mediator > class _logic_main_menu_letters_layout_stateless
    , template < typename _mediator > class _logic_main_menu_letters_meshes_creation_director
    , template < typename _mediator > class _logic_main_menu_letters_meshes_creator
    , template < typename _mediator > class _logic_main_menu_letters_meshes_destroyer
    , template < typename _mediator > class _logic_main_menu_letters_meshes_placement
    , template < typename _mediator > class _logic_main_menu_letters_meshes_renderer
    , template < typename _mediator > class _logic_main_menu_letters_meshes_stateless
    , template < typename _mediator > class _logic_main_menu_letters_meshes_storage
    , template < typename _mediator > class _logic_main_menu_letters_stateless
    , template < typename _mediator > class _logic_main_menu_letters_storage
    , template < typename _mediator > class _logic_main_menu_renderer
    , template < typename _mediator > class _logic_main_menu_selection_animation
    , template < typename _mediator > class _logic_main_menu_selection_animation_appear
    , template < typename _mediator > class _logic_main_menu_selection_animation_disappear
    , template < typename _mediator > class _logic_main_menu_selection_animation_idle
    , template < typename _mediator > class _logic_main_menu_selection_animation_idle_attention
    , template < typename _mediator > class _logic_main_menu_selection_animation_push
    , template < typename _mediator > class _logic_main_menu_selection_animation_push_attention
    , template < typename _mediator > class _logic_main_menu_selection_animation_push_weight
    , template < typename _mediator > class _logic_main_menu_selection_animation_select
    , template < typename _mediator > class _logic_main_menu_selection_animation_stateless
    , template < typename _mediator > class _logic_main_menu_selection_animation_unselect
    , template < typename _mediator > class _logic_main_menu_selection_mesh
    , template < typename _mediator > class _logic_main_menu_selection_stateless
    , template < typename _mediator > class _logic_main_menu_selection_tracker
    , template < typename _mediator > class _logic_main_menu_selection_tracking_director
    , template < typename _mediator > class _logic_main_menu_stateless
    , template < typename _mediator > class _logic_room
    , template < typename _mediator > class _logic_room_mesh
    , template < typename _mediator > class _logic_room_renderer
    , template < typename _mediator > class _logic_room_stateless
    , template < typename _mediator > class _logic_room_texture
    , template < typename _mediator > class _logic_sound
    , template < typename _mediator > class _logic_sound_stateless
    , template < typename _mediator > class _logic_text
    , template < typename _mediator > class _logic_text_stateless
    , template < typename _mediator > class _logic_title
    , template < typename _mediator > class _logic_title_stateless
    , template < typename _mediator > class _logic_touch
    , template < typename _mediator > class _logic_touch_stateless
    >
class shy_aggregator_types
{
    typedef typename _platform :: platform_math :: const_int_32 const_int_32 ;
    typedef typename _platform :: platform_scheduler platform_scheduler ;

    static const_int_32 _max_rasterizer_messages = 1000 ;
    static const_int_32 _max_render_messages = 3000 ; 

public :
    typedef _platform platform ;
    typedef typename platform_scheduler :: template module_wrapper < _engine_rasterizer , _max_rasterizer_messages > scheduled_engine_rasterizer ;
    typedef typename platform_scheduler :: template module_wrapper < _engine_render , _max_render_messages > scheduled_engine_render ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_amusement > scheduled_logic_amusement ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_amusement_renderer > scheduled_logic_amusement_renderer ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_application > scheduled_logic_application ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_camera > scheduled_logic_camera ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_controls > scheduled_logic_controls ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_core > scheduled_logic_core ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_door > scheduled_logic_door ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_door_mesh > scheduled_logic_door_mesh ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_entities > scheduled_logic_entities ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_fidget > scheduled_logic_fidget ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_game > scheduled_logic_game ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_image > scheduled_logic_image ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_land > scheduled_logic_land ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu > scheduled_logic_main_menu ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_animation > scheduled_logic_main_menu_animation ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_animation_shake > scheduled_logic_main_menu_animation_shake ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_choice > scheduled_logic_main_menu_choice ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation > scheduled_logic_main_menu_letters_animation ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_appear > scheduled_logic_main_menu_letters_animation_appear ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_disappear > scheduled_logic_main_menu_letters_animation_disappear ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_idle > scheduled_logic_main_menu_letters_animation_idle ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_selection > scheduled_logic_main_menu_letters_animation_selection ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_selection_push > scheduled_logic_main_menu_letters_animation_selection_push ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_selection_weight > scheduled_logic_main_menu_letters_animation_selection_weight ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_animation_unselection_weight > scheduled_logic_main_menu_letters_animation_unselection_weight ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_creation_director > scheduled_logic_main_menu_letters_creation_director ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_layout_position > scheduled_logic_main_menu_letters_layout_position ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_layout_row_rect > scheduled_logic_main_menu_letters_layout_row_rect ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_creation_director > scheduled_logic_main_menu_letters_meshes_creation_director ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_creator > scheduled_logic_main_menu_letters_meshes_creator ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_destroyer > scheduled_logic_main_menu_letters_meshes_destroyer ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_placement > scheduled_logic_main_menu_letters_meshes_placement ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_renderer > scheduled_logic_main_menu_letters_meshes_renderer ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_meshes_storage > scheduled_logic_main_menu_letters_meshes_storage ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_storage > scheduled_logic_main_menu_letters_storage ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_renderer > scheduled_logic_main_menu_renderer ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation > scheduled_logic_main_menu_selection_animation ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_appear > scheduled_logic_main_menu_selection_animation_appear ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_disappear > scheduled_logic_main_menu_selection_animation_disappear ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_idle > scheduled_logic_main_menu_selection_animation_idle ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_idle_attention > scheduled_logic_main_menu_selection_animation_idle_attention ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_push > scheduled_logic_main_menu_selection_animation_push ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_push_attention > scheduled_logic_main_menu_selection_animation_push_attention ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_push_weight > scheduled_logic_main_menu_selection_animation_push_weight ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_select > scheduled_logic_main_menu_selection_animation_select ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_animation_unselect > scheduled_logic_main_menu_selection_animation_unselect ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_mesh > scheduled_logic_main_menu_selection_mesh ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_tracker > scheduled_logic_main_menu_selection_tracker ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_selection_tracking_director > scheduled_logic_main_menu_selection_tracking_director ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_room > scheduled_logic_room ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_room_mesh > scheduled_logic_room_mesh ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_room_renderer > scheduled_logic_room_renderer ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_room_texture > scheduled_logic_room_texture ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_sound > scheduled_logic_sound ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_text > scheduled_logic_text ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_title > scheduled_logic_title ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_touch > scheduled_logic_touch ;
    
    typedef _mediator < mediator_types
        < _platform 
        , _engine_camera
        , _engine_math
        , scheduled_engine_rasterizer :: template scheduled_module
        , _engine_rasterizer_stateless
        , scheduled_engine_render :: template scheduled_module
        , _engine_render_stateless
        , scheduled_logic_amusement :: template scheduled_module
        , scheduled_logic_amusement_renderer :: template scheduled_module
        , _logic_amusement_stateless
        , scheduled_logic_application :: template scheduled_module
        , _logic_application_stateless
        , scheduled_logic_camera :: template scheduled_module
        , _logic_camera_stateless
        , scheduled_logic_controls :: template scheduled_module
        , _logic_controls_stateless
        , scheduled_logic_core :: template scheduled_module
        , _logic_core_stateless
        , scheduled_logic_door :: template scheduled_module
        , scheduled_logic_door_mesh :: template scheduled_module
        , _logic_door_stateless
        , scheduled_logic_entities :: template scheduled_module
        , _logic_entities_stateless
        , scheduled_logic_fidget :: template scheduled_module
        , _logic_fidget_stateless
        , scheduled_logic_game :: template scheduled_module
        , _logic_game_stateless
        , scheduled_logic_image :: template scheduled_module
        , _logic_image_stateless
        , scheduled_logic_land :: template scheduled_module
        , _logic_land_stateless
        , scheduled_logic_main_menu :: template scheduled_module
        , scheduled_logic_main_menu_animation :: template scheduled_module
        , scheduled_logic_main_menu_animation_shake :: template scheduled_module
        , _logic_main_menu_animation_stateless
        , scheduled_logic_main_menu_choice :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_appear :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_disappear :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_idle :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_selection :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_selection_push :: template scheduled_module
        , scheduled_logic_main_menu_letters_animation_selection_weight :: template scheduled_module
        , _logic_main_menu_letters_animation_stateless
        , scheduled_logic_main_menu_letters_animation_unselection_weight :: template scheduled_module
        , scheduled_logic_main_menu_letters_creation_director :: template scheduled_module
        , scheduled_logic_main_menu_letters_layout_position :: template scheduled_module
        , scheduled_logic_main_menu_letters_layout_row_rect :: template scheduled_module
        , _logic_main_menu_letters_layout_stateless
        , scheduled_logic_main_menu_letters_meshes_creation_director :: template scheduled_module
        , scheduled_logic_main_menu_letters_meshes_creator :: template scheduled_module
        , scheduled_logic_main_menu_letters_meshes_destroyer :: template scheduled_module
        , scheduled_logic_main_menu_letters_meshes_placement :: template scheduled_module
        , scheduled_logic_main_menu_letters_meshes_renderer :: template scheduled_module
        , _logic_main_menu_letters_meshes_stateless
        , scheduled_logic_main_menu_letters_meshes_storage :: template scheduled_module
        , _logic_main_menu_letters_stateless
        , scheduled_logic_main_menu_letters_storage :: template scheduled_module
        , scheduled_logic_main_menu_renderer :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_appear :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_disappear :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_idle :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_idle_attention :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_push :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_push_attention :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_push_weight :: template scheduled_module
        , scheduled_logic_main_menu_selection_animation_select :: template scheduled_module
        , _logic_main_menu_selection_animation_stateless
        , scheduled_logic_main_menu_selection_animation_unselect :: template scheduled_module
        , scheduled_logic_main_menu_selection_mesh :: template scheduled_module
        , _logic_main_menu_selection_stateless
        , scheduled_logic_main_menu_selection_tracker :: template scheduled_module
        , scheduled_logic_main_menu_selection_tracking_director :: template scheduled_module
        , _logic_main_menu_stateless
        , scheduled_logic_room :: template scheduled_module
        , scheduled_logic_room_mesh :: template scheduled_module
        , scheduled_logic_room_renderer :: template scheduled_module
        , _logic_room_stateless
        , scheduled_logic_room_texture :: template scheduled_module
        , scheduled_logic_sound :: template scheduled_module
        , _logic_sound_stateless
        , scheduled_logic_text :: template scheduled_module
        , _logic_text_stateless
        , scheduled_logic_title :: template scheduled_module
        , _logic_title_stateless
        , scheduled_logic_touch :: template scheduled_module
        , _logic_touch_stateless
        > >
        mediator_type ;
    typedef typename mediator_type :: messages messages ;
    
    typedef _engine_camera < mediator_type > engine_camera ;
    typedef _engine_math < mediator_type > engine_math ;
    typedef _engine_rasterizer_stateless < mediator_type > engine_rasterizer_stateless ;
    typedef _engine_render_stateless < mediator_type > engine_render_stateless ;
    typedef _logic_amusement_stateless < mediator_type > logic_amusement_stateless ;
    typedef _logic_application_stateless < mediator_type > logic_application_stateless ;
    typedef _logic_camera_stateless < mediator_type > logic_camera_stateless ;
    typedef _logic_controls_stateless < mediator_type > logic_controls_stateless ;
    typedef _logic_core_stateless < mediator_type > logic_core_stateless ;
    typedef _logic_door_stateless < mediator_type > logic_door_stateless ;
    typedef _logic_entities_stateless < mediator_type > logic_entities_stateless ;
    typedef _logic_fidget_stateless < mediator_type > logic_fidget_stateless ;
    typedef _logic_game_stateless < mediator_type > logic_game_stateless ;
    typedef _logic_image_stateless < mediator_type > logic_image_stateless ;
    typedef _logic_land_stateless < mediator_type > logic_land_stateless ;
    typedef _logic_main_menu_animation_stateless < mediator_type > logic_main_menu_animation_stateless ;
    typedef _logic_main_menu_letters_animation_stateless < mediator_type > logic_main_menu_letters_animation_stateless ;
    typedef _logic_main_menu_letters_layout_stateless < mediator_type > logic_main_menu_letters_layout_stateless ;
    typedef _logic_main_menu_letters_meshes_stateless < mediator_type > logic_main_menu_letters_meshes_stateless ;
    typedef _logic_main_menu_letters_stateless < mediator_type > logic_main_menu_letters_stateless ;
    typedef _logic_main_menu_selection_animation_stateless < mediator_type > logic_main_menu_selection_animation_stateless ;
    typedef _logic_main_menu_selection_stateless < mediator_type > logic_main_menu_selection_stateless ;
    typedef _logic_main_menu_stateless < mediator_type > logic_main_menu_stateless ;
    typedef _logic_room_stateless < mediator_type > logic_room_stateless ;
    typedef _logic_sound_stateless < mediator_type > logic_sound_stateless ;
    typedef _logic_text_stateless < mediator_type > logic_text_stateless ;
    typedef _logic_title_stateless < mediator_type > logic_title_stateless ;
    typedef _logic_touch_stateless < mediator_type > logic_touch_stateless ;
} ;

template < typename aggregator_types >
class shy_aggregator
{
    typedef typename aggregator_types :: mediator_type mediator_type ;
    typedef typename aggregator_types :: messages messages ;
    typedef typename aggregator_types :: platform platform ;
    typedef typename aggregator_types :: platform :: platform_pointer platform_pointer ;
    typedef typename aggregator_types :: platform :: platform_scheduler platform_scheduler ;
    typedef typename aggregator_types :: platform :: platform_scheduler :: scheduler scheduler ;
    
    typedef typename aggregator_types :: engine_render_stateless engine_render_stateless ;
    typedef typename aggregator_types :: logic_main_menu_letters_layout_stateless logic_main_menu_letters_layout_stateless ;
    typedef typename aggregator_types :: logic_main_menu_letters_meshes_stateless logic_main_menu_letters_meshes_stateless ;
    typedef typename aggregator_types :: logic_main_menu_selection_stateless logic_main_menu_selection_stateless ;
    typedef typename aggregator_types :: logic_main_menu_stateless logic_main_menu_stateless ;
    typedef typename aggregator_types :: logic_text_stateless logic_text_stateless ;
    
    typedef typename aggregator_types :: scheduled_engine_rasterizer :: template scheduled_module < mediator_type > engine_rasterizer ;
    typedef typename aggregator_types :: scheduled_engine_render :: template scheduled_module < mediator_type > engine_render ;
    typedef typename aggregator_types :: scheduled_logic_amusement :: template scheduled_module < mediator_type > logic_amusement ;
    typedef typename aggregator_types :: scheduled_logic_amusement_renderer :: template scheduled_module < mediator_type > logic_amusement_renderer ;
    typedef typename aggregator_types :: scheduled_logic_application :: template scheduled_module < mediator_type > logic_application ;
    typedef typename aggregator_types :: scheduled_logic_camera :: template scheduled_module < mediator_type > logic_camera ;
    typedef typename aggregator_types :: scheduled_logic_controls :: template scheduled_module < mediator_type > logic_controls ;
    typedef typename aggregator_types :: scheduled_logic_core :: template scheduled_module < mediator_type > logic_core ;
    typedef typename aggregator_types :: scheduled_logic_door :: template scheduled_module < mediator_type > logic_door ;
    typedef typename aggregator_types :: scheduled_logic_door_mesh :: template scheduled_module < mediator_type > logic_door_mesh ;
    typedef typename aggregator_types :: scheduled_logic_entities :: template scheduled_module < mediator_type > logic_entities ;
    typedef typename aggregator_types :: scheduled_logic_fidget :: template scheduled_module < mediator_type > logic_fidget ;
    typedef typename aggregator_types :: scheduled_logic_game :: template scheduled_module < mediator_type > logic_game ;
    typedef typename aggregator_types :: scheduled_logic_image :: template scheduled_module < mediator_type > logic_image ;
    typedef typename aggregator_types :: scheduled_logic_land :: template scheduled_module < mediator_type > logic_land ;
    typedef typename aggregator_types :: scheduled_logic_main_menu :: template scheduled_module < mediator_type > logic_main_menu ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_animation :: template scheduled_module < mediator_type > logic_main_menu_animation ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_animation_shake :: template scheduled_module < mediator_type > logic_main_menu_animation_shake ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_choice :: template scheduled_module < mediator_type > logic_main_menu_choice ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation :: template scheduled_module < mediator_type > logic_main_menu_letters_animation ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_appear :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_appear ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_disappear :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_disappear ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_idle :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_idle ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_selection :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_selection ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_selection_push :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_selection_push ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_selection_weight :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_selection_weight ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_animation_unselection_weight :: template scheduled_module < mediator_type > logic_main_menu_letters_animation_unselection_weight ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_creation_director :: template scheduled_module < mediator_type > logic_main_menu_letters_creation_director ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_layout_position :: template scheduled_module < mediator_type > logic_main_menu_letters_layout_position ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_layout_row_rect :: template scheduled_module < mediator_type > logic_main_menu_letters_layout_row_rect ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_creation_director :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_creation_director ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_creator :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_creator ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_destroyer :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_destroyer ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_placement :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_placement ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_renderer :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_renderer ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_meshes_storage :: template scheduled_module < mediator_type > logic_main_menu_letters_meshes_storage ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_letters_storage :: template scheduled_module < mediator_type > logic_main_menu_letters_storage ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_renderer :: template scheduled_module < mediator_type > logic_main_menu_renderer ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation :: template scheduled_module < mediator_type > logic_main_menu_selection_animation ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_appear :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_appear ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_disappear :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_disappear ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_idle :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_idle ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_idle_attention :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_idle_attention ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_push :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_push ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_push_attention :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_push_attention ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_push_weight :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_push_weight ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_select :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_select ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_animation_unselect :: template scheduled_module < mediator_type > logic_main_menu_selection_animation_unselect ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_mesh :: template scheduled_module < mediator_type > logic_main_menu_selection_mesh ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_tracker :: template scheduled_module < mediator_type > logic_main_menu_selection_tracker ;
    typedef typename aggregator_types :: scheduled_logic_main_menu_selection_tracking_director :: template scheduled_module < mediator_type > logic_main_menu_selection_tracking_director ;
    typedef typename aggregator_types :: scheduled_logic_room :: template scheduled_module < mediator_type > logic_room ;
    typedef typename aggregator_types :: scheduled_logic_room_mesh :: template scheduled_module < mediator_type > logic_room_mesh ;
    typedef typename aggregator_types :: scheduled_logic_room_renderer :: template scheduled_module < mediator_type > logic_room_renderer ;
    typedef typename aggregator_types :: scheduled_logic_room_texture :: template scheduled_module < mediator_type > logic_room_texture ;
    typedef typename aggregator_types :: scheduled_logic_sound :: template scheduled_module < mediator_type > logic_sound ;
    typedef typename aggregator_types :: scheduled_logic_text :: template scheduled_module < mediator_type > logic_text ;
    typedef typename aggregator_types :: scheduled_logic_title :: template scheduled_module < mediator_type > logic_title ;
    typedef typename aggregator_types :: scheduled_logic_touch :: template scheduled_module < mediator_type > logic_touch ;
public :
    shy_aggregator ( typename platform_pointer :: template pointer < const platform > ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void video_mode_changed ( ) ;
private :
    void _run_scheduler ( ) ;
private :
    mediator_type _mediator ;
    scheduler _scheduler ;

    engine_rasterizer _engine_rasterizer ;
    engine_render _engine_render ;
    engine_render_stateless _engine_render_stateless ;
    logic_amusement _logic_amusement ;
    logic_amusement_renderer _logic_amusement_renderer ;
    logic_application _logic_application ;
    logic_camera _logic_camera ;
    logic_controls _logic_controls ;
    logic_core _logic_core ;
    logic_door _logic_door ;
    logic_door_mesh _logic_door_mesh ;
    logic_entities _logic_entities ;
    logic_fidget _logic_fidget ;
    logic_game _logic_game ;
    logic_image _logic_image ;
    logic_land _logic_land ;
    logic_main_menu _logic_main_menu ;
    logic_main_menu_animation _logic_main_menu_animation ;
    logic_main_menu_animation_shake _logic_main_menu_animation_shake ;
    logic_main_menu_choice _logic_main_menu_choice ;
    logic_main_menu_letters_animation _logic_main_menu_letters_animation ;
    logic_main_menu_letters_animation_appear _logic_main_menu_letters_animation_appear ;
    logic_main_menu_letters_animation_disappear _logic_main_menu_letters_animation_disappear ;
    logic_main_menu_letters_animation_idle _logic_main_menu_letters_animation_idle ;
    logic_main_menu_letters_animation_selection _logic_main_menu_letters_animation_selection ;
    logic_main_menu_letters_animation_selection_push _logic_main_menu_letters_animation_selection_push ;
    logic_main_menu_letters_animation_selection_weight _logic_main_menu_letters_animation_selection_weight ;
    logic_main_menu_letters_animation_unselection_weight _logic_main_menu_letters_animation_unselection_weight ;
    logic_main_menu_letters_creation_director _logic_main_menu_letters_creation_director ;
    logic_main_menu_letters_layout_position _logic_main_menu_letters_layout_position ;
    logic_main_menu_letters_layout_row_rect _logic_main_menu_letters_layout_row_rect ;
    logic_main_menu_letters_layout_stateless _logic_main_menu_letters_layout_stateless ;
    logic_main_menu_letters_meshes_creation_director _logic_main_menu_letters_meshes_creation_director ;
    logic_main_menu_letters_meshes_creator _logic_main_menu_letters_meshes_creator ;
    logic_main_menu_letters_meshes_destroyer _logic_main_menu_letters_meshes_destroyer ;
    logic_main_menu_letters_meshes_placement _logic_main_menu_letters_meshes_placement ;
    logic_main_menu_letters_meshes_renderer _logic_main_menu_letters_meshes_renderer ;
    logic_main_menu_letters_meshes_stateless _logic_main_menu_letters_meshes_stateless ;
    logic_main_menu_letters_meshes_storage _logic_main_menu_letters_meshes_storage ;
    logic_main_menu_letters_storage _logic_main_menu_letters_storage ;
    logic_main_menu_renderer _logic_main_menu_renderer ;
    logic_main_menu_selection_animation _logic_main_menu_selection_animation ;
    logic_main_menu_selection_animation_appear _logic_main_menu_selection_animation_appear ;
    logic_main_menu_selection_animation_disappear _logic_main_menu_selection_animation_disappear ;
    logic_main_menu_selection_animation_idle _logic_main_menu_selection_animation_idle ;
    logic_main_menu_selection_animation_idle_attention _logic_main_menu_selection_animation_idle_attention ;
    logic_main_menu_selection_animation_push _logic_main_menu_selection_animation_push ;
    logic_main_menu_selection_animation_push_attention _logic_main_menu_selection_animation_push_attention ;
    logic_main_menu_selection_animation_push_weight _logic_main_menu_selection_animation_push_weight ;
    logic_main_menu_selection_animation_select _logic_main_menu_selection_animation_select ;
    logic_main_menu_selection_animation_unselect _logic_main_menu_selection_animation_unselect ;
    logic_main_menu_selection_mesh _logic_main_menu_selection_mesh ;
    logic_main_menu_selection_stateless _logic_main_menu_selection_stateless ;
    logic_main_menu_selection_tracker _logic_main_menu_selection_tracker ;
    logic_main_menu_selection_tracking_director _logic_main_menu_selection_tracking_director ;
    logic_main_menu_stateless _logic_main_menu_stateless ;
    logic_room _logic_room ;
    logic_room_mesh _logic_room_mesh ;
    logic_room_renderer _logic_room_renderer ;
    logic_room_texture _logic_room_texture ;
    logic_sound _logic_sound ;
    logic_text _logic_text ;
    logic_text_stateless _logic_text_stateless ;
    logic_title _logic_title ;
    logic_touch _logic_touch ;
} ;

template < typename aggregator_types >
shy_aggregator < aggregator_types > :: shy_aggregator ( typename platform_pointer :: template pointer < const platform > arg_platform )
: _mediator ( arg_platform )
{
    typename platform_pointer :: template pointer < engine_rasterizer > engine_rasterizer_ptr ;
    typename platform_pointer :: template pointer < engine_render > engine_render_ptr ;
    typename platform_pointer :: template pointer < engine_render_stateless > engine_render_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_amusement > logic_amusement_ptr ;
    typename platform_pointer :: template pointer < logic_amusement_renderer > logic_amusement_renderer_ptr ;
    typename platform_pointer :: template pointer < logic_application > logic_application_ptr ;
    typename platform_pointer :: template pointer < logic_camera > logic_camera_ptr ;
    typename platform_pointer :: template pointer < logic_controls > logic_controls_ptr ;
    typename platform_pointer :: template pointer < logic_core > logic_core_ptr ;
    typename platform_pointer :: template pointer < logic_door > logic_door_ptr ;
    typename platform_pointer :: template pointer < logic_door_mesh > logic_door_mesh_ptr ;
    typename platform_pointer :: template pointer < logic_entities > logic_entities_ptr ;
    typename platform_pointer :: template pointer < logic_fidget > logic_fidget_ptr ;
    typename platform_pointer :: template pointer < logic_game > logic_game_ptr ;
    typename platform_pointer :: template pointer < logic_image > logic_image_ptr ;
    typename platform_pointer :: template pointer < logic_land > logic_land_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu > logic_main_menu_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_animation > logic_main_menu_animation_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_animation_shake > logic_main_menu_animation_shake_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_choice > logic_main_menu_choice_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation > logic_main_menu_letters_animation_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_appear > logic_main_menu_letters_animation_appear_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_disappear > logic_main_menu_letters_animation_disappear_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_idle > logic_main_menu_letters_animation_idle_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_selection > logic_main_menu_letters_animation_selection_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_selection_push > logic_main_menu_letters_animation_selection_push_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_selection_weight > logic_main_menu_letters_animation_selection_weight_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_animation_unselection_weight > logic_main_menu_letters_animation_unselection_weight_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_creation_director > logic_main_menu_letters_creation_director_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_layout_position > logic_main_menu_letters_layout_position_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_layout_row_rect > logic_main_menu_letters_layout_row_rect_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_layout_stateless > logic_main_menu_letters_layout_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creation_director > logic_main_menu_letters_meshes_creation_director_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_creator > logic_main_menu_letters_meshes_creator_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_destroyer > logic_main_menu_letters_meshes_destroyer_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_placement > logic_main_menu_letters_meshes_placement_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_renderer > logic_main_menu_letters_meshes_renderer_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_stateless > logic_main_menu_letters_meshes_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_meshes_storage > logic_main_menu_letters_meshes_storage_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_letters_storage > logic_main_menu_letters_storage_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_renderer > logic_main_menu_renderer_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation > logic_main_menu_selection_animation_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_appear > logic_main_menu_selection_animation_appear_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_disappear > logic_main_menu_selection_animation_disappear_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_idle > logic_main_menu_selection_animation_idle_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_idle_attention > logic_main_menu_selection_animation_idle_attention_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_push > logic_main_menu_selection_animation_push_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_push_attention > logic_main_menu_selection_animation_push_attention_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_push_weight > logic_main_menu_selection_animation_push_weight_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_select > logic_main_menu_selection_animation_select_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_animation_unselect > logic_main_menu_selection_animation_unselect_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_mesh > logic_main_menu_selection_mesh_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_stateless > logic_main_menu_selection_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_tracker > logic_main_menu_selection_tracker_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_selection_tracking_director > logic_main_menu_selection_tracking_director_ptr ;
    typename platform_pointer :: template pointer < logic_main_menu_stateless > logic_main_menu_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_room > logic_room_ptr ;
    typename platform_pointer :: template pointer < logic_room_mesh > logic_room_mesh_ptr ;
    typename platform_pointer :: template pointer < logic_room_renderer > logic_room_renderer_ptr ;
    typename platform_pointer :: template pointer < logic_room_texture > logic_room_texture_ptr ;
    typename platform_pointer :: template pointer < logic_sound > logic_sound_ptr ;
    typename platform_pointer :: template pointer < logic_text > logic_text_ptr ;
    typename platform_pointer :: template pointer < logic_text_stateless > logic_text_stateless_ptr ;
    typename platform_pointer :: template pointer < logic_title > logic_title_ptr ;
    typename platform_pointer :: template pointer < logic_touch > logic_touch_ptr ;
    typename platform_pointer :: template pointer < scheduler > scheduler_ptr ;
    
    platform_pointer :: bind ( engine_rasterizer_ptr , _engine_rasterizer ) ;
    platform_pointer :: bind ( engine_render_ptr , _engine_render );
    platform_pointer :: bind ( engine_render_stateless_ptr , _engine_render_stateless );
    platform_pointer :: bind ( logic_amusement_ptr , _logic_amusement ) ;
    platform_pointer :: bind ( logic_amusement_renderer_ptr , _logic_amusement_renderer ) ;
    platform_pointer :: bind ( logic_application_ptr , _logic_application ) ;
    platform_pointer :: bind ( logic_camera_ptr , _logic_camera ) ;
    platform_pointer :: bind ( logic_controls_ptr , _logic_controls ) ;
    platform_pointer :: bind ( logic_core_ptr , _logic_core ) ;
    platform_pointer :: bind ( logic_door_ptr , _logic_door ) ;
    platform_pointer :: bind ( logic_door_mesh_ptr , _logic_door_mesh ) ;
    platform_pointer :: bind ( logic_entities_ptr , _logic_entities ) ;
    platform_pointer :: bind ( logic_fidget_ptr , _logic_fidget ) ;
    platform_pointer :: bind ( logic_game_ptr , _logic_game ) ;
    platform_pointer :: bind ( logic_image_ptr , _logic_image ) ;
    platform_pointer :: bind ( logic_land_ptr , _logic_land ) ;
    platform_pointer :: bind ( logic_main_menu_ptr , _logic_main_menu ) ;
    platform_pointer :: bind ( logic_main_menu_animation_ptr , _logic_main_menu_animation ) ;
    platform_pointer :: bind ( logic_main_menu_animation_shake_ptr , _logic_main_menu_animation_shake ) ;
    platform_pointer :: bind ( logic_main_menu_choice_ptr , _logic_main_menu_choice ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_ptr , _logic_main_menu_letters_animation ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_appear_ptr , _logic_main_menu_letters_animation_appear ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_disappear_ptr , _logic_main_menu_letters_animation_disappear ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_idle_ptr , _logic_main_menu_letters_animation_idle ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_selection_ptr , _logic_main_menu_letters_animation_selection ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_selection_push_ptr , _logic_main_menu_letters_animation_selection_push ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_selection_weight_ptr , _logic_main_menu_letters_animation_selection_weight ) ;
    platform_pointer :: bind ( logic_main_menu_letters_animation_unselection_weight_ptr , _logic_main_menu_letters_animation_unselection_weight ) ;
    platform_pointer :: bind ( logic_main_menu_letters_creation_director_ptr , _logic_main_menu_letters_creation_director ) ;
    platform_pointer :: bind ( logic_main_menu_letters_layout_position_ptr , _logic_main_menu_letters_layout_position ) ;
    platform_pointer :: bind ( logic_main_menu_letters_layout_row_rect_ptr , _logic_main_menu_letters_layout_row_rect ) ;
    platform_pointer :: bind ( logic_main_menu_letters_layout_stateless_ptr , _logic_main_menu_letters_layout_stateless ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_creation_director_ptr , _logic_main_menu_letters_meshes_creation_director ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_creator_ptr , _logic_main_menu_letters_meshes_creator ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_destroyer_ptr , _logic_main_menu_letters_meshes_destroyer ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_placement_ptr , _logic_main_menu_letters_meshes_placement ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_renderer_ptr , _logic_main_menu_letters_meshes_renderer ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_stateless_ptr , _logic_main_menu_letters_meshes_stateless ) ;
    platform_pointer :: bind ( logic_main_menu_letters_meshes_storage_ptr , _logic_main_menu_letters_meshes_storage ) ;
    platform_pointer :: bind ( logic_main_menu_letters_storage_ptr , _logic_main_menu_letters_storage ) ;
    platform_pointer :: bind ( logic_main_menu_renderer_ptr , _logic_main_menu_renderer ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_ptr , _logic_main_menu_selection_animation ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_appear_ptr , _logic_main_menu_selection_animation_appear ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_disappear_ptr , _logic_main_menu_selection_animation_disappear ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_idle_ptr , _logic_main_menu_selection_animation_idle ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_idle_attention_ptr , _logic_main_menu_selection_animation_idle_attention ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_push_ptr , _logic_main_menu_selection_animation_push ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_push_attention_ptr , _logic_main_menu_selection_animation_push_attention ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_push_weight_ptr , _logic_main_menu_selection_animation_push_weight ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_select_ptr , _logic_main_menu_selection_animation_select ) ;
    platform_pointer :: bind ( logic_main_menu_selection_animation_unselect_ptr , _logic_main_menu_selection_animation_unselect ) ;
    platform_pointer :: bind ( logic_main_menu_selection_mesh_ptr , _logic_main_menu_selection_mesh ) ;
    platform_pointer :: bind ( logic_main_menu_selection_stateless_ptr , _logic_main_menu_selection_stateless ) ;
    platform_pointer :: bind ( logic_main_menu_selection_tracker_ptr , _logic_main_menu_selection_tracker ) ;
    platform_pointer :: bind ( logic_main_menu_selection_tracking_director_ptr , _logic_main_menu_selection_tracking_director ) ;
    platform_pointer :: bind ( logic_main_menu_stateless_ptr , _logic_main_menu_stateless ) ;
    platform_pointer :: bind ( logic_room_ptr , _logic_room ) ;
    platform_pointer :: bind ( logic_room_mesh_ptr , _logic_room_mesh ) ;
    platform_pointer :: bind ( logic_room_renderer_ptr , _logic_room_renderer ) ;
    platform_pointer :: bind ( logic_room_texture_ptr , _logic_room_texture ) ;
    platform_pointer :: bind ( logic_sound_ptr , _logic_sound ) ;
    platform_pointer :: bind ( logic_text_ptr , _logic_text ) ;
    platform_pointer :: bind ( logic_text_stateless_ptr , _logic_text_stateless ) ;
    platform_pointer :: bind ( logic_title_ptr , _logic_title ) ;
    platform_pointer :: bind ( logic_touch_ptr , _logic_touch ) ;
    platform_pointer :: bind ( scheduler_ptr , _scheduler ) ;

    platform_scheduler :: register_module_in_scheduler ( engine_rasterizer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( engine_render_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_amusement_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_amusement_renderer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_application_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_camera_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_controls_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_core_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_door_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_door_mesh_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_entities_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_fidget_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_game_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_image_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_land_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_animation_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_animation_shake_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_choice_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_appear_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_disappear_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_idle_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_selection_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_selection_push_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_selection_weight_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_animation_unselection_weight_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_creation_director_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_layout_position_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_layout_row_rect_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_creation_director_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_creator_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_destroyer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_placement_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_renderer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_meshes_storage_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_letters_storage_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_renderer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_appear_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_disappear_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_idle_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_idle_attention_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_push_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_push_attention_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_push_weight_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_select_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_animation_unselect_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_mesh_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_tracker_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_main_menu_selection_tracking_director_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_room_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_room_mesh_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_room_renderer_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_room_texture_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_sound_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_text_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_title_ptr , scheduler_ptr ) ;
    platform_scheduler :: register_module_in_scheduler ( logic_touch_ptr , scheduler_ptr ) ;
    _mediator . register_modules
        ( engine_rasterizer_ptr
        , engine_render_ptr
        , engine_render_stateless_ptr
        , logic_amusement_ptr
        , logic_amusement_renderer_ptr
        , logic_application_ptr
        , logic_camera_ptr
        , logic_controls_ptr
        , logic_core_ptr
        , logic_door_ptr
        , logic_door_mesh_ptr
        , logic_entities_ptr
        , logic_fidget_ptr
        , logic_game_ptr
        , logic_image_ptr
        , logic_land_ptr
        , logic_main_menu_ptr
        , logic_main_menu_animation_ptr
        , logic_main_menu_animation_shake_ptr
        , logic_main_menu_choice_ptr
        , logic_main_menu_letters_animation_ptr
        , logic_main_menu_letters_animation_appear_ptr
        , logic_main_menu_letters_animation_disappear_ptr
        , logic_main_menu_letters_animation_idle_ptr
        , logic_main_menu_letters_animation_selection_ptr
        , logic_main_menu_letters_animation_selection_push_ptr
        , logic_main_menu_letters_animation_selection_weight_ptr
        , logic_main_menu_letters_animation_unselection_weight_ptr
        , logic_main_menu_letters_creation_director_ptr
        , logic_main_menu_letters_layout_position_ptr
        , logic_main_menu_letters_layout_row_rect_ptr
        , logic_main_menu_letters_layout_stateless_ptr
        , logic_main_menu_letters_meshes_creation_director_ptr
        , logic_main_menu_letters_meshes_creator_ptr
        , logic_main_menu_letters_meshes_destroyer_ptr
        , logic_main_menu_letters_meshes_placement_ptr
        , logic_main_menu_letters_meshes_renderer_ptr
        , logic_main_menu_letters_meshes_stateless_ptr
        , logic_main_menu_letters_meshes_storage_ptr
        , logic_main_menu_letters_storage_ptr
        , logic_main_menu_renderer_ptr
        , logic_main_menu_selection_animation_ptr
        , logic_main_menu_selection_animation_appear_ptr
        , logic_main_menu_selection_animation_disappear_ptr
        , logic_main_menu_selection_animation_idle_ptr
        , logic_main_menu_selection_animation_idle_attention_ptr
        , logic_main_menu_selection_animation_push_ptr
        , logic_main_menu_selection_animation_push_attention_ptr
        , logic_main_menu_selection_animation_push_weight_ptr
        , logic_main_menu_selection_animation_select_ptr
        , logic_main_menu_selection_animation_unselect_ptr
        , logic_main_menu_selection_mesh_ptr
        , logic_main_menu_selection_stateless_ptr
        , logic_main_menu_selection_tracker_ptr
        , logic_main_menu_selection_tracking_director_ptr
        , logic_main_menu_stateless_ptr
        , logic_room_ptr
        , logic_room_mesh_ptr
        , logic_room_renderer_ptr
        , logic_room_texture_ptr
        , logic_sound_ptr
        , logic_text_ptr
        , logic_text_stateless_ptr
        , logic_title_ptr
        , logic_touch_ptr
        ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: _run_scheduler ( )
{
    typename platform_pointer :: template pointer < scheduler > scheduler_ptr ;
    platform_pointer :: bind ( scheduler_ptr , _scheduler ) ;
    platform_scheduler :: run ( scheduler_ptr ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: init ( )
{
    _mediator . send ( typename messages :: init ( ) ) ;
    _run_scheduler ( ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: done ( )
{
    _mediator . send ( typename messages :: done ( ) ) ;
    _run_scheduler ( ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: render ( )
{
    _mediator . send ( typename messages :: render ( ) ) ;
    _run_scheduler ( ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: update ( )
{
    _mediator . send ( typename messages :: update ( ) ) ;
    _run_scheduler ( ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: video_mode_changed ( )
{
    _mediator . send ( typename messages :: video_mode_changed ( ) ) ;
    _run_scheduler ( ) ;
}
