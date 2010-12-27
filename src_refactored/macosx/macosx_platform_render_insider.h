#ifndef _macosx_platform_render_insider_included
#define _macosx_platform_render_insider_included

#include "macosx_texture_loader.h"

class shy_macosx_platform_render_insider
{
public :
    static void set_texture_loader ( shy_macosx_texture_loader * ) ;
    static void set_aspect_width ( float ) ;
    static void set_aspect_height ( float ) ;
} ;

#endif
