void shy_sender_common_init :: send ( so_called_message_common_init msg )
{
    so_called_common_engine_rasterizer :: receive ( msg ) ;
    so_called_common_engine_render :: receive ( msg ) ;
    so_called_common_logic_application_fsm :: receive ( msg ) ;
    so_called_common_logic_blanket_animation_appear :: receive ( msg ) ;
    so_called_common_logic_blanket_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_blanket_mesh :: receive ( msg ) ;
    so_called_common_logic_camera :: receive ( msg ) ;
    so_called_common_logic_core :: receive ( msg ) ;
    so_called_common_logic_door_animation_appear :: receive ( msg ) ;
    so_called_common_logic_entities :: receive ( msg ) ;
    so_called_common_logic_fidget :: receive ( msg ) ;
    so_called_common_logic_game :: receive ( msg ) ;
    so_called_common_logic_image :: receive ( msg ) ;
    so_called_common_logic_land :: receive ( msg ) ;
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_animation_shake :: receive ( msg ) ;
    so_called_common_logic_main_menu_choice :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_storage :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creation_director :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creator :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_storage :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_weight :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_tracking_director :: receive ( msg ) ;
    so_called_common_logic_observer_animation_flight :: receive ( msg ) ;
    so_called_common_logic_salutation :: receive ( msg ) ;
    so_called_common_logic_sound :: receive ( msg ) ;
    so_called_common_logic_text :: receive ( msg ) ;
    so_called_common_logic_title :: receive ( msg ) ;
    so_called_common_logic_touch :: receive ( msg ) ;
}