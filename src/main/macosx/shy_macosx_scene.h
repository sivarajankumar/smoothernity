@interface shy_macosx_scene : NSObject
{
@private
    NSRect _bounds ;
}

- init ;
- ( void ) set_viewport_rect : ( NSRect ) bounds ;
- ( void ) render ;
- ( void ) set_mouse_position : ( NSPoint ) position ;
- ( void ) mouse_left_button_down ;
- ( void ) mouse_left_button_up ;
- ( void ) video_mode_changed ;

@end
