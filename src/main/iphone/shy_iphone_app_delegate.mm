#include "./shy_iphone_app_delegate.h"
#include "./shy_iphone_view.h"

@implementation shy_iphone_app_delegate

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
