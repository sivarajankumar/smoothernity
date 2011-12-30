void shy_common_done_sender :: send ( so_called_common_done_message msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}
