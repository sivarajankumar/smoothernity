#include "macosx_platform.hpp"
#include "../facade/interface.hpp"

@interface shy_macosx_scene : NSObject
{
@private
    shy_macosx_sound_loader * _sound_loader ;
    shy_macosx_texture_loader * _texture_loader ;
    shy_macosx_platform_insider * _platform_insider ;
	shy_facade_interface * _facade ;
	NSRect _bounds ;
}

- init ;
- ( void ) set_viewport_rect : ( NSRect ) bounds ;
- ( void ) render ;
- ( void ) set_mouse_position : ( NSPoint ) position ;
- ( void ) mouse_left_button_down ;
- ( void ) mouse_left_button_up ;
- ( void ) video_mode_changed ;

@end
