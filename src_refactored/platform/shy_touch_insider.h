#ifndef _shy_platform_touch_insider_included
#define _shy_platform_touch_insider_included

class shy_platform_touch_insider
{
    friend class shy_platform_touch ;
public :
    static void set_enabled ( bool ) ;
    static void set_occured ( bool ) ;
    static void set_x ( float ) ;
    static void set_y ( float ) ;
private :
    static bool _enabled ;
    static bool _occured ;
    static float _x ;
    static float _y ;
} ;

#endif
