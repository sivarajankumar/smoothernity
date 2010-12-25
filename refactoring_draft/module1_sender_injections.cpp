#include "platform.hpp"
#include "module1.hpp"
#include "module2.hpp"

typedef so_called_platform :: platform_scheduler :: scheduled_context < my_module1 > :: module so_called_module1 ;
typedef so_called_platform :: platform_scheduler :: scheduled_context < my_module2 > :: module so_called_module2 ;

#include "module1_sender.cxx"

