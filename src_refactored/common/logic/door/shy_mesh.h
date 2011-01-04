#ifndef _shy_common_logic_door_mesh_included
#define _shy_common_logic_door_mesh_included

class _shy_common_logic_door_mesh
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_door_mesh > :: module shy_common_logic_door_mesh_scheduled ;

#endif
