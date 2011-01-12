void shy_facade_loadable :: init ( )
{
    so_called_common_engine_render_consts :: init ( ) ;
    so_called_platform_math_consts :: init ( ) ;
    so_called_platform_scheduler :: init ( ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_loadable :: done ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_loadable :: render ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_loadable :: update ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_loadable :: video_mode_changed ( )
{
    so_called_platform_scheduler :: run ( ) ;
}

