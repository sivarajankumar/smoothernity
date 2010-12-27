#ifndef _facade_loadable_included
#define _facade_loadable_included

class shy_facade_loadable
{
public :
    static void init ( ) ;
    static void done ( ) ;
    static void update ( ) ;
    static void render ( ) ;
    static void video_mode_changed ( ) ;
} ;

#endif
