class shy_platform_mouse_insider
{
    friend class shy_platform_mouse ;
public :
    static void set_left_button_down ( so_called_lib_std_bool ) ;
    static void set_enabled ( so_called_lib_std_bool ) ;
    static void set_x ( so_called_lib_std_float ) ;
    static void set_y ( so_called_lib_std_float ) ;
private :
    static so_called_lib_std_bool _enabled ;
    static so_called_lib_std_bool _left_button_down ;
    static so_called_lib_std_float _x ;
    static so_called_lib_std_float _y ;
} ;
