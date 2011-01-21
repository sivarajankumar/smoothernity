class shy_platform_mouse_insider
{
    friend class shy_platform_mouse ;
public :
    static void set_left_button_down ( bool ) ;
    static void set_enabled ( bool ) ;
    static void set_x ( float ) ;
    static void set_y ( float ) ;
private :
    static bool _enabled ;
    static bool _left_button_down ;
    static float _x ;
    static float _y ;
} ;
