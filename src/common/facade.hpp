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
#include "logic/main_menu/animation/animation.hpp"
#include "logic/main_menu/animation/stateless.hpp"
#include "logic/main_menu/choice.hpp"
#include "logic/main_menu/letters/animation/animation.hpp"
#include "logic/main_menu/letters/animation/appear.hpp"
#include "logic/main_menu/letters/animation/disappear.hpp"
#include "logic/main_menu/letters/animation/idle.hpp"
#include "logic/main_menu/letters/animation/selection.hpp"
#include "logic/main_menu/letters/animation/selection_push.hpp"
#include "logic/main_menu/letters/animation/selection_weight.hpp"
#include "logic/main_menu/letters/animation/stateless.hpp"
#include "logic/main_menu/letters/animation/unselection_weight.hpp"
#include "logic/main_menu/letters/creation_director.hpp"
#include "logic/main_menu/letters/layout/position.hpp"
#include "logic/main_menu/letters/layout/row_rect.hpp"
#include "logic/main_menu/letters/layout/stateless.hpp"
#include "logic/main_menu/letters/meshes/creation_director.hpp"
#include "logic/main_menu/letters/meshes/creator.hpp"
#include "logic/main_menu/letters/meshes/destroyer.hpp"
#include "logic/main_menu/letters/meshes/renderer.hpp"
#include "logic/main_menu/letters/meshes/placement.hpp"
#include "logic/main_menu/letters/meshes/stateless.hpp"
#include "logic/main_menu/letters/meshes/storage.hpp"
#include "logic/main_menu/letters/stateless.hpp"
#include "logic/main_menu/letters/storage.hpp"
#include "logic/main_menu/main_menu.hpp"
#include "logic/main_menu/renderer.hpp"
#include "logic/main_menu/selection/animation/animation.hpp"
#include "logic/main_menu/selection/animation/appear.hpp"
#include "logic/main_menu/selection/animation/disappear.hpp"
#include "logic/main_menu/selection/animation/idle.hpp"
#include "logic/main_menu/selection/animation/idle_attention.hpp"
#include "logic/main_menu/selection/animation/push.hpp"
#include "logic/main_menu/selection/animation/push_attention.hpp"
#include "logic/main_menu/selection/animation/push_weight.hpp"
#include "logic/main_menu/selection/animation/select.hpp"
#include "logic/main_menu/selection/animation/stateless.hpp"
#include "logic/main_menu/selection/animation/unselect.hpp"
#include "logic/main_menu/selection/mesh.hpp"
#include "logic/main_menu/selection/stateless.hpp"
#include "logic/main_menu/selection/tracker.hpp"
#include "logic/main_menu/selection/tracking_director.hpp"
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
    shy_facade ( typename platform :: platform_pointer :: template pointer < const platform > ) ;
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
        , shy_logic_main_menu_animation
        , shy_logic_main_menu_animation_stateless
        , shy_logic_main_menu_choice
        , shy_logic_main_menu_letters_animation
        , shy_logic_main_menu_letters_animation_appear
        , shy_logic_main_menu_letters_animation_disappear
        , shy_logic_main_menu_letters_animation_idle
        , shy_logic_main_menu_letters_animation_selection
        , shy_logic_main_menu_letters_animation_selection_push
        , shy_logic_main_menu_letters_animation_selection_weight
        , shy_logic_main_menu_letters_animation_stateless
        , shy_logic_main_menu_letters_animation_unselection_weight
        , shy_logic_main_menu_letters_creation_director
        , shy_logic_main_menu_letters_layout_position
        , shy_logic_main_menu_letters_layout_row_rect
        , shy_logic_main_menu_letters_layout_stateless
        , shy_logic_main_menu_letters_meshes_creation_director
        , shy_logic_main_menu_letters_meshes_creator
        , shy_logic_main_menu_letters_meshes_destroyer
        , shy_logic_main_menu_letters_meshes_placement
        , shy_logic_main_menu_letters_meshes_renderer
        , shy_logic_main_menu_letters_meshes_stateless
        , shy_logic_main_menu_letters_meshes_storage
        , shy_logic_main_menu_letters_stateless
        , shy_logic_main_menu_letters_storage
        , shy_logic_main_menu_renderer
        , shy_logic_main_menu_selection_animation
        , shy_logic_main_menu_selection_animation_appear
        , shy_logic_main_menu_selection_animation_disappear
        , shy_logic_main_menu_selection_animation_idle
        , shy_logic_main_menu_selection_animation_idle_attention
        , shy_logic_main_menu_selection_animation_push
        , shy_logic_main_menu_selection_animation_push_attention
        , shy_logic_main_menu_selection_animation_push_weight
        , shy_logic_main_menu_selection_animation_select
        , shy_logic_main_menu_selection_animation_stateless
        , shy_logic_main_menu_selection_animation_unselect
        , shy_logic_main_menu_selection_mesh
        , shy_logic_main_menu_selection_stateless
        , shy_logic_main_menu_selection_tracker
        , shy_logic_main_menu_selection_tracking_director
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
shy_facade < platform > :: shy_facade ( typename platform :: platform_pointer :: template pointer < const platform > arg_platform )
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
