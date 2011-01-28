void shy_facade_static :: init ( )
{
    so_called_platform_scheduler :: init ( ) ;
    so_called_sender_common_init :: send ( so_called_message_common_init ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_static :: done ( )
{
    so_called_sender_common_done :: send ( so_called_message_common_done ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_static :: update ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_static :: render ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_static :: video_mode_changed ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

