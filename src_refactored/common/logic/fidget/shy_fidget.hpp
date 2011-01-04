#include "shy_fidget.h"

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_fidget > _scheduled_context_type ;
template < > _scheduled_context_type _scheduled_context_type :: _singleton = _scheduled_context_type ( ) ;

