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
#include "engine_mesh.hpp"
#include "engine_rasterizer.hpp"
#include "engine_texture.hpp"
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
#include "logic_title.hpp"
#include "logic_touch.hpp"
#include "mediator.hpp"

template < typename platform >
class shy_facade
{
    typedef shy_mediator < shy_mediator_types
        < platform 
        , shy_engine_camera
        , shy_engine_math
        , shy_engine_mesh 
        , shy_engine_rasterizer
        , shy_engine_texture
        , shy_logic
        , shy_logic_application
        , shy_logic_camera
        , shy_logic_entities
        , shy_logic_fidget
        , shy_logic_game
        , shy_logic_image
        , shy_logic_land
        , shy_logic_sound
        , shy_logic_text
        , shy_logic_title
        , shy_logic_touch
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
    shy_engine_camera < _mediator_type > _engine_camera ;
    shy_engine_math < _mediator_type > _engine_math ;
    shy_engine_mesh < _mediator_type > _engine_mesh ;
    shy_engine_rasterizer < _mediator_type > _engine_rasterizer ;
    shy_engine_texture < _mediator_type > _engine_texture ;
    shy_logic < _mediator_type > _logic ;
    shy_logic_application < _mediator_type > _logic_application ;
    shy_logic_camera < _mediator_type > _logic_camera ;
    shy_logic_entities < _mediator_type > _logic_entities ;
    shy_logic_fidget < _mediator_type > _logic_fidget ;
    shy_logic_game < _mediator_type > _logic_game ;
    shy_logic_image < _mediator_type > _logic_image ;
    shy_logic_land < _mediator_type > _logic_land ;
    shy_logic_sound < _mediator_type > _logic_sound ;
    shy_logic_text < _mediator_type > _logic_text ;
    shy_logic_title < _mediator_type > _logic_title ;
    shy_logic_touch < _mediator_type > _logic_touch ;
} ;

template < typename platform >
shy_facade < platform > :: shy_facade ( )
{
    _mediator . register_modules
        ( _engine_mesh
        , _engine_rasterizer
        , _engine_texture
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
