namespace shy_guts
{
    static void * sound_loader = 0 ;
}

void shy_iphone_platform_sound_loader_insider :: set_sound_loader ( void * sound_loader )
{
    shy_guts :: sound_loader = sound_loader ;
}

void shy_iphone_platform_sound_loader_insider :: get_sound_loader ( void * & sound_loader )
{
    sound_loader = shy_guts :: sound_loader ;
}
