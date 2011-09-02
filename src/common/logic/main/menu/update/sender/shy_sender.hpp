void shy_common_logic_main_menu_update_sender :: send ( so_called_common_logic_main_menu_update_message msg )
{
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_animation_shake :: receive ( msg ) ;
    so_called_common_logic_main_menu_choice :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_appear :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_idle :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection_weight :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_unselection_weight :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_meshes_creation_director :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_appear :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_idle_attention :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_attention :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_weight :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_select :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_unselect :: receive ( msg ) ;
}
