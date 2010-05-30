inline void shy_iphone_platform :: time_get_current ( time_data & time )
{
    time . _time = CFAbsoluteTimeGetCurrent ( ) ;
}

inline void shy_iphone_platform :: time_diff_in_microseconds ( num_whole & result , const time_data & time1 , const time_data & time2 )
{
    CFAbsoluteTime diff = 0 ;
    if ( time1 . _time > time2 . _time )
        diff = time1 . _time - time2 . _time ;
    else
        diff = time2 . _time - time1 . _time ;
    result . _value = ( int ) ( diff * ( CFAbsoluteTime ) 1000000 ) ;
}
