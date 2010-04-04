#import "measurerAppDelegate.h"
#import "EAGLView.h"

@implementation measurerAppDelegate

@synthesize window ;
@synthesize glView ;

- ( void ) applicationDidFinishLaunching : ( UIApplication * ) application
{
	[ glView start_animation ] ;
}

- ( void ) applicationWillResignActive : ( UIApplication * ) application
{
	[ glView stop_animation ] ;
}

- ( void ) applicationDidBecomeActive : ( UIApplication * ) application
{
	[ glView start_animation ] ;
}

- ( void ) applicationWillTerminate : ( UIApplication * ) application
{
	[ glView stop_animation ] ;
}

- ( void ) dealloc
{
	[ window release ] ;
	[ glView release ] ;
	
	[ super dealloc ] ;
}

@end
