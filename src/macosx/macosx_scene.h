#import "macosx_platform.hpp"
#import "../common/measurer_facade.hpp"

@interface shy_macosx_scene : NSObject
{
	shy_measurer_facade < shy_macosx_platform > * measurer;
}
- init;

- (void)setViewportRect:(NSRect)bounds;
- (void)render;

@end
