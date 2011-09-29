#include "src/common/engine/rasterizer/shy_rasterizer_injections.h"
#include "src/common/engine/render/shy_render_injections.h"
#include "src/common/logic/amusement/renderer/shy_renderer_injections.h"
#include "src/common/logic/amusement/shy_amusement_injections.h"
#include "src/common/logic/application/fsm/shy_fsm_injections.h"
#include "src/common/logic/blanket/animation/appear/shy_appear_injections.h"
#include "src/common/logic/blanket/animation/disappear/shy_disappear_injections.h"
#include "src/common/logic/blanket/animation/fit/shy_fit_injections.h"
#include "src/common/logic/blanket/animation/shy_animation_injections.h"
#include "src/common/logic/blanket/mesh/shy_mesh_injections.h"
#include "src/common/logic/blanket/placement/shy_placement_injections.h"
#include "src/common/logic/blanket/renderer/shy_renderer_injections.h"
#include "src/common/logic/blanket/shy_blanket_injections.h"
#include "src/common/logic/camera/shy_camera_injections.h"
#include "src/common/logic/controls/shy_controls_injections.h"
#include "src/common/logic/core/shy_core_injections.h"
#include "src/common/logic/door/animation/appear/shy_appear_injections.h"
#include "src/common/logic/door/animation/shy_animation_injections.h"
#include "src/common/logic/door/mesh/shy_mesh_injections.h"
#include "src/common/logic/door/placement/shy_placement_injections.h"
#include "src/common/logic/door/renderer/shy_renderer_injections.h"
#include "src/common/logic/door/shy_door_injections.h"
#include "src/common/logic/door/texture/shy_texture_injections.h"
#include "src/common/logic/entities/shy_entities_injections.h"
#include "src/common/logic/fader/shy_fader_injections.h"
#include "src/common/logic/fidget/shy_fidget_injections.h"
#include "src/common/logic/font/mesh/generator/shy_generator_injections.h"
#include "src/common/logic/font/texture/generator/shy_generator_injections.h"
#include "src/common/logic/game/shy_game_injections.h"
#include "src/common/logic/image/shy_image_injections.h"
#include "src/common/logic/land/shy_land_injections.h"
#include "src/common/logic/main/menu/animation/shake/shy_shake_injections.h"
#include "src/common/logic/main/menu/animation/shy_animation_injections.h"
#include "src/common/logic/main/menu/choice/shy_choice_injections.h"
#include "src/common/logic/main/menu/letters/animation/appear/shy_appear_injections.h"
#include "src/common/logic/main/menu/letters/animation/disappear/shy_disappear_injections.h"
#include "src/common/logic/main/menu/letters/animation/idle/shy_idle_injections.h"
#include "src/common/logic/main/menu/letters/animation/selection/shy_selection_injections.h"
#include "src/common/logic/main/menu/letters/animation/selection/push/shy_push_injections.h"
#include "src/common/logic/main/menu/letters/animation/selection/weight/shy_weight_injections.h"
#include "src/common/logic/main/menu/letters/animation/shy_animation_injections.h"
#include "src/common/logic/main/menu/letters/animation/unselection/weight/shy_weight_injections.h"
#include "src/common/logic/main/menu/letters/creation/director/shy_director_injections.h"
#include "src/common/logic/main/menu/letters/layout/position/shy_position_injections.h"
#include "src/common/logic/main/menu/letters/layout/row/rect/shy_rect_injections.h"
#include "src/common/logic/main/menu/letters/meshes/creation/director/shy_director_injections.h"
#include "src/common/logic/main/menu/letters/meshes/creator/shy_creator_injections.h"
#include "src/common/logic/main/menu/letters/meshes/destroyer/shy_destroyer_injections.h"
#include "src/common/logic/main/menu/letters/meshes/placement/shy_placement_injections.h"
#include "src/common/logic/main/menu/letters/meshes/renderer/shy_renderer_injections.h"
#include "src/common/logic/main/menu/letters/meshes/storage/shy_storage_injections.h"
#include "src/common/logic/main/menu/letters/storage/shy_storage_injections.h"
#include "src/common/logic/main/menu/renderer/shy_renderer_injections.h"
#include "src/common/logic/main/menu/selection/animation/shy_animation_injections.h"
#include "src/common/logic/main/menu/selection/animation/appear/shy_appear_injections.h"
#include "src/common/logic/main/menu/selection/animation/disappear/shy_disappear_injections.h"
#include "src/common/logic/main/menu/selection/animation/idle/shy_idle_injections.h"
#include "src/common/logic/main/menu/selection/animation/idle/attention/shy_attention_injections.h"
#include "src/common/logic/main/menu/selection/animation/push/shy_push_injections.h"
#include "src/common/logic/main/menu/selection/animation/push/attention/shy_attention_injections.h"
#include "src/common/logic/main/menu/selection/animation/push/weight/shy_weight_injections.h"
#include "src/common/logic/main/menu/selection/animation/select/shy_select_injections.h"
#include "src/common/logic/main/menu/selection/animation/unselect/shy_unselect_injections.h"
#include "src/common/logic/main/menu/selection/mesh/shy_mesh_injections.h"
#include "src/common/logic/main/menu/selection/tracker/shy_tracker_injections.h"
#include "src/common/logic/main/menu/selection/tracking/director/shy_director_injections.h"
#include "src/common/logic/main/menu/shy_menu_injections.h"
#include "src/common/logic/observer/shy_observer_injections.h"
#include "src/common/logic/observer/animation/shy_animation_injections.h"
#include "src/common/logic/observer/animation/flight/shy_flight_injections.h"
#include "src/common/logic/ortho/shy_ortho_injections.h"
#include "src/common/logic/perspective/shy_perspective_injections.h"
#include "src/common/logic/room/shy_room_injections.h"
#include "src/common/logic/room/mesh/shy_mesh_injections.h"
#include "src/common/logic/room/renderer/shy_renderer_injections.h"
#include "src/common/logic/room/texture/shy_texture_injections.h"
#include "src/common/logic/salutation/animation/shy_animation_injections.h"
#include "src/common/logic/salutation/animation/zoom/shy_zoom_injections.h"
#include "src/common/logic/salutation/letters/animation/appear/shy_appear_injections.h"
#include "src/common/logic/salutation/letters/animation/disappear/shy_disappear_injections.h"
#include "src/common/logic/salutation/letters/animation/layout/shy_layout_injections.h"
#include "src/common/logic/salutation/letters/animation/roll/in/shy_in_injections.h"
#include "src/common/logic/salutation/letters/animation/roll/out/shy_out_injections.h"
#include "src/common/logic/salutation/letters/animation/shy_animation_injections.h"
#include "src/common/logic/salutation/letters/meshes/cleaner/shy_cleaner_injections.h"
#include "src/common/logic/salutation/letters/meshes/creator/shy_creator_injections.h"
#include "src/common/logic/salutation/letters/meshes/generator/shy_generator_injections.h"
#include "src/common/logic/salutation/letters/meshes/storage/shy_storage_injections.h"
#include "src/common/logic/salutation/letters/renderer/shy_renderer_injections.h"
#include "src/common/logic/salutation/letters/text/cleaner/shy_cleaner_injections.h"
#include "src/common/logic/salutation/letters/text/generator/shy_generator_injections.h"
#include "src/common/logic/salutation/letters/text/storage/shy_storage_injections.h"
#include "src/common/logic/salutation/renderer/shy_renderer_injections.h"
#include "src/common/logic/salutation/timer/appear/shy_appear_injections.h"
#include "src/common/logic/salutation/timer/disappear/shy_disappear_injections.h"
#include "src/common/logic/sound/shy_sound_injections.h"
#include "src/common/logic/text/letter/mesh/shy_mesh_injections.h"
#include "src/common/logic/text/shy_text_injections.h"
#include "src/common/logic/touch/shy_touch_injections.h"
#include "src/common/logic/vacuum/shy_vacuum_injections.h"

#include "./shy_init_injections.h"
#include "./shy_init.hpp"

