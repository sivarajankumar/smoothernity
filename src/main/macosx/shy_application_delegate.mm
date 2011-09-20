#include "./shy_application_delegate.h"

@implementation shy_application_delegate

- ( NSApplicationTerminateReply ) applicationShouldTerminate : ( NSApplication * ) sender
{
    NSLog ( @"should terminate" ) ;
    return NSTerminateNow ;
}

@end
