#include <UIKit/UIKit.h>

int main ( int argc , char * argv [ ] )
{
    NSAutoreleasePool * pool = [ [ NSAutoreleasePool alloc ] init ] ;
    int ret_val = UIApplicationMain ( argc , argv , nil , nil ) ;
    [ pool release ] ;
    return ret_val ;
}
