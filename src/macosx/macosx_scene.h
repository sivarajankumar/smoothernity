#import "macosx_platform.hpp"
#import "../common/facade.hpp"

@interface shy_macosx_scene : NSObject
{
	shy_facade < shy_macosx_platform > * measurer;
}

- init ;
- ( void ) set_viewport_rect : ( NSRect ) bounds ;
- ( void ) render ;

@end
