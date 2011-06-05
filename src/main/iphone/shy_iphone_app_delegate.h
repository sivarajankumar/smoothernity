#include <UIKit/UIKit.h>

@class EAGLView ;

@interface shy_iphone_app_delegate : NSObject < UIApplicationDelegate > 
{
    UIWindow * window ;
    EAGLView * glView ;
}

@property ( nonatomic , retain ) IBOutlet UIWindow * window ;
@property ( nonatomic , retain ) IBOutlet EAGLView * glView ;

@end

