#define char no_chars
#define double no_doubles
#define float no_floats
#define int no_ints
#define long no_longs
#define signed no_signeds
#define short no_shorts
#define unsigned no_unsigneds

#include "engine_camera.hpp"
#include "engine_math.hpp"
#include "engine_rasterizer.hpp"
#include "engine_render.hpp"
#include "engine_render_stateless.hpp"
#include "logic.hpp"
#include "logic_application.hpp"
#include "logic_camera.hpp"
#include "logic_entities.hpp"
#include "logic_fidget.hpp"
#include "logic_game.hpp"
#include "logic_image.hpp"
#include "logic_land.hpp"
#include "logic_sound.hpp"
#include "logic_text.hpp"
#include "logic_text_stateless.hpp"
#include "logic_title.hpp"
#include "logic_touch.hpp"
#include "mediator.hpp"

template < typename platform >
class shy_facade
{
    typedef typename platform :: platform_scheduler platform_scheduler ;
    typedef typename platform_scheduler :: template module_wrapper < shy_engine_rasterizer > scheduled_engine_rasterizer ;
    typedef typename platform_scheduler :: template module_wrapper < shy_engine_render > scheduled_engine_render ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic > scheduled_logic ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_application > scheduled_logic_application ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_camera > scheduled_logic_camera ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_entities > scheduled_logic_entities ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_fidget > scheduled_logic_fidget ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_game > scheduled_logic_game ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_image > scheduled_logic_image ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_land > scheduled_logic_land ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_sound > scheduled_logic_sound ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_text > scheduled_logic_text ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_title > scheduled_logic_title ;
    typedef typename platform_scheduler :: template module_wrapper < shy_logic_touch > scheduled_logic_touch ;
    
    typedef shy_mediator < shy_mediator_types
        < platform 
        , shy_engine_camera
        , shy_engine_math
        , scheduled_engine_rasterizer :: template scheduled_module
        , scheduled_engine_render :: template scheduled_module
        , shy_engine_render_stateless
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
        , shy_logic_text_stateless
        , scheduled_logic_title :: template scheduled_module
        , scheduled_logic_touch :: template scheduled_module
        > >
        _mediator_type ;
    typedef typename _mediator_type :: messages messages ;
public :
    shy_facade ( ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void video_mode_changed ( ) ;
private :
    _mediator_type _mediator ;
    typename scheduled_engine_rasterizer :: template scheduled_module < _mediator_type > _engine_rasterizer ;
    typename scheduled_engine_render :: template scheduled_module < _mediator_type > _engine_render ;
    shy_engine_render_stateless < _mediator_type > _engine_render_stateless ;
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
    shy_logic_text_stateless < _mediator_type > _logic_text_stateless ;
    typename scheduled_logic_title :: template scheduled_module < _mediator_type > _logic_title ;
    typename scheduled_logic_touch :: template scheduled_module < _mediator_type > _logic_touch ;
} ;

template < typename platform >
shy_facade < platform > :: shy_facade ( )
{
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

template < typename platform >
void shy_facade < platform > :: init ( )
{
    _mediator . send ( typename messages :: init ( ) ) ;
}

template < typename platform >
void shy_facade < platform > :: done ( )
{
    _mediator . send ( typename messages :: done ( ) ) ;
}

template < typename platform >
void shy_facade < platform > :: render ( )
{
    _mediator . send ( typename messages :: render ( ) ) ;
}

template < typename platform >
void shy_facade < platform > :: update ( )
{
    _mediator . send ( typename messages :: update ( ) ) ;
}

template < typename platform >
void shy_facade < platform > :: video_mode_changed ( )
{
    _mediator . send ( typename messages :: video_mode_changed ( ) ) ;
}

#undef char
#undef double
#undef float
#undef int
#undef long
#undef signed
#undef short
#undef unsigned
