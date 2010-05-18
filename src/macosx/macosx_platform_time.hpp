inline void shy_macosx_platform :: time_get_current ( time_data & time )
{
    time . _time = CFAbsoluteTimeGetCurrent ( ) ;
}

inline void shy_macosx_platform :: time_diff_in_microseconds ( int_32 & result , const time_data & time1 , const time_data & time2 )
{
    CFAbsoluteTime diff = 0 ;
    if ( time1 . _time > time2 . _time )
        diff = time1 . _time - time2 . _time ;
    else
        diff = time2 . _time - time1 . _time ;
    result = ( int_32 ) ( diff * ( CFAbsoluteTime ) 1000000 ) ;
}
