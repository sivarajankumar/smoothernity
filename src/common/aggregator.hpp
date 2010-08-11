template 
    < typename _platform
    , template < typename mediator > class _engine_camera
    , template < typename mediator > class _engine_math
    , template < typename mediator > class _engine_rasterizer
    , template < typename mediator > class _engine_rasterizer_stateless
    , template < typename mediator > class _engine_render
    , template < typename mediator > class _engine_render_stateless
    , template < typename mediator > class _logic_application
    , template < typename mediator > class _logic_application_stateless
    , template < typename mediator > class _logic_camera
    , template < typename mediator > class _logic_camera_stateless
    , template < typename mediator > class _logic_core
    , template < typename mediator > class _logic_core_stateless
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
    , template < typename mediator > class _logic_main_menu_layout
    , template < typename mediator > class _logic_main_menu_letters_creation_director
    , template < typename mediator > class _logic_main_menu_letters_storage
    , template < typename mediator > class _logic_main_menu_meshes_creation_director
    , template < typename mediator > class _logic_main_menu_meshes_storage
    , template < typename mediator > class _logic_main_menu_stateless
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
        typedef _logic_application < mediator > logic_application ;
        typedef _logic_application_stateless < mediator > logic_application_stateless ;
        typedef _logic_camera < mediator > logic_camera ;
        typedef _logic_camera_stateless < mediator > logic_camera_stateless ;
        typedef _logic_core < mediator > logic_core ;
        typedef _logic_core_stateless < mediator > logic_core_stateless ;
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
        typedef _logic_main_menu_layout < mediator > logic_main_menu_layout ;
        typedef _logic_main_menu_letters_creation_director < mediator > logic_main_menu_letters_creation_director ;
        typedef _logic_main_menu_letters_storage < mediator > logic_main_menu_letters_storage ;
        typedef _logic_main_menu_meshes_creation_director < mediator > logic_main_menu_meshes_creation_director ;
        typedef _logic_main_menu_meshes_storage < mediator > logic_main_menu_meshes_storage ;
        typedef _logic_main_menu_stateless < mediator > logic_main_menu_stateless ;
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
    , template < typename _mediator > class _logic_application
    , template < typename _mediator > class _logic_application_stateless
    , template < typename _mediator > class _logic_camera
    , template < typename _mediator > class _logic_camera_stateless
    , template < typename _mediator > class _logic_core
    , template < typename _mediator > class _logic_core_stateless
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
    , template < typename _mediator > class _logic_main_menu_layout
    , template < typename _mediator > class _logic_main_menu_letters_creation_director
    , template < typename _mediator > class _logic_main_menu_letters_storage
    , template < typename _mediator > class _logic_main_menu_meshes_creation_director
    , template < typename _mediator > class _logic_main_menu_meshes_storage
    , template < typename _mediator > class _logic_main_menu_stateless
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
    typedef typename _platform :: platform_scheduler platform_scheduler ;
public :
    typedef _platform platform ;
    typedef typename platform_scheduler :: template module_wrapper < _engine_rasterizer , 1000 > scheduled_engine_rasterizer ;
    typedef typename platform_scheduler :: template module_wrapper < _engine_render , 3000 > scheduled_engine_render ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_application > scheduled_logic_application ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_camera > scheduled_logic_camera ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_core > scheduled_logic_core ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_entities > scheduled_logic_entities ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_fidget > scheduled_logic_fidget ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_game > scheduled_logic_game ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_image > scheduled_logic_image ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_land > scheduled_logic_land ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu > scheduled_logic_main_menu ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_layout > scheduled_logic_main_menu_layout ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_creation_director > scheduled_logic_main_menu_letters_creation_director ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_letters_storage > scheduled_logic_main_menu_letters_storage ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_meshes_creation_director > scheduled_logic_main_menu_meshes_creation_director ;
    typedef typename platform_scheduler :: template module_wrapper < _logic_main_menu_meshes_storage > scheduled_logic_main_menu_meshes_storage ;
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
        , scheduled_logic_application :: template scheduled_module
        , _logic_application_stateless
        , scheduled_logic_camera :: template scheduled_module
        , _logic_camera_stateless
        , scheduled_logic_core :: template scheduled_module
        , _logic_core_stateless
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
        , scheduled_logic_main_menu_layout :: template scheduled_module
        , scheduled_logic_main_menu_letters_creation_director :: template scheduled_module
        , scheduled_logic_main_menu_letters_storage :: template scheduled_module
        , scheduled_logic_main_menu_meshes_creation_director :: template scheduled_module
        , scheduled_logic_main_menu_meshes_storage :: template scheduled_module
        , _logic_main_menu_stateless
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
    typedef _logic_application_stateless < mediator_type > logic_application_stateless ;
    typedef _logic_camera_stateless < mediator_type > logic_camera_stateless ;
    typedef _logic_core_stateless < mediator_type > logic_core_stateless ;
    typedef _logic_entities_stateless < mediator_type > logic_entities_stateless ;
    typedef _logic_fidget_stateless < mediator_type > logic_fidget_stateless ;
    typedef _logic_game_stateless < mediator_type > logic_game_stateless ;
    typedef _logic_image_stateless < mediator_type > logic_image_stateless ;
    typedef _logic_land_stateless < mediator_type > logic_land_stateless ;
    typedef _logic_main_menu_stateless < mediator_type > logic_main_menu_stateless ;
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
public :
    shy_aggregator ( typename platform_pointer :: template pointer < const platform > ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void video_mode_changed ( ) ;
private :
    mediator_type _mediator ;
    scheduler _scheduler ;

    typename aggregator_types :: engine_render_stateless _engine_render_stateless ;
    typename aggregator_types :: logic_main_menu_stateless _logic_main_menu_stateless ;
    typename aggregator_types :: logic_text_stateless _logic_text_stateless ;

    typename aggregator_types :: scheduled_engine_rasterizer :: template scheduled_module < mediator_type > _engine_rasterizer ;
    typename aggregator_types :: scheduled_engine_render :: template scheduled_module < mediator_type > _engine_render ;
    typename aggregator_types :: scheduled_logic_application :: template scheduled_module < mediator_type > _logic_application ;
    typename aggregator_types :: scheduled_logic_camera :: template scheduled_module < mediator_type > _logic_camera ;
    typename aggregator_types :: scheduled_logic_core :: template scheduled_module < mediator_type > _logic_core ;
    typename aggregator_types :: scheduled_logic_entities :: template scheduled_module < mediator_type > _logic_entities ;
    typename aggregator_types :: scheduled_logic_fidget :: template scheduled_module < mediator_type > _logic_fidget ;
    typename aggregator_types :: scheduled_logic_game :: template scheduled_module < mediator_type > _logic_game ;
    typename aggregator_types :: scheduled_logic_image :: template scheduled_module < mediator_type > _logic_image ;
    typename aggregator_types :: scheduled_logic_land :: template scheduled_module < mediator_type > _logic_land ;
    typename aggregator_types :: scheduled_logic_main_menu :: template scheduled_module < mediator_type > _logic_main_menu ;
    typename aggregator_types :: scheduled_logic_main_menu_layout :: template scheduled_module < mediator_type > _logic_main_menu_layout ;
    typename aggregator_types :: scheduled_logic_main_menu_letters_creation_director :: template scheduled_module < mediator_type > _logic_main_menu_letters_creation_director ;
    typename aggregator_types :: scheduled_logic_main_menu_letters_storage :: template scheduled_module < mediator_type > _logic_main_menu_letters_storage ;
    typename aggregator_types :: scheduled_logic_main_menu_meshes_creation_director :: template scheduled_module < mediator_type > _logic_main_menu_meshes_creation_director ;
    typename aggregator_types :: scheduled_logic_main_menu_meshes_storage :: template scheduled_module < mediator_type > _logic_main_menu_meshes_storage ;
    typename aggregator_types :: scheduled_logic_sound :: template scheduled_module < mediator_type > _logic_sound ;
    typename aggregator_types :: scheduled_logic_text :: template scheduled_module < mediator_type > _logic_text ;
    typename aggregator_types :: scheduled_logic_title :: template scheduled_module < mediator_type > _logic_title ;
    typename aggregator_types :: scheduled_logic_touch :: template scheduled_module < mediator_type > _logic_touch ;
} ;

template < typename aggregator_types >
shy_aggregator < aggregator_types > :: shy_aggregator ( typename platform_pointer :: template pointer < const platform > arg_platform )
: _mediator ( arg_platform )
{
    platform_scheduler :: register_module_in_scheduler ( _engine_rasterizer , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _engine_render , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_application , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_camera , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_core , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_entities , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_fidget , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_game , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_image , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_land , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu_layout , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu_letters_creation_director , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu_letters_storage , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu_meshes_creation_director , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_main_menu_meshes_storage , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_sound , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_text , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_title , _scheduler ) ;
    platform_scheduler :: register_module_in_scheduler ( _logic_touch , _scheduler ) ;
    _mediator . register_modules
        ( _engine_rasterizer
        , _engine_render
        , _engine_render_stateless
        , _logic_application
        , _logic_camera
        , _logic_core
        , _logic_entities
        , _logic_fidget
        , _logic_game
        , _logic_image
        , _logic_land
        , _logic_main_menu
        , _logic_main_menu_layout
        , _logic_main_menu_letters_creation_director
        , _logic_main_menu_letters_storage
        , _logic_main_menu_meshes_creation_director
        , _logic_main_menu_meshes_storage
        , _logic_main_menu_stateless
        , _logic_sound
        , _logic_text
        , _logic_text_stateless
        , _logic_title
        , _logic_touch
        ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: init ( )
{
    _mediator . send ( typename messages :: init ( ) ) ;
    platform_scheduler :: run ( _scheduler ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: done ( )
{
    _mediator . send ( typename messages :: done ( ) ) ;
    platform_scheduler :: run ( _scheduler ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: render ( )
{
    _mediator . send ( typename messages :: render ( ) ) ;
    platform_scheduler :: run ( _scheduler ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: update ( )
{
    _mediator . send ( typename messages :: update ( ) ) ;
    platform_scheduler :: run ( _scheduler ) ;
}

template < typename aggregator_types >
void shy_aggregator < aggregator_types > :: video_mode_changed ( )
{
    _mediator . send ( typename messages :: video_mode_changed ( ) ) ;
    platform_scheduler :: run ( _scheduler ) ;
}
