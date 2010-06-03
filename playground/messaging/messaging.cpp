#include "stdio.h"
#include "test_facade.hpp"

int main ( )
{
    printf ( "start\n" ) ;
    test_facade facade ;
    facade . start ( ) ;
    facade . on_some_event ( 1 ) ;
    facade . on_some_event ( 2 ) ;
    printf ( "finish\n" ) ;
	return 0 ;
}
