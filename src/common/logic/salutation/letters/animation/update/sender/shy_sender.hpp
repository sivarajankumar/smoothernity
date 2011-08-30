void shy_common_logic_salutation_letters_animation_update_sender :: send ( so_called_common_logic_salutation_letters_animation_update_message msg )
{
    so_called_common_logic_salutation_letters_animation_appear :: receive ( msg ) ;
    so_called_common_logic_salutation_letters_animation_disappear :: receive ( msg ) ;
    so_called_common_logic_salutation_letters_animation_roll_in :: receive ( msg ) ;
    so_called_common_logic_salutation_letters_animation_roll_out :: receive ( msg ) ;
}
