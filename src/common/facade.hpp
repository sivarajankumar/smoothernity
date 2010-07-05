#define char no_chars
#define double no_doubles
#define float no_floats
#define int no_ints
#define long no_longs
#define signed no_signeds
#define short no_shorts
#define unsigned no_unsigneds

#include "aggregator.hpp"
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
public :
    shy_facade ( platform & arg_platform ) ;
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void video_mode_changed ( ) ;
private :
    shy_aggregator < shy_aggregator_types
        < platform
        , shy_mediator
        , shy_engine_camera
        , shy_engine_math
        , shy_engine_rasterizer
        , shy_engine_render
        , shy_engine_render_stateless
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
        , shy_logic_text_stateless
        , shy_logic_title
        , shy_logic_touch
        > >
        _aggregator ;
} ;

template < typename platform >
shy_facade < platform > :: shy_facade ( platform & arg_platform )
: _aggregator ( arg_platform )
{
}

template < typename platform >
void shy_facade < platform > :: init ( )
{
    _aggregator . init ( ) ;
}

template < typename platform >
void shy_facade < platform > :: done ( )
{
    _aggregator . done ( ) ;
}

template < typename platform >
void shy_facade < platform > :: render ( )
{
    _aggregator . render ( ) ;
}

template < typename platform >
void shy_facade < platform > :: update ( )
{
    _aggregator . update ( ) ;
}

template < typename platform >
void shy_facade < platform > :: video_mode_changed ( )
{
    _aggregator . video_mode_changed ( ) ;
}

#undef char
#undef double
#undef float
#undef int
#undef long
#undef signed
#undef short
#undef unsigned
