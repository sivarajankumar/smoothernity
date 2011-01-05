#include "shy_sender_texture_loader_ready_request.h"

void shy_sender_common_engine_render_texture_loader_ready_request :: send ( so_called_message_common_engine_render_texture_loader_ready_request msg )
{
    so_called_common_engine_render :: receive ( msg ) ;
}

