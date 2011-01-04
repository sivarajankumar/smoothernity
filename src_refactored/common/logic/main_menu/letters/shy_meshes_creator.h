#ifndef _shy_common_logic_main_menu_letters_meshes_creator_included
#define _shy_common_logic_main_menu_letters_meshes_creator_included

class _shy_common_logic_main_menu_letters_meshes_creator
{
public :
    static void receive ( so_called_message_common_engine_render_mesh_create_reply ) ;
} ;

typedef so_called_platform_scheduler 
    :: scheduled_context < _shy_common_logic_main_menu_letters_meshes_creator > :: module 
    shy_common_logic_main_menu_letters_meshes_creator_scheduled ;

#endif
