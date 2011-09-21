#include "./shy_application_delegate.h"
#include "src/facade/shy_facade_injections.h"

@implementation shy_application_delegate

- ( NSApplicationTerminateReply ) applicationShouldTerminate : ( NSApplication * ) sender
{
    so_called_facade :: done ( ) ;
    return NSTerminateNow ;
}

@end
