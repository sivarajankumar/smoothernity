template 
    < typename _platform
    , template < typename mediator > class _engine_camera
    , template < typename mediator > class _engine_math
    , template < typename mediator > class _engine_rasterizer
    , template < typename mediator > class _engine_render
    , template < typename mediator > class _engine_render_stateless
    , template < typename mediator > class _logic 
    , template < typename mediator > class _logic_application
    , template < typename mediator > class _logic_camera
    , template < typename mediator > class _logic_entities
    , template < typename mediator > class _logic_fidget
    , template < typename mediator > class _logic_game
    , template < typename mediator > class _logic_image
    , template < typename mediator > class _logic_land
    , template < typename mediator > class _logic_sound
    , template < typename mediator > class _logic_text
    , template < typename mediator > class _logic_text_stateless
    , template < typename mediator > class _logic_title
    , template < typename mediator > class _logic_touch
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
        typedef _engine_render < mediator > engine_render ;
        typedef _engine_render_stateless < mediator > engine_render_stateless ;
        typedef _logic < mediator > logic ;
        typedef _logic_application < mediator > logic_application ;
        typedef _logic_camera < mediator > logic_camera ;
        typedef _logic_entities < mediator > logic_entities ;
        typedef _logic_fidget < mediator > logic_fidget ;
        typedef _logic_game < mediator > logic_game ;
        typedef _logic_image < mediator > logic_image ;
        typedef _logic_land < mediator > logic_land ;
        typedef _logic_sound < mediator > logic_sound ;
        typedef _logic_text < mediator > logic_text ;
        typedef _logic_text_stateless < mediator > logic_text_stateless ;
        typedef _logic_title < mediator > logic_title ;
        typedef _logic_touch < mediator > logic_touch ;
    } ;
} ;

template 
    < typename platform
    , template < typename mediator_types > class mediator
    , template < typename mediator > class engine_camera
    , template < typename mediator > class engine_math
    , template < typename mediator > class engine_rasterizer
    , template < typename mediator > class engine_render
    , template < typename mediator > class engine_render_stateless
    , template < typename mediator > class logic 
    , template < typename mediator > class logic_application
    , template < typename mediator > class logic_camera
    , template < typename mediator > class logic_entities
    , template < typename mediator > class logic_fidget
    , template < typename mediator > class logic_game
    , template < typename mediator > class logic_image
    , template < typename mediator > class logic_land
    , template < typename mediator > class logic_sound
    , template < typename mediator > class logic_text
    , template < typename mediator > class logic_text_stateless
    , template < typename mediator > class logic_title
    , template < typename mediator > class logic_touch
    >
class shy_aggregator
{
    typedef typename platform :: platform_scheduler platform_scheduler ;
    typedef typename platform :: platform_scheduler :: scheduler scheduler ;
    typedef typename platform_scheduler :: template module_wrapper < engine_rasterizer > scheduled_engine_rasterizer ;
    typedef typename platform_scheduler :: template module_wrapper < engine_render > scheduled_engine_render ;
    typedef typename platform_scheduler :: template module_wrapper < logic > scheduled_logic ;
    typedef typename platform_scheduler :: template module_wrapper < logic_application > scheduled_logic_application ;
    typedef typename platform_scheduler :: template module_wrapper < logic_camera > scheduled_logic_camera ;
    typedef typename platform_scheduler :: template module_wrapper < logic_entities > scheduled_logic_entities ;
    typedef typename platform_scheduler :: template module_wrapper < logic_fidget > scheduled_logic_fidget ;
    typedef typename platform_scheduler :: template module_wrapper < logic_game > scheduled_logic_game ;
    typedef typename platform_scheduler :: template module_wrapper < logic_image > scheduled_logic_image ;
    typedef typename platform_scheduler :: template module_wrapper < logic_land > scheduled_logic_land ;
    typedef typename platform_scheduler :: template module_wrapper < logic_sound > scheduled_logic_sound ;
    typedef typename platform_scheduler :: template module_wrapper < logic_text > scheduled_logic_text ;
    typedef typename platform_scheduler :: template module_wrapper < logic_title > scheduled_logic_title ;
    typedef typename platform_scheduler :: template module_wrapper < logic_touch > scheduled_logic_touch ;
    
    typedef mediator < mediator_types
        < platform 
        , engine_camera
        , engine_math
        , scheduled_engine_rasterizer :: template scheduled_module
        , scheduled_engine_render :: template scheduled_module
        , engine_render_stateless
        , scheduled_logic :: template scheduled_module
        , scheduled_logic_application :: template scheduled_module
        , scheduled_logic_camera :: template scheduled_module
        , scheduled_logic_entities :: template scheduled_module
        , scheduled_logic_fidget :: template scheduled_module
        , scheduled_logic_game :: template scheduled_module
        , scheduled_logic_image :: template scheduled_module
        , scheduled_logic_land :: template scheduled_module
        , scheduled_logic_sound :: template scheduled_module
        , scheduled_logic_text :: template scheduled_module
        , logic_text_stateless
        , scheduled_logic_title :: template scheduled_module
        , scheduled_logic_touch :: template scheduled_module
        > >
        _mediator_type ;
    typedef typename _mediator_type :: messages messages ;
public :
    shy_aggregator ( )
    {
        platform_scheduler :: register_module_in_scheduler ( _engine_rasterizer , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _engine_render , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_application , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_camera , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_entities , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_fidget , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_game , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_image , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_land , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_sound , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_text , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_title , _scheduler ) ;
        platform_scheduler :: register_module_in_scheduler ( _logic_touch , _scheduler ) ;
        _mediator . register_modules
            ( _engine_rasterizer
            , _engine_render
            , _engine_render_stateless
            , _logic
            , _logic_application
            , _logic_camera
            , _logic_entities
            , _logic_fidget
            , _logic_game
            , _logic_image
            , _logic_land
            , _logic_sound
            , _logic_text
            , _logic_text_stateless
            , _logic_title
            , _logic_touch
            ) ;
    }
    void init ( )
    {
        _mediator . send ( typename messages :: init ( ) ) ;
        platform_scheduler :: run ( _scheduler ) ;
    }
    void done ( )
    {
        _mediator . send ( typename messages :: done ( ) ) ;
        platform_scheduler :: run ( _scheduler ) ;
    }
    void render ( )
    {
        _mediator . send ( typename messages :: render ( ) ) ;
        platform_scheduler :: run ( _scheduler ) ;
    }
    void update ( )
    {
        _mediator . send ( typename messages :: update ( ) ) ;
        platform_scheduler :: run ( _scheduler ) ;
    }
    void video_mode_changed ( )
    {
        _mediator . send ( typename messages :: video_mode_changed ( ) ) ;
        platform_scheduler :: run ( _scheduler ) ;
    }
private :
    _mediator_type _mediator ;
    scheduler _scheduler ;
    typename scheduled_engine_rasterizer :: template scheduled_module < _mediator_type > _engine_rasterizer ;
    typename scheduled_engine_render :: template scheduled_module < _mediator_type > _engine_render ;
    engine_render_stateless < _mediator_type > _engine_render_stateless ;
    typename scheduled_logic :: template scheduled_module < _mediator_type > _logic ;
    typename scheduled_logic_application :: template scheduled_module < _mediator_type > _logic_application ;
    typename scheduled_logic_camera :: template scheduled_module < _mediator_type > _logic_camera ;
    typename scheduled_logic_entities :: template scheduled_module < _mediator_type > _logic_entities ;
    typename scheduled_logic_fidget :: template scheduled_module < _mediator_type > _logic_fidget ;
    typename scheduled_logic_game :: template scheduled_module < _mediator_type > _logic_game ;
    typename scheduled_logic_image :: template scheduled_module < _mediator_type > _logic_image ;
    typename scheduled_logic_land :: template scheduled_module < _mediator_type > _logic_land ;
    typename scheduled_logic_sound :: template scheduled_module < _mediator_type > _logic_sound ;
    typename scheduled_logic_text :: template scheduled_module < _mediator_type > _logic_text ;
    logic_text_stateless < _mediator_type > _logic_text_stateless ;
    typename scheduled_logic_title :: template scheduled_module < _mediator_type > _logic_title ;
    typename scheduled_logic_touch :: template scheduled_module < _mediator_type > _logic_touch ;
} ;
