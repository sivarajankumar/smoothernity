void shy_facade_static :: init ( )
{
    so_called_platform_math_consts :: init ( ) ;
    so_called_platform_scheduler :: init ( ) ;
    so_called_platform_scheduler :: run ( ) ;
}

void shy_facade_static :: done ( )
{
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

