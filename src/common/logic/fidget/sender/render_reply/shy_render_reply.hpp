void shy_common_logic_fidget_render_reply_sender :: send ( so_called_message_common_logic_fidget_render_reply msg )
{
    so_called_common_logic_game :: receive ( msg ) ;
    so_called_common_logic_main_menu_renderer :: receive ( msg ) ;
    so_called_common_logic_title :: receive ( msg ) ;
}
