#import "macosx_platform.hpp"
#import "../common/facade.hpp"

@interface shy_macosx_scene : NSObject
{
@private
	shy_facade < shy_macosx_platform > * _measurer;
}

- init ;
- ( void ) set_viewport_rect : ( NSRect ) bounds ;
- ( void ) render ;

@end
