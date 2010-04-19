inline
void 
shy_macosx_platform :: time_get_current 
    ( shy_macosx_platform :: time_data & time 
    )
{
//    time . _time = CFAbsoluteTimeGetCurrent ( ) ;
}

inline
shy_macosx_platform :: int_32 
shy_macosx_platform :: time_diff_in_microseconds 
    ( const shy_macosx_platform :: time_data & time1 
    , const shy_macosx_platform :: time_data & time2 
    )
{/*
    CFAbsoluteTime diff = 0 ;
    if ( time1 . _time > time2 . _time )
        diff = time1 . _time - time2 . _time ;
    else
        diff = time2 . _time - time1 . _time ;
    return ( int_32 ) ( diff * ( CFAbsoluteTime ) 1000000 ) ;
*/
	return 0 ;
}
