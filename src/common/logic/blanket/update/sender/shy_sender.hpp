void shy_common_logic_blanket_update_sender :: send ( so_called_common_logic_blanket_update_message msg )
{
    so_called_common_logic_blanket :: receive ( msg ) ;
    so_called_common_logic_blanket_animation_appear :: receive ( msg ) ;
    so_called_common_logic_blanket_animation_disappear :: receive ( msg ) ;
}
