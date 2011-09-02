void shy_common_logic_main_menu_launch_permit_sender :: send ( so_called_common_logic_main_menu_launch_permit_message msg )
{
    so_called_common_logic_main_menu :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_appear :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_idle :: receive ( msg ) ;
    so_called_common_logic_main_menu_letters_animation_selection :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_idle_attention :: receive ( msg ) ;
    so_called_common_logic_main_menu_selection_animation_push_attention :: receive ( msg ) ;
}
