inline void shy_iphone_platform :: touch_occured ( num_whole & result )
{
    result . _value = ( shy_iphone_platform_utility :: _touch_occured == true ) ;
}

inline void shy_iphone_platform :: touch_x ( num_fract & result )
{
    result . _value = shy_iphone_platform_utility :: _touch_x ;
}

inline void shy_iphone_platform :: touch_y ( num_fract & result )
{
    result . _value = shy_iphone_platform_utility :: _touch_y ;
}
