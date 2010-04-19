#import "macosx_scene.h"

@implementation shy_macosx_scene

- init
{
    self = [super init];
    if (self) {
		measurer = new shy_measurer_facade < shy_macosx_platform > ( ) ;
    }
    return self;
}

- (void)dealloc
{
	measurer -> done ( ) ;
	delete measurer ;
    [super dealloc];
}

- (void)setViewportRect:(NSRect)bounds
{
    glViewport( bounds.origin.x, bounds.origin.y, bounds.size.width, bounds.size.height);
	measurer -> init ( ) ;
}

// This method renders our scene.  We could optimize it in any of several ways, including factoring out the repeated OpenGL initialization calls and either hanging onto the GLU quadric object or creating a display list thet draws the Earth, but the details of how it's implemented aren't important here.  The main thing to note is that we've factored our drawing code out of our NSOpenGLView subclass to enable MainController to use it when rendering in FullScreen mode.
- (void)render
{
	measurer -> render ( ) ;
	measurer -> update ( ) ;
    glFinish();
}

@end
