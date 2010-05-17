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
public :
    void init ( ) ;
    void done ( ) ;
    void render ( ) ;
    void update ( ) ;
    void video_mode_changed ( ) ;
private :
    shy_mediator < shy_mediator_types
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
        _mediator ;
} ;

template < typename platform >
void shy_facade < platform > :: init ( )
{
    _mediator . init ( ) ;
}

template < typename platform >
void shy_facade < platform > :: done ( )
{
    _mediator . done ( ) ;
}

template < typename platform >
void shy_facade < platform > :: render ( )
{
    _mediator . render ( ) ;
}

template < typename platform >
void shy_facade < platform > :: update ( )
{
    _mediator . update ( ) ;
}

template < typename platform >
void shy_facade < platform > :: video_mode_changed ( )
{
    _mediator . video_mode_changed ( ) ;
}

#undef char
#undef double
#undef float
#undef int
#undef long
#undef signed
#undef short
#undef unsigned

