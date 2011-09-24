#include "./shy_application_delegate.h"
#include "src/facade/shy_facade_injections.h"

@implementation shy_application_delegate

- ( NSApplicationTerminateReply ) applicationShouldTerminate : ( NSApplication * ) sender
{
    so_called_facade :: game_done ( ) ;
    so_called_facade :: application_done ( ) ;
    return NSTerminateNow ;
}

@end
