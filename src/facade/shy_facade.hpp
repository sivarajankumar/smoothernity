void shy_facade :: application_init ( )
{
    so_called_profile ( so_called_platform_profile :: init ( ) ) ;
    so_called_profile ( so_called_profile_init :: init ( ) ) ;

    so_called_loadable ( so_called_loadable_loader :: load ( ) ) ;
}

void shy_facade :: application_done ( )
{
    so_called_profile ( so_called_platform_profile_insider :: generate ( ) ) ;
    so_called_generator ( so_called_platform_generator :: write ( ) ) ;
}

void shy_facade :: game_init ( )
{
    so_called_platform_render :: init ( ) ;
    so_called_platform_render_texture_loader :: init ( ) ;
    so_called_platform_scheduler :: init ( ) ;
    so_called_platform_sound_loader :: init ( ) ;
    so_called_common_init :: init ( ) ;

    so_called_common_init_sender :: send ( so_called_common_init_message ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade :: game_done ( )
{
    so_called_common_done_sender :: send ( so_called_common_done_message ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;

    so_called_common_done :: done ( ) ;

    so_called_platform_render :: done ( ) ;
    so_called_platform_render_texture_loader :: done ( ) ;
    so_called_platform_scheduler :: done ( ) ;
    so_called_platform_sound_loader :: done ( ) ;
}

void shy_facade :: next_frame ( )
{
    so_called_profile ( so_called_platform_profile_insider :: next_frame ( ) ) ;
    so_called_trace ( so_called_platform_trace_insider :: next_frame ( ) ) ;

    so_called_common_next_frame_sender :: send ( so_called_common_next_frame_message ( ) ) ;
    so_called_platform_scheduler :: run ( ) ;
}
