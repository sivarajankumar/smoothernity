#include "./shy_application_delegate.h"
#include <iostream>

@implementation shy_application_delegate

- ( NSApplicationTerminateReply ) applicationShouldTerminate : ( NSApplication * ) sender
{
    std :: cerr << "should terminate" << std :: endl ;
    return NSTerminateNow ;
}

- ( void ) applicationDidFinishLaunching : ( NSNotification * ) notification
{
    std :: cerr << "did finish launching" << std :: endl ;
}

@end
