namespace shy_guts
{
    static void * texture_loader = 0 ;
}

void shy_macosx_platform_render_texture_loader_insider :: set_texture_loader ( void * texture_loader )
{
    shy_guts :: texture_loader = texture_loader ;
}

void shy_macosx_platform_render_texture_loader_insider :: get_texture_loader ( void * & texture_loader )
{
    texture_loader = shy_guts :: texture_loader ;
}
