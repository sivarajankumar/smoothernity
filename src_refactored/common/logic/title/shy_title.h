#ifndef _shy_common_logic_title_included
#define _shy_common_logic_title_included

class _shy_common_logic_title
{
public :
    static void receive ( so_called_message_common_engine_render_aspect_reply ) ;
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
} ;

typedef so_called_platform_scheduler :: scheduled_context < _shy_common_logic_title > :: module shy_common_logic_title_scheduled ;

#endif
