#ifndef _shy_platform_mouse_included
#define _shy_platform_mouse_included

class shy_platform_mouse_insider ;

class shy_platform_mouse
{
    friend class shy_platform_mouse_insider ;
    typedef so_called_platform_math :: num_fract num_fract ;
    typedef so_called_platform_math :: num_whole num_whole ;
public :
    static void enabled ( num_whole & ) ;
    static void left_button_down ( num_whole & ) ;
    static void x ( num_fract & ) ;
    static void y ( num_fract & ) ;
private :
    static bool _enabled ;
    static bool _left_button_down ;
    static float _x ;
    static float _y ;
} ;

#endif 
