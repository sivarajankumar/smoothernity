#define char no_chars
#define double no_doubles
#define float no_floats
#define int no_ints
#define long no_longs
#define signed no_signeds
#define short no_shorts
#define unsigned no_unsigneds

#include "aggregator.hpp"
#include "engine/camera.hpp"
#include "engine/math.hpp"
#include "engine/rasterizer/rasterizer.hpp"
#include "engine/rasterizer/stateless.hpp"
#include "engine/render/render.hpp"
#include "engine/render/stateless.hpp"
#include "logic/application/application.hpp"
#include "logic/application/stateless.hpp"
#include "logic/camera/camera.hpp"
#include "logic/camera/stateless.hpp"
#include "logic/core/core.hpp"
#include "logic/core/stateless.hpp"
#include "logic/entities/entities.hpp"
#include "logic/entities/stateless.hpp"
#include "logic/fidget/fidget.hpp"
#include "logic/fidget/stateless.hpp"
#include "logic/game/game.hpp"
#include "logic/game/stateless.hpp"
#include "logic/image/image.hpp"
#include "logic/image/stateless.hpp"
#include "logic/land/land.hpp"
#include "logic/land/stateless.hpp"
#include "logic/main_menu/layout.hpp"
#include "logic/main_menu/letters_creation_director.hpp"
#include "logic/main_menu/letters_storage.hpp"
#include "logic/main_menu/main_menu.hpp"
#include "logic/main_menu/meshes_creation_director.hpp"
#include "logic/main_menu/meshes_creator.hpp"
#include "logic/main_menu/meshes_renderer.hpp"
#include "logic/main_menu/meshes_placement.hpp"
#include "logic/main_menu/meshes_storage.hpp"
#include "logic/main_menu/renderer.hpp"
#include "logic/main_menu/stateless.hpp"
#include "logic/sound/sound.hpp"
#include "logic/sound/stateless.hpp"
#include "logic/text/stateless.hpp"
#include "logic/text/text.hpp"
#include "logic/title/stateless.hpp"
#include "logic/title/title.hpp"
#include "logic/touch/stateless.hpp"
#include "logic/touch/touch.hpp"
#include "mediator.hpp"

template < typename platform >
class shy_facade
{
public :
    shy_facade ( const platform & ) ;
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
        , shy_engine_rasterizer_stateless
        , shy_engine_render
        , shy_engine_render_stateless
        , shy_logic_application
        , shy_logic_application_stateless
        , shy_logic_camera
        , shy_logic_camera_stateless
        , shy_logic_core
        , shy_logic_core_stateless
        , shy_logic_entities
        , shy_logic_entities_stateless
        , shy_logic_fidget
        , shy_logic_fidget_stateless
        , shy_logic_game
        , shy_logic_game_stateless
        , shy_logic_image
        , shy_logic_image_stateless
        , shy_logic_land
        , shy_logic_land_stateless
        , shy_logic_main_menu
        , shy_logic_main_menu_layout
        , shy_logic_main_menu_letters_creation_director
        , shy_logic_main_menu_letters_storage
        , shy_logic_main_menu_meshes_creation_director
        , shy_logic_main_menu_meshes_creator
        , shy_logic_main_menu_meshes_placement
        , shy_logic_main_menu_meshes_renderer
        , shy_logic_main_menu_meshes_storage
        , shy_logic_main_menu_renderer
        , shy_logic_main_menu_stateless
        , shy_logic_sound
        , shy_logic_sound_stateless
        , shy_logic_text
        , shy_logic_text_stateless
        , shy_logic_title
        , shy_logic_title_stateless
        , shy_logic_touch
		, shy_logic_touch_stateless
        > >
        _aggregator ;
} ;

template < typename platform >
shy_facade < platform > :: shy_facade ( const platform & arg_platform )
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
