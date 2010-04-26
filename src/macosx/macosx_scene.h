#import "macosx_platform.hpp"
#import "../common/facade.hpp"

@interface shy_macosx_scene : NSObject
{
@private
	shy_facade < shy_macosx_platform > * _measurer;
	NSRect _bounds ;
}

- init ;
- ( void ) set_viewport_rect : ( NSRect ) bounds ;
- ( void ) render ;
- ( void ) set_mouse_position : ( NSPoint ) position ;
- ( void ) mouse_left_button_down ;

@end
