#ifndef _shy_common_logic_application_fsm_behaviour_injections_included
#define _shy_common_logic_application_fsm_behaviour_injections_included

#ifdef shy_build_loadable_way
    #include "src/common/logic/application/fsm/behaviour/loadable/shy_loadable_injections.h"
    typedef so_called_common_logic_application_fsm_behaviour_loadable so_called_common_logic_application_fsm_behaviour ;
#endif

#ifdef shy_build_static_way
    #include "src/common/logic/application/fsm/behaviour/static/shy_static_injections.h"
    typedef so_called_common_logic_application_fsm_behaviour_static so_called_common_logic_application_fsm_behaviour ;
#endif

#endif
