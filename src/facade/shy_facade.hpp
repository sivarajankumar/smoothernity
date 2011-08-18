void shy_facade :: init ( )
{
    so_called_platform_render :: init ( ) ;
    so_called_platform_render_texture_loader :: init ( ) ;
    so_called_platform_scheduler :: init ( ) ;
    so_called_platform_sound_loader :: init ( ) ;
    so_called_common_init :: init ( ) ;

    so_called_loadable_loader :: load ( ) ;

    so_called_sender_common_init :: send ( so_called_message_common_init ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade :: done ( )
{
    so_called_sender_common_done :: send ( so_called_message_common_done ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;

    so_called_common_done :: done ( ) ;

    so_called_platform_render :: done ( ) ;
    so_called_platform_render_texture_loader :: done ( ) ;
    so_called_platform_scheduler :: done ( ) ;
    so_called_platform_sound_loader :: done ( ) ;
}

void shy_facade :: render ( )
{
    so_called_sender_common_render :: send ( so_called_message_common_render ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade :: update ( )
{
    so_called_sender_common_update :: send ( so_called_message_common_update ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade :: video_mode_changed ( )
{
    so_called_sender_common_video_mode_changed :: send ( so_called_message_common_video_mode_changed ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}