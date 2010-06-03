#include "scheduled_aggregator.hpp"
#include "test_aggregator.hpp"
#include "test_first_module.hpp"
#include "test_second_module.hpp"
#include "test_controller.hpp"
#include "test_mediator.hpp"
#include "test_messages.hpp"

class test_facade
{
public :
    void start ( )
    {
        _aggregator . start ( ) ;
    }
    void on_some_event ( int arg )
    {
        _aggregator . on_some_event ( arg ) ;
    }
private :
    scheduled_aggregator
        < test_first_module 
        , test_second_module 
        , test_controller
        , test_mediator
        , test_messages
        > _aggregator ;
} ;
